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

# 3. UI Styling Configurations (Fixed Syntax Matrix)
if not st.session_state["logged_in"]:
    # Login Screen Styling
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Orbitron:wght@700;900&display=swap');
        
        .stApp { 
            background: linear-gradient(rgba(11, 15, 25, 0.85), rgba(11, 15, 25, 0.9)), 
                        url("data:image/jpeg;base64,""" + bg_base64 + """") no-repeat center center fixed;
            background-size: cover;
            color: #f8fafc; 
            font-family: 'Inter', sans-serif !important;
        }
        .login-box {
            background: rgba(30, 41, 59, 0.4);
            padding: 30px;
            border-radius: 12px;
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .stTextInput>div>div>input { 
            background-color: rgba(15, 23, 42, 0.8) !important; 
            color: #ffffff !important; 
            border: 1px solid #475569 !important; 
            border-radius: 6px !important;
            font-family: 'Inter', sans-serif !important;
        }
        .stButton>button { 
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
        }
        h1, h2, h3, .brand-logo {
            font-family: 'Orbitron', sans-serif !important;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    # Dashboard Dashboard Styling
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
            <p style="color: #e11d48; font-size: 0.85rem; margin: 0; font-weight: 600; letter-spacing: 0.5px;">Schedule: Friday & Saturday (19:00 - 23:00)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("#### ⚔️ Confirm Attendance")
        st.write("Are you available to participate this Friday?")
        col_yes, col_no = st.columns(2)
        
        with col_yes:
            if st.button("✅ Yes, I'll be active"):
                if st.session_state["username"] not in st.session_state["rsvp_yes"]:
                    st.session_state["rsvp_yes"].append(st.session_state["username"])
                    if st.session_state["username"] in st.session_state["rsvp_no"]:
                        st.session_state["rsvp_no"].remove(st.session_state["username"])
                    st.success("Confirmed active!")
                    st.rerun()
        with col_no:
            if st.button("❌ No, I'll miss it"):
                if st.session_state["username"] not in st.session_state["rsvp_no"]:
                    st.session_state["rsvp_no"].append(st.session_state["username"])
                    if st.session_state["username"] in st.session_state["rsvp_yes"]:
                        st.session_state["rsvp_yes"].remove(st.session_state["username"])
                    st.warning("Marked as inactive.")
                    st.rerun()
        
        st.write(f"**Total Available Players:** {len(st.session_state['rsvp_yes'])}")
        with st.expander("View Check-in List"):
            st.write(", ".join(st.session_state["rsvp_yes"]))

        st.write("---")
        st.write("#### 📜 Guild Regulations")
        st.info("1. Respect all members. Zero tolerance for toxicity.\n"
                "2. Earn a minimum of **1,000 Glory Points weekly**.\n"
                "3. Use the required guild name tag change format within 10 days.\n"
                "4. Requirements to stay: Account level 60+ / Heroic Tier 3+.")

    # ---- TAB 2: ROSTER ----
    with portal_tabs[1]:
        st.write("#### 👑 High Command Architecture")
        leaders = {
            "♱  DARK": {"Role": "Guild Leader", "Level": "74", "Style": "Vanguard Rusher"},
            "♱  YENG": {"Role": "Co-Leader", "Level": "69", "Style": "All-Rounder"},
            "♱ KUROTŚUI": {"Role": "Officer / Admin", "Level": "71", "Style": "Sniper"},
            f"{st.session_state['username'] if st.session_state['username'] else 'YOU'}": {"Role": "Site Creator / Architect", "Level": "99", "Style": "Core Support System"},
            "♱  PRIDE": {"Role": "Officer / Admin", "Level": "68", "Style": "Flanker"},
            "♱  EMMA": {"Role": "Officer / Admin", "Level": "65", "Style": "In-Game Leader"},
            "♱ EVILMAN†": {"Role": "Officer / Admin", "Level": "64", "Style": "Assault Node"}
        }
        for name, info in leaders.items():
            with st.expander(f"⭐ {name} — {info['Role']}"):
                st.write(f"• **Level:** {info['Level']}  \n• **Playstyle:** {info['Style']}")
                
        st.write("#### ⚔️ Active Vanguard Units")
        enforcers = {
            "♱  KAISER": "Level 63 | Assault Node",
            "♱  SAVAGE.": "Level 65 | Strike Specialist",
            "♱ﾠDAMZY 🌾": "Level 61 | Rearguard Suppression",
            "♱  HEMJAY": "Level 62 | Infiltration Unit",
            "♱  ᏁᎮᎴ": "Level 61 | Combat Node"
        }
        for name, details in enforcers.items():
            with st.expander(f"• {name}"):
                st.write(f"📊 **Details:** {details}")

    # ---- TAB 3: CONNECTIONS ----
    with portal_tabs[2]:
        st.write("#### 📡 Operational Links")
        st.write("Access our communication channels and social feed below:")
        
        col_whatsapp, col_tiktok = st.columns(2)
        with col_whatsapp:
            st.markdown('<a href="https://chat.whatsapp.com/LFHtTSLYkNc5IT2iRFWbYy" target="_blank" class="social-btn wa-color">💬 WhatsApp Chat</a>', unsafe_allow_html=True)
        with col_tiktok:
            st.markdown('<a href="https://www.tiktok.com/" target="_blank" class="social-btn tt-color">📱 TikTok Feed</a>', unsafe_allow_html=True)
            
        st.caption("Note: Use the WhatsApp portal for active war lineup communications.")
