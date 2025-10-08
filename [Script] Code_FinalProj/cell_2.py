import os, requests, datetime as dt
import pandas as pd, numpy as np
import plotly.graph_objects as go
import gradio as gr

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
EQ_CSV = os.path.join(DATA_DIR, "earthquakes.csv")
EONET_CSV = os.path.join(DATA_DIR, "eonet_events.csv")

REGIONS = {
    "Global": None,
    "Japan": [30, 46, 129, 146],
    "SEA (Southeast Asia)": [-11, 21, 92, 122],
    "US West": [30, 50, -125, -110]
}