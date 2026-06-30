import streamlit as st
import datetime

# 1. Page Configuration
st.set_page_config(page_title="♱ ANARCHY Quantum Network", page_icon="⚔️", layout="centered")

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
    st.session_state["rsvp_yes"] = ["♱  DARK", "♱  YENG"]
if "rsvp_no" not in st.session_state:
    st.session_state["rsvp_no"] = []

# 3. Futuristic Glassmorphism & Cyber HUD Custom CSS
st.markdown("""
    <style>
    /* Neon Cyberpunk Base */
    .stApp { 
        background-color: #030708; 
        background-image: linear-gradient(rgba(18, 24, 38, 0.5) 1px, transparent 0), linear-gradient(90deg, rgba(18, 24, 38, 0.5) 1px, transparent 0);
        background-size: 40px 40px;
        color: #e2e8f0; 
    }
    
    /* Futuristic Cyber Inputs */
    .stTextInput>div>div>input { 
        background-color: #0d1117 !important; 
        color: #00f0ff !important; 
        border: 1px solid #00f0ff !important; 
        box-shadow: 0 0 10px rgba(0, 240, 255, 0.15);
        font-family: 'Courier New', monospace;
    }
    
    /* Neon Laser Buttons */
    .stButton>button { 
        background: linear-gradient(90deg, #ff0055, #9900ff); 
        color: white; 
        border: 1px solid #ff0055; 
        border-radius: 0px; 
        width: 100%; 
        font-weight: bold; 
        text-transform: uppercase; 
        letter-spacing: 2px;
        font-family: 'Courier New', monospace;
        box-shadow: 0 0 15px rgba(255, 0, 85, 0.4); 
        transition: 0.4s ease; 
    }
    .stButton>button:hover { 
        transform: translateY(-2px); 
        box-shadow: 0 0 25px rgba(153, 0, 255, 0.8); 
        border: 1px solid #00f0ff;
        color: #00f0ff; 
    }
    
    /* Holo-Display Containers */
    .countdown-box { 
        background: rgba(10, 15, 26, 0.75); 
        border: 1px solid #00f0ff; 
        padding: 25px; 
        border-radius: 4px; 
        text-align: center; 
        margin-bottom: 25px; 
        box-shadow: 0 0 20px rgba(0, 240, 255, 0.2), inset 0 0 15px rgba(0, 240, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    .rules-card { 
        background: rgba(15, 22, 36, 0.6); 
        border-left: 3px solid #ff0055; 
        border-right: 1px solid rgba(255, 0, 85, 0.2);
        border-top: 1px solid rgba(255, 0, 85, 0.2);
        border-bottom: 1px solid rgba(255, 0, 85, 0.2);
        padding: 15px; 
        margin-bottom: 12px; 
        font-family: 'Courier New', monospace;
    }
    
    /* Quantum Comms Button */
    .whatsapp-btn { 
        display: block; 
        background: linear-gradient(90deg, #00f0ff, #0077ff); 
        color: #030708 !important; 
        text-align: center; 
        padding: 14px; 
        border-radius: 0px; 
        font-weight: bold; 
        text-decoration: none; 
        margin: 20px auto; 
        width: 90%; 
        box-shadow: 0 0 15px rgba(0, 240, 255, 0.4); 
        text-transform: uppercase; 
        letter-spacing: 2px;
        font-family: 'Courier New', monospace;
    }
    .whatsapp-btn:hover { 
        box-shadow: 0 0 30px rgba(0, 119, 255, 0.8); 
        transform: scale(1.01);
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGIN GATEWAY ---
if not st.session_state["logged_in"]:
    st.markdown("<h1 style='text-align: center; color: #ff0055; font-size: 3.5rem; font-family: monospace; text-shadow: 0 0 20px rgba(255,0,85,0.6);'>♱ ANARCHY ♱</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #00f0ff; letter-spacing: 4px; font-family: monospace;'>INITIALIZING QUANTUM NETLINK...</p>", unsafe_allow_html=True)
    st.write("---")
    
    user_name = st.text_input("🎮 ENTER YOUR FREE FIRE GAME NAME (IGN)")
    input_password = st.text_input("🔑 ENTER GUILD CODE WORD / PASSWORD", type="password")

    if st.button("AUTHENTICATE IDENTITY"):
        if user_name.strip() == "":
            st.error("CRITICAL ERROR: Please enter your Free Fire name.")
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
            st.error("ACCESS DENIED: Incorrect guild password.")

# --- DASHBOARD ---
else:
    # Cyber HUD Header
    col_header, col_logout = st.columns([3, 1])
    with col_header:
        st.markdown(f"<h1 style='color: #ff0055; font-family: monospace; text-shadow: 0 0 10px rgba(255,0,85,0.4); margin-bottom: 0;'>♱ ANARCHY // MAIN_FRAME</h1>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #00f0ff; font-family: monospace;'>SYS_OPERATOR: {st.session_state['username']} {'[OVERSEER_CLASS]' if st.session_state['is_admin'] else '[COMBAT_CLASS]'}</p>", unsafe_allow_html=True)
    with col_logout:
        st.write("")
        if st.button("TERMINATE LINK"):
            st.session_state["logged_in"] = False
            st.session_state["is_admin"] = False
            st.rerun()
        
    st.write("---")
    
    portal_tabs = st.tabs(["⚡ CORE_DIRECTIVES", "🧬 NEURAL_ROSTER", "🎬 COMBAT_CLIPS", "📡 COMMS_ARRAY"])
    
    # ---- TAB 1: CORE DIRECTIVES & COUNTDOWN ----
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
        <div class="countdown-box">
            <h3 style="color: #00f0ff; margin: 0; letter-spacing: 3px; font-family: monospace;">⚠️ TARGET TIME TO NEXT GUILD WAR</h3>
            <h2 style="color: #ffffff; font-family: 'Courier New', monospace; font-size: 2.3rem; margin: 12px 0; text-shadow: 0 0 15px rgba(255,255,255,0.4);">
                {days:02d}D : {hours:02d}H : {minutes:02d}M : {seconds:02d}S
            </h2>
            <p style="color: #a0aec0; font-size: 0.85rem; font-family: monospace; margin: 0;">SYNCHRONIZED WINDOW: FRI & SAT // 1900 - 2300 HOURS</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("### 🌌 Combat Node Deployment Status")
        st.write("Confirm your terminal presence for the upcoming Friday raid:")
        col_yes, col_no = st.columns(2)
        
        with col_yes:
            if st.button("📡 INITIALIZE DEPLOYMENT"):
                if st.session_state["username"] not in st.session_state["rsvp_yes"]:
                    st.session_state["rsvp_yes"].append(st.session_state["username"])
                    if st.session_state["username"] in st.session_state["rsvp_no"]:
                        st.session_state["rsvp_no"].remove(st.session_state["username"])
                    st.success("Telemetry Locked: Deployed.")
                    st.rerun()
        with col_no:
            if st.button("❌ ABORT DEPLOYMENT"):
                if st.session_state["username"] not in st.session_state["rsvp_no"]:
                    st.session_state["rsvp_no"].append(st.session_state["username"])
                    if st.session_state["username"] in st.session_state["rsvp_yes"]:
                        st.session_state["rsvp_yes"].remove(st.session_state["username"])
                    st.warning("Telemetry Updated: Standby Mode.")
                    st.rerun()
        
        st.write(f"**Vanguard Nodes Synchronized:** `{len(st.session_state['rsvp_yes'])}` units online.")
        with st.expander("Expand Active Grid Headcount"):
            st.write(", ".join(st.session_state["rsvp_yes"]))

        st.write("---")
        
        st.write("### 📜 Protocol Directives")
        rules = [
            "[SEC_01] Zero communication toxicity. Absolute baseline operational synchronization.",
            "[SEC_02] Generate minimum **1,000 Energy Matrix Points weekly** or face automated partition purge.",
            "[SEC_03] 10-day identification modification protocol mandatory upon grid insertion.",
            "[SEC_04] Daily simulation matrix drills initialize at exactly 2200 hours.",
            "[SEC_05] Baseline Specifications required: Level 60+ // Prime Tier 3+.",
            "[SEC_10] Adhere strictly to the command architecture. **Fear the Elders** 🗿."
        ]
        for rule in rules:
            st.markdown(f'<div class="rules-card">{rule}</div>', unsafe_allow_html=True)

    # ---- TAB 2: ROSTER TERMINAL (With You in 4th Spot) ----
    with portal_tabs[1]:
        st.write("### 📢 ACTIVE QUANTUM SIGNATURES")
        st.info("⚡ Select an operational node below to decode combat data, rank indexes, and tactical specialties.")
        
        st.write("#### 👑 High Command Architecture")
        leaders = {
            "♱  DARK": {"Role": "Guild Leader // System Root", "Level": "74", "Style": "High-Velocity Rush / Vanguard CQC"},
            "♱  YENG": {"Role": "Co-Leader // Network Admin", "Level": "69", "Style": "Adaptive Flex / All-Rounder"},
            "♱ KUROTŚUI": {"Role": "Network Admin", "Level": "71", "Style": "Long-Range Heavy Ordinance Sniper"},
            f"{st.session_state['username'] if st.session_state['username'] else 'YOU'}": {"Role": "Systems Architect // Site Creator", "Level": "99", "Style": "Full-Stack Core Dev / Tactical Logic Overlay"},
            "♱  PRIDE": {"Role": "Network Admin", "Level": "68", "Style": "Flanker / Stealth Operations"},
            "♱  EMMA": {"Role": "Network Admin", "Level": "65", "Style": "Tactical Coordinator / IGL Matrix"}
        }
        
        for leader, info in leaders.items():
            with st.expander(f"🔮 {leader} // {info['Role']}"):
                st.write(f"🧬 **Hardware Level:** {info['Level']}")
                st.write(f"🎯 **Combat Vector:** {info['Style']}")
                st.write("📈 **Weekly Threshold:** `VERIFIED // SAFE`")
                
        st.write("#### ⚔️ Active Vanguard Units")
        enforcers = {
            "♱  KAISER": "Level 63 | Assault Node",
            "♱  SAVAGE.": "Level 65 | Strike Specialist",
            "♱ﾠDAMZY🪶": "Level 61 | Rearguard Suppression Sniper",
            "♱ﾠHEMJAY": "Level 62 | Entry Infiltration Unit"
        }
        for enforcer, details in enforcers.items():
            with st.expander(f"⬡ {enforcer}"):
                st.write(f"📊 **Telemetry Logs:** {details}")
                st.write("🚨 **Link Status:** Active Core Loop...")

    # ---- TAB 3: COMBAT CLIPS ----
    with portal_tabs[2]:
        st.write("### 🎬 TRANSMISSION FEED: GUILD SHOWCASE")
        st.info("⚡ System Link Active: Streaming latest high-tier operator profiles.")
        st.video("guild_intro.mp4")
        st.markdown("<p style='font-family: monospace; font-size: 0.85rem; color: #a0aec0; text-align: center;'>⚡ TRACK DATA // Featuring: ANARCHY High Command</p>", unsafe_allow_html=True)

    # ---- TAB 4: NETWORK LINKS ----
    with portal_tabs[3]:
        st.write("### 📡 Main Intercom Array")
        st.write("Establish live voice links, route backup telemetry channels, and bridge chat vectors to our main communications array:")
        st.markdown(f'<a href="https://chat.whatsapp.com/LFHtTSLYkNc5IT2iRFWbYy?s=sh&p=a&mlu=2" target="_blank" class="whatsapp-btn">⚡ BRIDGE QUANTUM COMMS LINK</a>', unsafe_allow_html=True)

    # --- ADMIN OVERSEER CONSOLE ---
    if st.session_state["is_admin"]:
        st.write("---")
        st.markdown("<h2 style='color: #ff0055; font-family: monospace; text-shadow: 0 0 10px rgba(255,0,85,0.4);'>🛡️ OVERSEER COMMAND CONSOLE</h2>", unsafe_allow_html=True)
        
        st.write("### 📝 Inject Node Activity Log")
        member_name = st.text_input("Target Node Designation")
        action = st.selectbox("Command Variable", ["Promote to Enforcer Rank", "Override 1k Points Threshold", "Transmit Low Energy Alert", "Queue Node For Deletion (Purge)"])
        
        if st.button("COMMIT INJECTION"):
            if member_name:
                st.success(f"System Log Altered: **{action}** successfully compiled for **{member_name}**.")
            else:
                st.error("Compilation Interrupted: Node name undefined.")

        st.write("### 📢 Pulse System-Wide Network Broadcast")
        alert_msg = st.text_input("Broadcast Array Telemetry", placeholder="Guild War starts in 1 hour! Get 100pts!")
        if st.button("INITIALIZE BROADCAST WAVE"):
            if alert_msg:
                st.toast(f"BROADCAST VECTOR INITIATED: {alert_msg}")
                st.sidebar.error(f"🚨 BROADCAST: {alert_msg}")
            else:
                st.warning("Cannot pulse empty transmission waves.")
