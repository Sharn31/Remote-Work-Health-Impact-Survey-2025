# --- Footer ---
import streamlit as st 
def show_footer():
    st.markdown("""
        <style>
            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: transparent;
                text-align: center;
                padding: 10px;
                font-size: 13px;
                color: grey;
            }
        </style>
        <div class="footer">
            🔒 Login Required | Designed and Developed by <b>❤️Sharndeep Kaur</b>
        </div>
    """, unsafe_allow_html=True)

show_footer()
