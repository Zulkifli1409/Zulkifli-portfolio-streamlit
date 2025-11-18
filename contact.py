import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import re
import html
import hashlib
import time

# Import email configuration
try:
    from email_config import EMAIL_CONFIG
except ImportError:
    # Default configuration if email_config.py doesn't exist
    EMAIL_CONFIG = {
        "enabled": False,
        "sender_email": "your-email@gmail.com",
        "sender_password": "your-app-password",
        "receiver_email": "zul140904@gmail.com",
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 465
    }

# Rate limiting setup
if 'last_submission_time' not in st.session_state:
    st.session_state.last_submission_time = 0
if 'submission_count' not in st.session_state:
    st.session_state.submission_count = 0

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validate phone format (optional, allows empty)"""
    if not phone:
        return True
    # Allow international formats: +, digits, spaces, hyphens
    pattern = r'^[\+]?[\d\s\-\(\)]+$'
    return re.match(pattern, phone) is not None

def sanitize_input(text):
    """Sanitize user input to prevent XSS and injection attacks"""
    if not text:
        return ""
    # Remove HTML tags and escape special characters
    text = html.escape(str(text))
    # Remove any potential script tags
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.IGNORECASE | re.DOTALL)
    return text.strip()

def check_rate_limit():
    """Check if user is submitting too frequently (anti-spam)"""
    current_time = time.time()
    time_since_last = current_time - st.session_state.last_submission_time
    
    # Reset counter after 1 hour
    if time_since_last > 3600:
        st.session_state.submission_count = 0
    
    # Allow max 3 submissions per hour
    if st.session_state.submission_count >= 3 and time_since_last < 3600:
        return False, f"Too many submissions. Please try again in {int((3600 - time_since_last) / 60)} minutes."
    
    # Require at least 30 seconds between submissions
    if time_since_last < 30:
        return False, f"Please wait {int(30 - time_since_last)} seconds before submitting again."
    
    return True, None

st.markdown(
    """
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet">
""",
    unsafe_allow_html=True,
)

def send_email(name, email, company, phone, subject, message, budget):
    """Send email notification when form is submitted (with security measures)"""
    
    # Check if email is enabled
    if not EMAIL_CONFIG.get("enabled", False):
        return False
    
    try:
        # Sanitize all inputs
        name = sanitize_input(name)
        email = sanitize_input(email)
        company = sanitize_input(company)
        phone = sanitize_input(phone)
        subject = sanitize_input(subject)
        message = sanitize_input(message)
        budget = sanitize_input(budget)
        
        # Get email configuration
        sender_email = EMAIL_CONFIG["sender_email"]
        sender_password = EMAIL_CONFIG["sender_password"]
        receiver_email = EMAIL_CONFIG["receiver_email"]
        smtp_server = EMAIL_CONFIG["smtp_server"]
        smtp_port = EMAIL_CONFIG["smtp_port"]
        
        # Create message
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"New Contact Form: {subject}"
        msg["From"] = sender_email
        msg["To"] = receiver_email
        
        # Create HTML email body
        html = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px; background-color: #f4f4f4;">
                    <div style="background-color: #ffc107; padding: 20px; text-align: center;">
                        <h1 style="color: #1a1a1a; margin: 0;">New Contact Form Submission</h1>
                    </div>
                    <div style="background-color: white; padding: 30px; margin-top: 20px; border-radius: 5px;">
                        <h2 style="color: #ffc107; border-bottom: 2px solid #ffc107; padding-bottom: 10px;">Contact Details</h2>
                        <table style="width: 100%; margin: 20px 0;">
                            <tr>
                                <td style="padding: 10px; font-weight: bold; width: 150px;">Name:</td>
                                <td style="padding: 10px;">{name}</td>
                            </tr>
                            <tr style="background-color: #f9f9f9;">
                                <td style="padding: 10px; font-weight: bold;">Email:</td>
                                <td style="padding: 10px;">{email}</td>
                            </tr>
                            <tr>
                                <td style="padding: 10px; font-weight: bold;">Company:</td>
                                <td style="padding: 10px;">{company if company else 'Not provided'}</td>
                            </tr>
                            <tr style="background-color: #f9f9f9;">
                                <td style="padding: 10px; font-weight: bold;">Phone:</td>
                                <td style="padding: 10px;">{phone if phone else 'Not provided'}</td>
                            </tr>
                            <tr>
                                <td style="padding: 10px; font-weight: bold;">Project Type:</td>
                                <td style="padding: 10px;">{subject}</td>
                            </tr>
                            <tr style="background-color: #f9f9f9;">
                                <td style="padding: 10px; font-weight: bold;">Budget:</td>
                                <td style="padding: 10px;">{budget}</td>
                            </tr>
                        </table>
                        
                        <h2 style="color: #ffc107; border-bottom: 2px solid #ffc107; padding-bottom: 10px; margin-top: 30px;">Project Details</h2>
                        <div style="padding: 15px; background-color: #f9f9f9; border-left: 4px solid #ffc107; margin: 20px 0;">
                            {message.replace(chr(10), '<br>')}
                        </div>
                        
                        <div style="margin-top: 30px; padding: 15px; background-color: #e8f5e9; border-radius: 5px;">
                            <p style="margin: 0; color: #2e7d32;">
                                <strong>📅 Submitted:</strong> {datetime.now().strftime('%B %d, %Y at %I:%M %p WIB')}
                            </p>
                        </div>
                    </div>
                    <div style="text-align: center; margin-top: 20px; color: #666; font-size: 12px;">
                        <p>This email was sent from your portfolio contact form</p>
                    </div>
                </div>
            </body>
        </html>
        """
        
        # Attach HTML content
        part = MIMEText(html, "html")
        msg.attach(part)
        
        # Send email via SMTP
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        
        return True
    except Exception as e:
        print(f"Error sending email: {str(e)}")  # Log to console instead of showing to user
        return False

def app():
    st.markdown(
        """
    <style>
.stApp {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 50%, #1a1a1a 100%);
        font-family: 'Poppins', sans-serif;
    }
/* Global Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 50%, #1a1a1a 100%);
    color: #ffffff;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    overflow-x: hidden;
}

/* Animated Background */
.main > div {
    position: relative;
}

.main > div::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
        radial-gradient(circle at 20% 50%, rgba(255, 193, 7, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(255, 235, 59, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 40% 80%, rgba(255, 193, 7, 0.08) 0%, transparent 50%);
    animation: backgroundFloat 20s ease-in-out infinite;
    z-index: -1;
}

@keyframes backgroundFloat {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    33% { transform: translateY(-20px) rotate(1deg); }
    66% { transform: translateY(10px) rotate(-1deg); }
}

/* Hero Section */
.contact-hero {
    background: linear-gradient(135deg, #ffc107 0%, #ffeb3b 50%, #fbc02d 100%);
    color: #1a1a1a;
    text-align: center;
    padding: 4rem 2rem;
    border-radius: 20px;
    margin-bottom: 3rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 40px rgba(255, 193, 7, 0.3);
    animation: heroGlow 3s ease-in-out infinite alternate;
}

@keyframes heroGlow {
    0% { box-shadow: 0 20px 40px rgba(255, 193, 7, 0.3); }
    100% { box-shadow: 0 25px 50px rgba(255, 193, 7, 0.5); }
}

.contact-hero::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
    animation: heroShine 6s linear infinite;
}

@keyframes heroShine {
    0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
    100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
}

.contact-hero h1 {
        -webkit-text-fill-color: black !important;
    background: none !important;
    -webkit-background-clip: border-box !important;
    font-size: 3.5rem;
    color: white !important;
    font-weight: 800;
    margin-bottom: 1rem;
    animation: titleBounce 2s ease-out;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}

@keyframes titleBounce {
    0% { transform: translateY(-100px) opacity(0); }
    50% { transform: translateY(10px); }
    100% { transform: translateY(0) opacity(1); }
}

.availability-badge {
    display: inline-block;
    background: #1a1a1a;
    color: #ffc107;
    padding: 0.8rem 2rem;
    border-radius: 50px;
    font-weight: 600;
    margin-top: 2rem;
    animation: badgePulse 2s ease-in-out infinite;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

@keyframes badgePulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}

/* Contact Containers */
.contact-container, .response-container {
    background: linear-gradient(135deg, #2d2d2d 0%, #1a1a1a 100%);
    padding: 2rem;
    border-radius: 15px;
    border: 2px solid #ffc107;
    margin-bottom: 2rem;
    position: relative;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    animation: containerSlideIn 1s ease-out;
}

@keyframes containerSlideIn {
    0% { transform: translateX(-50px); opacity: 0; }
    100% { transform: translateX(0); opacity: 1); }
}

.contact-container:hover, .response-container:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(255, 193, 7, 0.2);
    border-color: #ffeb3b;
}

.contact-container h3, .response-container h3 {
    color: #ffc107;
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
    animation: textGlow 2s ease-in-out infinite alternate;
}

@keyframes textGlow {
    0% { text-shadow: 0 0 5px rgba(255, 193, 7, 0.5); }
    100% { text-shadow: 0 0 15px rgba(255, 193, 7, 0.8); }
}

/* Contact Items */
.contact-item, .response-item {
    background: rgba(255, 193, 7, 0.1);
    padding: 0.1rem;
    border-radius: 10px;
    margin-bottom: 0.5rem;
    border-left: 4px solid #ffc107;
    transition: all 0.3s ease;
    animation: itemFadeIn 1s ease-out;
}

@keyframes itemFadeIn {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}

.contact-item:hover, .response-item:hover {
    background: rgba(255, 193, 7, 0.2);
    transform: translateX(10px);
    border-left-width: 6px;
}

.contact-link {
    color: #ffeb3b !important;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.3s ease;
    position: relative;
}

.contact-link::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    width: 0;
    height: 2px;
    background: #ffc107;
    transition: width 0.3s ease;
}

.contact-link:hover {
    color: #ffc107 !important;
    text-shadow: 0 0 10px rgba(255, 193, 7, 0.5);
}

.contact-link:hover::after {
    width: 100%;
}

/* Contact Cards */
.contact-card {
    background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
    padding: 3rem 2rem;
    border-radius: 20px;
    margin: 2rem 0;
    border: 2px solid #ffc107;
    position: relative;
    overflow: hidden;
    animation: cardFloat 6s ease-in-out infinite;
}

@keyframes cardFloat {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

.contact-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 193, 7, 0.1), transparent);
    transition: left 0.5s ease;
}

.contact-card:hover::before {
    left: 100%;
}

.contact-card h3 {
    color: #ffc107;
    margin-bottom: 1rem;
    animation: headingPulse 3s ease-in-out infinite;
}

@keyframes headingPulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.02); }
}

/* CTA Buttons */
.cta-buttons {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: center;
    margin-top: 2rem;
}

.cta-button {
    background: linear-gradient(135deg, #ffc107 0%, #ffeb3b 100%);
    color: #1a1a1a !important;
    padding: 1rem 2rem;
    border-radius: 50px;
    text-decoration: none !important;  /* ⬅️ ini kunci hilangkan underline */
    font-weight: 700;
    font-size: 1rem;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 10px 20px rgba(255, 193, 7, 0.3);
    position: relative;
    overflow: hidden;
    animation: buttonBounce 3s ease-in-out infinite;
}

@keyframes buttonBounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-5px); }
}

.cta-button::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    background: rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    transition: all 0.3s ease;
    transform: translate(-50%, -50%);
}

.cta-button:hover {
    transform: translateY(-8px) scale(1.05);
    box-shadow: 0 20px 40px rgba(255, 193, 7, 0.4);
    color: #1a1a1a !important;
}

.cta-button:hover::before {
    width: 300px;
    height: 300px;
}

/* Social Links */
.social-links {
        display: flex;
        justify-content: center;
        gap: 3rem;  /* Increased gap between icons */
        margin: 2rem 0;
        flex-wrap: wrap;
    }

    .social-links a {
        font-size: 3.5rem !important;  /* Increased icon size */
        color: #ffc107;
        transition: all 0.3s ease;
        margin: 0 10px;
    }

    .social-links a:hover {
        color: #ffeb3b;
        transform: scale(1.2) rotate(5deg);
    }

.social-link {
    display: inline-block;
    font-size: 2.5rem;
    padding: 1rem;
    background: linear-gradient(135deg, #ffc107 0%, #ffeb3b 100%);
    color: #1a1a1a;
    border-radius: 50%;
    text-decoration: none;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 10px 20px rgba(255, 193, 7, 0.3);
    animation: socialFloat 4s ease-in-out infinite;
}

.social-link:nth-child(odd) {
    animation-delay: 0.5s;
}

@keyframes socialFloat {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-15px) rotate(5deg); }
}

.social-link:hover {
    transform: translateY(-10px) scale(1.2) rotate(15deg);
    box-shadow: 0 20px 40px rgba(255, 193, 7, 0.5);
    background: linear-gradient(135deg, #ffeb3b 0%, #ffc107 100%);
}

/* Form Styles */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div > div > div {
    background: rgba(255, 193, 7, 0.1) !important;
    border: 2px solid #ffc107 !important;
    border-radius: 10px !important;
    color: #ffffff !important;
    transition: all 0.3s ease !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus,
.stSelectbox > div > div > div > div:focus {
    border-color: #ffeb3b !important;
    box-shadow: 0 0 20px rgba(255, 193, 7, 0.3) !important;
    transform: scale(1.02) !important;
}

.stButton > button {
    background: linear-gradient(135deg, #ffc107 0%, #ffeb3b 100%) !important;
    color: #1a1a1a !important;
    border: none !important;
    border-radius: 50px !important;
    font-weight: 700 !important;
    font-size: 1.1rem !important;
    padding: 0.8rem 2rem !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 10px 20px rgba(255, 193, 7, 0.3) !important;
    animation: submitPulse 2s ease-in-out infinite !important;
}

@keyframes submitPulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.02); }
}

.stButton > button:hover {
    transform: translateY(-5px) scale(1.05) !important;
    box-shadow: 0 20px 40px rgba(255, 193, 7, 0.4) !important;
}

/* Expander Styles */
.streamlit-expanderHeader {
    background: rgba(255, 193, 7, 0.1) !important;
    border: 2px solid #ffc107 !important;
    border-radius: 10px !important;
    color: #ffc107 !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

.streamlit-expanderHeader:hover {
    background: rgba(255, 193, 7, 0.2) !important;
    transform: translateX(10px) !important;
}

.streamlit-expanderContent {
    background: rgba(26, 26, 26, 0.9) !important;
    border: 2px solid #ffc107 !important;
    border-top: none !important;
    border-radius: 0 0 10px 10px !important;
    color: #ffffff !important;
    animation: expanderSlide 0.5s ease-out !important;
}

@keyframes expanderSlide {
    0% { opacity: 0; transform: translateY(-20px); }
    100% { opacity: 1; transform: translateY(0); }
}

/* Success/Error Messages */
.stSuccess {
    background: linear-gradient(135deg, #4caf50 0%, #8bc34a 100%) !important;
    border: 2px solid #4caf50 !important;
    border-radius: 15px !important;
    animation: successSlide 0.5s ease-out !important;
}

@keyframes successSlide {
    0% { transform: translateX(-100%); opacity: 0; }
    100% { transform: translateX(0); opacity: 1; }
}

.stError {
    background: linear-gradient(135deg, #f44336 0%, #ff5722 100%) !important;
    border: 2px solid #f44336 !important;
    border-radius: 15px !important;
    animation: errorShake 0.5s ease-out !important;
}

@keyframes errorShake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-10px); }
    75% { transform: translateX(10px); }
}

/* Responsive Design */
@media (max-width: 768px) {
    .contact-hero h1 {
        font-size: 2.5rem;
    }
    
    .cta-buttons {
        flex-direction: column;
        align-items: center;
    }
    
    .cta-button {
        width: 100%;
        max-width: 300px;
    }
    
    .social-links {
        gap: 1rem;
    }
    
    .social-link {
        font-size: 2rem;
        padding: 0.8rem;
    }
}

/* Loading Animation */
@keyframes loading {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* Particle Effect */
.contact-hero::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
        radial-gradient(circle at 25% 25%, rgba(255, 193, 7, 0.2) 2px, transparent 2px),
        radial-gradient(circle at 75% 75%, rgba(255, 235, 59, 0.2) 1px, transparent 1px);
    background-size: 50px 50px, 30px 30px;
    animation: particleFloat 10s linear infinite;
    pointer-events: none;
}

@keyframes particleFloat {
    0% { transform: translateY(0px) translateX(0px); }
    100% { transform: translateY(-100px) translateX(50px); }
}
    </style>
    """,
        unsafe_allow_html=True,
    )

    # Hero Section
    st.markdown(
        """
    <div class="contact-hero">
        <h1 style="color: white; margin-bottom: 1rem;">📞 Let's Connect!</h1>
        <p style="font-size: 1.2rem; margin-bottom: 1rem; opacity: 0.9;">
            Ready to discuss your next project or explore collaboration opportunities?
        </p>
        <p style="font-size: 1rem; opacity: 0.8;">
            I'm always excited to hear about new challenges and innovative ideas.
        </p>
        <div class="availability-badge">
            🟢 Available for new projects
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Contact Methods
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="contact-container">', unsafe_allow_html=True)
        st.markdown("### 📬 Get In Touch")

        st.markdown('<div class="contact-item">', unsafe_allow_html=True)
        st.markdown("**📧 Email**")
        st.markdown(
            '<a href="mailto:zul140904@example.com" class="contact-link">zul140904@gmail.com</a>',
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="contact-item">', unsafe_allow_html=True)
        st.markdown("**📱 Phone / WhatsApp**")
        st.markdown(
            '<a href="tel:+6289508109402" class="contact-link">+62 895-0810-9402</a>',
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="contact-item">', unsafe_allow_html=True)
        st.markdown("**💼 LinkedIn**")
        st.markdown(
            '<a href="https://linkedin.com/in/zulkifli1409" class="contact-link" target="_blank">linkedin.com/in/zulkifli1409</a>',
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="contact-item">', unsafe_allow_html=True)
        st.markdown("**🐙 GitHub**")
        st.markdown(
            '<a href="https://github.com/zulkifli1409" class="contact-link" target="_blank">github.com/zulkifli1409</a>',
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="response-container">', unsafe_allow_html=True)
        st.markdown("### ⏰ Response Time")

        st.markdown('<div class="response-item">', unsafe_allow_html=True)
        st.markdown("**⚡ Quick Response Guaranteed**")
        st.markdown("""
        • Email: Within 24 hours  
        • WhatsApp: Within 2-4 hours  
        • LinkedIn: Within 24 hours
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="response-item">', unsafe_allow_html=True)
        st.markdown("**🌍 Location & Timezone**")
        st.markdown("""
        📍 Aceh, Lhokseumawe, Indonesia  
        🕐 UTC+7 (WIB - Western Indonesia Time)  
        💻 Available for remote collaboration worldwide
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="response-item">', unsafe_allow_html=True)
        st.markdown("**🎯 Best Time to Reach**")
        st.markdown("""
        Monday - Friday: 9:00 AM - 6:00 PM WIB  
        Weekend: 10:00 AM - 2:00 PM WIB  
        Urgent matters: Anytime via WhatsApp
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # Call to Action Section
    st.markdown(
        """
    <div class="contact-card" style="text-align: center; color: white; border-left: none;">
        <h3 style="margin-bottom: 1rem;">🚀 Ready to Work Together?</h3>
        <p style="font-size: 1.1rem; margin-bottom: 2rem; opacity: 0.9;">
            Let's discuss how I can help bring your next project to life with cutting-edge technology and proven expertise.
        </p>
        <div class="cta-buttons">
            <a href="mailto:zul1409@gmail.com?subject=Project Inquiry&body=Hi, I'm interested in discussing a project with you." class="cta-button">
                📧 Send Email
            </a>
            <a href="https://wa.me/6289508109402?text=Hi, I'd like to discuss a project with you" class="cta-button" target="_blank">
                💬 WhatsApp Chat
            </a>
            <a href="#" class="cta-button">
                📋 Download Resume
            </a>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Social Media Links
    st.markdown(
        """
    <div class="contact-card" style="text-align: center;">
        <h3 style="margin-bottom: 2rem;">🌐 Connect on Social Media</h3>
        <div class="social-links">
            <a href="https://linkedin.com/in/zulkifli1409" target="_blank" title="LinkedIn" style="text-decoration: none;">
                <i class="fab fa-linkedin"></i>
            </a>
            <a href="https://github.com/zulkifli1409" target="_blank" title="GitHub" style="text-decoration: none;">
                <i class="fab fa-github"></i>
            </a>
            <a href="https://instagram.com/zulkiflii.i" target="_blank" title="Instagram" style="text-decoration: none;">
                <i class="fab fa-instagram"></i>
            </a>
            <a href="#" target="_blank" title="YouTube" style="text-decoration: none;">
                <i class="fab fa-youtube"></i>
            </a>
        </div>
        <p style="color: #666; margin-top: 1rem; font-size: 0.9rem;">
            Follow me for updates on latest projects and tech insights!
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Contact Form (Optional)
    st.markdown("---")
    st.markdown("### 📝 Quick Contact Form")

    with st.form("contact_form"):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Your Name *", placeholder="Zulkifli")
            email = st.text_input("Your Email *", placeholder="zul140904@gmail.com")

        with col2:
            company = st.text_input("Company (Optional)", placeholder="Your Company")
            phone = st.text_input("Phone (Optional)", placeholder="+62 812-3456-7890")

        subject = st.selectbox(
            "Project Type *",
            [
                "Cybersecurity Audit / Penetration Testing",
                "Digital Forensics & OSINT Investigation",
                "Automation & Python Scripting",
                "AI/ML Project",
                "Web Development",
                "Mobile App",
                "Consulting",
                "Other",
            ],
        )

        message = st.text_area(
            "Project Details *",
            placeholder="Tell me about your project, timeline, and requirements...",
            height=120,
        )

        budget = st.selectbox(
            "Budget Range (Optional)",
            [
                "< Rp5.000.000",
                "Rp5.000.000 - Rp15.000.000",
                "Rp15.000.000 - Rp50.000.000",
                "Rp50.000.000+",
                "Let's discuss",
            ],
        )

        submitted = st.form_submit_button("🚀 Send Message", use_container_width=True)

        if submitted:
            # Validate required fields
            if not name or not email or not message:
                st.error("❌ Please fill in all required fields (marked with *)")
            # Validate email format
            elif not validate_email(email):
                st.error("❌ Please enter a valid email address")
            # Validate phone format (if provided)
            elif phone and not validate_phone(phone):
                st.error("❌ Please enter a valid phone number")
            # Check message length (prevent spam)
            elif len(message) < 10:
                st.error("❌ Message is too short. Please provide more details (minimum 10 characters)")
            elif len(message) > 5000:
                st.error("❌ Message is too long. Please keep it under 5000 characters")
            else:
                # Check rate limit
                can_submit, rate_limit_msg = check_rate_limit()
                
                if not can_submit:
                    st.error(f"🚫 {rate_limit_msg}")
                else:
                    # Sanitize inputs
                    name_clean = sanitize_input(name)
                    email_clean = sanitize_input(email)
                    company_clean = sanitize_input(company)
                    phone_clean = sanitize_input(phone)
                    message_clean = sanitize_input(message)
                    
                    # Show loading spinner
                    with st.spinner("🔐 Sending your secure message..."):
                        # Try to send email
                        email_sent = send_email(
                            name_clean, email_clean, company_clean, 
                            phone_clean, subject, message_clean, budget
                        )
                        
                        if email_sent:
                            st.success(
                                "🎉 Thank you for your message! I'll get back to you within 24 hours. "
                                "Your information will be kept confidential and secure."
                            )
                            st.balloons()
                        else:
                            st.warning(
                                "⚠️ Your message was received, but email notification failed. "
                                "I'll still contact you at the email/phone you provided. "
                                "For faster response, please reach me via WhatsApp: +62 895-0810-9402"
                            )
                        
                        # Update rate limit tracking
                        st.session_state.last_submission_time = time.time()
                        st.session_state.submission_count += 1
                        
                        # Log the submission securely
                        try:
                            # Create unique submission ID
                            submission_id = hashlib.sha256(
                                f"{email_clean}{time.time()}".encode()
                            ).hexdigest()[:12]
                            
                            with open("contact_submissions.txt", "a", encoding="utf-8") as f:
                                f.write(f"\n{'='*80}\n")
                                f.write(f"Submission ID: {submission_id}\n")
                                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                                f.write(f"Name: {name_clean}\n")
                                f.write(f"Email: {email_clean}\n")
                                f.write(f"Company: {company_clean if company_clean else 'N/A'}\n")
                                f.write(f"Phone: {phone_clean if phone_clean else 'N/A'}\n")
                                f.write(f"Project Type: {subject}\n")
                                f.write(f"Budget: {budget}\n")
                                f.write(f"Message:\n{message_clean}\n")
                                f.write(f"{'='*80}\n")
                        except Exception as e:
                            # Log error but don't show to user
                            print(f"Error logging submission: {str(e)}")

    # FAQ Section
    st.markdown("---")
    st.markdown("### ❓ Frequently Asked Questions")

    with st.expander("💰 What are your rates?"):
        st.write(
        """
        My rates start from IDR 50,000 per hour, depending on project complexity.  
        For bigger projects (e.g., cybersecurity assessments or digital forensics), we can discuss fixed pricing packages.
        """
        )

    with st.expander("⏳ How long does a typical project take?"):
        st.write(
            """
        Typical timelines vary by project type:
        - **Web Development**: 1-2 weeks  
        - **AI/ML Projects**: About 1 month  
        - **Mobile Apps**: About 1 month  
        - **Server Setup & Backend**: Around 1 month  
        - **Python Scripting & Automation**: 1-3 weeks  
        - **Cybersecurity Audit & Penetration Testing**: 1-3 weeks  
        - **Digital Forensics Investigation**: Case-dependent, usually 1-2 weeks
        
        I provide clear timeline estimates before starting and keep you updated regularly.
        """
        )

    with st.expander("🤝 Do you work with international clients?"):
        st.write(
            """
        Currently, I mostly collaborate with clients in Indonesia, but I’m open to international projects where communication can be handled smoothly online.
        """
        )

    with st.expander("🔧 What technologies do you specialize in?"):
        st.write(
            """
        - **Full-Stack Web Development (React, Node.js, PHP, Flutter)**  
        - **Cybersecurity & Digital Forensics (Penetration Testing, Malware Analysis, OSINT)**  
        - **Automation & Scripting (Python, Selenium, Scrapy)**  
        - **AI/ML for Threat Intelligence & Risk Scoring**  
        - **Database & Cloud Services (MySQL, MongoDB, Firebase)**  
        - And more based on project needs!
        """
        )

    with st.expander("⚙️ How does your work process look like?"):
        st.write(
            """
        - Initial consultation to understand your needs  
        - Proposal & timeline agreement  
        - Development with regular updates  
        - Revision phase to refine the result  
        - Delivery & support after completion  
        - Free consultation available anytime!
        - Strict confidentiality for sensitive projects (cybersecurity & forensic cases)  
        """
        )

    with st.expander("🔄 Do you offer revisions and guarantees?"):
        st.write(
            """
        Yes! I provide revisions on development projects and detailed reports for cybersecurity/forensics work.  
        Post-project support is included to ensure everything runs smoothly and securely.
        """
        )
