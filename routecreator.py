import pandas as pd
import urllib.request
import sys

def log(*args): print(*args, file=sys.stderr, flush=True)

# path to clipped regularpoints with colums id, lon, lat
coordinates = pd.read_csv("points.csv")

# query setup
pre = "http://localhost:8989/route/?"
point = "&point="
spacer = "%2C"
end = "&type=gpx&locale=de&profile=car&instructions=false"

# definition of central point
CENTER_LAT = "48.214275"
CENTER_LON = "16.357838"
center = "point=" + CENTER_LAT + spacer + CENTER_LON

# query and save as gpx in subfolder
for index, row in coordinates.head().iterrows():
    # print(row["x"], row["y"])
    req = pre + center + point + str(row["y"]) + spacer + str(row["x"]) + end
    try:
        resp = urllib.request.urlopen(req)
        gpxData = str(resp.read(), "utf-8")
        fileName = "route_" + str(index).zfill(4)
        saveFile = open("gpx_files" + "/{0}.gpx".format(fileName), "w")
        log("processed nr ", str(index))
        saveFile.write(gpxData)
        saveFile.close()
    except:
        print("bad request on index " + str(index))
        pass
