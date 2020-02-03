# Python script for checking if the User Name can see the next tab

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
