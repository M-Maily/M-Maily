import contextily as cx
import geopandas as gpd
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

# read Natural_Neighbourhoods
file_name_zones = "data/Natural_Neighbourhoods.geojson"
gdfd = gpd.read_file(file_name_zones)
gdf=gdfd.to_crs({'init': 'epsg:27700'})
gdf = gdf.set_geometry("geometry")
# read Local_Biodiversity_Sites
file_name_bio = "data/Local_Biodiversity_Sites.geojson"
gsdfd = gpd.read_file(file_name_bio)
gsdf=gsdfd.to_crs({'init': 'epsg:27700'})
gsdf =  gsdf.set_geometry("geometry")

# Plot neighbourhoods
ax=gdf.plot(alpha=0.3, edgecolor='k', facecolor='silver',zorder=2 )
# Green areas
gsdf.plot(ax=ax, alpha=0.9, color='mediumseagreen', label='Biodiversity Sites', zorder=1 )

# add background
cx.add_basemap(ax, source=cx.providers.Stamen.TonerLite, crs=gdf.crs)

# Set axis and Labels
ax.locator_params(nbins=3)
ax.set_title('Biodiversity Sites in Edinburgh')
ax.set_xlabel('Easting')
ax.set_ylabel('Northing')
# Legend
green_patch = mpatches.Patch(color='mediumseagreen', alpha=0.9, label='Biodiversity Sites')
gray_patch = mpatches.Patch(facecolor='silver', edgecolor='black', alpha = 0.3, label = 'Neighbourhoods')
leg = plt.legend(handles=[green_patch, gray_patch], loc='lower right')
#plt.savefig('ED_green.png')
plt.show()
