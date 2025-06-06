import streamlit as st


def app():
    st.markdown(
        """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 50%, #1a1a1a 100%);
        font-family: 'Poppins', sans-serif;
    }
    
    /* Main title styling */
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(45deg, #FFD700, #FFA500, #FFFF00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 2rem;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from {
            text-shadow: 0 0 20px #FFD700, 0 0 30px #FFD700, 0 0 40px #FFD700;
        }
        to {
            text-shadow: 0 0 30px #FFA500, 0 0 40px #FFA500, 0 0 50px #FFA500;
        }
    }
    
    /* Profile section styling */
    .profile-section {
        background: rgba(255, 215, 0, 0.1);
        border: 2px solid #FFD700;
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 30px rgba(255, 215, 0, 0.3);
        animation: slideInLeft 1s ease-out;
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Avatar container */
    .avatar-container {
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-10px);
        }
    }
    
    /* Section headers */
    .section-header {
        font-size: 2rem;
        font-weight: 600;
        color: #FFD700;
        margin: 2rem 0 1rem 0;
        text-align: center;
        position: relative;
        animation: fadeInUp 1s ease-out;
    }
    
    .section-header::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 3px;
        background: linear-gradient(90deg, #FFD700, #FFA500, #FFFF00);
        animation: expandWidth 1s ease-out 0.5s both;
    }
    
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
    
    @keyframes expandWidth {
        from {
            width: 0;
        }
        to {
            width: 100px;
        }
    }
    
    /* Service cards */
    .service-card {
        background: linear-gradient(135deg, rgba(255, 215, 0, 0.15), rgba(255, 165, 0, 0.15));
        border: 1px solid #FFD700;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
        animation: fadeInUp 1s ease-out;
        position: relative;
        overflow: hidden;
    }
    
    .service-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 215, 0, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .service-card:hover::before {
        left: 100%;
    }
    
    .service-card:hover {
        transform: translateY(-10px) scale(1.05);
        box-shadow: 0 20px 40px rgba(255, 215, 0, 0.4);
        border-color: #FFA500;
    }
    
    /* Text styling */
    .main-text {
        color: #f0f0f0;
        font-size: 1.1rem;
        line-height: 1.8;
        text-align: justify;
        animation: fadeIn 1s ease-out 0.5s both;
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    
    /* Stats section */
    .stats-container {
        background: rgba(0, 0, 0, 0.7);
        border: 2px solid #FFD700;
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        animation: slideInUp 1s ease-out;
    }
    
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(50px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Metric styling */
    .metric-container {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(135deg, rgba(255, 215, 0, 0.1), rgba(255, 165, 0, 0.1));
        border-radius: 15px;
        margin: 0.5rem;
        transition: all 0.3s ease;
        animation: bounceIn 1s ease-out;
    }
    
    .metric-container:hover {
        transform: scale(1.1);
        background: linear-gradient(135deg, rgba(255, 215, 0, 0.2), rgba(255, 165, 0, 0.2));
    }
    
    @keyframes bounceIn {
        0%, 20%, 40%, 60%, 80%, 100% {
            transition-timing-function: cubic-bezier(0.215, 0.610, 0.355, 1.000);
        }
        0% {
            opacity: 0;
            transform: scale3d(.3, .3, .3);
        }
        20% {
            transform: scale3d(1.1, 1.1, 1.1);
        }
        40% {
            transform: scale3d(.9, .9, .9);
        }
        60% {
            opacity: 1;
            transform: scale3d(1.03, 1.03, 1.03);
        }
        80% {
            transform: scale3d(.97, .97, .97);
        }
        100% {
            opacity: 1;
            transform: scale3d(1, 1, 1);
        }
    }
    
    /* Education section */
    .education-item {
        background: rgba(255, 215, 0, 0.05);
        border-left: 4px solid #FFD700;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 0 15px 15px 0;
        transition: all 0.3s ease;
        animation: slideInRight 1s ease-out;
    }
    
    .education-item:hover {
        background: rgba(255, 215, 0, 0.15);
        transform: translateX(10px);
        box-shadow: 0 5px 15px rgba(255, 215, 0, 0.3);
    }
    
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Divider styling */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #FFD700, transparent);
        margin: 3rem 0;
        animation: fadeIn 1s ease-out;
    }
    
    /* Pulse animation for important elements */
    .pulse {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% {
            box-shadow: 0 0 0 0 rgba(255, 215, 0, 0.7);
        }
        70% {
            box-shadow: 0 0 0 10px rgba(255, 215, 0, 0);
        }
        100% {
            box-shadow: 0 0 0 0 rgba(255, 215, 0, 0);
        }
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem;
        }
        .section-header {
            font-size: 1.5rem;
        }
        .profile-section {
            padding: 1rem;
        }
    }
</style>
    """,
        unsafe_allow_html=True,
    )

    # Header dengan animasi
    st.markdown('<h1 class="main-title">👨‍💻 About Me</h1>', unsafe_allow_html=True)

    # Profile section menggunakan container khusus
    st.markdown('<div class="profile-section">', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(
            '<div class="section-header">Hello! I\'m Zulkifli</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class="main-text">
        I’m Zulkifli, a 6th-semester IT student at Politeknik Negeri Lhokseumawe, based in Aceh. 
        I’m passionate about full stack web development and also deeply interested in cybersecurity, 
        AI, and building tech tools that solve real-world problems.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class="main-text">
        So far, I've worked on several projects, including an open recruitment website 
        for a student community and various campus-based applications. I love working 
        with technologies like Python, PHP, Flutter, C, and MySQL to bring ideas to life.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class="main-text">
        My dream is to build a tech startup that contributes to the development of Aceh, 
        by creating impactful digital solutions and empowering the local community through innovation.
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        # Avatar dengan animasi float
        st.markdown(
            """
       <div class="avatar-container" style="text-align: center; margin-top: 7rem;">
            <div class="pulse" style="width: 300px; height: 300px; 
                        background: linear-gradient(135deg, #FFD700 0%, #FFA500 50%, #FFFF00 100%); 
                        border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                        font-size: 3rem; color: #000; margin: 0 auto; border: 4px solid #FFA500; overflow: hidden;">
                <img src="https://i.ibb.co/nMkDyMgd/97692902.jpg" alt="Foto Kamu" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%;">
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")

    # What I Do section
    st.markdown(
        '<div class="section-header">🚀 What I Do</div>', unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        <div class="service-card">
            <h4 style="color: #FFD700; margin-bottom: 1rem;">🌐 Full Stack Web Development</h4>
            <p style="color: #f0f0f0;">
            Building responsive and dynamic web applications using technologies like PHP, Python, MySQL, and Flutter.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class="service-card">
            <h4 style="color: #FFD700; margin-bottom: 1rem;">🔐 Cybersecurity Enthusiast</h4>
            <p style="color: #f0f0f0;">
            Exploring system and network security, and learning how to build basic tools to understand how systems can be protected.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="service-card">
            <h4 style="color: #FFD700; margin-bottom: 1rem;">🛠️ Tool & Script Development</h4>
            <p style="color: #f0f0f0;">
            Creating command-line tools and automation scripts using Python and C for learning and solving real-world tasks.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class="service-card">
            <h4 style="color: #FFD700; margin-bottom: 1rem;">🖥️ Self-Hosted Server Setup</h4>
            <p style="color: #f0f0f0;">
            Setting up personal servers with Proxmox, and installing services like Nextcloud for hands-on virtualization and infrastructure experience.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # Personal Interests
    st.markdown(
        '<div class="section-header">🎯 Personal Interests</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
    <div class="main-text">
    When I'm not coding or studying, I enjoy exploring emerging technologies like cybersecurity and AI, 
    experimenting with personal server setups, and working on side projects that challenge my skills. 
    I’m also passionate about contributing to open-source, learning new programming languages, 
    and dreaming of building a tech startup to support development in Aceh.
    </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Education & Certifications
    st.markdown(
        '<div class="section-header">🎓 Education & Certifications</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="education-item">
        <h4 style="color: #FFD700; margin-bottom: 0.5rem;">D4 Information Technology and Computer Science (Informatics Engineering)</h4>
        <p style="color: #FFA500; font-weight: 600;">Politeknik Negeri Lhokseumawe (2022 - 2026, Semester 6)</p>
        <p style="color: #f0f0f0;">Currently pursuing a diploma with focus on information technology and computer science.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
    <div class="education-item">
        <h4 style="color: #FFD700; margin-bottom: 0.5rem;">Code Generation and Optimization Using IBM Granite</h4>
        <p style="color: #FFA500; font-weight: 600;">IBM (2025)</p>
        <p style="color: #f0f0f0;">Training on code generation and optimization techniques using IBM Granite platform.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="education-item">
        <h4 style="color: #FFD700; margin-bottom: 0.5rem;">Junior Mobile Programmer</h4>
        <p style="color: #FFA500; font-weight: 600;">Vocational School Graduate Academy - Kominfo/Digitalent (2024)</p>
        <p style="color: #f0f0f0;">Basic training in mobile application programming and development.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="education-item">
        <h4 style="color: #FFD700; margin-bottom: 0.5rem;">ACA Business User Hands-on</h4>
        <p style="color: #FFA500; font-weight: 600;">Alibaba Cloud Global (2024)</p>
        <p style="color: #f0f0f0;">Hands-on training for business users on the Alibaba Cloud platform.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="education-item">
        <h4 style="color: #FFD700; margin-bottom: 0.5rem;">Alibaba Cloud Certified Developers</h4>
        <p style="color: #FFA500; font-weight: 600;">Alibaba Cloud Global (2024)</p>
        <p style="color: #f0f0f0;">Certification for cloud developers focusing on Alibaba Cloud technologies.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="education-item">
        <h4 style="color: #FFD700; margin-bottom: 0.5rem;">Junior Web Developer / Entry-Level Web Developer</h4>
        <p style="color: #FFA500; font-weight: 600;">Badan Nasional Sertifikasi Profesi (BNSP) (2023)</p>
        <p style="color: #f0f0f0;">Official certification of competency in entry-level web development.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="education-item">
        <h4 style="color: #FFD700; margin-bottom: 0.5rem;">Junior Web Developer</h4>
        <p style="color: #FFA500; font-weight: 600;">Vocational School Graduate Academy - Kominfo/Digitalent (2023)</p>
        <p style="color: #f0f0f0;">Fundamental web development training supporting fullstack skills.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )


    # Stats section
    st.markdown("---")
    # st.markdown(
    #     '<div class="section-header">📊 Quick Stats</div>', unsafe_allow_html=True
    # )

    # st.markdown('<div class="stats-container">', unsafe_allow_html=True)
    # col1, col2, col3, col4 = st.columns(4)

    # with col1:
    #     st.markdown(
    #         """
    #     <div class="metric-container">
    #         <h2 style="color: #FFD700; font-size: 2.5rem; margin: 0;">5+</h2>
    #         <p style="color: #f0f0f0; margin: 0.5rem 0 0 0;">Years Experience</p>
    #     </div>
    #     """,
    #         unsafe_allow_html=True,
    #     )

    # with col2:
    #     st.markdown(
    #         """
    #     <div class="metric-container">
    #         <h2 style="color: #FFD700; font-size: 2.5rem; margin: 0;">50+</h2>
    #         <p style="color: #f0f0f0; margin: 0.5rem 0 0 0;">Projects Completed</p>
    #     </div>
    #     """,
    #         unsafe_allow_html=True,
    #     )

    # with col3:
    #     st.markdown(
    #         """
    #     <div class="metric-container">
    #         <h2 style="color: #FFD700; font-size: 2.5rem; margin: 0;">25+</h2>
    #         <p style="color: #f0f0f0; margin: 0.5rem 0 0 0;">Happy Clients</p>
    #     </div>
    #     """,
    #         unsafe_allow_html=True,
    #     )

    # with col4:
    #     st.markdown(
    #         """
    #     <div class="metric-container">
    #         <h2 style="color: #FFD700; font-size: 2.5rem; margin: 0;">3</h2>
    #         <p style="color: #f0f0f0; margin: 0.5rem 0 0 0;">Certifications</p>
    #     </div>
    #     """,
    #         unsafe_allow_html=True,
    #     )

    # st.markdown("</div>", unsafe_allow_html=True)
