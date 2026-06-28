import streamlit as st
from datetime import datetime

# 1. Page Configuration
st.set_page_config(page_title="♱ ANARCHY Guild Portal", page_icon="⚔️", layout="centered")

# 2. Permanent Guild Credentials
GUILD_PASSWORD = "anarchy2026"
MASTER_ADMIN_PASSWORD = "anarchyadmin"

# 3. Persistent Database Initialization (Fixed command)
if "db_initialized" not in st.query_params:
    if "guild_orders" not in st.session_state:
        st.session_state["guild_orders"] = """**1.)** Avoid low level of insults and lust messages while talking on the GC.
        
**2.)** 1k guild points minimum per week or instant kick!!🥀.

**3.)** New members must use the custom name tag given by the admin (**Mr.Kυяσтѕυкι**).

**4.)** Guild Wars: Fridays & Saturdays (7pm - 11pm).

**5.)** Requirements: Level 60+, Prime 3+, 40% active in GC and FF."""

    if "user_presence" not in st.session_state:
        st.session_state["user_presence"] = {
            "♱  DARK": {"status": "Offline", "last_seen": "Never"},
            "♱ KUROTŚUI": {"status": "Offline", "last_seen": "Never"},
            "♱  SAVAGE.": {"status": "Offline", "last_seen": "Never"},
            "♱  EMMA": {"status": "Offline", "last_seen": "Never"},
            "♱  YENG": {"status": "Offline", "last_seen": "Never"},
            "♱  KAISER": {"status": "Offline", "last_seen": "Never"},
            "♱  PRIDE": {"status": "Offline", "last_seen": "Never"},
        }
    st.query_params["db_initialized"] = "true"

# Initialize state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "is_admin" not in st.session_state:
    st.session_state["is_admin"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

# Styling
st.markdown("""
    <style>
    .main { background-color: #0b0c10; color: #c5c6c7; }
    .stButton>button { background-color: #ff4500; color: white; border-radius: 5px; width: 100%; font-weight: bold; }
    .status-online { color: #00ff00; font-weight: bold; }
    .status-offline { color: #ff3333; }
    </style>
""", unsafe_allow_html=True)

# --- LOGIN ---
if not st.session_state["logged_in"]:
    st.title("🛡️ ♱ ANARCHY 🛡️")
    user_name = st.text_input("Free Fire Name")
    password = st.text_input("Password", type="password")
    
    if st.button("Sync Dashboard"):
        if password == MASTER_ADMIN_PASSWORD:
            st.session_state["logged_in"] = True
            st.session_state["is_admin"] = True
            st.session_state["username"] = user_name
            st.session_state["user_presence"][user_name] = {"status": "Online", "last_seen": datetime.now().strftime("%H:%M")}
            st.rerun()
        elif password == GUILD_PASSWORD:
            st.session_state["logged_in"] = True
            st.session_state["username"] = user_name
            st.session_state["user_presence"][user_name] = {"status": "Online", "last_seen": datetime.now().strftime("%H:%M")}
            st.rerun()
        else:
            st.error("Invalid password.")

# --- DASHBOARD ---
else:
    st.title("⚔️ ♱ﾠᴀɴᴀʀᴄʜʏ ⚔️")
    if st.button("Disconnect"):
        st.session_state["user_presence"][st.session_state["username"]]["status"] = "Offline"
        st.session_state["logged_in"] = False
        st.rerun()
        
    portal_tabs = st.tabs(["📜 ORDERS", "👥 ROSTER", "🛡️ ADMIN"])
    
    with portal_tabs[0]:
        st.markdown(st.session_state["guild_orders"])
        
    with portal_tabs[1]:
        for user, data in st.session_state["user_presence"].items():
            color = "status-online" if data["status"] == "Online" else "status-offline"
            st.markdown(f"{user}: <span class='{color}'>{data['status']}</span>", unsafe_allow_html=True)

    with portal_tabs[2]:
        if st.session_state["is_admin"]:
            st.write("### Admin Editor")
            new_rules = st.text_area("Edit Rules", value=st.session_state["guild_orders"])
            if st.button("Save Rules"):
                st.session_state["guild_orders"] = new_rules
                st.rerun()
        else:
            st.warning("Admin access required.")
