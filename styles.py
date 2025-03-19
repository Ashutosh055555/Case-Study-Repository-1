# Professional green color palette
COLORS = {
    'primary': '#2E7D32',      # Dark green
    'secondary': '#4CAF50',    # Medium green
    'accent': '#81C784',       # Light green
    'text': '#1A1A1A',         # Dark text
    'background': '#F5F9F5',   # Light green background
    'white': '#FFFFFF',
    'border': '#E0E7E0'
}

# Custom CSS styles for the application
CUSTOM_CSS = f"""
    <style>
    .main-header {{
        font-size: 5rem;
        color: {COLORS['primary']};
        text-align: center;
        padding: 1.5rem;
        font-weight: bold;
        background: linear-gradient(135deg, {COLORS['background']}, {COLORS['white']});
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-bottom: 4px solid {COLORS['secondary']};
    }}
    .subheader {{
        font-size: 1.6rem;
        color: {COLORS['primary']};
        padding: 0.7rem 0;
        border-bottom: 3px solid {COLORS['secondary']};
        margin-bottom: 1.2rem;
        font-weight: 600;
    }}
    .metric-card {{
        background: linear-gradient(135deg, {COLORS['white']}, {COLORS['background']});
        padding: 1.2rem;
        border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        border: 1px solid {COLORS['border']};
        transition: transform 0.2s ease;
    }}
    .metric-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }}
    .stButton>button {{
        background-color: {COLORS['secondary']};
        color: {COLORS['white']};
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        border: none;
        transition: all 0.3s ease;
    }}
    .stButton>button:hover {{
        background-color: {COLORS['primary']};
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }}
    .stSelectbox label, .stMultiSelect label {{
        color: {COLORS['primary']};
        font-weight: 600;
        font-size: 1rem;
    }}
    a {{
        color: {COLORS['secondary']};
        text-decoration: none;
        font-weight: 500;
        transition: color 0.2s ease;
    }}
    a:hover {{
        color: {COLORS['primary']};
        text-decoration: underline;
    }}
    .row-header {{
        font-weight: 600;
        color: {COLORS['primary']};
    }}
    .stDataFrame {{
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        border: 1px solid {COLORS['border']};
    }}
    .stExpander {{
        border-radius: 10px;
        border: 1px solid {COLORS['border']};
        background-color: {COLORS['white']};
    }}
    .dataframe {{
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        margin: 1rem 0;
        border-radius: 10px;
        overflow: hidden;
    }}
    .dataframe th {{
        background-color: {COLORS['primary']};
        color: {COLORS['white']};
        padding: 12px;
        text-align: left;
        font-weight: 600;
    }}
    .dataframe td {{
        padding: 10px;
        border-bottom: 1px solid {COLORS['border']};
    }}
    .dataframe tr:nth-child(even) {{
        background-color: {COLORS['background']};
    }}
    .dataframe tr:hover {{
        background-color: #E8F5E9;
    }}
    .result-item {{
        background: {COLORS['white']};
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 0.8rem;
        border: 1px solid {COLORS['border']};
        transition: transform 0.2s ease;
    }}
    .result-item:hover {{
        transform: translateX(5px);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }}
    </style>
"""

# Welcome message HTML
WELCOME_HTML = f"""
    <div style='background: linear-gradient(135deg, {COLORS['white']}, {COLORS['background']}); 
                padding: 1.5rem; 
                border-radius: 12px; 
                margin-bottom: 2rem;
                border: 1px solid {COLORS['border']};
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);'>
        <h2 style='color: {COLORS['primary']}; margin-bottom: 1rem; font-size: 1.5rem;'>
            Welcome to EMB Global's Case Study Repository
        </h2>
        <p style='color: {COLORS['text']}; margin-bottom: 0.5rem; line-height: 1.6;'>
            Explore our comprehensive portfolio of work across various industries and service categories. 
            Use the filters below to discover relevant case studies and success stories that showcase our expertise 
            and innovative solutions.
        </p>
    </div>
"""

# Footer HTML with team credits
FOOTER_HTML = f"""
    <div style='margin-top: 4rem; 
                padding: 1.5rem; 
                background: linear-gradient(135deg, {COLORS['white']}, {COLORS['background']}); 
                border-radius: 12px; 
                text-align: center;
                border: 1px solid {COLORS['border']};
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);'>
        <div style='margin-bottom: 1rem;'>
            <p style='color: {COLORS['primary']}; margin: 0; font-weight: 500;'>
                EMB Global Case Study Repository © 2024
            </p>
        </div>
        <div style='display: flex; justify-content: center; gap: 2rem; margin-top: 1rem;'>
            <div style='text-align: center;'>
                <p style='color: {COLORS['secondary']}; margin: 0; font-weight: 600;'>Business Analyst</p>
                <p style='color: {COLORS['text']}; margin: 0;'>Bhoomi</p>
            </div>
            <div style='text-align: center;'>
                <p style='color: {COLORS['secondary']}; margin: 0; font-weight: 600;'>Developer</p>
                <p style='color: {COLORS['text']}; margin: 0;'>Ashutosh</p>
            </div>
            <div style='text-align: center;'>
                <p style='color: {COLORS['secondary']}; margin: 0; font-weight: 600;'>DevOps</p>
                <p style='color: {COLORS['text']}; margin: 0;'>Manav</p>
            </div>
        </div>
    </div>
"""

# Search results count HTML template
def get_search_count_html(count, search_text):
    return f"""
        <div style='background: linear-gradient(135deg, {COLORS['white']}, {COLORS['background']}); 
                    padding: 1rem; 
                    border-radius: 8px; 
                    margin-bottom: 1rem;
                    border: 1px solid {COLORS['border']};'>
            Found <span style='color: {COLORS['primary']}; font-weight: bold;'>{count}</span> results containing '{search_text}'
        </div>
    """

# Metric card HTML template
def get_metric_card_html(count):
    return f"""
        <div class='metric-card'>
            <h3 style='color: {COLORS['primary']}; margin: 0; font-size: 1.2rem;'>Number of Links</h3>
            <p style='color: {COLORS['secondary']}; font-size: 2.5rem; margin: 0.5rem 0; font-weight: bold;'>{count}</p>
        </div>
    """

# Result item HTML template
def get_result_item_html(content):
    return f"""
        <div class='result-item'>
            {content}
        </div>
    """
