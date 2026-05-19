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