import requests
import pandas as pd
from datetime import datetime
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
from matplotlib.colors import BoundaryNorm
from matplotlib.cm import get_cmap
from matplotlib.patches import Patch
import ast
import folium
from folium.plugins import MarkerCluster
import reverse_geocoder as rg
import re
import pycountry
import os
import numpy as np
import geopandas as gpd
import fiona
import sys
from shapely.geometry import Point
from sklearn.cluster import DBSCAN
import ruptures as rpt
from haversine import haversine
import imageio
from statsmodels.tsa.seasonal import STL


# function to get the ISO3 code of a country

def get_iso3(country_name):
    try:
        return pycountry.countries.lookup(country_name).alpha_3
    except:
        return None
    

# function that creates gifs

def gif_maker(*files, path, duration=1000):
    images = []
    for file in files:
        images.append(imageio.imread(file))
    imageio.mimsave(f"{path}.gif", images, duration = duration)


# function that does STL decomposition on monthly user counts

def STL_decomposition (df, variable, figtitle):
    ts = df.set_index("year_month_dt")[variable].asfreq("MS")
    stl = STL(ts, period=12)
    result = stl.fit()

    # plot
    fig, axes = plt.subplots(4, 1, figsize=(16, 10), sharex=True)

    components = [
        (ts,             "Raw Numbers",  "Users"),
        (result.trend,   "Trend",     "Users"),
        (result.seasonal,"Seasonal",  "Deviation"),
        (result.resid,   "Residual",  "Deviation"),
    ]

    for ax, (data, title, yl) in zip(axes, components):
        ax.plot(data, linewidth=1.2)
        ax.set_title(title, fontsize=20, fontweight="bold", loc="left", pad=4)
        ax.set_ylabel(yl, fontsize=17)
        ax.grid(axis="x", alpha=0.3)
        ax.grid(axis="y", alpha=0.3)
        ax.set_axisbelow(True)
        ax.spines[["top","right"]].set_visible(False)

    # xticks: mark every January
    years = pd.date_range(ts.index.min(), ts.index.max(), freq="YS")
    axes[-1].set_xticks(years)
    axes[-1].set_xticklabels([d.year for d in years], rotation=45, ha="right", fontsize=12)
    axes[-1].set_xlabel("Year", fontsize=17)

    # Residuals: zero-line
    axes[-1].axhline(0, color="gray", linewidth=0.8, linestyle="--")
    axes[2].axhline(0, color="gray", linewidth=0.8, linestyle="--")

    fig.suptitle(f"STL Decomposition - {figtitle}", fontsize=20, fontweight="bold", y=1.01)

    plt.tight_layout()
    plt.savefig(f"../Products/STL_{variable}.png", dpi=300, bbox_inches="tight")
    plt.close()

    seasonal_strength = 1 - (np.var(result.resid) / np.var(result.seasonal + result.resid))
    trend_strength    = 1 - (np.var(result.resid) / np.var(result.trend    + result.resid))

    print(f"Seasonal strength {figtitle}: {seasonal_strength:.3f}")
    print(f"Trend strength {figtitle}:    {trend_strength:.3f}")