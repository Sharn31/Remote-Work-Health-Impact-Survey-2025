import streamlit as st 
import sqlite3
from remote_job_health_impact_dashboard import show_dashboard
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

def add_user(username,email,password):
    sqlite3.connect("app_users.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO app_users (username,email,password)VALUES(?,?,?)",(username,email,password))
    
    conn.commit()
    #conn.close()

def login_user(username,password):
    sqlite3.connect("app_users.db")
    cursor=conn.cursor()   
    cursor.execute("SELECT * FROM app_users WHERE username=? AND password =?",(username,password))
    data=cursor.fetchone()
    #conn.close()
    return data 

def show_signup():
    st.subheader("Create New Account")

    
    new_user = st.text_input("Create Username")
    new_email=st.text_input("Enter your email")
    new_pass = st.text_input("Create Password", type="password")
    if st.button("Sign Up"):
        if not new_user or not new_email or not new_pass:
            st.warning("Please enter username, email, and password.")
        elif user_exists(new_user):
            st.warning("Username already exists. Please choose a different one.")
        elif email_exists(new_email):
            st.warning("Email already used. Try logging in.")
        else:
            add_user(new_user, new_email, new_pass)
            st.success("✅ Account created successfully. You can now login.")


def show_login():
    st.subheader("Sign In")
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_user(user, password):
            st.session_state.logged_in = True
            st.session_state.username = user
            st.success(f"Welcome {user} 🎉")
        else:
            st.error("Invalid username or password.")

def user_exists(username):
    cursor.execute("SELECT 1 FROM app_users WHERE username=?", (username,))
    return cursor.fetchone() is not None

def email_exists(email):
    cursor.execute("SELECT 1 FROM app_users WHERE email=?", (email,))
    return cursor.fetchone() is not None

###Main
def main():
    st.set_page_config("Login App",layout="centered")
    create_user_table()
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        show_dashboard(st.session_state["username"])#calling dashboard

    else:
        menu = st.sidebar.selectbox("Sign up/Login", ["Sign In", "Sign Up"])
        if menu == "Sign In":
            show_login()
        elif menu == "Sign Up":
            show_signup()

if __name__ == "__main__":
    main()


    