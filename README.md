# Master\_Thesis

Spatial Analyses of the CrowdWater Data Collected by Citizen Scientists



This MSc thesis, dedicated to the spatial analysis of CrowdWater data consists of three parts. In the first part, spatial and temporal analyses are conducted to detect patterns and distributions in the data. Also, spots where long-term time series are produced, are identified and analyzed. In the second part, the motivations of individuals to contribute to the project are investigated. In the third part, the spread of the app is analyzed and factors influencing the spread are identified.



Structure:

Master\_Thesis/

├── Code/

│ ├── functions.py

│ ├── Download\_clean\_data.ipynb

│ ├── Part1\_Spatial.ipynb

│ ├── Part1\_Temporal.ipynb

│ ├── Part1\_Persistent\_Spots.ipynb

│ ├── Part1\_Switzerland.ipynb

│ ├── Part1\_Categories.ipynb

│ ├── Part1\_User\_Groups.ipynb

│ ├── Part2.ipynb

│ ├── Part2\_Survey.ipynb

│ ├── Part3.ipynb

│ ├── Part3\_Regression.ipynb

│ ├── Part3\_Switzerland.ipynb

│ ├── Part3\_Regression\_Switzerland.ipynb

├── Products/

│ ├── Part1/

│ │ ├── figures used in Part 1 of the thesis

│ ├── Part2/

│ │ ├── figures used in Part 2 of the thesis

│ ├── Part3/

│ │ ├── figures used in Part 3 of the thesis

│ ├── Hydro\_Categories/

│ │ ├── figures of CrowdWater categories

│ ├── CSVs/

│ │ ├── additional CSVs produced during the thesis

│ ├── Overview.html

├── Additional\_Data/

│ ├── Education\_index.csv

│ ├── Education\_index.xlsx

│ ├── Switzerland\_GDP\_Pop.csv

│ ├── Switzerland\_GDP\_Pop.xlsx

│ ├── HDR25\_Statistical\_Annex\_HDI\_Table.xlsx

├── CW\_Outreaches/

│ ├── CW\_outreach\_2020.xlsx

│ ├── CW\_outreach\_2021.xlsx

│ ├── CW\_outreach\_2022.xlsx

│ ├── CW\_outreach\_2023.xlsx

│ ├── CW\_outreach\_2024.xlsx

│ ├── CW\_outreach\_2025.xlsx

│ ├── CW\_outreach\_2026.xlsx

│ ├── CW\_outreach\_merged.xlsx

├── Interviews\_Survey/

│ ├── Survey\_Analysis.xlsx

│ ├── Survey\_Results.xlsx

│ ├── Interview\_Analysis.xlsx

│ ├── Interview\_FCS.mp3

│ ├── Interview\_SBR\_Part1.mp3

│ ├── Interview\_SBR\_Part2.mp3

├── Borders/

│ ├── ne\_10m\_admin\_0\_countries/ <-- shapefile

│ ├── ne\_10m\_admin\_1\_states\_provinces/ <-- shapefile

│ ├── ne\_10m\_populated\_places/ <-- shapefile

│ ├── ne\_110m\_admin\_0\_countries/ <-- shapefile

│ ├── swissboundaries3d\_2026-01\_2056\_5728/ <-- shapefile

├── CWData\_clean7.csv

├── CWData\_Switzerland.csv

├── CWData\_superusers.csv

├── CWData\_betweeners.csv

├── CWData\_onetimers.csv

├── .gitignore <-- raw download data and some data visualizations I made using Excel are not included

├── README.md



Setup

pip install requests pandas matplotlib folium reverse-geocoder pycountry numpy geopandas fiona shapely scikit-learn ruptures haversine timezonefinder scipy cartopy libpysal esda statsmodels pymann-kendall pyproj pycountry-convert seaborn imageio geopy wbgapi openpyxl



Data

The CrowdWater data is downloaded from Spotteron (using the Spotteron API) automatically by running the file "Master\_Thesis/Code/Download\_clean\_data.ipynb".



Execution

Run all cells (outputs are automatically saved to the correct subfolder in "Master\_Thesis/Products/")

