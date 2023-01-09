import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="Multipage app",
    page_icon=""
)

# set a navigation bar horizontally on the main page using streamlit-option-menu
# https://github.com/victoryhb/streamlit-option-menu
selected = option_menu(
    menu_title= None,
    options=["Homepage", "Projects", "Contact"],
    icons=["house","book","envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {"font-size": "25px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)


def switch_page(page_name: str):
    from streamlit import _RerunData, _RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")

    page_name = standardize_name(page_name)

    pages = get_pages("streamlit_app.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise _RerunException(
                _RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")

if selected == "Projects":
    switch_page("Projects")

if selected == "Contact":
    switch_page("Contact")


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
