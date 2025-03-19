import streamlit as st
import pandas as pd

from config import PREDEFINED_SKUS, SKU_COLUMNS, SEARCH_COLUMNS
from styles import (
    CUSTOM_CSS, WELCOME_HTML, FOOTER_HTML,
    get_search_count_html, get_metric_card_html, get_result_item_html
)
from utils import (
    load_sheet_data, search_dataframe, count_links,
    get_non_empty_skus, make_clickable_link, format_result_text,
    get_filtered_data, get_unique_values
)

# Page configuration
st.set_page_config(
    page_title="EMB GLOBAL- Case Study Repo",
    page_icon="📚",
    layout="wide"
)

# Apply custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Main title
st.markdown('<p class="main-header">EMB GLOBAL - Case Study Repository</p>', unsafe_allow_html=True)

# Welcome message
st.markdown(WELCOME_HTML, unsafe_allow_html=True)

# Load the data
try:
    df = load_sheet_data()
except Exception as e:
    st.error(str(e))
    st.stop()

# Add search functionality at the top
st.markdown('<p class="subheader">Search Case Studies</p>', unsafe_allow_html=True)
search_text = st.text_input("Enter keywords to search across all fields", "")

# Apply search if there's search text
if search_text:
    df_search = search_dataframe(df, search_text, SEARCH_COLUMNS)
    st.markdown(get_search_count_html(len(df_search), search_text), unsafe_allow_html=True)
    
    if not df_search.empty:
        st.markdown('<p class="subheader">Search Results</p>', unsafe_allow_html=True)
        for _, row in df_search.iterrows():
            result_text = format_result_text(row, SKU_COLUMNS)
            st.markdown(get_result_item_html(result_text), unsafe_allow_html=True)

# Create two columns for filters
col1, col2 = st.columns(2)

with col1:
    st.markdown('<p class="subheader">Industry Filter</p>', unsafe_allow_html=True)
    industries = get_unique_values(df, 'Industry')
    selected_industries = st.multiselect(
        "Select Industries",
        options=industries,
        default=[]
    )
    
    if selected_industries:
        filtered_df_industry = get_filtered_data(df, 'industry', selected_industries, SKU_COLUMNS)
        link_count = count_links(filtered_df_industry['Link'])
        st.markdown(get_metric_card_html(link_count), unsafe_allow_html=True)
        
        st.markdown("### Breakdown by Industry")
        industry_counts = filtered_df_industry.groupby('Industry').agg({
            'Link': lambda x: count_links(x)
        }).reset_index()
        industry_counts.columns = ['Industry', 'Link Count']
        st.dataframe(industry_counts, use_container_width=True)

        st.markdown("### Case Studies by Industry")
        for industry in selected_industries:
            industry_links = filtered_df_industry[filtered_df_industry['Industry'] == industry]
            if not industry_links.empty:
                st.markdown(f"#### {industry}")
                for _, row in industry_links.iterrows():
                    if row['Link_URL']:
                        result_text = format_result_text(row, SKU_COLUMNS)
                        st.markdown(get_result_item_html(result_text), unsafe_allow_html=True)

with col2:
    st.markdown('<p class="subheader">SKU Filter</p>', unsafe_allow_html=True)
    
    selected_skus = st.multiselect(
        "Select SKUs",
        options=sorted(PREDEFINED_SKUS),
        default=[]
    )
    
    if selected_skus:
        # Ensure filtering across all SKU columns
        sku_mask = df[SKU_COLUMNS].apply(
            lambda row: row.astype(str).str.contains('|'.join(selected_skus), case=False, na=False), axis=1
        ).any(axis=1)

        filtered_df_sku = df[sku_mask]  # Apply filter
        link_count = count_links(filtered_df_sku['Link'])

        st.markdown(get_metric_card_html(link_count), unsafe_allow_html=True)
        
        # Breakdown by SKU
        st.markdown("### Breakdown by SKU")
        sku_counts = pd.DataFrame()

        for sku in selected_skus:
            sku_mask = df[SKU_COLUMNS].apply(lambda row: row.astype(str).str.contains(sku, case=False, na=False)).any(axis=1)
            count = count_links(df.loc[sku_mask, 'Link'])
            
            sku_counts = pd.concat([sku_counts, pd.DataFrame({'SKU': [sku], 'Link Count': [count]})], ignore_index=True)

        st.dataframe(sku_counts, use_container_width=True)

        # Case Studies by SKU
        st.markdown("### Case Studies by SKU")
        for sku in selected_skus:
            sku_links = filtered_df_sku[
                filtered_df_sku[SKU_COLUMNS].apply(lambda row: row.astype(str).str.contains(sku, case=False, na=False)).any(axis=1)
            ]
            
            if not sku_links.empty:
                st.markdown(f"#### {sku}")
                for _, row in sku_links.iterrows():
                    if row.get('Link_URL'):  
                        result_text = format_result_text(row, SKU_COLUMNS)
                        st.markdown(get_result_item_html(result_text), unsafe_allow_html=True)

# Show combined results if both filters are active
if selected_industries and selected_skus:
    st.markdown('<p class="subheader">Combined Filter Results</p>', unsafe_allow_html=True)
    # Using OR logic: either industry matches OR SKU matches
    industry_mask = df['Industry'].isin(selected_industries)
    sku_mask = df[SKU_COLUMNS].isin(selected_skus).any(axis=1)
    # Using | (OR) instead of & (AND)
    combined_filter = df[industry_mask | sku_mask]
    
    link_count = count_links(combined_filter['Link'])
    st.markdown(get_metric_card_html(link_count), unsafe_allow_html=True)
    
    st.markdown("""
        <div style='margin-bottom: 1rem; color: #2E7D32; font-style: italic;'>
            Showing results that match either selected Industries OR selected SKUs
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Combined Results")
    for _, row in combined_filter.iterrows():
        if row['Link_URL']:
            result_text = format_result_text(row, SKU_COLUMNS)
            st.markdown(get_result_item_html(result_text), unsafe_allow_html=True)

# Show raw data option with custom styling
with st.expander("View All Case Studies"):
    display_df = df.copy()

    # Fixing potential missing values
    display_df[SKU_COLUMNS] = display_df[SKU_COLUMNS].astype(str).fillna("")
    
    # Ensure Link_URL is valid
    display_df['Link'] = display_df.apply(lambda x: make_clickable_link(x['Link_URL'], x['Link_Text']) if pd.notna(x['Link_URL']) else "", axis=1)
    
    # Ensure the correct column names are used
    display_columns = ['Client / Use Case', 'Category', 'Industry', 'Link'] + SKU_COLUMNS
    
    # Display the dataframe
    st.write(display_df[display_columns].to_html(escape=False, classes='dataframe'), unsafe_allow_html=True)

# Footer
st.markdown(FOOTER_HTML, unsafe_allow_html=True)
