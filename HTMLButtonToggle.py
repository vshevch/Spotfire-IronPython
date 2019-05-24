# More Reading Matterial: 
# * https://community.tibco.com/wiki/using-ironpython-call-script-tibco-spotfire
# * http://tainguyen.me/blog/spotfire-calling-another-script-with-parameters-and-receive-returned-value/

from Spotfire.Dxp.Application.Visuals import HtmlTextArea
for vis in Document.ActivePageReference.Visuals:
	if vis.Title == 'nbuttons':
	
		# Each line finds and replaces a part of the visualization's HTML code
		HTMLcode = vis.As[HtmlTextArea]().HtmlContent.replace('id=lwuc style="FLOAT: left; DISPLAY: visible"','id=lwuc style="FLOAT: left; DISPLAY: none"') 
		HTMLcode = HTMLcode.replace('id=lwc style="FLOAT: left; DISPLAY: none"','id=lwc style="FLOAT: left; DISPLAY: visible"')

		HTMLcode = HTMLcode.replace('id=fwuc style="FLOAT: left; DISPLAY: none"','id=fwuc style="FLOAT: left; DISPLAY: visible"') 
		HTMLcode = HTMLcode.replace('id=fwc style="FLOAT: left; DISPLAY: visible"','id=fwc style="FLOAT: left; DISPLAY: none"')

		HTMLcode = HTMLcode.replace('id=nfyuc style="FLOAT: left; DISPLAY: none"','id=nfyuc style="FLOAT: left; DISPLAY: visible"') 
		HTMLcode = HTMLcode.replace('id=nfyc style="FLOAT: left; DISPLAY: visible"','id=nfyc style="FLOAT: left; DISPLAY: none"')

		HTMLcode = HTMLcode.replace('id=nauc style="FLOAT: left; DISPLAY: none"','id=nauc style="FLOAT: left; DISPLAY: visible"') 
		HTMLcode = HTMLcode.replace('id=nac style="FLOAT: left; DISPLAY: visible"','id=nac style="FLOAT: left; DISPLAY: none"')

		vis.As[HtmlTextArea]().HtmlContent = HTMLcode
