import time
from System import DateTime
from datetime import date,datetime,timedelta
from Spotfire.Dxp.Data import IndexSet,RowSelection
from Spotfire.Dxp.Data import DataValueCursor
from Spotfire.Dxp.Application.Visuals import HtmlTextArea

# To find the closest day (Friday) for Upper limit of filter 

start_date = datetime.today() 
day_num = start_date.weekday()

# Fiscal Start
if (datetime.today().month == 11 or datetime.today().month == 12):
	Document.Properties["Fiscalstart"] = date(datetime.today().year,10,31).strftime('%Y-%m-%d')
else:
	Document.Properties["Fiscalstart"] = date((datetime.today().year-1),10,31).strftime('%Y-%m-%d')

# hardwiring the Day for Thursday
day_num_target = 4 

days_ago = (7 + day_num - day_num_target) % 7

if days_ago == 0:
	days_ago = 7
to_date = start_date - timedelta(days=days_ago)

# Initialize variables / Properties
Document.Properties["newusage"] = ""
Document.Properties["existingusage"] = ""

sum_new = 0.00 
sum_existing = 0.00
sum_new_used = 0.00 
sum_ex_used = 0.00
new_usage = 0.00
ex_usage = 0.00


dT = Document.Data.Tables["NEEDS_NAVIGATOR"]
dcolumn = dT.Columns["TO_DATE"]

cursorn = DataValueCursor.CreateFormatted(dT.Columns["NEW_CUSTOMER"]);
cursore = DataValueCursor.CreateFormatted(dT.Columns["EXISTING_CUSTOMER"]);

cursornu = DataValueCursor.CreateFormatted(dT.Columns["NN_USED_NEW_CUSTOMER"]);
cursoreu = DataValueCursor.CreateFormatted(dT.Columns ["NN_USED_EXISTING_CUSTOMER"]);

#Find max date (mx) and display date (mxd)
mxd = dcolumn.RowValues.GetMaxValue().ValidValue 

# If the latest Data is not loaded then flip back to the max available date
if date(mxd.Year,mxd.Month,mxd.Day) < datetime.date(to_date) :
	mx = date(mxd.Year,mxd.Month,mxd.Day)
else:
	mx = to_date.date()

wf = mx+ timedelta(days=-7)
mf = mx+ timedelta(days=-28)

Document.Properties["dlw"] = wf.ToString()
Document.Properties["dfw"] = mf.ToString()
Document.Properties["dateupper"] = to_date.ToString()[0:10]

# Building the IndexSet for the conditions ... to count and calculate 
Sm = " [DIVNAME] is not null AND [TO_DATE] > date('" + Document.Properties["dlw"] + "') and [TO_DATE] < date('" + Document.Properties["dateupper"] + "')  and ([ROLE] = 'BRM' or [ROLE] = 'ABM' or [ROLE] = 'FSM' or [ROLE] = 'PBA' or [ROLE] = 'PILO' or [ROLE]='SRB')"
mnrows = dT.Select(Sm)

for row in Document.ActiveDataTableReference.GetRows(mnrows.AsIndexSet(), cursorn,cursore,cursornu,cursoreu):
		
	if cursorn.IsCurrentValueValid :
		sum_new += float(cursorn.CurrentValue)	
	if cursore.IsCurrentValueValid :
		sum_existing += float(cursore.CurrentValue)
	if cursornu.IsCurrentValueValid :
		sum_new_used += float(cursornu.CurrentValue)	
	if cursoreu.IsCurrentValueValid :
		sum_ex_used += float(cursoreu.CurrentValue)

# Just in Case to Avoid division by Zero

if sum_new > 0 :
	new_usage  = ( sum_new_used / sum_new) * 100

if sum_existing > 0 :
	ex_usage = (float(sum_ex_used) / sum_existing) * 100

	Document.Properties["div"] = None
	Document.Properties["launchmarket"] = None
	Document.Properties["launchtransit"] = None

Document.Properties["newusage"] = new_usage.ToString()[0:5]
Document.Properties["existingusage"] = ex_usage.ToString()[0:5]

#Document.Properties["newusage"] = new_usage.ToString()[0:5] + ' %'
#Document.Properties["existingusage"] = ex_usage.ToString()[0:5] + ' %'

Document.Properties["mxdate"] = date(mxd.Year,mxd.Month,mxd.Day).strftime('%Y-%B-%d')	

Document.ActivePageReference = Document.Pages[1]

for vis in Document.ActivePageReference.Visuals:
	if vis.Title == 'burgermenu':
		xcode = vis.As[HtmlTextArea]().HtmlContent
		if xcode.find('id=bm style="VISIBILITY: hidden"') == -1:
			ccode = xcode.replace('id=btns style="FLOAT: right; PADDING-TOP: 5px; VISIBILITY: visible"','id=btns style="FLOAT: right; PADDING-TOP: 5px; VISIBILITY: hidden"')
			vis.As[HtmlTextArea]().HtmlContent = ccode.replace('id=bm style="VISIBILITY: collapse"','id=bm style="VISIBILITY: visible"')
		else:
			ccode = xcode.replace('id=btns style="FLOAT: right; PADDING-TOP: 5px; VISIBILITY: visible"','id=btns style="FLOAT: right; PADDING-TOP: 5px; VISIBILITY: hidden"')
			vis.As[HtmlTextArea]().HtmlContent = ccode.replace('id=bm style="VISIBILITY: hidden"','id=bm style="VISIBILITY: visible"')
