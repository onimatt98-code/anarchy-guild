import streamlit as st
import datetime

# 1. Page Configuration
st.set_page_config(page_title="♱ ANARCHY QUANTUM NETWORK", page_icon="⚔️", layout="centered")

# 2. Guild Passwords
MEMBER_PASSWORD = "anarchy2026"
ADMIN_PASSWORD = "anarchyadmin" 

# Initialize session state for persistent data
if "logged_in" not in st.session_state: st.session_state["logged_in"] = False
if "is_admin" not in st.session_state: st.session_state["is_admin"] = False
if "username" not in st.session_state: st.session_state["username"] = ""
if "rsvp_yes" not in st.session_state: st.session_state["rsvp_yes"] = ["♱  DARK", "♱  YENG"]
if "rsvp_no" not in st.session_state: st.session_state["rsvp_no"] = []

# 3. Enhanced Cyber HUD CSS
st.markdown("""
    <style>
    .stApp { background-color: #030708; color: #e2e8f0; font-family: 'Courier New', monospace; }
    .hud-box { background: rgba(10, 15, 26, 0.75); border: 1px solid #00f0ff; padding: 25px; border-radius: 4px; text-align: center; box-shadow: 0 0 20px rgba(0, 240, 255, 0.2); }
    .video-hud { border: 2px solid #ff0055; box-shadow: 0 0 20px rgba(255, 0, 85, 0.3); padding: 5px; border-radius: 4px; }
    .stButton>button { background: linear-gradient(90deg, #ff0055, #9900ff); color: white; border: none; width: 100%; font-weight: bold; text-transform: uppercase; letter-spacing: 2px; }
    .whatsapp-btn { display: block; background: linear-gradient(90deg, #00f0ff, #0077ff); color: #030708 !important; text-align: center; padding: 14px; text-decoration: none; font-weight: bold; letter-spacing: 2px; }
    </style>
""", unsafe_allow_html=True)

# --- LOGIN GATEWAY ---
if not st.session_state["logged_in"]:
    st.markdown("<h1 style='text-align: center; color: #ff0055;'>♱ ANARCHY ♱</h1>", unsafe_allow_html=True)
    user_name = st.text_input("// ENTER OPERATOR CODENAME")
    input_password = st.text_input("// DECRYPT ACCESS CIPHER", type="password")

    if st.button("AUTHENTICATE IDENTITY"):
        if input_password == ADMIN_PASSWORD:
            st.session_state.update({"logged_in": True, "is_admin": True, "username": user_name.strip()})
            st.rerun()
        elif input_password == MEMBER_PASSWORD:
            st.session_state.update({"logged_in": True, "is_admin": False, "username": user_name.strip()})
            st.rerun()
        else: st.error("ACCESS DENIED: Signature Mismatch")

# --- DASHBOARD ---
else:
    st.markdown(f"## ⚔️ ANARCHY // {st.session_state['username']}")
    if st.button("TERMINATE LINK"): st.session_state.update({"logged_in": False, "is_admin": False}); st.rerun()
    
    tabs = st.tabs(["⚡ CORE_DIRECTIVES", "🧬 NEURAL_ROSTER", "🎥 MEDIA_FEED", "📡 COMMS"])
    
    with tabs[0]:
        st.markdown('<div class="hud-box"><h3>⚠️ GUILD WAR READY</h3><p>Fri/Sat // 1900-2300 HRS</p></div>', unsafe_allow_html=True)
    
    with tabs[1]:
        st.write("### 📢 QUANTUM SIGNATURES")
        st.markdown("* 👑 **DARK** | 🛡️ **KUROTŚUI** | 🛡️ **PRIDE** | 🛡️ **EMMA** | 🛡️ **YENG**")
    
    with tabs[2]:
        st.write("### 🎥 TRANSMISSION FEED: GUILD SHOWCASE")
        st.markdown('<div class="video-hud">', unsafe_allow_html=True)
        # REPLACE THE URL BELOW WITH YOUR YOUTUBE VIDEO URL
        st.video("https://www.youtube.com/watch?v=YOUR_VIDEO_ID") 
        st.markdown('</div>', unsafe_allow_html=True)
        
    with tabs[3]:
        st.markdown('<a href="https://chat.whatsapp.com/LFHtTSLYkNc5IT2iRFWbYy" class="whatsapp-btn">⚡ BRIDGE QUANTUM COMMS</a>', unsafe_allow_html=True)

    # --- ADMIN OVERSEER CONSOLE ---
    if st.session_state["is_admin"]:
        st.divider()
        st.warning("🛡️ OVERSEER COMMAND CONSOLE")
        target = st.text_input("Target Node Designation")
        action = st.selectbox("Command", ["Promote", "Purge Node", "Low Energy Alert"])
        if st.button("EXECUTE PROTOCOL"):
            st.success(f"Log: {action} applied to {target}")
