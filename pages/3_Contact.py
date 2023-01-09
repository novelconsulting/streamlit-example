import streamlit as st

st.set_page_config(
    page_title="Multipage app",
    page_icon=""
)

st.title("Contact Us")

contact_form = """
<form action="https://formsubmit.co/rolandtannous@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Yout name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Details of your problem"></textarea>
     <input type="hidden" name="_captcha" value="false">
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
