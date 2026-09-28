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
import pycountry_convert as pc


# function to get the ISO3 code of a country

ISO3_OVERRIDES = {
    "Russia": "RUS",
}

def get_iso3(country_name):
    if country_name in ISO3_OVERRIDES:
        return ISO3_OVERRIDES[country_name]
    try:
        return pycountry.countries.lookup(country_name).alpha_3
    except LookupError:
        return None
    

# function that creates gifs

def gif_maker(*files, path, duration=1000):
    images = []
    for file in files:
        images.append(imageio.imread(file))
    imageio.mimsave(f"{path}.gif", images, duration = duration)


# function that keeps fontsize in figures constant

def setup_figure_style(base_fontsize=14):
    plt.rcParams.update({
        'font.size': base_fontsize,
        'axes.labelsize': base_fontsize + 4,
        'axes.titlesize': base_fontsize + 7,
        'xtick.labelsize': base_fontsize,
        'ytick.labelsize': base_fontsize,
        'legend.fontsize': base_fontsize,
        'legend.title_fontsize': base_fontsize + 4,
        'figure.titlesize': base_fontsize + 7
    })


# function that retrieves the continent based on the country name

def country_to_continent(country_name):
    try:
        country_alpha2 = pc.country_name_to_country_alpha2(country_name)
        continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        continent_map = {
            "AF": "Africa", "AS": "Asia", "EU": "Europe",
            "NA": "North America", "SA": "South America",
            "OC": "Oceania", "AN": "Antarctica"
        }
        return continent_map.get(continent_code, "Unknown")
    except:
        return "Unknown"
    

# function that calculates Cramér's V

def cramers_v(chi2, table):
    n = table.sum().sum()
    r, k = table.shape
    return np.sqrt(chi2 / (n * (min(r, k) - 1)))