from Spotfire.Dxp.Application.Visuals import *
import Spotfire.Dxp.Application.Visuals.Maps.MarkerLayerVisualization
from Spotfire.Dxp.Application.Visuals.Maps import *
from System.Drawing import Color

def ChangColorScheme(ApplyColorScheme):
	markerLayer.ColorAxis.Coloring.Clear()
	markerLayer.ColorAxis.Coloring.Apply(ApplyColorScheme)

for page in Document.Pages:  #Loop through every page
    if page.Title == 'MAPS':  #End the iteration if page titled 'Exclude'
        for visual in page.Visuals:  #On this page, loop through every visual
            if visual.Title == 'NN_MapChart':  #End the iteration if visual titled 'Nope'
					mapChart = visual.As[MapChart]()
					for layer in mapChart.Layers:
												
						# You need to skip the first layer
						markerLayer = None
						try:
							markerLayer = layer.As[Spotfire.Dxp.Application.Visuals.Maps.MarkerLayerVisualization]()
						except:
							pass
						
						if markerLayer != None: 
							if markerLayer.Title == "kzhou_vlad_usage": #Name of the Layer
								
								SelectProp = Document.Properties["NewCustomers"] #Pull the property
								
								if SelectProp == "Y":
									ChangColorScheme("NewCustomer")	
								elif SelectProp == "N":
									ChangColorScheme("ExistingCustomer")
