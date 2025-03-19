import re
import pandas as pd
from config import SHEET_URL, RELEVANT_COLUMNS

def extract_url(link):
    """Extract URL from hyperlink formula or direct URL"""
    if isinstance(link, str):
        if '=HYPERLINK' in link:
            url_match = re.search(r'=HYPERLINK\("([^"]+)"', link)
            if url_match:
                return url_match.group(1)
        return link
    return ''

def extract_text(link):
    """Extract text from hyperlink formula or use URL as text"""
    if isinstance(link, str):
        if '=HYPERLINK' in link:
            text_match = re.search(r',"([^"]+)"\)', link)
            if text_match:
                return text_match.group(1)
        return link
    return ''

def make_clickable_link(url, text):
    """Create clickable link HTML"""
    if url and text:
        return f'<a href="{url}" target="_blank">{text}</a>'
    return ''

def get_non_empty_skus(row, sku_columns):
    """Get non-empty SKUs from a row"""
    return [s for s in row[sku_columns] if isinstance(s, str) and s.strip() != '']

def count_links(series):
    """Count non-empty links in a series"""
    return sum(1 for x in series if isinstance(x, str) and x.strip() != '')

def search_dataframe(df, search_text, columns):
    """Search across specified columns in dataframe"""
    if not search_text:
        return df
    
    mask = pd.Series(False, index=df.index)
    for column in columns:
        mask |= df[column].astype(str).str.contains(search_text, case=False, na=False)
    return df[mask]

def load_sheet_data():
    """Load and process data from Google Sheet"""
    try:
        url = SHEET_URL.replace('/edit#gid=', '/export?format=csv&gid=')
        
        # Read the data
        df = pd.read_csv(url)
        
        # Select only the relevant columns
        df = df[RELEVANT_COLUMNS]
        
        # Clean up the data
        df = df.fillna('')
        
        # Extract URLs and texts from links
        df['Link_URL'] = df['Link'].apply(extract_url)
        df['Link_Text'] = df['Link'].apply(extract_text)
        
        return df
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")

def format_result_text(row, sku_columns):
    """Format row data into display text"""
    non_empty_skus = get_non_empty_skus(row, sku_columns)
    sku_text = f" | SKUs: {', '.join(non_empty_skus)}" if non_empty_skus else ""
    client = f"**{row['Client / Use Case']}**" if row['Client / Use Case'] != '' else ""
    category = f"Category: {row['Category']}" if row['Category'] != '' else ""
    industry = f"Industry: {row['Industry']}" if row['Industry'] != '' else ""
    
    parts = [p for p in [client, category, industry, status] if p != ""]
    base_text = " | ".join(parts)
    
    if row['Link_URL']:
        link = make_clickable_link(row['Link_URL'], row['Link_Text'])
        return f"{base_text}{sku_text} | {link}"
    return f"{base_text}{sku_text}"

def get_filtered_data(df, filter_type, filter_values, sku_columns):
    """Get filtered dataframe based on filter type and values"""
    if filter_type == 'industry':
        return df[df['Industry'].isin(filter_values)]
    elif filter_type == 'sku':
        return df[df[sku_columns].isin(filter_values).any(axis=1)]
    return df

def get_unique_values(df, column):
    """Get sorted unique non-empty values from a column"""
    return sorted([i for i in df[column].unique() if isinstance(i, str) and i.strip() != ''])
