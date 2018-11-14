# Original Document: https://spotfired.blogspot.com/2014/03/change-filters-programatically-from.html

import Spotfire.Dxp.Application.Filters as filters

myPanel = Document.ActivePageReference.FilterPanel
# Select Data Table to Use
BDG_Filter = myPanel.TableGroups[0]
# Select which Filter from Data Table to Use
myFilter = BDG_Filter.GetFilter("Month, Year of Create Month")
# Declare filter's type (ex. ItemFilter, ListBoxFilter, etc.)
lbFilter = myFilter.FilterReference.As[filters.ItemFilter]()

# Extract Date Value from DropDown Menu
date_value = Document.Properties["Filter2"]

# Pass DropDown Selection to the Filter
lbFilter.Value = date_value
