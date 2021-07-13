import geopandas as gpd
import os

gpx_path = "/home/bright/Routing/gpx_files_wien/"
project_path = "/home/bright/Routing/"

gdf = gpd.GeoDataFrame()

for dirpath, subdirs, files in os.walk(gpx_path):
    for f in files:
        gdf = gdf.append(gpd.read_file(os.path.join(dirpath, f), driver="GPX", layer="tracks"))
gdf.to_file(project_path + "wien.gpkg", driver="GPKG")
