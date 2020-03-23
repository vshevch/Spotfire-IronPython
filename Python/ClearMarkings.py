# Source Data: https://naveengoje.com/2014/12/23/spotfire-ironpython-reset-markings/

from Spotfire.Dxp.Data import *

for dataTable in Document.Data.Tables:
	if dataTable.Name == 'StatsCan_FSA': # Name of the Tab
		for marking in Document.Data.Markings:
			rows = RowSelection(IndexSet(dataTable.RowCount, False))
			marking.SetSelection(rows, dataTable)
