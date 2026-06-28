import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="♱ ANARCHY Guild Portal", page_icon="⚔️", layout="centered")

# 2. Permanent Guild Credentials
GUILD_PASSWORD = "anarchy2026"  # The one password for the entire clan
ADMIN_EMAILS = ["dark@gmail.com", "kurotsuki@gmail.com", "savage@gmail.com", "emma@anarchy.com", "yeng@anarchy.com"]

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
    
    /* WhatsApp Button Styling */
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
    st.write("Enter your Game Name and the Guild Password to sync with the dashboard.")
    
    user_name = st.text_input("Your Free Fire Name", placeholder="e.g., ♱  DARK")
    access_password = st.text_input("Guild Password", type="password", placeholder="Enter official clan password")
    
    # Simple check to see if an admin wants to use their master email instead
    admin_email_input = st.text_input("Admin Email (Optional - Leave blank if regular member)", placeholder="admin@gmail.com")

    if st.button("Access Dashboard"):
        if access_password == GUILD_PASSWORD and user_name.strip() != "":
            st.session_state["logged_in"] = True
            st.session_state["username"] = user_name.strip()
            
            # Check if this user logged in with a verified admin email
            if admin_email_input.lower() in ADMIN_EMAILS:
                st.session_state["is_admin"] = True
            
            st.success("Access Granted!")
            st.rerun()
        elif user_name.strip() == "":
            st.error("Please enter your Free Fire name so the clan knows who you are.")
        else:
            st.error("Incorrect Guild Password. Ask your leadership group for the correct passcode.")

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
    
    # Guild Rules
    with portal_tabs[0]:
        st.write("### Sup gamers 🤯.")
        st.error("New guild war season¿?!! New rules!! Here are the new rules !!!!😑.")
        
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

    # Members List
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

    # Community Links
    with portal_tabs[2]:
        st.write("### 🔗 ANARCHY OFFICIAL HUBS")
        st.write("Quickly hop off the web dashboard directly into our active chat channels below:")
        
        whatsapp_invite_url = "https://chat.whatsapp.com/LFHtTSLYkNc5IT2iRFWbYy?s=sh&p=a&mlu=2"
        st.markdown(f'<a href="{whatsapp_invite_url}" target="_blank" class="whatsapp-btn">🟢 JOIN OFFICIAL WHATSAPP GC</a>', unsafe_allow_html=True)
        st.info("💡 Clicking the green button opens your WhatsApp client directly into the clan chat.")

# --- PRIVILEGED ADMIN ONLY PANEL ---
if st.session_state["is_admin"]:
    st.divider()
    st.write("### 🛡️ Admin Management Console")
    st.info(f"Secure Admin Session Verified.")
    st.write(f"Current System Master Password: `{GUILD_PASSWORD}`")
