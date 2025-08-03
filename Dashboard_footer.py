import streamlit as st

def dashboard_footer():
    st.markdown("""<hr style="margin-top: 40px;">""", unsafe_allow_html=True)
    st.markdown(
        """
        <div style='text-align: center; color: grey; font-size: 14px;'>
            Designed and Developed by <b>❤️ Sharndeep Kaur</b>
        </div>
        """,
        unsafe_allow_html=True
    )
