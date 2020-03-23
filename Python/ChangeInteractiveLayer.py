# You need to add a script parameter to make this work.
# In 'Edit Script' window, go to 'Script parameters' section, click 'Add...', and select the Visualisation and Document Property (optional, used for dropdown menu) you want to use

from Spotfire.Dxp.Data import * 		#Required for clearMarkings function
from Spotfire.Dxp.Application.Visuals import *  #Required for viz.Layer toggling

# function to clear data Markings
def clearMarkings(desLayer):
	for dataTable in Document.Data.Tables:
		if dataTable.Name == desLayer:
			for marking in Document.Data.Markings:
				rows = RowSelection(IndexSet(dataTable.RowCount, False))
				marking.SetSelection(rows, dataTable)

# determines which layer to clear				
if LayerName == 'FSCs':
	desiredLayer = 'StatsCan_FSA'
elif LayerName == 'StatsCan_FSA':
	desiredLayer = 'FSCs'

# layer toggeling
viz = MapViz.As[VisualContent]() # externally defined Spotfire Script Parameter

for I in viz.Layers:
	if I.Title == LayerName:
		viz.InteractiveLayerReference = I
	clearMarkings(desiredLayer)
