from Spotfire.Dxp.Application.Visuals import HtmlTextArea
for vis in Document.ActivePageReference.Visuals:
	if vis.Title == 'burgermenu':
		
		xcode = vis.As[HtmlTextArea]().HtmlContent		
		ccode = xcode.replace('id=bm style="VISIBILITY: visible"','id=bm style="VISIBILITY: hidden"')		
		vis.As[HtmlTextArea]().HtmlContent = ccode.replace('id=btns style="FLOAT: right; PADDING-TOP: 5px; VISIBILITY: hidden"','id=btns style="FLOAT: right; PADDING-TOP: 5px; VISIBILITY: visible"')
