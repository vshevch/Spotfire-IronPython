# You need to add a script parameter to make this work.
# In 'Edit Script' window, go to 'Script parameters' section, click 'Add...', and select the visualisation you want to control

from Spotfire.Dxp.Application.Visuals import *

v = viz.As[VisualContent]()
for l in v.Layers:
  if l.Title == “Swedish”:
    if l.Enabled == True:
      l.Enabled = False
    else:
      l.Enabled = True
      
#Original Link: https://datashoptalk.com/ironpython-in-spotfire-creating-a-button-to-toggle-a-map-layer-on-and-off/
