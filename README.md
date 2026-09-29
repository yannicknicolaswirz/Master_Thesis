# Master\_Thesis

Spatial Analyses of the CrowdWater Data Collected by Citizen Scientists



This MSc thesis, dedicated to the spatial analysis of CrowdWater data consists of three parts. In the first part, spatial and temporal analyses are conducted to detect patterns and distributions in the data. Also, spots where long-term time series are produced, are identified and analyzed. In the second part, the motivations of individuals to contribute to the project are investigated. In the third part, the spread of the app is analyzed and factors influencing the spread are identified.



Structure:

SDS210\_Project\_Yannick\_Wirz/



├── notebooks/



│ ├── Project.ipynb



├── outputs/ <-- output images



├── .gitignore <-- Landsat composites are not included



├── README.md



Setup

pip install pandas numpy matplotlib scipy xarray rasterio rioxarray glob



Data

The Landsat composites are not included in the repository, they were provided in the UZH course but can also be downloaded through Google Earth Engine.



Execution

Save Landsat composites in "data/raw/" (file name: "LandsatComposite\_Zurich\_{year}.tif")

Start Jupyter Notebook (bash: jupyter notebook notebooks/analysis.ipynb)

Run all cells (outputs are automatically saved to "outputs/")

