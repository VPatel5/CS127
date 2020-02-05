# Name: Vraj Patel
# Email: vraj.patel24@myhunter.cuny.edu
# Date: October 25, 2019
# This program 

import folium

mapWorld = folium.Map(location=[40.75, -74.125])

folium.Marker(location=[40.768731, -73.964915], popup="Hunter College").add_to(mapWorld)

mapWorld.save(outfile='nycMap.html')
