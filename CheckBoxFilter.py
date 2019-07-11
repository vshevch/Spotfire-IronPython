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
     
