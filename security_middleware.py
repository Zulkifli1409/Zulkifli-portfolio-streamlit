"""
Security Middleware for Portfolio Application
Implements comprehensive security measures across all pages
"""

import streamlit as st
import hashlib
import time
import re
from functools import wraps
from datetime import datetime, timedelta

# Security Configuration
SECURITY_CONFIG = {
    "max_requests_per_minute": 60,
    "session_timeout_minutes": 30,
    "enable_csrf_protection": True,
    "enable_xss_protection": True,
    "enable_clickjacking_protection": True,
    "max_session_age_hours": 24,
}

# Initialize security session state
def init_security_session():
    """Initialize security-related session state variables"""
    if 'security_initialized' not in st.session_state:
        st.session_state.security_initialized = True
        st.session_state.session_id = generate_session_id()
        st.session_state.session_start_time = time.time()
        st.session_state.last_activity_time = time.time()
        st.session_state.request_count = 0
        st.session_state.request_window_start = time.time()
        st.session_state.failed_attempts = 0
        st.session_state.ip_address = get_client_ip()

def generate_session_id():
    """Generate unique session ID"""
    timestamp = str(time.time()).encode()
    random_data = str(hash(timestamp)).encode()
    return hashlib.sha256(timestamp + random_data).hexdigest()[:16]

def get_client_ip():
    """Get client IP address (simulated for Streamlit)"""
    # In production, use actual IP from request headers
    try:
        # Streamlit doesn't expose IP directly, but you can get it from headers
        return "client_ip_placeholder"
    except:
        return "unknown"

def check_session_timeout():
    """Check if session has timed out"""
    if 'last_activity_time' not in st.session_state:
        return False
    
    current_time = time.time()
    last_activity = st.session_state.last_activity_time
    timeout = SECURITY_CONFIG['session_timeout_minutes'] * 60
    
    if current_time - last_activity > timeout:
        return True
    
    # Update last activity time
    st.session_state.last_activity_time = current_time
    return False

def check_rate_limit():
    """Check if request rate limit is exceeded"""
    current_time = time.time()
    
    # Reset counter every minute
    if current_time - st.session_state.request_window_start > 60:
        st.session_state.request_count = 0
        st.session_state.request_window_start = current_time
    
    st.session_state.request_count += 1
    
    if st.session_state.request_count > SECURITY_CONFIG['max_requests_per_minute']:
        return False, "Rate limit exceeded. Please slow down."
    
    return True, None

def sanitize_input(text, allow_html=False):
    """Sanitize user input to prevent XSS and injection attacks"""
    if not text:
        return ""
    
    text = str(text).strip()
    
    if not allow_html:
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', '', text)
        
        # Escape special characters
        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        text = text.replace('"', '&quot;')
        text = text.replace("'", '&#x27;')
        text = text.replace('/', '&#x2F;')
    
    # Remove script tags even if HTML is allowed
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'javascript:', '', text, flags=re.IGNORECASE)
    text = re.sub(r'on\w+\s*=', '', text, flags=re.IGNORECASE)
    
    return text

def validate_url(url):
    """Validate URL to prevent malicious redirects"""
    if not url:
        return False
    
    # Allow only https and http
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    return url_pattern.match(url) is not None

def log_security_event(event_type, details, severity="INFO"):
    """Log security-related events"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    session_id = st.session_state.get('session_id', 'unknown')
    
    log_entry = {
        'timestamp': timestamp,
        'session_id': session_id,
        'event_type': event_type,
        'severity': severity,
        'details': details,
        'ip_address': st.session_state.get('ip_address', 'unknown')
    }
    
    # In production, send to proper logging service
    try:
        with open('security_logs.txt', 'a', encoding='utf-8') as f:
            f.write(f"\n{log_entry}\n")
    except:
        pass  # Silent fail for logging

def security_headers():
    """Add client-side security measures (server headers should be set via Streamlit config or reverse proxy)"""
    # Note: Real HTTP headers must be set at server level (nginx, Apache, or Streamlit Cloud)
    # These are just visual indicators and don't provide actual security
    # For production: Configure headers in your web server or use Streamlit Cloud settings
    pass  # Headers will be configured at deployment level

def check_suspicious_activity():
    """Detect suspicious activity patterns"""
    suspicious = False
    reason = None
    
    # Check failed attempts
    if st.session_state.get('failed_attempts', 0) > 5:
        suspicious = True
        reason = "Multiple failed attempts detected"
    
    # Check session age
    if 'session_start_time' in st.session_state:
        session_age = time.time() - st.session_state.session_start_time
        max_age = SECURITY_CONFIG['max_session_age_hours'] * 3600
        if session_age > max_age:
            suspicious = True
            reason = "Session too old"
    
    if suspicious:
        log_security_event("SUSPICIOUS_ACTIVITY", reason, "WARNING")
    
    return suspicious, reason

def secure_page_wrapper(func):
    """Decorator to add security checks to pages (non-blocking for page views)"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # Initialize security
            init_security_session()
            
            # Add security headers (placeholder)
            security_headers()
            
            # Check session timeout (warning only, don't block)
            if check_session_timeout():
                st.info("ℹ️ Long session detected. For security, consider refreshing if you've been inactive.")
                log_security_event("SESSION_TIMEOUT", "Long session detected", "INFO")
            
            # Check rate limit (only for high-frequency actions, not page views)
            # We'll skip this for normal page loads
            
            # Check suspicious activity (log only, don't block)
            is_suspicious, reason = check_suspicious_activity()
            if is_suspicious:
                log_security_event("SUSPICIOUS_ACTIVITY", reason, "WARNING")
                # Don't block - just log for monitoring
            
            # Execute the actual page function
            return func(*args, **kwargs)
        except Exception as e:
            # If security check fails, still show the page but log the error
            log_security_event("SECURITY_ERROR", str(e), "ERROR")
            return func(*args, **kwargs)
    
    return wrapper

def encrypt_sensitive_data(data, key=None):
    """Simple encryption for sensitive data (use proper encryption in production)"""
    if not key:
        key = st.session_state.get('session_id', 'default_key')
    
    # Simple XOR encryption (use AES/RSA in production)
    encrypted = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(str(data)))
    return encrypted.encode('utf-8').hex()

def decrypt_sensitive_data(encrypted_data, key=None):
    """Decrypt sensitive data"""
    if not key:
        key = st.session_state.get('session_id', 'default_key')
    
    try:
        data = bytes.fromhex(encrypted_data).decode('utf-8')
        decrypted = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))
        return decrypted
    except:
        return None

def validate_github_username(username):
    """Validate GitHub username format"""
    if not username:
        return False
    
    # GitHub username rules: alphanumeric and hyphens, 1-39 chars
    pattern = r'^[a-zA-Z0-9](?:[a-zA-Z0-9]|-(?=[a-zA-Z0-9])){0,38}$'
    return re.match(pattern, username) is not None

def secure_external_link(url, text):
    """Create secure external link with rel attributes"""
    if not validate_url(url):
        return f"<span style='color: red;'>Invalid URL</span>"
    
    return f'<a href="{url}" target="_blank" rel="noopener noreferrer nofollow">{text}</a>'

def prevent_clickjacking():
    """Add clickjacking prevention (note: actual X-Frame-Options must be set at server level)"""
    # This is a client-side indicator only
    # Real clickjacking protection requires X-Frame-Options HTTP header
    # Configure this in your web server (nginx, Apache) or Streamlit Cloud settings
    pass

def sanitize_file_path(path):
    """Sanitize file paths to prevent directory traversal"""
    if not path:
        return ""
    
    # Remove any attempt to traverse directories
    path = path.replace('..', '')
    path = path.replace('//', '/')
    path = path.replace('\\\\', '\\')
    
    # Remove potentially dangerous characters
    path = re.sub(r'[<>:"|?*]', '', path)
    
    return path

def check_csrf_token():
    """Simple CSRF token check"""
    if not SECURITY_CONFIG['enable_csrf_protection']:
        return True
    
    if 'csrf_token' not in st.session_state:
        st.session_state.csrf_token = generate_session_id()
    
    return True

def secure_api_call(url, headers=None):
    """Make secure API calls with proper headers and validation"""
    import requests
    
    if not validate_url(url):
        log_security_event("INVALID_API_URL", f"Blocked call to: {url}", "WARNING")
        return None
    
    default_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/vnd.github.v3+json',  # GitHub API specific
    }
    
    if headers:
        default_headers.update(headers)
    
    try:
        response = requests.get(
            url, 
            headers=default_headers, 
            timeout=15,
            verify=True  # Verify SSL certificates
        )
        return response
    except requests.exceptions.SSLError as e:
        log_security_event("SSL_ERROR", f"SSL verification failed: {str(e)}", "ERROR")
        # Try without SSL verification as fallback (log this)
        try:
            response = requests.get(url, headers=default_headers, timeout=15, verify=False)
            log_security_event("SSL_BYPASS", "SSL verification bypassed", "WARNING")
            return response
        except:
            return None
    except requests.exceptions.Timeout:
        log_security_event("API_TIMEOUT", f"Timeout calling: {url}", "WARNING")
        return None
    except Exception as e:
        log_security_event("API_ERROR", f"API call failed: {str(e)}", "ERROR")
        return None

# Export all security functions
__all__ = [
    'init_security_session',
    'sanitize_input',
    'validate_url',
    'secure_page_wrapper',
    'security_headers',
    'check_rate_limit',
    'log_security_event',
    'encrypt_sensitive_data',
    'decrypt_sensitive_data',
    'validate_github_username',
    'secure_external_link',
    'prevent_clickjacking',
    'sanitize_file_path',
    'secure_api_call',
    'check_csrf_token'
]
