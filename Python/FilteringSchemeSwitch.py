#Might need to import these modules
import Spotfire.Dxp.Application.Filters as filters
from Spotfire.Dxp.Data import DataPropertyClass

# Select a panel to filter on
myPanel = Document.ActivePageReference.FilterPanel

# Switch the filtering scheme
for fs in Document.FilteringSchemes:
    if fs.FilteringSelectionReference.Name == "Filtering scheme": 
        myPanel.FilteringSchemeReference = fs
        
# This normally used with a filter see other python codes in this folder
