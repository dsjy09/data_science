#%% markdown

### This script will generate a population and volcano web map

#%%
import folium
import pandas as pd

html = """<h4>Volcano information:</h4>
Height: %s m
"""
# %%
data=pd.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
name=list(data["NAME"])
elevation=list(data["ELEV"])

# %%

map=folium.Map(location=[38.58,-99.09],zoom_start=6)

fg=folium.FeatureGroup(name="My Map")

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    else:
        return 'blue'

for lt,ln,name,el in zip(lat, lon, name,elevation):
    iframe = folium.IFrame(html=html % name, width=200, height=100)
    fg.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(iframe),icon=folium.Icon(color_producer(el))))

map.add_child(fg)

map.save("map.html")

# %%
