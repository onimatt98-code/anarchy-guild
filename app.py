import streamlit as st
import datetime
import base64
import os

# 1. Page Configuration (Clean & Portable Layout)
st.set_page_config(page_title="ANARCHY Guild Portal", page_icon="⚔️", layout="centered")

# 2. Guild Passwords
MEMBER_PASSWORD = "anarchy2026"
ADMIN_PASSWORD = "anarchyadmin" 

# Initialize session state for keeping track of logins and RSVPs
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "is_admin" not in st.session_state:
    st.session_state["is_admin"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""
if "rsvp_yes" not in st.session_state:
    st.session_state["rsvp_yes"] = ["♱  DARK", "♱  YENG"]
if "rsvp_no" not in st.session_state:
    st.session_state["rsvp_no"] = []

# Helper function to load your background image safely
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

bg_base64 = get_base64_image("60308.jpg")

# 3. UI Styling with Background Image and Premium Fonts Configuration
if not st.session_state["logged_in"]:
    # Login Screen: Full Premium Wallpaper Background with Cool Fonts
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Orbitron:wght@700;900&display=swap');
        
        .stApp {{ 
            background: linear-gradient(rgba(11, 15, 25, 0.85), rgba(11, 15, 25, 0.9)), 
                        url("data:image/jpeg;base64,{bg_base64}") no-repeat center center fixed;
            background-size: cover;
            color: #f8fafc; 
            font-family: 'Inter', sans-serif !important;
        }}
        .login-box {{
            background: rgba(30, 41, 59, 0.4);
            padding: 30px;
            border-radius: 12px;
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}
        .stTextInput>div>div>input {{ 
            background-color: rgba(15, 23, 42, 0.8) !important; 
            color: #ffffff !important; 
            border: 1px solid #475569 !important; 
            border-radius: 6px !important;
            font-family: 'Inter', sans-serif !important;
        }}
        .stButton>button {{ 
            background: #e11d48; 
            color: white; 
            border: none;
            border-radius: 6px; 
            width: 100%; 
            font-weight: 700; 
            padding: 10px;
            box-shadow: 0 4px 15px rgba(225, 29, 72, 0.4);
            font-family: 'Orbitron', sans-serif !important;
            letter-spacing: 2px;
        }}
        h1, h2, h3, .brand-logo {{
            font-family: 'Orbitron', sans-serif !important;
        }}
        </style>
    """, unsafe_allow_html=True)
else:
    # Dashboard Screen: Clean Dark Theme for Max Readability with Cool Fonts
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Orbitron:wght@700;900&display=swap');
        
        .stApp { 
            background-color: #0f172a; 
            color: #f8fafc; 
            font-family: 'Inter', sans-serif !important;
        }
        .stTextInput>div>div>input { 
            background-color: #1e293b !important; 
            color: #ffffff !important; 
            border: 1px solid #334155 !important; 
            border-radius: 6px !important;
            font-family: 'Inter', sans-serif !important;
        }
        .stButton>button { 
            background-color: #e11d48; 
            color: white; 
            border: none;
            border-radius: 6px; 
            width: 100%; 
            font-weight: 700; 
            padding: 10px;
            font-family: 'Orbitron', sans-serif !important;
            letter-spacing: 1px;
        }
        .countdown-card { 
            background: #1e293b; 
            border: 1px solid #334155; 
            padding: 20px; 
            border-radius: 8px; 
            text-align: center; 
            margin-bottom: 20px; 
        }
        .countdown-card h2 {
            font-family: 'Orbitron', sans-serif !important;
            font-weight: 900;
        }
        .social-btn {
            display: block;
            text-align: center;
            padding: 12px 6px;
            border-radius: 6px;
            font-weight: bold;
            text-decoration: none;
            width: 100%;
            font-size: 0.9rem;
            font-family: 'Orbitron', sans-serif !important;
            letter-spacing: 1px;
        }
        .wa-color { background-color: #25d366; color: white !important; }
        .tt-color { background: linear-gradient(90deg, #00f2fe, #4facfe); color: #000000 !important; }
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Orbitron', sans-serif !important;
        }
        </style>
    """, unsafe_allow_html=True)

# --- LOGIN GATEWAY ---
if not st.session_state["logged_in"]:
    st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 900; text-shadow: 0px 0px 15px #e11d48; letter-spacing: 4px;'>♱ ANARCHY ♱</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8; font-weight:600; letter-spacing: 4px; font-size: 0.8rem;'>GUILD MEMBER PORTAL</p>", unsafe_allow_html=True)
    
    # Wrap login fields inside a semi-transparent container
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    user_name = st.text_input("🎮 Free Fire Game Name (IGN)")
    input_password = st.text_input("🔑 Guild Password", type="password")

    if st.button("Log In"):
        if user_name.strip() == "":
            st.error("Please enter your Free Fire game name.")
        elif input_password == ADMIN_PASSWORD:
            st.session_state["logged_in"] = True
            st.session_state["is_admin"] = True
            st.session_state["username"] = user_name.strip()
            st.rerun()
        elif input_password == MEMBER_PASSWORD:
            st.session_state["logged_in"] = True
            st.session_state["is_admin"] = False
            st.session_state["username"] = user_name.strip()
            st.rerun()
        else:
            st.error("Incorrect guild password.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- MAIN PORTAL ---
else:
    col_header, col_logout = st.columns([3, 1])
    with col_header:
        st.markdown(f"<h3 style='margin:0;'>Welcome back, {st.session_state['username']}</h3>", unsafe_allow_html=True)
    with col_logout:
        if st.button("Log Out"):
            st.session_state["logged_in"] = False
            st.session_state["is_admin"] = False
            st.rerun()
        
    st.write("---")
    
    portal_tabs = st.tabs(["📢 Dashboard", "🧬 Guild Roster", "📡 Guild Connections"])
    
    # ---- TAB 1: DASHBOARD & COUNTDOWN ----
    with portal_tabs[0]:
        now = datetime.datetime.now()
        target_day = 4  # Friday
        days_ahead = target_day - now.weekday()
        if days_ahead <= 0:
            if days_ahead == 0 and now.hour < 19:
                pass
            else:
                days_ahead += 7
        
        target_war_date = datetime.datetime.combine(now.date() + datetime.timedelta(days=days_ahead), datetime.time(19, 0, 0))
        time_remaining = target_war_date - now
        
        days, remainder = divmod(int(time_remaining.total_seconds()), 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        st.markdown(f"""
        <div class="countdown-card">
            <h5 style="color: #94a3b8; margin: 0; letter-spacing: 1px;">Next Guild War Countdown</h5>
            <h2 style="color: #ffffff; margin: 10px 0;">
                {days}d : {hours}h : {minutes}m : {seconds}s
            </h2>
            <p style="color: #e11d48; font-size: 0.85rem; margin: 0; font-weight: 600; letter-spacing: 0.5px;">Schedule:
