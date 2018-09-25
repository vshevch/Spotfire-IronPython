# You need to add a script parameter to make this work.
# In 'Edit Script' window, go to 'Script parameters' section, click 'Add...', and select the Visualisation and Document Property (optional, used for dropdown menu) you want to use
 
from Spotfire.Dxp.Application.Visuals import *

viz = MapViz.As[VisualContent]()

for I in viz.Layers:
	if I.Title == LayerName: #LayerName is a DocumentProperty, but this script works with static variable as well
		viz.InteractiveLayerReference = I
