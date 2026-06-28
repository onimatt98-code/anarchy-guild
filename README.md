import streamlit as st

# Set up the page configuration with a knight emblem
st.set_page_config(page_title="♱ﾠᴀɴᴀʀᴄʜʏ Guild Portal", page_icon="⚔️", layout="centered")

# Custom CSS for an elite, dark gaming vibe matching your emblem theme
st.markdown("""
    <style>
    .main { background-color: #0b0c10; color: #c5c6c7; }
    h1, h2, h3 { color: #ff4500 !important; font-family: 'Impact', sans-serif; text-align: center; }
    .guild-header { text-align: center; font-size: 24px; font-weight: bold; color: #ff4500; }
    .guild-id { text-align: center; font-size: 14px; color: #888888; margin-bottom: 20px; }
    .stButton>button { background-color: #ff4500; color: white; border-radius: 5px; width: 100%; font-weight: bold; }
    .stButton>button:hover { background-color: #cc3700; color: white; }
    </style>
""", unsafe_allow_html=True)

# Initialize a simple data store for accounts in session state
if "guild_accounts" not in st.session_state:
    st.session_state["guild_accounts"] = {"dark@gmail.com": "leader123"} 

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "current_user" not in st.session_state:
    st.session_state["current_user"] = ""

# --- LOGIN & SIGN UP GATEWAY ---
if not st.session_state["logged_in"]:
    st.markdown("<h1>🛡️ ♱ﾠᴀɴᴀʀᴄʜʏ 🛡️</h1>")
    st.markdown("<p style='text-align: center; color: #888;'>GUILD ID: 3077980409</p>", unsafe_allow_html=True)
    st.write("Welcome recruit. Access requires a verified guild account sync.")
    
    # Selection tabs for Sign In vs Creating an Account
    auth_tabs = st.tabs(["🔴 Sign In with Google", "📝 Create Guild Account"])
    
    # Tab 1: Sign In
    with auth_tabs[0]:
        login_email = st.text_input("Google Email Address", placeholder="username@gmail.com", key="log_email")
        login_password = st.text_input("Password", type="password", key="log_pass")
        
        if st.button("Log In"):
            if login_email in st.session_state["guild_accounts"] and st.session_state["guild_accounts"][login_email] == login_password:
                st.session_state["logged_in"] = True
                st.session_state["current_user"] = login_email
                st.success("Access Granted!")
                st.rerun()
            else:
                st.error("Invalid credentials. If you are new, head over to the 'Create Guild Account' tab.")
                
    # Tab 2: Create Account
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
                st.success("Account created successfully! Click on the 'Sign In with Google' tab above to log in.")

# --- GUILD LEADER DASHBOARD & SECTIONS ---
else:
    # Header showcasing the Dark Knight leadership
    st.markdown("<h1>⚔️ ♱ﾠᴀɴᴀʀᴄʜʏ ⚔️</h1>")
    st.markdown("<div class='guild-header'>♱ﾠDark..guild leader</div>", unsafe_allow_html=True)
    st.markdown("<div class='guild-id'>GUILD ID: 3077980409 • LEVEL 6</div>", unsafe_allow_html=True)
    
    st.write(f"Secure Session: `{st.session_state['current_user']}`")
    
    if st.button("Disconnect Session", use_container_width=False):
        st.session_state["logged_in"] = False
        st.session_state["current_user"] = ""
        st.rerun()
        
    st.divider()
    
    # App Tabs: Rules and the verified Roster list
    portal_tabs = st.tabs(["📜 GUILD ORDERS", "👥 MEMBERS ROSTER"])
    
    # --- TAB 1: RULES ---
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
        
        > **IN ADDITION:** No posting of 1 v 1 screenshots except it's an Official match hosted by the admins.
        
        **8.)** **Performance Cut:** Members who stay in the bottom 3 of the leaderboard for two weeks straight will be removed to make room for stronger players. We only keep the best.
        
        **9.)** **Chain of Command:** Any public disrespect or arguing with Admins in the GC is considered mutiny. Take your complaints to DMs or face an instant ban 🗿.
        
        **10.)** Fear the elders of anarchy 🗿
        """)
        
        st.divider()
        st.warning("⚠️ NOTE: This is not for the weak, if u can't cooperate pls kindly leave 🥀🥀.")

    # --- TAB 2: MEMBERS ---
    with portal_tabs[1]:
        st.subheader("📢 OFFICIAL MEMBERS ROSTER")
        st.write("Active units detected in server database:")
        
        # Comprehensive membership lists gathered from ALL your screenshots
        members_list = [
            "♱  DARK", "♱  SAVAGE.", "♱  KAISER", "♱  EMMA", "♱  PRIDE",
            "♱ﾠDAMZY🪶", "IME々DAVE★", "♱ YENG", "♱ KUROTŚUI", "♱ CUBA",
            "B₂KMUBBY🪶", "GS JOKERツ", "🪶 HAKUTSUK", "♱ \"SONXC\"", "♱ SHADOW",
            "D🪶A🪶D🪶Y🪶!", "I'M GRAMPX☠️", "♱ SHEGZY", "LEVI™", "♱ GHOST",
            "T WING", "♱ ITACHI", "♱ SLIME", "♱LĀŚTBØRŃ", ">ONE ISAGI¿",
            "♱ SMART", "♱ MONSTER", "JYROKILLA☠️☠️", "♱ BANDIT", "♱ MORGAN",
            "乂MR▪SHADOU", "EVIL🪶★TØXÎÇ", "♱ CHARLIE", "♱ MARCELO", "♱ DRAGON•"
        ]
        
        for i, member in enumerate(members_list, start=1):
            st.markdown(f"**{i}.** `{member}`")
