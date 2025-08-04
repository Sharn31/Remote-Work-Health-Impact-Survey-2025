import streamlit as st 
import sqlite3
from remote_job_health_impact_dashboard import show_dashboard
from Login_footer import show_footer
from Dashboard_footer import dashboard_footer
from streamlit_option_menu import option_menu
import hashlib
import re
st.title("🧑‍💻Remote Work Health Impact Survey 2025")


conn = sqlite3.connect('app_users.db', check_same_thread=False)
cursor = conn.cursor()
def create_user_table():
     
    
    cursor.execute(
        '''CREATE TABLE  IF NOT EXIsTS app_users(
        username TEXT PRIMARY KEY,
        email TEXT,
        password TEXT)
                ''')
    conn.commit()
    #conn.close()
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_email(email):
    # Basic email regex pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)


def add_user(username,email,password):
    
    sqlite3.connect("app_users.db")
    cursor=conn.cursor()
    hashed_pass = hash_password(password)
    cursor.execute("INSERT INTO app_users (username,email,password)VALUES(?,?,?)",(username,email,hashed_pass))
    
    conn.commit()
    #conn.close()

def login_user(username,password):
    sqlite3.connect("app_users.db")
    cursor=conn.cursor()  
    hashed_pass = hash_password(password) 
    cursor.execute("SELECT * FROM app_users WHERE username=? AND password =?",(username,hashed_pass))
    data=cursor.fetchone()
    #conn.close()
    return data 

def show_signup():
    st.subheader("🛅Create New Account")

    
    new_user = st.text_input("Create Username")
    new_email=st.text_input("Enter your email")
    new_pass = st.text_input("Create Password", type="password")
    if st.button("Sign Up"):
        if not new_user or not new_email or not new_pass:
            st.warning("Please enter username, email, and password.")
        elif user_exists(new_user):
            st.warning("Username already exists. Please choose a different one.")
        elif not is_valid_email(new_email):
            st.warning("Invalid email format. Please enter a valid email.")
        elif email_exists(new_email):
            st.warning("Email already used. Try logging in.")
        else:
            add_user(new_user, new_email, new_pass)
            st.success("✅ Account created successfully. You can now login.")


def show_login():
    st.subheader("🔐Sign In")
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("🔓Login"):
        if login_user(user, password):
            st.session_state.logged_in = True
            st.session_state.username = user
            st.success(f"Welcome {user} 🎉")
            st.rerun() 
        else:
            st.error("Invalid username or password.")

def user_exists(username):
    cursor.execute("SELECT 1 FROM app_users WHERE username=?", (username,))
    return cursor.fetchone() is not None

def email_exists(email):
    cursor.execute("SELECT 1 FROM app_users WHERE email=?", (email,))
    return cursor.fetchone() is not None




def main():
    
   
    st.set_page_config("Login App", layout="centered")
    create_user_table()
    # Inject full sidebar styling
    st.markdown("""
        <style>
            [data-testid="stSidebar"] {
                background-color: #1f3bb3;
                padding-top: 30px;
            }
            [data-testid="stSidebar"] img {
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 120px;
                border-radius: 10px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "";
                display: block;
                margin-bottom: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        show_dashboard(st.session_state["username"])  # Your dashboard function
    else:
        with st.sidebar:
            st.sidebar.image("logo.png", width=200)
            selected = option_menu(
                menu_title="",
                options=["Sign In", "Sign Up"],
                icons=["box-arrow-in-right", "person-plus"],
                default_index=0,
                orientation="vertical",
                styles={
                    "container": {
                        "padding": "0px",
                        "background-color": "#1f3bb3"
                    },
                    "icon": {
                        "color": "white",
                        "font-size": "20px"
                    },
                    "nav-link": {
                        "font-size": "16px",
                        "color": "white",
                        "text-align": "center",
                        "margin": "5px",
                        "--hover-color": "#3949ab"
                    },
                    "nav-link-selected": {
                        "background-color": "#061d41",
                        "font-weight": "bold",
                        "color": "white"
                    }
                }
            )

        if selected == "Sign In":
            show_login()
        elif selected == "Sign Up":
            show_signup()

        show_footer()
if __name__ == "__main__":
    main()