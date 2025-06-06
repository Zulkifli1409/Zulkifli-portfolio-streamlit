import streamlit as st
import requests


def header(title):
    st.markdown(
        f"""
    <div class="header-container">
        <h1 class="main-header">{title}</h1>
        <div class="header-glow"></div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def load_portfolio_data(github_user="zulkifli1409"):
    url = f"https://api.github.com/users/{github_user}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        return {"projects": []}
    repos = response.json()
    projects = []
    for repo in repos:
        projects.append(
            {
                "title": repo["name"],
                "description": repo["description"] or "No description provided.",
                "url": repo["html_url"],
                "language": repo["language"] or "N/A",
                "stars": repo["stargazers_count"],
                "forks": repo["forks_count"],
            }
        )
    return {"projects": projects}


def app():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Poppins:wght@300;400;600;700&display=swap');
        
        /* Global Styles */
        .stApp {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 50%, #1a1a1a 100%);
        font-family: 'Poppins', sans-serif;
    }
        
        /* Animated Background */
        .stApp::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                radial-gradient(circle at 20% 80%, rgba(255, 215, 0, 0.08) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(255, 165, 0, 0.08) 0%, transparent 50%),
                radial-gradient(circle at 40% 40%, rgba(255, 255, 0, 0.05) 0%, transparent 50%);
            animation: backgroundFloat 12s ease-in-out infinite alternate;
            pointer-events: none;
            z-index: -1;
        }
        
        @keyframes backgroundFloat {
            0% { transform: translateX(0) translateY(0) rotate(0deg); }
            100% { transform: translateX(-30px) translateY(-30px) rotate(2deg); }
        }
        
        /* Header Styles */
        .header-container {
            position: relative;
            text-align: center;
            margin: 2rem 0 3rem 0;
            animation: headerSlideDown 1s ease-out;
        }
        
        .main-header {
            font-family: 'Orbitron', monospace !important;
            font-size: 4rem !important;
            font-weight: 900 !important;
            background: linear-gradient(45deg, #FFD700, #FFA500, #FFFF00, #FFD700, #FFA500) !important;
            background-size: 400% 400% !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-clip: text !important;
            animation: gradientWave 4s ease-in-out infinite, textGlow 2s ease-in-out infinite alternate !important;
            margin: 0 !important;
            text-shadow: 0 0 50px rgba(255, 215, 0, 0.6) !important;
            position: relative !important;
        }
        
        .header-glow {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 300px;
            height: 100px;
            background: radial-gradient(ellipse, rgba(255, 215, 0, 0.3) 0%, transparent 70%);
            animation: glowPulse 3s ease-in-out infinite;
            z-index: -1;
        }
        
        @keyframes headerSlideDown {
            from {
                transform: translateY(-50px);
                opacity: 0;
            }
            to {
                transform: translateY(0);
                opacity: 1;
            }
        }
        
        @keyframes gradientWave {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        @keyframes textGlow {
            from { 
                text-shadow: 0 0 30px rgba(255, 215, 0, 0.6);
                filter: drop-shadow(0 0 20px rgba(255, 215, 0, 0.4));
            }
            to { 
                text-shadow: 0 0 50px rgba(255, 215, 0, 0.9);
                filter: drop-shadow(0 0 30px rgba(255, 215, 0, 0.7));
            }
        }
        
        @keyframes glowPulse {
            0%, 100% { 
                transform: translate(-50%, -50%) scale(1);
                opacity: 0.3;
            }
            50% { 
                transform: translate(-50%, -50%) scale(1.2);
                opacity: 0.6;
            }
        }
        
        /* Filter Section Styles */
        .stTextInput > div > div > input {
            background: rgba(0, 0, 0, 0.7) !important;
            border: 2px solid rgba(255, 215, 0, 0.3) !important;
            border-radius: 15px !important;
            color: #FFD700 !important;
            font-family: 'Poppins', sans-serif !important;
            padding: 0.8rem 1rem !important;
            font-size: 1rem !important;
            transition: all 0.3s ease !important;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #FFD700 !important;
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.4) !important;
            transform: scale(1.02) !important;
        }
        
        .stSelectbox > div > div > div {
            background: rgba(0, 0, 0, 0.7) !important;
            border: 2px solid rgba(255, 215, 0, 0.3) !important;
            border-radius: 15px !important;
            color: #FFD700 !important;
            transition: all 0.3s ease !important;
        }
        
        .stSelectbox > div > div > div:hover {
            border-color: #FFD700 !important;
            box-shadow: 0 0 15px rgba(255, 215, 0, 0.3) !important;
        }
        
        .stSlider > div > div > div > div {
            background: linear-gradient(90deg, #FFD700, #FFA500) !important;
        }
        
        /* Project Card Styles */
        .project-card {
            background: linear-gradient(135deg, rgba(255, 215, 0, 0.08), rgba(0, 0, 0, 0.6));
            border: 2px solid transparent;
            border-radius: 20px;
            padding: 2rem;
            margin: 1.5rem 0;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(15px);
            animation: cardFadeIn 0.8s ease-out forwards;
            transform: translateY(30px);
            opacity: 0;
            box-shadow: 
                0 10px 30px rgba(0, 0, 0, 0.5),
                inset 0 1px 0 rgba(255, 215, 0, 0.1);
        }
        
        .project-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            border-radius: 18px;
            padding: 2px;
            background: linear-gradient(45deg, #FFD700, #FFA500, #FFFF00, #FFD700);
            background-size: 300% 300%;
            animation: borderFlow 4s ease-in-out infinite;
            mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            mask-composite: exclude;
            z-index: -1;
        }
        
        .project-card::after {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 215, 0, 0.1), transparent);
            transition: left 0.6s ease;
        }
        
        .project-card:hover::after {
            left: 100%;
        }
        
        .project-card:hover {
            transform: translateY(-15px) scale(1.03);
            border-color: #FFD700;
            box-shadow: 
                0 25px 50px rgba(0, 0, 0, 0.6),
                0 0 30px rgba(255, 215, 0, 0.4),
                inset 0 1px 0 rgba(255, 215, 0, 0.2);
            background: linear-gradient(135deg, rgba(255, 215, 0, 0.15), rgba(0, 0, 0, 0.7));
        }
        
        @keyframes cardFadeIn {
            to {
                transform: translateY(0);
                opacity: 1;
            }
        }
        
        @keyframes borderFlow {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        /* Staggered Animation */
        .project-card:nth-child(odd) { animation-delay: 0.2s; }
        .project-card:nth-child(even) { animation-delay: 0.4s; }
        
        /* Project Title */
        .project-title {
            font-family: 'Orbitron', monospace;
            font-size: 1.5rem;
            font-weight: 700;
            color: #FFD700;
            margin-bottom: 1rem;
            text-shadow: 0 0 15px rgba(255, 215, 0, 0.5);
            animation: titleGlow 2s ease-in-out infinite alternate;
            position: relative;
        }
        
        .project-title::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: linear-gradient(90deg, #FFD700, #FFA500);
            transition: width 0.3s ease;
        }
        
        .project-card:hover .project-title::after {
            width: 100%;
        }
        
        @keyframes titleGlow {
            from { text-shadow: 0 0 15px rgba(255, 215, 0, 0.5); }
            to { text-shadow: 0 0 25px rgba(255, 215, 0, 0.8); }
        }
        
        /* Project Description */
        .project-desc {
            color: #e0e0e0;
            font-size: 1rem;
            line-height: 1.6;
            margin-bottom: 1.5rem;
            opacity: 0.9;
            transition: opacity 0.3s ease;
        }
        
        .project-card:hover .project-desc {
            opacity: 1;
            color: #f0f0f0;
        }
        
        /* Project Stats */
        .project-stats {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
            padding: 0.8rem;
            background: rgba(255, 215, 0, 0.05);
            border-radius: 12px;
            border: 1px solid rgba(255, 215, 0, 0.1);
            transition: all 0.3s ease;
        }
        
        .project-stats:hover {
            background: rgba(255, 215, 0, 0.1);
            border-color: rgba(255, 215, 0, 0.3);
            transform: scale(1.02);
        }
        
        .project-stats div {
            font-family: 'Orbitron', monospace;
            font-weight: 600;
            color: #FFA500;
            font-size: 0.9rem;
            text-shadow: 0 0 10px rgba(255, 165, 0, 0.3);
            animation: statsPulse 3s ease-in-out infinite alternate;
        }
        
        @keyframes statsPulse {
            from { color: #FFA500; }
            to { color: #FFD700; }
        }
        
        /* Project Link */
        .project-link {
            display: inline-block;
            background: linear-gradient(135deg, #FFD700, #FFA500);
            color: #000 !important;
            padding: 0.8rem 1.5rem;
            border-radius: 25px;
            text-decoration: none;
            font-family: 'Orbitron', monospace;
            font-weight: 600;
            font-size: 0.9rem;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            text-shadow: none;
            box-shadow: 0 5px 15px rgba(255, 215, 0, 0.3);
        }
        
        .project-link::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.5s ease;
        }
        
        .project-link:hover::before {
            left: 100%;
        }
        
        .project-link:hover {
            background: linear-gradient(135deg, #FFFF00, #FFD700);
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(255, 215, 0, 0.5);
            color: #000 !important;
        }
        
        /* Warning and Info Messages */
        .stAlert {
            background: rgba(255, 215, 0, 0.1) !important;
            border: 1px solid rgba(255, 215, 0, 0.3) !important;
            border-radius: 15px !important;
            color: #FFD700 !important;
            animation: alertFadeIn 0.5s ease-out !important;
        }
        
        @keyframes alertFadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .main-header {
                font-size: 2.5rem !important;
            }
            
            .project-card {
                padding: 1.5rem;
                margin: 1rem 0;
            }
            
            .project-title {
                font-size: 1.3rem;
            }
            
            .project-stats {
                flex-direction: column;
                gap: 0.5rem;
            }
            
            .project-stats div {
                font-size: 0.8rem;
            }
        }
        
        @media (max-width: 480px) {
            .main-header {
                font-size: 2rem !important;
            }
            
            .project-card {
                padding: 1rem;
            }
            
            .project-title {
                font-size: 1.2rem;
            }
        }
        
        /* Scrollbar Styling */
        ::-webkit-scrollbar {
            width: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(0, 0, 0, 0.3);
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #FFD700, #FFA500);
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #FFFF00, #FFD700);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    header("🚀 Projects")

    data = load_portfolio_data()
    projects = data.get("projects", [])

    if not projects:
        st.warning("No projects found or failed to fetch from GitHub.")
        return

    # Filter inputs dengan styling
    st.markdown('<div class="filter-section">', unsafe_allow_html=True)
    search_term = st.text_input(
        "🔍 Search projects by title:", placeholder="Enter project name..."
    ).lower()
    language_filter = st.selectbox(
        "💻 Filter by programming language:",
        options=["All"]
        + sorted(set(p["language"] for p in projects if p["language"] != "N/A")),
    )
    min_stars = st.slider("⭐ Minimum stars:", 0, max(p["stars"] for p in projects), 0)
    st.markdown("</div>", unsafe_allow_html=True)

    # Filter projects sesuai filter
    filtered_projects = []
    for p in projects:
        if search_term not in p["title"].lower():
            continue
        if language_filter != "All" and p["language"] != language_filter:
            continue
        if p["stars"] < min_stars:
            continue
        filtered_projects.append(p)

    if not filtered_projects:
        st.info(
            "🔍 No projects matched your search/filter criteria. Try adjusting your filters!"
        )
        return

    # Tampilkan jumlah project yang ditemukan
    st.markdown(
        f"""
    <div style="text-align: center; margin: 2rem 0;">
        <span style="color: #FFD700; font-family: 'Orbitron', monospace; font-size: 1.2rem; font-weight: 600;">
            Found {len(filtered_projects)} project{'s' if len(filtered_projects) != 1 else ''} ✨
        </span>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Buat 2 kolom dengan st.columns
    cols = st.columns(2)
    for i, project in enumerate(filtered_projects):
        col = cols[i % 2]
        with col:
            st.markdown(
                f"""
                <div class="project-card" onclick="window.open('{project['url']}', '_blank')">
                    <div class="project-title">{project['title']}</div>
                    <div class="project-desc">{project['description']}</div>
                    <div class="project-stats">
                        <div>🌐 {project['language']}</div>
                        <div>⭐ {project['stars']}</div>
                        <div>🍴 {project['forks']}</div>
                    </div>
                    <a class="project-link" href="{project['url']}" target="_blank" rel="noopener noreferrer">View on GitHub →</a>
                </div>
                """,
                unsafe_allow_html=True,
            )
