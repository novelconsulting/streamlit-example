import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="Multipage app",
    page_icon=""
)

# set a navigation bar horizontally on the main page using streamlit-option-menu
# https://github.com/victoryhb/streamlit-option-menu



st.title("Main Page")
st.sidebar.success("Select a page above")

if "my_input " not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit=st.button("Submit")
if submit:
    st.session_state["my_input"] =  my_input
    st.write("You have entered", my_input)

# to be used for selected page in case we go that way
#def.createPage():
#  st.empty()
#  st.title("PAGE HOME")
#
#  return true
