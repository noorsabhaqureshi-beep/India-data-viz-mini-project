import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("india.csv")

list_of_states = list(df['State'].unique())
list_of_states.insert(0,"Overall India")

st.sidebar.title("India's Data Visualization" )

selected_state=st.sidebar.selectbox("select a state",list_of_states)

primary = st.sidebar.selectbox("select a primary parameter",sorted(df.columns[5:]))

secondary = st.sidebar.selectbox("select a secondary parameter",sorted(df.columns[5:]))

plot = st.sidebar.button("Plot Graph")

if plot:

    st.text("size represents primary parameter")
    st.text("color represents secondary parameter")

    if selected_state == "Overall India":
        fig = px.scatter_mapbox(df,lat="Latitude",lon="Longitude",size = primary,
                                color = secondary, zoom = 4, size_max=35,
                                mapbox_style="carto-positron", hover_name="District",
                                width=1200, height=800)
        st.plotly_chart(fig, use_container_width=True)

    else:

        state_df = df[df["State"]== selected_state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary,
                                color=secondary, zoom=5, size_max=35,
                                mapbox_style="carto-positron", hover_name="District",
                                width=1200, height=800)
        st.plotly_chart(fig, use_container_width=True)
