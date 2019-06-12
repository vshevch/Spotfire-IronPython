# === Range Filter Navigation ===

from Spotfire.Dxp.Application import Filters as filters

myPanel = Document.ActivePageReference.FilterPanel
myFilter = myPanel.TableGroups[0].GetFilter("filterName")
rangeFilter = myFilter.FilterReference.As[filters.RangeFilter]()

#sets the low range to one step up and high range to one step down
rangeFilter.StepLowLimitUp()
rangeFilter.StepHighLimitDown()

#Sets the low range to one step down and high range to one step up
#rangeFilter.StepLowLimitDown()
#rangeFilter.StepHighLimitUp()
