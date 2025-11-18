import streamlit as st
import plotly.graph_objects as go
from security_middleware import secure_page_wrapper

@secure_page_wrapper
def app():
    st.markdown("""
    <style>
    /* Skills Page CSS dengan Tema Kuning-Hitam dan Animasi */

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Poppins:wght@300;400;600;700&display=swap');

/* Global Styles untuk Skills Page */
.stApp {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 50%, #1a1a1a 100%);
        font-family: 'Poppins', sans-serif;
    }

/* Animated Background Pattern */
.stApp::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
        radial-gradient(circle at 20% 80%, rgba(255, 215, 0, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(255, 165, 0, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 40% 40%, rgba(255, 255, 0, 0.05) 0%, transparent 50%);
    animation: backgroundShift 10s ease-in-out infinite alternate;
    pointer-events: none;
    z-index: -1;
}

@keyframes backgroundShift {
    0% {
        transform: translateX(0) translateY(0) scale(1);
    }
    100% {
        transform: translateX(-20px) translateY(-20px) scale(1.1);
    }
}

/* Main Title Styling */
h1 {
    font-family: 'Orbitron', monospace !important;
    font-size: 3.5rem !important;
    font-weight: 900 !important;
    text-align: center !important;
    background: linear-gradient(45deg, #FFD700, #FFA500, #FFFF00, #FFD700) !important;
    background-size: 300% 300% !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    animation: gradientShift 3s ease-in-out infinite, titleGlow 2s ease-in-out infinite alternate !important;
    margin-bottom: 3rem !important;
    text-shadow: 0 0 30px rgba(255, 215, 0, 0.5) !important;
}

@keyframes gradientShift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

@keyframes titleGlow {
    from {
        filter: drop-shadow(0 0 20px #FFD700) drop-shadow(0 0 30px #FFA500);
    }
    to {
        filter: drop-shadow(0 0 30px #FFA500) drop-shadow(0 0 40px #FFFF00);
    }
}

/* Section Cards */
.section-card {
    background: linear-gradient(135deg, rgba(255, 215, 0, 0.1), rgba(255, 165, 0, 0.05));
    border: 2px solid transparent;
    background-clip: padding-box;
    border-radius: 20px;
    padding: 2rem;
    margin: 1.5rem 0;
    position: relative;
    backdrop-filter: blur(15px);
    box-shadow: 
        0 10px 30px rgba(0, 0, 0, 0.5),
        inset 0 1px 0 rgba(255, 215, 0, 0.2);
    animation: cardSlideIn 0.8s ease-out forwards;
    transform: translateY(30px);
    opacity: 0;
    overflow: hidden;
}

.section-card::before {
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
    animation: borderGlow 4s ease-in-out infinite;
    mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    mask-composite: exclude;
    z-index: -1;
}

@keyframes borderGlow {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

@keyframes cardSlideIn {
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

/* Staggered Animation untuk Cards */
.section-card:nth-child(1) { animation-delay: 0.2s; }
.section-card:nth-child(2) { animation-delay: 0.4s; }
.section-card:nth-child(3) { animation-delay: 0.6s; }
.section-card:nth-child(4) { animation-delay: 0.8s; }

/* Section Headers */
.section-card h3 {
    color: #FFD700 !important;
    font-family: 'Orbitron', monospace !important;
    font-weight: 700 !important;
    font-size: 1.5rem !important;
    text-align: center !important;
    margin-bottom: 2rem !important;
    position: relative !important;
    animation: headerPulse 2s ease-in-out infinite alternate !important;
}

.section-card h3::after {
    content: '';
    position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%);
    width: 60px;
    height: 3px;
    background: linear-gradient(90deg, #FFD700, #FFA500, #FFFF00);
    border-radius: 2px;
    animation: underlineExpand 1s ease-out 0.5s both;
}

@keyframes headerPulse {
    from { text-shadow: 0 0 10px rgba(255, 215, 0, 0.5); }
    to { text-shadow: 0 0 20px rgba(255, 215, 0, 0.8); }
}

@keyframes underlineExpand {
    from { width: 0; }
    to { width: 60px; }
}

/* Skill Container */
.skill-container {
    background: rgba(0, 0, 0, 0.3);
    border: 1px solid rgba(255, 215, 0, 0.3);
    border-radius: 15px;
    padding: 1.5rem;
    margin: 1rem 0;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    animation: skillFadeIn 0.6s ease-out forwards;
    transform: translateX(-30px);
    opacity: 0;
}

.skill-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 215, 0, 0.1), transparent);
    transition: left 0.6s ease;
}

.skill-container:hover::before {
    left: 100%;
}

.skill-container:hover {
    transform: translateY(-8px) scale(1.02);
    border-color: #FFD700;
    box-shadow: 
        0 20px 40px rgba(0, 0, 0, 0.4),
        0 0 20px rgba(255, 215, 0, 0.3);
    background: rgba(255, 215, 0, 0.05);
}

@keyframes skillFadeIn {
    to {
        transform: translateX(0);
        opacity: 1;
    }
}

/* Staggered Animation untuk Skills */
.skill-container:nth-child(1) { animation-delay: 0.1s; }
.skill-container:nth-child(2) { animation-delay: 0.2s; }
.skill-container:nth-child(3) { animation-delay: 0.3s; }
.skill-container:nth-child(4) { animation-delay: 0.4s; }
.skill-container:nth-child(5) { animation-delay: 0.5s; }

/* Skill Name */
.skill-name {
    font-family: 'Orbitron', monospace;
    font-weight: 600;
    font-size: 1.1rem;
    color: #FFD700;
    margin-bottom: 0.8rem;
    text-shadow: 0 0 10px rgba(255, 215, 0, 0.3);
    animation: textGlow 2s ease-in-out infinite alternate;
}

@keyframes textGlow {
    from { text-shadow: 0 0 10px rgba(255, 215, 0, 0.3); }
    to { text-shadow: 0 0 15px rgba(255, 215, 0, 0.6); }
}

/* Skill Bar Container */
.skill-bar {
    background: rgba(0, 0, 0, 0.5);
    border: 1px solid rgba(255, 215, 0, 0.2);
    border-radius: 25px;
    height: 12px;
    overflow: hidden;
    position: relative;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.3);
}

.skill-bar::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(90deg, 
        rgba(255, 215, 0, 0.1) 0%, 
        rgba(255, 215, 0, 0.05) 50%, 
        rgba(255, 215, 0, 0.1) 100%);
    animation: shimmer 3s ease-in-out infinite;
}

@keyframes shimmer {
    0%, 100% { transform: translateX(-100%); }
    50% { transform: translateX(100%); }
}

/* Skill Progress */
.skill-progress {
    height: 100%;
    background: linear-gradient(90deg, #FFD700, #FFA500, #FFFF00);
    border-radius: 25px;
    position: relative;
    animation: progressLoad 2s ease-out forwards;
    transform-origin: left;
    transform: scaleX(0);
    box-shadow: 
        0 0 10px rgba(255, 215, 0, 0.5),
        inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

.skill-progress::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(90deg, 
        rgba(255, 255, 255, 0.2), 
        transparent 30%, 
        transparent 70%, 
        rgba(255, 255, 255, 0.2));
    animation: progressShine 2s ease-in-out infinite;
}

@keyframes progressLoad {
    to {
        transform: scaleX(1);
    }
}

@keyframes progressShine {
    0%, 100% { transform: translateX(-100%); }
    50% { transform: translateX(200%); }
}

/* Percentage Text */
.skill-container div[style*="text-align: right"] {
    font-family: 'Orbitron', monospace !important;
    font-weight: 600 !important;
    color: #FFA500 !important;
    font-size: 0.9rem !important;
    margin-top: 0.5rem !important;
    animation: percentagePulse 2s ease-in-out infinite alternate !important;
}

@keyframes percentagePulse {
    from { color: #FFA500; }
    to { color: #FFD700; }
}

/* Plotly Chart Customization */
.js-plotly-plot {
    background: rgba(255, 215, 0, 0.02) !important;
    border: 2px solid rgba(255, 215, 0, 0.3) !important;
    border-radius: 20px !important;
    padding: 1rem !important;
    margin: 2rem 0 !important;
    animation: chartFadeIn 1s ease-out !important;
}

@keyframes chartFadeIn {
    from {
        opacity: 0;
        transform: scale(0.9);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

/* Floating Particles Effect */
.section-card::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
        radial-gradient(circle at 10% 20%, rgba(255, 215, 0, 0.1) 0%, transparent 1%),
        radial-gradient(circle at 90% 80%, rgba(255, 165, 0, 0.1) 0%, transparent 1%),
        radial-gradient(circle at 50% 50%, rgba(255, 255, 0, 0.05) 0%, transparent 1%);
    animation: particles 8s linear infinite;
    pointer-events: none;
    z-index: 1;
}

@keyframes particles {
    0%, 100% {
        transform: translateY(0) rotate(0deg);
        opacity: 1;
    }
    50% {
        transform: translateY(-20px) rotate(180deg);
        opacity: 0.7;
    }
}

/* Responsive Design */
@media (max-width: 768px) {
    h1 {
        font-size: 2.5rem !important;
    }
    
    .section-card {
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .section-card h3 {
        font-size: 1.3rem !important;
    }
    
    .skill-container {
        padding: 1rem;
    }
    
    .skill-name {
        font-size: 1rem;
    }
}

@media (max-width: 480px) {
    h1 {
        font-size: 2rem !important;
    }
    
    .section-card {
        padding: 1rem;
    }
    
    .section-card h3 {
        font-size: 1.2rem !important;
    }
}
    </style>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="section-card">
        <h1 style="color: #333; margin-bottom: 2rem;">Technical Skills</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Programming Languages
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="section-card">
            <h3 style="color: #667eea; margin-bottom: 1.5rem;">💻 Programming Languages</h3>
        </div>
        """, unsafe_allow_html=True)
        
        skills_prog = {
            "Python": 60,
            "JavaScript": 50,
            "SQL": 70,
            "C": 50
        }
        
        for skill, level in skills_prog.items():
            st.markdown(f"""
            <div class="skill-container">
                <div class="skill-name">{skill}</div>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: {level}%;"></div>
                </div>
                <div style="text-align: right; font-size: 0.9rem; color: #667eea; margin-top: 0.2rem;">{level}%</div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="section-card">
            <h3 style="color: #667eea; margin-bottom: 1.5rem;">🌐 Web Technologies</h3>
        </div>
        """, unsafe_allow_html=True)
        
        skills_web = {
            "React.js": 30,
            "HTML/CSS": 80,
            "Flask": 60
        }
        
        for skill, level in skills_web.items():
            st.markdown(f"""
            <div class="skill-container">
                <div class="skill-name">{skill}</div>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: {level}%;"></div>
                </div>
                <div style="text-align: right; font-size: 0.9rem; color: #667eea; margin-top: 0.2rem;">{level}%</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Data Science & ML
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
        <div class="section-card">
            <h3 style="color: #667eea; margin-bottom: 1.5rem;">🤖 Data Science & ML</h3>
        </div>
        """, unsafe_allow_html=True)
        
        skills_ds = {
            "TensorFlow": 10,
            "Scikit-learn": 10,
            "Pandas": 40,
            "NumPy": 40,
            "Matplotlib": 30
        }
        
        for skill, level in skills_ds.items():
            st.markdown(f"""
            <div class="skill-container">
                <div class="skill-name">{skill}</div>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: {level}%;"></div>
                </div>
                <div style="text-align: right; font-size: 0.9rem; color: #667eea; margin-top: 0.2rem;">{level}%</div>
            </div>
            """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="section-card">
            <h3 style="color: #667eea; margin-bottom: 1.5rem;">☁️ Tools & Platforms</h3>
        </div>
        """, unsafe_allow_html=True)
        
        skills_tools = {
            "AWS": 50,
            "Docker": 20,
            "Git": 80,
            "PostgreSQL": 50
        }
        
        for skill, level in skills_tools.items():
            st.markdown(f"""
            <div class="skill-container">
                <div class="skill-name">{skill}</div>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: {level}%;"></div>
                </div>
                <div style="text-align: right; font-size: 0.9rem; color: #667eea; margin-top: 0.2rem;">{level}%</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Skills Radar Chart
    st.markdown("""
    <div class="section-card">
        <h3 style="color: #667eea; margin-bottom: 1.5rem;">📊 Skills Overview</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Create radar chart
    categories = ['Programming', 'Web', 'Data Science', 'Tools']
    # Rata-rata persentase tiap kategori (bisa kamu sesuaikan)
    values = [
        sum(skills_prog.values())/len(skills_prog),
        sum(skills_web.values())/len(skills_web),
        sum(skills_ds.values())/len(skills_ds),
        sum(skills_tools.values())/len(skills_tools),
    ]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        fillcolor='rgba(102, 126, 234, 0.2)',
        line=dict(color='rgba(102, 126, 234, 1)', width=2),
        name='Skills Level'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=False,
        title="Skills Proficiency Level",
        font=dict(size=14),
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
