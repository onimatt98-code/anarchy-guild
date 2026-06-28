import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="♱ ANARCHY Guild Portal", page_icon="⚔️", layout="centered")

# 2. Permanent Guild Credentials
GUILD_PASSWORD = "anarchy2026"
# Only these emails will unlock the Admin Management Console
ADMIN_EMAILS = ["dark@gmail.com", "kurotsuki@gmail.com", "emma@gmail.com", "yeng@gmail.com", "pride@gmail.com"]

# Initialize login states
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "is_admin" not in st.session_state:
    st.session_state["is_admin"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

# 3. Clean Theme Custom Styling
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
    </style>
""", unsafe_allow_html=True)

# --- LOGIN GATEWAY ---
if not st.session_state["logged_in"]:
    st.title("🛡️ ♱ ANARCHY 🛡️")
    st.caption("GUILD ID: 3077980409 • LEVEL 6")
    
    st.write("### ⚔️ Clan Verification")
    user_name = st.text_input("Your Free Fire Name", placeholder="e.g., ♱  DARK")
    access_password = st.text_input("Guild Password", type="password", placeholder="Enter official clan password")
    admin_email_input = st.text_input("Administrative Email (Required for Admin Access)", placeholder="Enter email to verify rank")

    if st.button("Access Dashboard"):
        if access_password == GUILD_PASSWORD and user_name.strip() != "":
            st.session_state["logged_in"] = True
            st.session_state["username"] = user_name.strip()
            
            # Admin Authentication Check
            if admin_email_input.lower() in ADMIN_EMAILS:
                st.session_state["is_admin"] = True
                st.success("Administrative Access Verified.")
            else:
                st.session_state["is_admin"] = False
                st.info("Logged in as Member.")
            st.rerun()
        elif user_name.strip() == "":
            st.error("Please enter your Free Fire name.")
        else:
            st.error("Incorrect Guild Password.")

# --- LEADERSHIP DASHBOARD ---
else:
    st.title("⚔️ ♱ﾠᴀɴᴀʀᴄʜʏ ⚔️")
    st.subheader(f"Welcome back, {st.session_state['username']} ⚔️")
    
    if st.button("Disconnect Session"):
        st.session_state["logged_in"] = False
        st.session_state["is_admin"] = False
        st.session_state["username"] = ""
        st.rerun()
        
    st.divider()
    
    portal_tabs = st.tabs(["📜 GUILD ORDERS", "👥 MEMBERS ROSTER", "💬 COMMUNITY HUBS"])
    
    with portal_tabs[0]:
        st.write("### Sup gamers 🤯.")
        st.error("New guild war season¿?!! New rules!! Here are the new rules !!!!😑.")
        st.markdown("""
        **1.)** Avoid low level of insults and lust messages while talking on the GC, don't insult your admins they have that power for a reason.
        **2.)** Failure to get 1k guild points weekly leads to instant kick!!🥀.
        **3.)** New players have 10 days to adopt the guild name tag provided by the admin.
        **4.)** Guild war time: 7 pm - 11 pm on Fridays & Saturdays (minimum 100 points).
        **5.)** Requirements: Level 60+, Prime 3+, 40% activity.
        **6.)** Daily guild training 10pm-11pm.
        **7.)** Zero Tolerance: Ignoring admin tags results in instant kick.
        **8.)** Performance Cut: Bottom 3 players removed every two weeks.
        **9.)** Chain of Command: No public disrespect to Admins.
        **10.)** Fear the elders of anarchy 🗿
        """)
        st.divider()
        st.warning("⚠️ NOTE: This is not for the weak, if u can't cooperate pls kindly leave 🥀🥀.")

    with portal_tabs[1]:
        st.write("### 📢 OFFICIAL MEMBERS ROSTER")
        st.write("**Core Leadership Group:**")
        st.markdown("""
        * 👑 **♱  DARK** (Guild Leader)
        * 🛡️ **♱ KUROTŚUI** (Admin)
        * 🛡️ **♱  PRIDE** (Admin)
        * 🛡️ **♱  EMMA** (Admin)
        * 🛡️ **♱  YENG** (Admin)
        """)
        st.write("**Active Roster Enforcers:**")
        st.markdown("""
        * ⚔️ **♱  KAISER**
        * ⚔️ **♱  SAVAGE.**
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

    with portal_tabs[2]:
        st.write("### 🔗 ANARCHY OFFICIAL HUBS")
        whatsapp_invite_url = "https://chat.whatsapp.com/LFHtTSLYkNc5IT2iRFWbYy?s=sh&p=a&mlu=2"
        st.markdown(f'<a href="{whatsapp_invite_url}" target="_blank" class="whatsapp-btn">🟢 JOIN OFFICIAL WHATSAPP GC</a>', unsafe_allow_html=True)

# --- PRIVILEGED ADMIN ONLY PANEL ---
if st.session_state["is_admin"]:
    st.divider()
    st.write("### 🛡️ Admin Management Console")
    st.info(f"Secure Admin Session Verified.")
