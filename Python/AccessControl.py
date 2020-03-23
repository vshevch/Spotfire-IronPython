# ---- Python script for checking if the User Name can see the next tab ----

#Import Module(s)
from System.Threading import Thread

#Allowed Users List
yesUsers = ["UserName1", "UserName2"]

#Get Username from Spotfire
username = Thread.CurrentPrincipal.Identity.Name
currentUser = username
#strip out the @Domain component (usernames only)
if username.find("@") > 0:
	currentUser = username[0:username.find("@")] 

# Allow/Deny Access
if currentUser in yesUsers:
	Document.ActivePageReference = Document.Pages[2]
else:
	Document.ActivePageReference = Document.Pages[3]

# ------ If using datasheet for control ------

#Import Modules
from System.Threading import Thread
from Spotfire.Dxp.Data import *

#Get Username from Spotfire
username = Thread.CurrentPrincipal.Identity.Name
currentUser = username
#strip out the @Domain component (usernames only)
if username.find("@") > 0:
	currentUser = username[0:username.find("@")] 
	
# Check Users Against the Permission Table
dt = Document.Data.Tables["STAT_UserAccess"]
cursor = DataValueCursor.CreateFormatted(dt.Columns["User Name"])
permission = 'N'

for Rows in dt.GetRows(cursor):
	if currentUser == cursor.CurrentValue:
		permission = 'Y'

# Allow/Deny Access
if permission == 'Y':
	Document.ActivePageReference = Document.Pages[6]
elif permission == 'N':
	Document.ActivePageReference = Document.Pages[7]
