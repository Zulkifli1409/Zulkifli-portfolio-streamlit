import streamlit as st
import datetime

# Security imports
from security_middleware import (
    init_security_session,
    security_headers,
    prevent_clickjacking,
    log_security_event,
    check_csrf_token
)

st.set_page_config(
    page_title="Zulkifli - Portfolio",
    page_icon="👨‍💻",
    initial_sidebar_state="collapsed",
    menu_items={
        'Report a bug': "https://github.com/zulkifli1409/portfolio/issues",
        'About': "Secure Portfolio Application with enterprise-grade security"
    }
)

# Initialize security
init_security_session()
security_headers()
prevent_clickjacking()
check_csrf_token()

# Log page access
log_security_event("PAGE_ACCESS", "Main portfolio page loaded", "INFO")

import home, about, skills, projects, contact
st.markdown("""
<style>
    /* Reset default styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        padding: 1rem 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        border: 2px solid #FFD700;
        margin-bottom: 2rem;
    }
    
    /* Individual tab styling */
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        padding: 0 24px;
        background: linear-gradient(135deg, #2d2d2d 0%, #1a1a1a 100%);
        border-radius: 12px;
        color: #FFD700;
        font-weight: 600;
        font-size: 16px;
        border: 2px solid transparent;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Hover effect */
    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
        color: #1a1a1a;
        border-color: #FFD700;
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(255, 215, 0, 0.4);
    }
    
    /* Active tab styling */
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
        color: #1a1a1a;
        border-color: #FFD700;
        transform: scale(1.05);
        box-shadow: 0 8px 30px rgba(255, 215, 0, 0.6);
        z-index: 2;
    }
    
    /* Glow effect untuk active tab */
    .stTabs [data-baseweb="tab"][aria-selected="true"]::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, #FFD700, #FFA500, #FFD700);
        border-radius: 12px;
        z-index: -1;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    /* Header styling */
    .portfolio-header {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        border: 3px solid #FFD700;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .portfolio-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255, 215, 0, 0.1) 0%, transparent 70%);
        animation: rotate 20s linear infinite;
        z-index: 0;
    }
    
    .header-content {
        position: relative;
        z-index: 1;
        display: flex;
        align-items: center;
        gap: 1.5rem;
    }
    
    .header-icon {
        font-size: 4rem;
        animation: bounce 2s ease-in-out infinite;
        filter: drop-shadow(0 0 20px rgba(255, 215, 0, 0.5));
    }
    
    .header-text h1 {
        margin: 0;
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3.5rem;
        font-weight: 800;
        text-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        animation: textGlow 3s ease-in-out infinite alternate;
    }
    
    .header-text p {
        margin: 0.5rem 0 0 0;
        color: #FFD700;
        font-size: 1.3rem;
        font-weight: 500;
        opacity: 0.9;
    }
    
    /* Keyframe animations */
    @keyframes glow {
        0% { box-shadow: 0 0 20px rgba(255, 215, 0, 0.4); }
        100% { box-shadow: 0 0 30px rgba(255, 215, 0, 0.8); }
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    
    @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    @keyframes textGlow {
        0% { text-shadow: 0 0 20px rgba(255, 215, 0, 0.5); }
        100% { text-shadow: 0 0 30px rgba(255, 215, 0, 0.8); }
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .stTabs [data-baseweb="tab-list"] {
            padding: 0.5rem 1rem;
            flex-wrap: wrap;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            padding: 0 16px;
            font-size: 14px;
            margin-bottom: 8px;
        }
        
        .header-content {
            flex-direction: column;
            text-align: center;
        }
        
        .header-text h1 {
            font-size: 2.5rem;
        }
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1a1a1a;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #FFD700, #FFA500);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #FFA500, #FFD700);
    }
</style>
""", unsafe_allow_html=True)

# Header dengan animasi dan styling baru
st.markdown("""
<div class="portfolio-header">
    <div class="header-content">
        <div class="header-icon">👨‍💻</div>
        <div class="header-text">
            <h1>Zulkifli</h1>
            <p>✨ Portfolio & Professional Profile ✨</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Enhanced Tab Navigation dengan animasi
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏠 Home", 
    "👤 About", 
    "🛠️ Skills", 
    "📂 Projects", 
    "📞 Contact"
])

# JavaScript untuk enhanced interactivity
st.markdown("""
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Add click sound effect (optional)
    const tabs = document.querySelectorAll('[data-baseweb="tab"]');
    tabs.forEach(tab => {
        tab.addEventListener('click', function() {
            // Add ripple effect
            const ripple = document.createElement('span');
            ripple.style.position = 'absolute';
            ripple.style.borderRadius = '50%';
            ripple.style.background = 'rgba(255, 255, 255, 0.6)';
            ripple.style.transform = 'scale(0)';
            ripple.style.animation = 'ripple 0.6s linear';
            ripple.style.left = '50%';
            ripple.style.top = '50%';
            ripple.style.width = '20px';
            ripple.style.height = '20px';
            ripple.style.marginLeft = '-10px';
            ripple.style.marginTop = '-10px';
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
});

// Add ripple animation
const style = document.createElement('style');
style.textContent = `
    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
</script>
""", unsafe_allow_html=True)

# Tab content dengan animasi fade-in
with tab1:
    st.markdown('<div class="tab-content" style="animation: fadeIn 0.5s ease-in;">', unsafe_allow_html=True)
    home.app()
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="tab-content" style="animation: fadeIn 0.5s ease-in;">', unsafe_allow_html=True)
    about.app()
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="tab-content" style="animation: fadeIn 0.5s ease-in;">', unsafe_allow_html=True)
    skills.app()
    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="tab-content" style="animation: fadeIn 0.5s ease-in;">', unsafe_allow_html=True)
    projects.app()
    st.markdown('</div>', unsafe_allow_html=True)

with tab5:
    st.markdown('<div class="tab-content" style="animation: fadeIn 0.5s ease-in;">', unsafe_allow_html=True)
    contact.app()
    st.markdown('</div>', unsafe_allow_html=True)

# Footer dengan tema yang konsisten
# Dapatkan waktu saat ini
current_time = datetime.datetime.now()
year = current_time.year
# Format tanggal, bulan, dan tahun
date_str = current_time.strftime("%B %d, %Y")

st.markdown(
    f"""
<div style="
    margin-top: 3rem;
    padding: 1.5rem;
    background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
    border-radius: 15px;
    border: 2px solid #FFD700;
    text-align: center;
    color: #FFD700;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
">
    <p style="margin: 0; font-weight: 500;">
        ✨ Made with passion using Streamlit ✨
    </p>
    <p style="margin: 0.5rem 0 0 0; opacity: 0.8; font-size: 0.9rem;">
        Last updated on {date_str}
    </p>
    <p style="margin: 0.5rem 0 0 0; opacity: 0.8; font-size: 0.9rem;">
        © {year} Zulkifli Portfolio - All rights reserved
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# CSS untuk fade-in animation content
st.markdown("""
<style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .tab-content {
        animation: fadeIn 0.5s ease-in;
    }
</style>
""", unsafe_allow_html=True)
