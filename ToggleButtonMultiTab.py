from Spotfire.Dxp.Application.Visuals import HtmlTextArea

#Uncomment button parameters below for testing
# Button1 = "ON"
# Button2 = "ON"
# Button3 = "ON"
# Button4 = "ON"
# Button5 = "OFF"


#Loops through every Page and every Visualization
for page in Document.Pages:
	for vis in page.Visuals:
		if vis.Title == 'NavPanel_2':
			# Each line finds and replaces a part of the visualization's HTML code
			HTMLcode = vis.As[HtmlTextArea]().HtmlContent
			
			# Button settings are defined in the Script that calls this script
			if Button1 == "ON":
				HTMLcode = HTMLcode.replace('id=Button1_ON style="DISPLAY: none;','id=Button1_ON style="DISPLAY: inline-block;') 
				HTMLcode = HTMLcode.replace('id=Button1_OFF style="DISPLAY: inline-block;','id=Button1_OFF style="DISPLAY: none;') 
				
			elif Button1 == "OFF":
				HTMLcode = HTMLcode.replace('id=Button1_ON style="DISPLAY: inline-block;','id=Button1_ON style="DISPLAY: none;') 
				HTMLcode = HTMLcode.replace('id=Button1_OFF style="DISPLAY: none;','id=Button1_OFF style="DISPLAY: inline-block;') 

			if Button2 == "ON":
				HTMLcode = HTMLcode.replace('id=Button2_ON style="DISPLAY: none;','id=Button2_ON style="DISPLAY: inline-block;') 
				HTMLcode = HTMLcode.replace('id=Button2_OFF style="DISPLAY: inline-block;','id=Button2_OFF style="DISPLAY: none;') 
				
			elif Button2 == "OFF":
				HTMLcode = HTMLcode.replace('id=Button2_ON style="DISPLAY: inline-block;','id=Button2_ON style="DISPLAY: none;') 
				HTMLcode = HTMLcode.replace('id=Button2_OFF style="DISPLAY: none;','id=Button2_OFF style="DISPLAY: inline-block;') 
			
			if Button3 == "ON":
				HTMLcode = HTMLcode.replace('id=Button3_ON style="DISPLAY: none;','id=Button3_ON style="DISPLAY: inline-block;') 
				HTMLcode = HTMLcode.replace('id=Button3_OFF style="DISPLAY: inline-block;','id=Button3_OFF style="DISPLAY: none;') 
				
			elif Button3 == "OFF":
				HTMLcode = HTMLcode.replace('id=Button3_ON style="DISPLAY: inline-block;','id=Button3_ON style="DISPLAY: none;') 
				HTMLcode = HTMLcode.replace('id=Button3_OFF style="DISPLAY: none;','id=Button3_OFF style="DISPLAY: inline-block;') 
			
			if Button4 == "ON":
				HTMLcode = HTMLcode.replace('id=Button4_ON style="DISPLAY: none;','id=Button4_ON style="DISPLAY: inline-block;') 
				HTMLcode = HTMLcode.replace('id=Button4_OFF style="DISPLAY: inline-block;','id=Button4_OFF style="DISPLAY: none;') 
				
			elif Button4 == "OFF":
				HTMLcode = HTMLcode.replace('id=Button4_ON style="DISPLAY: inline-block;','id=Button4_ON style="DISPLAY: none;') 
				HTMLcode = HTMLcode.replace('id=Button4_OFF style="DISPLAY: none;','id=Button4_OFF style="DISPLAY: inline-block;') 
				
			if Button5 == "ON":
				HTMLcode = HTMLcode.replace('id=Button5_ON style="DISPLAY: none;','id=Button5_ON style="DISPLAY: inline-block;') 
				HTMLcode = HTMLcode.replace('id=Button5_OFF style="DISPLAY: inline-block;','id=Button5_OFF style="DISPLAY: none;') 
				
			elif Button5 == "OFF":
				HTMLcode = HTMLcode.replace('id=Button5_ON style="DISPLAY: inline-block;','id=Button5_ON style="DISPLAY: none;') 
				HTMLcode = HTMLcode.replace('id=Button5_OFF style="DISPLAY: none;','id=Button5_OFF style="DISPLAY: inline-block;') 


			vis.As[HtmlTextArea]().HtmlContent = HTMLcode
