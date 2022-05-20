import pandas
import folium

istanbul_coordinates = (41.01384000000007, 28.94966000000005)

data = pandas.read_csv("data.csv", sep=";", encoding="utf-8")

county_names = data["COUNTY_NAME"]
addresses_list = tuple(data["ADDRESS"] + ", " + data["COUNTY_NAME"])
latitudes = tuple(float(coordinate) for coordinate in data["LATITUDE"])
longitudes = tuple(float(coordinate) for coordinate in data["LONGITUDE"])
coordinates_list = zip(latitudes, longitudes)

html = '<a href="https://www.google.com/maps/search/?api=1&query=%s,%s" target="_blank"><center>%s</center></a>'

map = folium.Map(location=istanbul_coordinates, zoom_start=12, tiles="Stamen Terrain")

feature_groups = {key: folium.FeatureGroup(name=key, show=False) for key in county_names.unique()}

for county_name, address, coordinates in zip(data["COUNTY_NAME"], addresses_list, coordinates_list):
    iframe = folium.IFrame(html % (coordinates[0], coordinates[1], address), width=500, height=60)
    feature_groups[county_name].add_child(folium.CircleMarker(location=coordinates, radius=10, popup=folium.Popup(iframe), fill_color='red', color='grey', fill_opacity=0.7))

for fg in feature_groups:
    map.add_child(feature_groups[fg])

map.add_child(folium.LayerControl())

map.save("index.html")