from Spotfire.Dxp.Application.Visuals import *

v = viz.As[VisualContent]()
for l in v.Layers:
  if l.Title == “Swedish”:
    if l.Enabled == True:
      l.Enabled = False
    else:
      l.Enabled = True
      
#Original Link: https://datashoptalk.com/ironpython-in-spotfire-creating-a-button-to-toggle-a-map-layer-on-and-off/
