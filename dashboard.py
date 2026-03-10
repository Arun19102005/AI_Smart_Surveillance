import streamlit as st
import pandas as pd
import os
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="AI Smart Surveillance",
    page_icon="🚨",
    layout="wide"
)

st_autorefresh(interval=5000)

st.title("🚨 AI Smart Surveillance Control Center")

file_path = "alerts.csv"

if not os.path.exists(file_path):
    st.warning("No alerts detected yet.")
    st.stop()

data = pd.read_csv(file_path)

data["Time"] = pd.to_datetime(data["Time"], errors="coerce")

# STATUS
if len(data) > 0:
    st.error("⚠ THREAT DETECTED")
else:
    st.success("SYSTEM SAFE")

st.divider()

# METRICS
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Alerts", len(data))

if len(data) > 0:
    latest_time = data["Time"].max()
    col2.metric("Latest Alert", latest_time.strftime("%H:%M:%S"))
else:
    col2.metric("Latest Alert", "None")

col3.metric(
    "Unique Locations",
    data[["Latitude", "Longitude"]].drop_duplicates().shape[0]
)

today = pd.Timestamp.today().date()

alerts_today = data[data["Time"].dt.date == today].shape[0]

col4.metric("Alerts Today", alerts_today)

st.divider()

# TIMELINE
st.subheader("📈 Alert Timeline")

chart_data = data.dropna(subset=["Time"])

if len(chart_data) > 0:

    chart_data["Hour"] = chart_data["Time"].dt.hour

    fig = px.histogram(
        chart_data,
        x="Hour",
        nbins=24,
        title="Alerts by Hour"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("No valid alert times to display timeline.")

st.divider()

# MAP
st.subheader("📍 Alert Locations")

map_data = data.rename(columns={
    "Latitude": "lat",
    "Longitude": "lon"
})

st.map(map_data)

st.divider()

# IMAGE
st.subheader("📸 Latest Detection Image")

if len(data) > 0:

    latest = data.sort_values("Time", ascending=False).iloc[0]

    image_path = latest["Image"]

    if os.path.exists(image_path):
        st.image(image_path, width=400)

st.divider()

# TABLE
st.subheader("📋 Alert Records")

st.dataframe(
    data.sort_values("Time", ascending=False),
    use_container_width=True
)