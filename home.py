import streamlit as st

def app():
    st.markdown("""
    <style>
/* Global Styles */
.stApp {
    background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
    color: #ffffff;
}

/* Hero Section */
.hero-container {
    text-align: center;
    padding: 3rem 2rem;
    background: linear-gradient(135deg, #000000 0%, #333333 50%, #1a1a1a 100%);
    border-radius: 20px;
    margin-bottom: 2rem;
    box-shadow: 0 20px 40px rgba(255, 193, 7, 0.1);
    position: relative;
    overflow: hidden;
    animation: fadeInUp 1s ease-out;
}

.hero-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 193, 7, 0.1), transparent);
    animation: shimmer 3s infinite;
}

.hero-title {
    font-size: 3.5rem !important;
    font-weight: 700 !important;
    color: #ffc107 !important;
    margin-bottom: 0.5rem !important;
    text-shadow: 0 0 20px rgba(255, 193, 7, 0.3);
    animation: glow 2s ease-in-out infinite alternate;
}

.hero-subtitle {
    font-size: 1.5rem !important;
    color: #e0e0e0 !important;
    margin-bottom: 1rem !important;
    font-weight: 300 !important;
    animation: fadeIn 1.5s ease-out;
}

.hero-description {
    font-size: 1.1rem !important;
    color: #b0b0b0 !important;
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.6;
    animation: fadeIn 2s ease-out;
}

/* Stats Cards */
.stat-card {
    background: linear-gradient(145deg, #2d2d2d, #1a1a1a);
    padding: 2rem 1rem;
    border-radius: 15px;
    text-align: center;
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.3),
        inset 0 1px 0 rgba(255, 193, 7, 0.1);
    border: 1px solid rgba(255, 193, 7, 0.2);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    animation: slideInUp 0.8s ease-out;
    animation-fill-mode: both;
}

.stat-card:nth-child(1) { animation-delay: 0.1s; }
.stat-card:nth-child(2) { animation-delay: 0.2s; }
.stat-card:nth-child(3) { animation-delay: 0.3s; }
.stat-card:nth-child(4) { animation-delay: 0.4s; }

.stat-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 
        0 15px 40px rgba(0, 0, 0, 0.4),
        0 0 30px rgba(255, 193, 7, 0.2);
    border-color: #ffc107;
}

.stat-number {
    font-size: 2.5rem;
    font-weight: 700;
    color: #ffc107;
    margin-bottom: 0.5rem;
    text-shadow: 0 0 10px rgba(255, 193, 7, 0.3);
}

.stat-label {
    font-size: 0.9rem;
    color: #e0e0e0;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 500;
}

/* Section Card */
.section-card {
    background: linear-gradient(145deg, #2d2d2d, #1a1a1a);
    padding: 2rem;
    border-radius: 20px;
    margin-bottom: 2rem;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    border: 1px solid rgba(255, 193, 7, 0.1);
    animation: fadeInUp 1s ease-out;
}

/* Project Cards */
.project-card {
    background: linear-gradient(145deg, #2d2d2d, #1a1a1a);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.3),
        inset 0 1px 0 rgba(255, 193, 7, 0.1);
    border: 1px solid rgba(255, 193, 7, 0.2);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    animation: slideInUp 1s ease-out;
    animation-fill-mode: both;
}

.project-card:nth-child(1) { animation-delay: 0.2s; }
.project-card:nth-child(2) { animation-delay: 0.4s; }
.project-card:nth-child(3) { animation-delay: 0.6s; }

.project-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 193, 7, 0.05), transparent);
    transition: left 0.6s ease;
}

.project-card:hover::before {
    left: 100%;
}

.project-card:hover {
    transform: translateY(-10px) rotateX(5deg);
    box-shadow: 
        0 20px 40px rgba(0, 0, 0, 0.4),
        0 0 30px rgba(255, 193, 7, 0.15);
    border-color: #ffc107;
}

.project-title {
    color: #ffc107 !important;
    font-size: 1.3rem !important;
    font-weight: 600 !important;
    margin-bottom: 1rem !important;
    text-shadow: 0 0 5px rgba(255, 193, 7, 0.2);
}

.project-card p {
    color: #b0b0b0 !important;
    line-height: 1.6;
    margin-bottom: 1.5rem !important;
}

.project-tech {
    background: linear-gradient(135deg, #ffc107, #ffb300);
    color: #000000 !important;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 500;
    margin: 0.2rem 0.3rem 0.2rem 0;
    display: inline-block;
    box-shadow: 0 2px 8px rgba(255, 193, 7, 0.3);
    transition: all 0.3s ease;
}

.project-tech:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(255, 193, 7, 0.4);
}

.project-card a {
    color: #ffc107;
    text-decoration: none;
    font-weight: 600;
    position: relative;
    transition: color 0.3s ease;
}

.project-card a::after {
    content: '';
    position: absolute;
    width: 100%;
    height: 2px;
    bottom: -3px;
    left: 0;
    background-color: #ffc107;
    transform: scaleX(0);
    transform-origin: right;
    transition: transform 0.3s ease;
}

.project-card a:hover {
    color: #ffca28; /* sedikit lebih cerah saat hover */
}

.project-card a:hover::after {
    transform: scaleX(1);
    transform-origin: left;
}


/* Animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideInUp {
    from {
        opacity: 0;
        transform: translateY(50px) scale(0.9);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

@keyframes glow {
    from {
        text-shadow: 0 0 20px rgba(255, 193, 7, 0.3);
    }
    to {
        text-shadow: 0 0 30px rgba(255, 193, 7, 0.6), 0 0 40px rgba(255, 193, 7, 0.3);
    }
}

@keyframes shimmer {
    0% {
        left: -100%;
    }
    100% {
        left: 100%;
    }
}

/* Floating animation for project cards */
.floating {
    animation: floating 3s ease-in-out infinite;
}

@keyframes floating {
    0%, 100% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-5px);
    }
}

.floating:nth-child(2) {
    animation-delay: 1s;
}

.floating:nth-child(3) {
    animation-delay: 2s;
}

/* Responsive Design */
@media (max-width: 768px) {
    .hero-title {
        font-size: 2.5rem !important;
    }
    
    .hero-subtitle {
        font-size: 1.2rem !important;
    }
    
    .hero-description {
        font-size: 1rem !important;
    }
    
    .stat-card {
        padding: 1.5rem 0.8rem;
    }
    
    .stat-number {
        font-size: 2rem;
    }
    
    .project-card {
        padding: 1.5rem;
    }
}
    </style>
    """, unsafe_allow_html=True)

    # Hero Section
    st.markdown(
        """
    <div class="hero-container">
        <h1 class="hero-title">Zulkifli</h1>
        <h2 class="hero-subtitle">CyberSecurity</h2>
        <p class="hero-description">
    I'm a passionate IT student specializing in web development, cybersecurity, and Android app development. I enjoy building secure, full-stack applications and turning innovative ideas into practical digital solutions
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Quick Stats
    # col1, col2, col3, col4 = st.columns(4)

    # with col1:
    #     st.markdown("""
    #     <div class="stat-card">
    #         <div class="stat-number">10+</div>
    #         <div class="stat-label">Projects</div>
    #     </div>
    #     """, unsafe_allow_html=True)

    # with col2:
    #     st.markdown("""
    #     <div class="stat-card">
    #         <div class="stat-number">5+</div>
    #         <div class="stat-label">Years Experience</div>
    #     </div>
    #     """, unsafe_allow_html=True)

    # with col3:
    #     st.markdown("""
    #     <div class="stat-card">
    #         <div class="stat-number">20+</div>
    #         <div class="stat-label">Happy Clients</div>
    #     </div>
    #     """, unsafe_allow_html=True)

    # with col4:
    #     st.markdown("""
    #     <div class="stat-card">
    #         <div class="stat-number">100+</div>
    #         <div class="stat-label">Commits</div>
    #     </div>
    #     """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Featured Projects Section
    st.markdown("""
    <div class="section-card">
        <h2 style="color: #00000; margin-bottom: 1rem;">🌟 Featured Projects</h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="project-card floating">
            <h3 class="project-title">Or-Komit</h3>
            <p>Online platform to simplify new member registration and data management for Komit community.</p>
            <span class="project-tech">HTML</span>
            <span class="project-tech">CSS</span>
            <span class="project-tech">JavaScript</span>
            <span class="project-tech">PHP</span>
            <span class="project-tech">MySQL</span>
            <span class="project-tech">Bootstrap</span>
            <p><a href="https://orkomit.treatstart.com/" target="_blank" style="color: #FFD700;">Live</a></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="project-card floating">
            <h3 class="project-title">SmartEye</h3>
            <p>Real-time object detection using YOLOv5 and Flutter for live camera, video, or images with high precision.</p>
            <span class="project-tech">Dart</span>
            <span class="project-tech">Python</span>
            <span class="project-tech">API</span>
            <p><a href="https://github.com/Zulkifli1409/smarteye" target="_blank" style="color: #FFD700;">GitHub Repo</a></p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(
            """
        <div class="project-card floating">
            <h3 class="project-title">X-Scraper</h3>
            <p>A Python-based tweet scraping tool for the X platform, featuring auto-login and robust filtering.</p>
            <span class="project-tech">Python</span>
            <p><a href="https://github.com/Zulkifli1409/X-Scraper" target="_blank" style="color: #FFD700;">GitHub Repo</a></p>
        </div>
        """,
            unsafe_allow_html=True,
        )
