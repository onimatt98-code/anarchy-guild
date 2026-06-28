import streamlit as st
from datetime import datetime

# 1. Page Configuration
st.set_page_config(page_title="♱ ANARCHY Guild Portal", page_icon="⚔️", layout="centered")

# 2. Permanent Guild Credentials
GUILD_PASSWORD = "anarchy2026"
MASTER_ADMIN_PASSWORD = "anarchyadmin"

# 3. Persistent Database Initialization (Using Streamlit's fragment-safe dictionary)
if "db_initialized" not in st.experimental_get_query_params():
    if "guild_orders" not in st.session_state:
        st.session_state["guild_orders"] = """**1.)** Avoid low level of insults and lust messages while talking on the GC, don't insult your admins they have that power for a reason.
        
**2.)** A failure of getting up to 1k guild points during the end of the week will lead to instant kick!!🥀.

**3.)** Any new players will have only 10 days to change their previous names to the name tag that must be given to you by the admin (**Mr.Kυяσтѕυкι**).

**4.)** Since guild war time has been changed completely 🥀, (**7 pm - 11 pm on Fridays & Saturdays**), you should get at least 100 guild points.

**5.)** New requirements for guild: Level 60 upward, Prime 3 upward, 40% active in GC and FF.

**6.)** There will be guild training every day if possible from 10pm to 11pm.

**7.)** **Zero Tolerance Policy:** If an Admin tags you for a Guild War task and you ignore it, you will be kicked immediately.

**8.)** **Performance Cut:** Members who stay in the bottom 3 of the leaderboard for two weeks straight will be removed.

**9.)** **Chain of Command:** Any public disrespect or arguing with Admins in the GC is an instant ban 🗿.

**10.)** Fear the elders of anarchy 🗿"""

    if "user_presence" not in st.session_state:
        # Default baseline tracking matrix for full squad
        st.session_state["user_presence"] = {
            "♱  DARK": {"status": "Offline", "last_seen": "Never"},
            "♱ KUROTŚUI": {"status": "Offline", "last_seen": "Never"},
            "♱  SAVAGE.": {"status": "Offline", "last_seen": "Never"},
            "♱  EMMA": {"status": "Offline", "last_seen": "Never"},
            "♱  YENG": {"status": "Offline", "last_seen": "Never"},
            "♱  KAISER": {"status": "Offline", "last_seen": "Never"},
            "♱  PRIDE": {"status": "Offline", "last_seen": "Never"},
            "♱ﾠDAMZY🪶": {"status": "Offline", "last_seen": "Never"},
            "♱ﾠHEMJAY": {"status": "Offline", "last_seen": "Never"},
        }

# Initialize dynamic operational variables
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "is_admin" not in st.session_state:
    st.session_state["is_admin"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

# 4. Clean Dark-Gaming Theme UI Architecture
st.markdown("""
    <style>
    .main { background-color: #0b0c10; color: #c5c6c7; }
    .stButton>button { background-color: #ff4500; color: white; border-radius: 5px; width: 100%; font-weight: bold; }
    .stButton>button:hover { background-color: #cc3700; color: white; }
    
    .whatsapp-btn {
        display: block;
        background-color: #25D366;
        color: white !important;
        text-align: center;
        padding: 12px;
        border-radius: 8px;
        font-weight: bold;
        text-decoration: none;
        margin: 15px auto;
        width: 80%;
    }
    .whatsapp-btn:hover { background-color: #128C7E; }
    
    .status-online { color: #00ff00; font-weight: bold; font-family: monospace; }
    .status-offline { color: #ff3333; font-weight: bold; font-family: monospace; }
    .timestamp { color: #888888; font-size: 12px; font-family: monospace; }
    </style>
""", unsafe_allow_html=True)

# --- LOGIN GATEWAY ---
if not st.session_state["logged_in"]:
    st.title("🛡️ ♱ ANARCHY 🛡️")
    st.caption("GUILD ID: 3077980409 • LEVEL 6")
    
    st.write("### ⚔️ Portal Verification")
    st.write("Enter your Game Name and password to sync with the network core.")
    
    user_name = st.text_input("Free Fire Name", placeholder="e.g., ♱ KAISER")
    access_password = st.text_input("Password", type="password", placeholder="Enter clan or admin passcode")
    
    if st.button("Sync Dashboard"):
        cleaned_name = user_name.strip()
        current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if cleaned_name == "":
            st.error("Identification required. Input your Free Fire name layout.")
        
        elif access_password == MASTER_ADMIN_PASSWORD:
            st.session_state["logged_in"] = True
            st.session_state["is_admin"] = True
            st.session_state["username"] = cleaned_name
            
            # Log admin online in persistent dict
            st.session_state["user_presence"][cleaned_name] = {"status": "Online", "last_seen": current_time_str}
            st.success("Master Administrative Access Granted!")
            st.rerun()
            
        elif access_password == GUILD_PASSWORD:
            st.session_state["logged_in"] = True
            st.session_state["is_admin"] = False
            st.session_state["username"] = cleaned_name
            
            # Log member online in persistent dict
            st.session_state["user_presence"][cleaned_name] = {"status": "Online", "last_seen": current_time_str}
            st.success("Access Granted!")
            st.rerun()
            
        else:
            st.error("Access Denied. Passcode mismatch.")

# --- MAIN DASHBOARD INTERFACE ---
else:
    st.title("⚔️ ♱ﾠᴀɴᴀʀᴄʜʏ ⚔️")
    st.subheader(f"Logged in as: {st.session_state['username']}")
    
    if st.button("Disconnect Session"):
        # Switch status to offline safely upon logout
        current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state["user_presence"][st.session_state["username"]] = {"status": "Offline", "last_seen": current_time_str}
        
        st.session_state["logged_in"] = False
        st.session_state["is_admin"] = False
        st.session_state["username"] = ""
        st.rerun()
        
    st.divider()
    
    portal_tabs = st.tabs(["📜 GUILD ORDERS", "👥 MEMBERS ROSTER", "💬 COMMUNITY HUBS"])
    
    # Guild Orders Tab (Loads dynamically from system state database)
    with portal_tabs[0]:
        st.write("### Sup gamers 🤯.")
        st.error("New guild war season¿?!! New rules!! Here are the new rules !!!!😑.")
        
        st.markdown(st.session_state["guild_orders"])
        
        st.divider()
        st.warning("⚠️ NOTE: This is not for the weak, if u can't cooperate pls kindly leave 🥀🥀.")

    # Members Presence Tracking Roster
    with portal_tabs[1]:
        st.write("### 📢 OFFICIAL MEMBERS ROSTER")
        
        st.write("**Core Leadership Group:**")
        st.markdown("""
        * 👑 **♱  DARK** (Guild Leader)
        * 🛡️ **♱ KUROTŚUI** (Admin)
        * 🛡️ **♱  SAVAGE.** (Admin)
        * 🛡️ **♱  EMMA** (Admin)
        * 🛡️ **♱  YENG** (Admin)
        """)
        
        st.write("**Active Roster Enforcers:**")
        st.markdown("""
        * ⚔️ **♱  KAISER**
        * ⚔️ **♱  PRIDE**
        * ⚔️ **♱ﾠDAMZY🪶**
        * ⚔️ **♱ﾠHEMJAY**
        """)
        
        st.divider()
        st.write("### 📋 Full Bench Roster")
        extra_members = [
            "IME々DAVE★", "♱ CUBA", "B₂KMUBBY🪶", "GS JOKERツ", "🪶 HAKUTSUK", 
            "♱ \"SONXC\"", "♱ SHADOW", "D🪶A🪶D🪶Y🪶!", "I'M GRAMPX☠️", "♱ SHEGZY", 
            "LEVI™", "♱ GHOST", "T WING", "♱ ITACHI", "♱ SLIME", "♱LĀŚTBØRŃ", 
            ">ONE ISAGI¿", "♱ SMART", "♱ MONSTER", "JYROKILLA☠️☠️", "♱ BANDIT", 
            "♱ MORGAN", "乂MR▪SHADOU", "EVIL🪶★TØXÎÇ", "♱ CHARLIE", "♱ MARCELO", "♱ DRAGON•"
        ]
        for idx, b_member in enumerate(extra_members, start=10):
            st.markdown(f"**{idx}.** `{b_member}`")

    # Community Redirect Links
    with portal_tabs[2]:
        st.write("### 🔗 ANARCHY OFFICIAL HUBS")
        whatsapp_invite_url = "https://chat.whatsapp.com/LFHtTSLYkNc5IT2iRFWbYy?s=sh&p=a&mlu=2"
        st.markdown(f'<a href="{whatsapp_invite_url}" target="_blank" class="whatsapp-btn">🟢 JOIN OFFICIAL WHATSAPP GC</a>', unsafe_allow_html=True)

# --- PRIVILEGED REAL-TIME ADMIN MANAGEMENT CORE ---
if st.session_state["is_admin"]:
    st.divider()
    st.write("## 🛡️ Admin Management Console")
    st.info(f"Verified Session Control Matrix: {st.session_state['username']}")
    
    # 1. LIVE PRESENCE LOG INTERFACE
    st.write("### 👥 Live Presence Tracker (Online / Offline)")
    
    for user, data in st.session_state["user_presence"].items():
        if data["status"] == "Online":
            st.markdown(f"👤 **{user}** — <span class='status-online'>🟢 Online Now</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"👤 **{user}** — <span class='status-offline'>🔴 Offline</span> <span class='timestamp'>(Last sync: {data['last_seen']})</span>", unsafe_allow_html=True)
            
    st.divider()
    
    # 2. PERSISTENT LIVE RULES MODIFIER
    st.write("### 📝 Edit Guild Orders & Announcements")
    st.write("Modify the text block below to change the live rules on the front dashboard instantly.")
    
    updated_text = st.text_area("Edit Live Rules Markdown", value=st.session_state["guild_orders"], height=300)
    
    if st.button("💾 Save & Publish System Updates"):
        st.session_state["guild_orders"] = updated_text
        st.success("System updated successfully! Changes are live on the front page.")
        st.rerun()
