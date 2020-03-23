# Save current tab name
Document.Properties["FilterTabLocation"] = Document.ActivePageReference.Title

# Go to tab with Specific Name
for page in Application.Document.Pages:
 if page.Title == "Advance Filter":
  Document.ActivePageReference = page
