# Original Document: https://spotfired.blogspot.com/2014/03/change-filters-programatically-from.html

import Spotfire.Dxp.Application.Filters as filters

myPanel = Document.ActivePageReference.FilterPanel
# Select Data Table to Use # use print(myPanel.TableGroups[0].Context) to check name
BDG_Filter = myPanel.TableGroups[0] 
# Select which Filter from Data Table to Use
myFilter = BDG_Filter.GetFilter("Month, Year of Create Month")
# Declare filter's type (ex. ItemFilter, ListBoxFilter, etc.)
lbFilter = myFilter.FilterReference.As[filters.ItemFilter]()

# Extract Date Value from DropDown Menu (The "Name" of "Select property" from Property Control)
date_value = Document.Properties["DateFilter"]

# Pass DropDown Selection to the Filter
lbFilter.Value = date_value


# Filter #2

import Spotfire.Dxp.Application.Filters as filters
#import Spotfire.Dxp.Application.Filters.ListBoxFilter
#from Spotfire.Dxp.Application.Filters import FilterTypeIdentifiers
from Spotfire.Dxp.Data import DataPropertyClass
#from System import String

myPanel = Document.ActivePageReference.FilterPanel
myFilter= myPanel.TableGroups[0].GetFilter("Rep Name")
lbFilter = myFilter.FilterReference.As[filters.ListBoxFilter]()
lbFilter.IncludeAllValues=False
strVals = Document.Properties["RepNameBDG"]

if strVals == None:
	lbFilter.Reset()
else:
	lbFilter.SetSelection(strVals)

#if strVals!=String.Empty:
#  lbFilter.SetSelection(strVals)
#else:
#  lbFilter.Reset()
