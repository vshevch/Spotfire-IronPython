from Spotfire.Dxp.Application.Visuals import *

for page in Document.Pages:  #Loop through every page
    if page.Title <> 'Exclude':  #End the iteration if page titled 'Exclude'
        for visual in page.Visuals:  #On this page, loop through every visual
            if visual.Title == 'DualAxisGraph':  #End the iteration if visual titled 'Nope'

					lChart = visual.As[CombinationChart]()

					def ChartValues(low, high):
						lChart.YAxis.IndexedRange["FSM Volume"] = AxisRange(low, high)
						lChart.YAxis.IndexedRange["FP Volume"] = AxisRange(low, high)
						
					if Document.Properties["DivisionDropDown"] == "- ALL -":
						ChartValues(0, 10000)

					elif Document.Properties["MarketDropDown"] == None and Document.Properties["MarketDropDown"] != "- ALL -":
						ChartValues(0, 2000)
						
					elif Document.Properties["TransitDropDown"] == None and Document.Properties["MarketDropDown"] != None:
						ChartValues(0, 250)
						
					elif Document.Properties["TransitDropDown"] != None:
						ChartValues(0, 90)
