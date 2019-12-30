from Spotfire.Dxp.Data import IndexSet,RowSelection
from Spotfire.Dxp.Data import DataValueCursor
tableName = "BCO_Information_Link"

SourceValue = 'market'
TargetValue = 'region'

SourceProper = SourceValue[0:1].upper() + SourceValue[1:].lower()
SourceColumn = SourceValue.upper()

TargetProper = TargetValue[0:1].upper() + TargetValue[1:].lower()
TargetColumn = TargetValue.upper()

#Building the IndexSet to find the parent division of the market
if Document.Properties[SourceProper] != None:	
	Sm = "[" + SourceColumn + "] = '" + Document.Properties[SourceProper] + "'"

#Initializing variables 
rowcount = 0 
dT = Document.Data.Tables[tableName]
cursorD = DataValueCursor.CreateFormatted(dT.Columns[TargetColumn]);	
mrows = dT.Select(Sm)

#Find the division from the first row
for row in Document.ActiveDataTableReference.GetRows(mrows.AsIndexSet(), cursorD):	
	if cursorD.CurrentValue != '(Empty)':
		Document.Properties[TargetProper] = cursorD.CurrentValue
		break
