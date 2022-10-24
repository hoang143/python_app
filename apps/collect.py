import streamlit as st
import leafmap.foliumap as leafmap

def app():
    # page_title = st.title("Map")
    m = leafmap.Map(locate_control=True)
    m.add_basemap("ROADMAP")
    m.to_streamlit(height = 450, width = 830)
