from System import DateTime
from datetime import datetime
from datetime import timedelta
from System.Globalization import CultureInfo

# Initialization of all Scripting components

import Spotfire.Dxp.Application.Filters.ListBoxFilter
import Spotfire.Dxp.Application.Filters as filters
from Spotfire.Dxp.Application.Filters import FilterTypeIdentifiers
from Spotfire.Dxp.Application.Filters import ItemFiltering
from Spotfire.Dxp.Application.Filters import RangeFilter,ValueRange


from System.Threading import Thread
from Spotfire.Dxp.Data import *

##### Script parameters: 
# page: Define which page to forward to.  Right now we want to point to the next page (Report)


#Function: setdate
#####  Description: Sets the Date filter to Current Month logic 

def setdate() :
	today = DateTime.Today
	
	dl = datetime(today.AddMonths(-2).Year,today.AddMonths(-2).Month,1)
	dh = datetime(today.AddMonths(-1).Year,today.AddMonths(-1).Month,1)

# Stripping out the time segment and setting the document properties for Display
	
	#Document.Properties["dl"] = (DateTime.ParseExact(dl.strftime('%d/%m/%Y'),'dd/MM/yyyy',CultureInfo.InvariantCulture)).ToString().Substring(0,10)
	#Document.Properties["dh"] = (DateTime.ParseExact(dh.strftime('%d/%m/%Y'),'dd/MM/yyyy',CultureInfo.InvariantCulture)).ToString().Substring(0,10)

	#Document.Properties["dl"] = dl.ToString().Substring(0,10)
	#Document.Properties["dh"] = dh.ToString().Substring(0,10)

	Document.Properties["dl"] = dl.date().strftime('%m/%d/%Y')
	HighLabel = dh + timedelta (days = -1)
	Document.Properties["dh"] = HighLabel.date().strftime('%m/%d/%Y')
		
	myPanel = Document.ActivePageReference.FilterPanel
	myFilter = myPanel.TableGroups[0].GetFilter("Scan Date") 

	lblFilter = myFilter.FilterReference.As[RangeFilter]()
	lblFilter.ValueRange = ValueRange(DateTime.ParseExact(dl.strftime('%m/%d/%Y'),'MM/dd/yyyy',CultureInfo.InvariantCulture),DateTime.ParseExact(dh.strftime('%m/%d/%Y'),'MM/dd/yyyy',CultureInfo.InvariantCulture))

#Function: setAccessParameters
#####  Description:gets current logged in user
def setAccessParameters() :
	#Get Username from Spotfire
	username = Thread.CurrentPrincipal.Identity.Name
	currentUser = username
	#strip out the @Domain component (usernames only)
	if username.find("@") > 0:
		currentUser = username[0:username.find("@")] 

	#configure to use for report (see below)
	Document.Properties["username"] = currentUser	
	Document.Properties["UnknownUser"] = ""
	Document.Properties["LoginUser"] = ""


#Function: validateUser
#####  Description:Sets the appropriate access level filter for the current logged in user
def validateUser():

	tr = []	
	validuser = 0
	dt = Document.Data.Tables["Access"]
	rowlist = IndexSet(dt.RowCount,True)

	cursor1 = DataValueCursor.CreateFormatted(dt.Columns["active_dir_id"])
	cursor2 = DataValueCursor.CreateFormatted(dt.Columns["access_level"])
	cursor3 = DataValueCursor.CreateFormatted(dt.Columns["transit"])
	cursor4 = DataValueCursor.CreateFormatted(dt.Columns["rpt_name"])

	#Search to get the access /transit for the User 
	for row in dt.GetRows(rowlist,cursor1, cursor2, cursor3,cursor4): 
		if Document.Properties["username"].upper() == cursor1.CurrentValue.upper() and cursor4.CurrentValue == "Destruction":
			Document.Properties["accesslevel"] = cursor2.CurrentValue
			Document.Properties["transit"] = cursor3.CurrentValue  			
			tr.append(cursor3.CurrentValue)			
			validuser = 1
				
	if validuser == 1:				
		Document.Properties["LoginUser"] = "User ID: "+(Document.Properties["username"])	
		Document.Properties["UnknownUser"] = ""
		myPanel = Document.ActivePageReference.FilterPanel
		myFilter = myPanel.TableGroups[0].GetFilter("TR_flt").FilterReference		
		txtFilter = myFilter.As[filters.ListBoxFilter]()

		# Checking the User Access Level and filtering accordingly
		
		if Document.Properties["accesslevel"] == "2":
			txtFilter.IncludeAllValues = False	
			txtFilter.SetSelection(tr)			
			
		elif Document.Properties["accesslevel"] == "1":
			txtFilter.Reset()			
			txtFilter.IncludeAllValues = True

		#In case access is NULL 
		else:
			txtFilter.Reset()
			txtFilter.IncludeAllValues = False	
			#txtFilter.Value = ItemFiltering.None
			

		#Display the report based on set filter
		setdate()
		Document.ActivePageReference = Document.Pages[1]
	else:			
		Document.Properties["LoginUser"] = ""
		Document.Properties["accesslevel"] = ""
		Document.Properties["transit"] = ""
		Document.Properties["UnknownUser"] = """No information matching your User ID was found. 
												You do not have any active records to be displayed OR your User ID ("""+(Document.Properties["username"])+""") was not found in the database.
												
												For Destruction Report access inquiries/errors, call Distribution Channel Operation (DCO) for support at 1-877-678-7777."""

#Main Program 
setAccessParameters()
validateUser()





#Function: setFSMFilter
##### sets to filter out everyone but the logged in user. 
# * Try/catch is used here because securityFilter here is a radio button,
#   it only accepts values availble in the data table. Unmatched value will cause exception.
#def setFSMFilter(securityFilter) :
#	try:
#		#Match user name to table, if yes, advance to next page
#		securityFilter.Value=(Document.Properties["username"])
#		(Document.Properties["LoginUser"]) = "User ID: "+(Document.Properties["username"])	
#		(Document.Properties["UnknownUser"]) = ""
#		Document.ActivePageReference = Page	
		#return True
#	except ValueError:
		#Match user name to table, if no, roll back everything, show error message
#		securityFilter.Value=ItemFiltering.None
#		(Document.Properties["UnknownUser"]) = """No information matching your User ID was found. 
#												You do not have any active records to be displayed OR your User ID ("""+(Document.Properties["username"])+""") was not found in the database.
#												Please contact SmartCoreSpotfire.Support@bmo.com for support."""
#		(Document.Properties["LoginUser"]) = ""
		#return False

#Main Program:
#Point to main filte rpanel.
#Remove<--myPanel = Document.ActivePageReference.FilterPanel
###### TableGroups is a reference to the tables listed in the FilterPanel.
# The order is important in a TableGroup, as the index has a one-to-one relation to the order found in the FilterPanel
# To check the current FilterPanel index, right click on the filter panel, select "Organize Filter"
# Count the tables from top to bottom, and index starts at 0
##### String passed into GetFilter is the exact name of a filter in the FilterPanel.
##### Debug: When an action control doesn't change a filter as expected, check the followings first.
# 1. TableGroup index
# 2. Filter name
# 3. Is filter enabled or not
# 4. Filter type & its accepted inputs
#* GetFilter returns the FilterHandle, a node in a filter group
#* FilterReference returns the actual filter the node is poiting to
#----------------------------------------------------------------
#Remove<-- myFilter=myPanel.TableGroups[3].GetFilter("User ID").FilterReference
# Set filter type to radio button
#Remove<--myFilter.TypeId = FilterTypeIdentifiers.RadioButtonFilter
# cast filter
#Remove<--rbFilter = myFilter.As[filters.RadioButtonFilter]()
#setAccessParameters()
#setFSMFilter()
