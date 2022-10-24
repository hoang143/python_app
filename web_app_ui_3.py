#streamlit run C:\Users\84965\Desktop\web_app_ui_2\web_app_ui_2.py

import streamlit as st
import time
import requests
import json
from streamlit_option_menu import option_menu
from apps import collect, depthsurvey   # import your app modules here

import pandas as pd
import numpy as np
import plost
from PIL import Image
import matplotlib.pyplot as plt
import altair as alt
import plotly.figure_factory as ff
import plotly.graph_objects as go


# ------------------------------ Page setting ------------------------------
st.set_page_config( page_title = "THE F.I.R.S.T",
					layout = "wide")
#st.markdown("#")
#------------------------------- Aplly CSS ----------------------------------
with open('style.css', encoding='utf-8-sig') as file:
	data = file.read()
	print(data)
	st.markdown(f'<style>{data}</style>', unsafe_allow_html=True)

# ------------------------------ Initialization ------------------------------

# ------- Page structure -------

display_section = st.empty()
gauge_section = st.empty()

# ------------------------------ Functions ------------------------------
def plot_gauge(_gauge_val, unit, title1):
	fig = go.Figure(go.Indicator(
	    mode = "gauge+number",
	    value = _gauge_val,
	    domain = {'x': [0, 0.4], 'y': [0.7, 1]},
	    title = {'text': title1 + "(" + unit + ")"}))
	st.plotly_chart(fig)

# ---------------------------------------- WHILE LOOP ----------------------------------------
# ----------------------------------------............----------------------------------------
#while True:

# ------------------------------ Read-only content ------------------------------

# ---------------- Gauge section ----------------

#----------------- Display section ---------------
apps = [
{"func": collect.app, "title": "Collect", "icon": "house"},
{"func": depthsurvey.app, "title": "Depth survey", "icon": "map"},
]
titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

#----------------------------- Side bar ---------------------------
with st.sidebar:
    selected = option_menu(
        "Ground Station",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )
    genre = st.radio(
    'Which mode you want?',
    ('Auto Mode', 'Manual Mode'))
    mode = st.selectbox('Mode',('Waypoints','Zigzac path'))
    tar_lat = st.number_input('Waypoint latitude')
    tar_lng = st.number_input('Waypoint longitude')
    check_box = st.checkbox('Start')
	
display_section.empty()
with display_section.container():
	test1, test2, test3, test4 = st.columns(4)
	with test1:
		test1.empty()
		with test1.container():
			tab1, tab2 = st.tabs(["Pick Point", "Tracking Posision"])
			with tab2:
				df = pd.DataFrame(
					{
					"lat": [1, 2, 3, 4],
					"lon": [10, 20, 30, 40],
					}
					)
				st.map(df)
			with tab1:
				for app in apps:
				    if app["title"] == selected:
				        app["func"]()
				        break
	with test4:
		str = "00:00:00"
		operating_time = st.text_input("Operating Time ", str)
		current_point_target = st.text_input("Current Point Target ","hello")
		longitude = st.text_input("\tLongitude, Latitude ")
		distance = st.text_input("Distance ")
		number_point_target = st.text_input("\tNumber Point Target")
		toward_the_point_target = st.text_input("Toward the point target: ")
gauge_section.empty()
with gauge_section.container():
	usv_speed_col, batt_col, depth_col = st.columns(3)
	with usv_speed_col:
		plot_gauge(3, "m/s", "Speed")
	with batt_col:
		plot_gauge(70, "%", "Battery")
	with depth_col:
		plot_gauge(2.6, "m", "Depth")
# secs = 0
# str.empty()
# while(check_box):
# 	mm, ss = secs//60, secs%60
# 	str.metric("countdown", f"{mm:02d}:{ss:02d}")
# 	secs = secs+1
# 	time.sleep(1)
