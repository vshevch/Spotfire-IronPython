# Uncheck All Values
from Spotfire.Dxp.Application.Visuals import VisualContent
from Spotfire.Dxp.Application import Filters as filters
from Spotfire.Dxp.Application.Filters import FilterTypeIdentifiers

# Get the filter panel on the current active page
filterPanel = Document.ActivePageReference.FilterPanel
# Perform filtering action
for tableGroup in filterPanel.TableGroups:
 for fh in tableGroup.FilterHandles:
  if fh.Visible:
   if (fh.FilterReference.TypeId == FilterTypeIdentifiers.CheckBoxFilter):
    cbFilter = fh.FilterReference.As[filters.CheckBoxFilter]()
    for checkedValues in cbFilter.Values:
     cbFilter.Uncheck(checkedValues)
     
# Check Box Filter

import Spotfire.Dxp.Application.Filters as filters
#import Spotfire.Dxp.Application.Filters.ListBoxFilter
#from Spotfire.Dxp.Application.Filters import FilterTypeIdentifiers
from Spotfire.Dxp.Data import DataPropertyClass
#from System import String

myPanel = Document.ActivePageReference.FilterPanel
# Here you can insert Select Filtering Scheme python code [see the code in the folder]
myFilter= myPanel.TableGroups[0].GetFilter("Fiscal YTD Flag")
lbFilter = myFilter.FilterReference.As[filters.CheckBoxFilter]()

# Available Options
lbFilter.Reset() # Resets the filter (includes all)
lbFilter.Check("Y")
lbFilter.Uncheck("Y")
lbFilter.IncludeEmpty=False
