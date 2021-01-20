#%% markdown

### This script will generate a population and volcano web map

#%%
import folium
import pandas as pd


# %%
data=pd.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
name=list(data["NAME"])
elevation=list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'blue'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red'

map=folium.Map(location=[38.58,-99.09],zoom_start=6)

fgv=folium.FeatureGroup(name="Vocanoes")

for lt,ln,name,el in zip(lat, lon, name,elevation):
    fgv.add_child(folium.Marker(location=[lt,ln], popup=name,icon=folium.Icon(color_producer(el))))
    #fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=name,fill_color=color_producer(el), color='grey', fill_capacity=0.7))

fgp=folium.FeatureGroup(name="Population")
#fg.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read())))
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005']<10000000 else 'orange' if 10000000 <= x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map.html")

# %%
