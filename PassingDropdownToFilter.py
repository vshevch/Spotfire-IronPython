# Document Used for Research: https://spotfired.blogspot.com/2014/03/change-filters-programatically-from.html

# Filter #1 - Item Filter -

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


# Filter #2 - List Box Filter -

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

# Filter #3 - Check Box Filter -

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
