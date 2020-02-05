# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: November 01, 2019
# This program

import folium
import pandas as pd

# collisionsThHunterBday.csv
# thMap.html

fileName = input("Enter CSV file name: ")

outputFile = input("Enter output file name: ")

mapCUNY = folium.Map(location=[40.768731, -73.964915])

df = pd.read_csv(fileName)

for index,row in df.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["TIME"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapCUNY)

mapCUNY.save(outfile=outputFile)
