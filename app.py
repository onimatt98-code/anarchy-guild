import streamlit as st
import datetime

# 1. Page Configuration (Clean & Compact)
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

# 3. Clean & Modern Mobile-Friendly Styling
st.markdown("""
    <style>
    /* Clean Dark Mode Theme */
    .stApp { 
        background-color: #0f172a; 
        color: #f8fafc; 
    }
    
    /* Standard Modern Text Inputs */
    .stTextInput>div>div>input { 
        background-color: #1e293b !important; 
        color: #ffffff !important; 
        border: 1px solid #334155 !important; 
        border-radius: 6px !important;
    }
    
    /* Professional Clean Button */
    .stButton>button { 
        background-color: #e11d48; 
        color: white; 
        border: none;
        border-radius: 6px; 
        width: 100%; 
        font-weight: 600; 
        padding: 10px;
        transition: 0.2s ease; 
    }
    .stButton>button:hover { 
        background-color: #be123c;
        color: white;
    }
    
    /* Simple Info Box for Countdown */
    .countdown-card { 
        background: #1e293b; 
        border: 1px solid #334155; 
        padding: 20px; 
        border-radius: 8px; 
        text-align: center; 
        margin-bottom: 20px; 
    }
    
    /* WhatsApp Redirection Button */
    .whatsapp-link { 
        display: block; 
        background-color: #25d366; 
        color: white !important; 
        text-align: center; 
        padding: 12px; 
        border-radius: 6px; 
        font-weight: bold; 
        text-decoration: none; 
        margin: 20px auto; 
        width: 100%; 
    }
    .whatsapp-link:hover { 
        background-color: #20ba5a;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGIN GATEWAY ---
if not st.session_state["logged_in"]:
    st.markdown("<h2 style='text-align: center; color: #e11d48; font-weight: 800;'>♱ ANARCHY ♱</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>Guild Member Portal</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Simple, clear standard labels
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

# --- MAIN PORTAL ---
else:
    # Minimal Top Bar
    col_header, col_logout = st.columns([3, 1])
    with col_header:
        st.markdown(f"<h3 style='margin:0;'>Welcome back, {st.session_state['username']}</h3>", unsafe_allow_html=True)
    with col_logout:
        if st.button("Log Out"):
            st.session_state["logged_in"] = False
            st.session_state["is_admin"] = False
            st.rerun()
        
    st.write("---")
    
    # Modern Portable Tabs
    portal_tabs = st.tabs(["📢 Dashboard", "🧬 Guild Roster", "🎬 Combat Clips", "📡 Group Chat"])
    
    # ---- TAB 1: DASHBOARD & COUNTDOWN ----
    with portal_tabs[0]:
        # Simple Countdown Logic
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
            <h5 style="color: #94a3b8; margin: 0;">Next Guild War Countdown</h5>
            <h2 style="color: #ffffff; margin: 10px 0;">
                {days}d : {hours}h : {minutes}m : {seconds}s
            </h2>
            <p style="color: #e11d48; font-size: 0.85rem; margin: 0; font-weight: 600;">Schedule: Friday & Saturday (19:00 - 23:00)</p>
        </div>
        """, unsafe_allow_html=True)
        
        # RSVP Check-in System
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
        
        # Simple Rules Display
        st.write("#### 📜 Guild Regulations")
        st.info("1. Respect all members. Zero tolerance for toxicity.\n"
                "2. Earn a minimum of **1,000 Glory Points weekly**.\n"
                "3. Use the required guild name tag change format within 10 days.\n"
                "4. Requirements to stay: Account level 60+ / Heroic Tier 3+.")

    # ---- TAB 2: ROSTER (With you placed perfectly at 4th) ----
    with portal_tabs[1]:
        st.write("#### 👑 High Command")
        
        leaders = {
            "♱  DARK": {"Role": "Guild Leader", "Level": "74", "Style": "Vanguard Rusher"},
            "♱  YENG": {"Role": "Co-Leader", "Level": "69", "Style": "All-Rounder"},
            "♱ KUROTŚUI": {"Role": "Officer", "Level": "71", "Style": "Sniper"},
            f"{st.session_state['username'] if st.session_state['username'] else 'YOU'}": {"Role": "Site Creator / Architect", "Level": "99", "Style": "Core Support"},
            "♱  PRIDE": {"Role": "Officer", "Level": "68", "Style": "Flanker"},
            "♱  EMMA": {"Role": "Officer", "Level": "65", "Style": "In-Game Leader"}
        }
        
        for name, info in leaders.items():
            with st.expander(f"⭐ {name} — {info['Role']}"):
                st.write(f"• **Level:** {info['Level']}  \n• **Playstyle:** {info['Style']}")
                
        st.write("#### ⚔️ Main Squad")
        enforcers = ["♱  KAISER", "♱  SAVAGE.", "♱ﾠDAMZY🪶", "♱ﾠHEMJAY"]
        for name in enforcers:
            st.text(f"• {name}")

    # ---- TAB 3: COMBAT CLIPS (Natively Embedded Internal Video Player) ----
    with portal_tabs[2]:
        st.write("#### 🎬 Guild Showcase Video")
        
        # Plays cleanly inside the web container using the file hosted in your directory
        st.video("guild_intro.mp4")
        
        st.caption("Featuring profiles of: DARK, YENG, KUROTŚUI, EMMA, PRIDE, & SAVAGE.")

    # ---- TAB 4: GROUP CHAT LINK ----
    with portal_tabs[3]:
        st.write("#### 📡 Communication Bridge")
        st.write("Tap the button below to switch over to our WhatsApp group for squad calls and active war coordination:")
        st.markdown(f'<a href="https://chat.whatsapp.com/LFHtTSLYkNc5IT2iRFWbYy?s=sh&p=a&mlu=2" target="_blank" class="whatsapp-link">Join WhatsApp Group Chat</a>', unsafe_allow_html=True)
