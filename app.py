import streamlit as st

# 1. Page Configuration (Must be first)
st.set_page_config(page_title="♱ ANARCHY Guild Portal", page_icon="⚔️", layout="centered")

# 2. Safely Initialize Session State Keys & Permanent Admin Accounts
if "guild_accounts" not in st.session_state:
    st.session_state["guild_accounts"] = {
        "dark@gmail.com": "leader123",            # Your Master Account
        "kurotsuki@gmail.com": "kuropass77",      # Kuro
        "savage@gmail.com": "savagepass88",       # Savage
        "emma@anarchy.com": "emma77",             # Emma (Admin)
        "yeng@anarchy.com": "yeng77",             # Yeng (Admin)
    } 

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "current_user" not in st.session_state:
    st.session_state["current_user"] = ""

# Track users who are actively viewing the app during this session
if "online_users" not in st.session_state:
    st.session_state["online_users"] = set()

# 3. Apply Dark Gaming Theme CSS
st.markdown("""
    <style>
    .main { background-color: #0b0c10; color: #c5c6c7; }
    h1, h2, h3 { color: #ff4500 !important; font-family: 'Impact', sans-serif; text-align: center; }
    .guild-header { text-align: center; font-size: 24px; font-weight: bold; color: #ff4500; }
    .guild-id { text-align: center; font-size: 14px; color: #888888; margin-bottom: 20px; }
    .stButton>button { background-color: #ff4500; color: white; border-radius: 5px; width: 100%; font-weight: bold; }
    .stButton>button:hover { background-color: #cc3700; color: white; }
    
    /* Green Online / Gray Offline Custom Styling */
    .status-online { color: #00ff00; font-weight: bold; font-size: 14px; }
    .status-offline { color: #555555; font-size: 14px; }
    
    /* WhatsApp Button Custom Styling */
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
    st.markdown("<h1>🛡️ ♱ ANARCHY 🛡️</h1>")
    st.markdown("<p style='text-align: center; color: #888;'>GUILD ID: 3077980409</p>", unsafe_allow_html=True)
    st.write("Welcome recruit. Access requires a verified guild account sync.")
    
    auth_tabs = st.tabs(["🔴 Sign In", "📝 Create Guild Account"])
    
    # Sign In Tab
    with auth_tabs[0]:
        login_email = st.text_input("Google Email Address", placeholder="username@gmail.com", key="log_email")
        login_password = st.text_input("Password", type="password", key="log_pass")
        
        if st.button("Log In"):
            if login_email in st.session_state["guild_accounts"] and st.session_state["guild_accounts"][login_email] == login_password:
                st.session_state["logged_in"] = True
                st.session_state["current_user"] = login_email
                st.session_state["online_users"].add(login_email)
                st.success("Access Granted!")
                st.rerun()
            else:
                st.error("Invalid credentials. If you are new, head over to the 'Create Guild Account' tab.")
                
    # Create Account Tab
    with auth_tabs[1]:
        new_email = st.text_input("Enter Google Email to Register", placeholder="yourname@gmail.com", key="new_email")
        new_password = st.text_input("Create Account Password", type="password", key="new_pass")
        confirm_password = st.text_input("Confirm Account Password", type="password", key="conf_pass")
        
        if st.button("Register Account"):
            if "@" not in new_email:
                st.error("Please enter a valid Google email format.")
            elif new_email in st.session_state["guild_accounts"]:
                st.error("An account with this email already exists.")
            elif new_password != confirm_password:
                st.error("Passwords do not match.")
            elif len(new_password) < 4:
                st.error("Password must be at least 4 characters long.")
            else:
                st.session_state["guild_accounts"][new_email] = new_password
                st.success("Account created successfully! Click on the 'Sign In' tab above to log in.")

# --- LEADERSHIP DASHBOARD ---
else:
    # Auto-ensure user is marked online if they are logged in
    st.session_state["online_users"].add(st.session_state["current_user"])

    st.markdown("<h1>⚔️ ♱ﾠᴀɴᴀʀᴄʜʏ ⚔️</h1>")
    st.markdown("<div class='guild-header'>♱ﾠDark..guild leader</div>", unsafe_allow_html=True)
    st.markdown("<div class='guild-id'>GUILD ID: 3077980409 • LEVEL 6</div>", unsafe_allow_html=True)
    
    st.write(f"Secure Session: `{st.session_state['current_user']}`")
    
    if st.button("Disconnect Session"):
        if st.session_state["current_user"] in st.session_state["online_users"]:
            st.session_state["online_users"].remove(st.session_state["current_user"])
        st.session_state["logged_in"] = False
        st.session_state["current_user"] = ""
        st.rerun()
        
    st.divider()
    
    portal_tabs = st.tabs(["📜 GUILD ORDERS", "👥 MEMBERS ROSTER", "💬 COMMUNITY HUBS"])
    
    # Guild Rules
    with portal_tabs[0]:
        st.subheader("Sup gamers 🤯.")
        st.error("New guild war season¿?!!\n\nNew rules!!.\n\nHere are the new rules !!!!😑.")
        
        st.markdown("""
        **1.)** Avoid low level of insults and lust messages while talking on the GC, don't insult your admins they have that power for a reason.
        
        **2.)** A failure of getting up to 1k guild points during the end of the week will lead to instant kick!!🥀. *(Note: if u have a sensible reason we can let it slide)* And also don't play any other mode when guild war is on.
        
        **3.)** Any new players will have only 10 days to change their previous names to the name tag that must be given to you by the admin (**Mr.Kυяσтѕυкι**). Failure to do so will be instantly kicked. If you change your name without the custom font you'll be given a grace period of 10 days to change your name to the custom font. Members who haven't changed their name will be kicked.
        
        **4.)** Since guild war time has been changed completely 🥀, (**7 pm - 11 pm on Fridays & Saturdays**), you should get at least 100 guild points.
        
        **5.)** New requirements for guild has being changed:
        * **I.** Level 60 upward
        * **II.** Prime 3 upward
        * **III.** Must be 40% active in GC and FF.
        
        **6.)** There will be guild training every day if possible from 10pm to 11pm. Failure to participate in one of them will result in a temporary kick as a warning.
        
        **7.)** **Zero Tolerance Policy:** If an Admin tags you for a Guild War task and you ignore it while being active in-game, you will be kicked immediately. No excuses 🥀.
        
        **8.)** **Performance Cut:** Members who stay in the bottom 3 of the leaderboard for two weeks straight will be removed to make room for stronger players. We only keep the best.
        
        **9.)** **Chain of Command:** Any public disrespect or arguing with Admins in the GC is considered mutiny. Take your complaints to DMs or face an instant ban 🗿.
        
        **10.)** Fear the elders of anarchy 🗿
        """)
        
        st.divider()
        st.warning("⚠️ NOTE: This is not for the weak, if u can't cooperate pls kindly leave 🥀🥀.")

    # Members List & Presence Indicators
    with portal_tabs[1]:
        st.subheader("📢 OFFICIAL MEMBERS ROSTER")
        
        # Swapped tracking over to their designated admin emails
        members_list = [
            ("♱  DARK", "dark@gmail.com"),
            ("♱ KUROTŚUI", "kurotsuki@gmail.com"),
            ("♱  SAVAGE.", "savage@gmail.com"),
            ("♱  EMMA", "emma@anarchy.com"),
            ("♱  YENG", "yeng@anarchy.com"),
            ("♱  KAISER", "kaiser@gmail.com"),
            ("♱  PRIDE", "pride@gmail.com"),
            ("♱ﾠDAMZY🪶", "damzy@gmail.com"),
            ("♱ﾠHEMJAY", "hemjay@gmail.com")
        ]
        
        st.write("### 🟢 Real-time Presence Tracker")
        for display_name, account_email in members_list:
            if account_email in st.session_state["online_users"]:
                st.markdown(f"**{display_name}** — <span class='status-online'>● Online</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"**{display_name}** — <span class='status-offline'>○ Offline</span>", unsafe_allow_html=True)
                
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

    # Group Links and Chat Aggregators
    with portal_tabs[2]:
        st.subheader("🔗 ANARCHY OFFICIAL HUBS")
        st.write("Quickly hop off the web dashboard directly into our active chat channels below:")
        
        # WhatsApp Redirect Widget Linked Directly
        whatsapp_invite_url = "https://chat.whatsapp.com/LFHtTSLYkNc5IT2iRFWbYy?s=sh&p=a&mlu=2"
        
        st.markdown(f'<a href="{whatsapp_invite_url}" target="_blank" class="whatsapp-btn">🟢 JOIN OFFICIAL WHATSAPP GC</a>', unsafe_allow_html=True)
        st.info("💡 Clicking the green button opens your WhatsApp client directly into the clan chat.")

# --- SHARED LEADERSHIP SECURITY LOG PANEL ---
# Grants full administrative visibility to you and all designated core admins
admin_list = ["dark@gmail.com", "kurotsuki@gmail.com", "savage@gmail.com", "emma@anarchy.com", "yeng@anarchy.com"]
if st.session_state["current_user"] in admin_list:
    st.divider()
    st.subheader("🛡️ Admin Security Log")
    st.info(f"Logged in as Verified Administrator: `{st.session_state['current_user']}`")
    st.write("Registered accounts currently stored in system memory:")
    for active_email in st.session_state["guild_accounts"].keys():
        st.code(f"• {active_email}")
