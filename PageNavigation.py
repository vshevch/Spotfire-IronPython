# Source Material: http://spotfired.blogspot.com/2014/08/toggle-page-navigation.html

#Navigate to specific named page
for page in Document.Pages:
	if page.Title == 'Data  ADV':
		Document.ActivePageReference = page
      
#Navigate to the first page
Document.ActivePageReference = Document.Pages[0]

#Loop Document Pages
for p in Document.Pages: print p.Title

#Toogle Page Navigation
if Document.Pages.NavigationMode == Document.Pages.NavigationMode.Tabs:
   Document.Pages.NavigationMode = Document.Pages.NavigationMode.Links
elif Document.Pages.NavigationMode == Document.Pages.NavigationMode.Links:
   Document.Pages.NavigationMode = Document.Pages.NavigationMode.None
elif Document.Pages.NavigationMode == Document.Pages.NavigationMode.None:
   Document.Pages.NavigationMode = Document.Pages.NavigationMode.Tabs

#Go to First page
Document.ActivePageReference = Document.Pages[0].Title

#Delete First page
Document.Pages[0].Remove()


#go to last page
print Document.Pages[(Document.Pages.Count-1)].Title

#Delete last page
Document.ActivePageReference = Document.Pages.RemoveAt(Document.Pages.Count-1)

#Delete all pages!
print Document.Pages.Clear()

#Create a page
p = Document.Pages.AddNew()
p.Title = "New Page"

#current page number
print Document.Pages.IndexOf(Document.ActivePageReference)

#total pages
print Document.Pages.Count
