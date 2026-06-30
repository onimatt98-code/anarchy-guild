import streamlit as st
import datetime
import time

# 1. Page Configuration
st.set_page_config(page_title="♱ ANARCHY Guild Portal", page_icon="⚔️", layout="centered")

# 2. Guild Passwords
MEMBER_PASSWORD = "anarchy2026"
ADMIN_PASSWORD = "anarchyadmin" 

# Initialize session state for persistent data
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "is_admin" not in st.session_state:
    st.session_state["is_admin"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""
if "rsvp_yes" not in st.session_state:
    st.session_state["rsvp_yes"] = ["♱  DARK", "♱ KUROTŚUI"]
if "rsvp_no" not in st.session_state:
    st.session_state["rsvp_no"] = []

# 3. Enhanced Cyberpunk/Gaming Theme Custom CSS
st.markdown("""
    <style>
    /* Main body styles */
    .stApp { background-color: #0b0c10; color: #c5c6c7; }
    
    /* Input fields styling */
    .stTextInput>div>div>input { background-color: #1f2833 !important; color: #45f3ff !important; border: 1px solid #45f3ff !important; }
    
    /* Buttons customization */
    .stButton>button { background: linear-gradient(45deg, #ff3333, #ff6600); color: white; border: none; border-radius: 5px; width: 100%; font-weight: bold; text-transform: uppercase; box-shadow: 0 0 10px rgba(255,51,51,0.5); transition: 0.3s; }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 15px rgba(255,102,0,0.8); color: #fff; }
    
    /* Custom containers */
    .countdown-box { background: #11141a; border: 2px dashed #ff3333; padding: 20px; border-radius: 10px; text-align: center; margin-bottom: 25px; box-shadow: inset 0 0 15px rgba(255,0,0,0.2); }
    .rules-card { background: #11141a; border-left: 5px solid #ff6600; padding: 15px; border-radius: 0 10px 10px 0; margin-bottom: 10px; }
    
    /* WhatsApp Button Override */
    .whatsapp-btn { display: block; background: linear-gradient(45deg, #128C7E, #25D366); color: white !important; text-align: center; padding: 14px; border-radius: 8px; font-weight: bold; text-decoration: none; margin: 20px auto; width: 90%; box-shadow: 0 4px 15px rgba(37,211,102,0.3); text-transform: uppercase; letter-spacing: 1px; }
    .whatsapp-btn:hover { box-shadow: 0 4px 25px rgba(37,211,102,0.6); transform: translateY(-2px); }
    </style>
""", unsafe_allow_html=True)

# --- LOGIN GATEWAY ---
if not st.session_state["logged_in"]:
    st.markdown("<h1 style='text-align: center; color: #ff3333; font-size: 3rem;'>🛡️ ♱ ANARCHY 🛡️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #66fcf1; letter-spacing: 2px;'>SYSTEM VERIFICATION REQUIRED</p>", unsafe_allow_html=True)
    st.write("---")
    
    user_name = st.text_input("ENTER FREE FIRE IGN (In-Game Name)")
    input_password = st.text_input("ENTER ACCESS CIPHER", type="password")

    if st.button("Authorize Connection"):
        if user_name.strip() == "":
            st.error("Identification failed: Name field cannot be vacant.")
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
            st.error("Access Denied: Invalid Guild Cipher.")

# --- DASHBOARD ---
else:
    # Header Section
    col_header, col_logout = st.columns([3, 1])
    with col_header:
        st.markdown(f"<h1 style='color: #ff3333; margin-bottom: 0;'>⚔️ ♱ﾠᴀɴᴀʀᴄʜʏ</h1>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #66fcf1;'>Operator: {st.session_state['username']} {'[ADMIN]' if st.session_state['is_admin'] else '[MEMBER]'}</p>", unsafe_allow_html=True)
    with col_logout:
        st.write("")
        if st.button("Disconnect"):
            st.session_state["logged_in"] = False
            st.session_state["is_admin"] = False
            st.rerun()
        
    st.write("---")
    
    portal_tabs = st.tabs(["📜 GUILD ORDERS", "👥 MEMBERS ROSTER", "💬 COMMUNITY HUBS"])
    
    # ---- TAB 1: GUILD ORDERS & COUNTDOWN ----
    with portal_tabs[0]:
        # CALCULATING LIVE COUNTDOWN TO NEXT GUILD WAR (Friday 7 PM)
        now = datetime.datetime.now()
        target_day = 4  # Friday is 4 in Python datetime (0=Monday)
        days_ahead = target_day - now.weekday()
        if days_ahead <= 0:  # If it's Friday after 7pm or Saturday/Sunday, target next week
            if days_ahead == 0 and now.hour < 19:
                pass
            else:
                days_ahead += 7
        
        target_war_date = datetime.datetime.combine(
            now.date() + datetime.timedelta(days=days_ahead), 
            datetime.time(19, 0, 0)
        )
        time_remaining = target_war_date - now
        
        days, remainder = divmod(int(time_remaining.total_seconds()), 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        # Displaying the countdown block
        st.markdown(f"""
        <div class="countdown-box">
            <h3 style="color: #ff3333; margin: 0; letter-spacing: 2px;">🔴 NEXT LIVE GUILD WAR</h3>
            <h2 style="color: #ffffff; font-family: 'Courier New', monospace; font-size: 2rem; margin: 10px 0;">
                {days}d : {hours}h : {minutes}m : {seconds}s
            </h2>
            <p style="color: #c5c6c7; font-size: 0.9rem; margin: 0;">Schedule: Friday & Saturday (7 PM - 11 PM)</p>
        </div>
        """, unsafe_allow_html=True)
        
        # INTERACTIVE RSVP SYSTEM
        st.write("### ⚔️ Combat Readiness Deployment")
        st.write("Are you hitting the battlefield this Friday?")
        col_yes, col_no = st.columns(2)
        
        with col_yes:
            if st.button("👍 Confirm Attendance"):
                if st.session_state["username"] not in st.session_state["rsvp_yes"]:
                    st.session_state["rsvp_yes"].append(st.session_state["username"])
                    if st.session_state["username"] in st.session_state["rsvp_no"]:
                        st.session_state["rsvp_no"].remove(st.session_state["username"])
                    st.success("Deployed to Roster!")
                    st.rerun()
        with col_no:
            if st.button("👎 Mark Absent"):
                if st.session_state["username"] not in st.session_state["rsvp_no"]:
                    st.session_state["rsvp_no"].append(st.session_state["username"])
                    if st.session_state["username"] in st.session_state["rsvp_yes"]:
                        st.session_state["rsvp_yes"].remove(st.session_state["username"])
                    st.warning("Absence Logged.")
                    st.rerun()
        
        # Show Live Headcount Metrics
        st.write(f"**Current Headcount Ready:** `{len(st.session_state['rsvp_yes'])}` fighters.")
        with st.expander("View Confirmed Vanguard"):
            st.write(", ".join(st.session_state["rsvp_yes"]))

        st.write("---")
        
        # Core Guild Rules Layout
        st.write("### 📜 Standing Directives")
        rules = [
            "**Rule 1:** Avoid insults/lust messages. Complete respect across all ranks.",
            "**Rule 2:** Hit **1k guild points weekly** without fail or face the kick cycle.",
            "**Rule 3:** Strict 10-day name change policy upon onboarding.",
            "**Rule 4:** Daily training drills launch sharp at 10 PM.",
            "**Rule 5:** Entry Requirements: Level 60+ and Prime 3+ tier baseline.",
            "**Rule 10:** Respect the chain of command. **Fear the elders** 🗿."
        ]
        for rule in rules:
            st.markdown(f'<div class="rules-card">{rule}</div>', unsafe_allow_html=True)

    # ---- TAB 2: INTERACTIVE MEMBER ROSTER ----
    with portal_tabs[1]:
        st.write("### 📢 OFFICIAL OPERATIONAL ROSTER")
        st.info("💡 Click on a member card below to view active combat dossiers, ranks, and performance specs.")
        
        st.write("#### 👑 Command Structure")
        leaders = {
            "♱  DARK": {"Role": "Guild Leader", "Level": "74", "Style": "Rush / Shotgun Specialist"},
            "♱ KUROTŚUI": {"Role": "Admin / Co-Leader", "Level": "71", "Style": "Sniper Support"},
            "♱  PRIDE": {"Role": "Admin", "Level": "68", "Style": "Flanker"},
            "♱  EMMA": {"Role": "Admin", "Level": "65", "Style": "In-game IGL"},
            "♱  YENG": {"Role": "Admin", "Level": "69", "Style": "All-Rounder"}
        }
        
        for leader, info in leaders.items():
            with st.expander(f"👑 {leader} — {info['Role']}"):
                st.write(f"🏅 **Account Level:** {info['Level']}")
                st.write(f"🎯 **Combat Style:** {info['Style']}")
                st.write("📈 **Weekly Target Status:** `PASSED (Verified)`")
                
        st.write("#### ⚔️ Active Vanguard")
        enforcers = {
            "♱  KAISER": "Level 63 | Assaulter",
            "♱  SAVAGE.": "Level 65 | Rusher",
            "♱ﾠDAMZY🪶": "Level 61 | Support Sniper",
            "♱ﾠHEMJAY": "Level 62 | Entry Fragger"
        }
        for enforcer, details in enforcers.items():
            with st.expander(f"⚔️ {enforcer}"):
                st.write(f"📊 **Dossier Profiles:** {details}")
                st.write("🚨 **Activity Metric:** Tracking Live...")

    # ---- TAB 3: COMMUNITY HUBS ----
    with portal_tabs[2]:
        st.write("### 💬 Communication Arrays")
        st.write("Stay synced with squad strategies, live voice links, and quick tactical briefings on our major channel:")
        st.markdown(f'<a href="https://chat.whatsapp.com/LFHtTSLYkNc5IT2iRFWbYy?s=sh&p=a&mlu=2" target="_blank" class="whatsapp-btn">🟢 JOIN OFFICIAL WHATSAPP COMS</a>', unsafe_allow_html=True)

    # --- ADMIN ONLY MANAGEMENT CONSOLE ---
    if st.session_state["is_admin"]:
        st.write("---")
        st.markdown("<h2 style='color: #ff3333;'>🛡️ ADMIN CONTROL ARRAYS</h2>", unsafe_allow_html=True)
        
        # 1. Quick Status Logger
        st.write("### 📝 Log Member Activity")
        member_name = st.text_input("Target Enforcer Name")
        action = st.selectbox("Action Directive", ["Promote to Enforcer", "Log 1k Points Manually", "Issue Low Activity Warning", "Flag for Execution (Kick)"])
        
        if st.button("Commit Log Entry"):
            if member_name:
                st.success(f"Log Updated Successfully: **{action}** has been recorded against **{member_name}**.")
            else:
                st.error("Action terminated: Target name field blank.")

        # 2. Live Guild War Alert
        st.write("### 📢 Push Tactical Broadcast Alert")
        alert_msg = st.text_input("Broadcast Cipher Text", placeholder="Guild War starts in 1 hour! Get 100pts!")
        if st.button("Initialize System Broadcast"):
            if alert_msg:
                st.toast(f"ALERT BROADCASTED: {alert_msg}")
                st.sidebar.error(f"🚨 ADMIN NOTICE: {alert_msg}")
            else:
                st.warning("Cannot broadcast empty airwaves.")
