from Spotfire.Dxp.Application.Visuals import HtmlTextArea

# You need to pass parameters to make this work. Currently, a different Spotfire Script passes the parameters to this script
# For testing use these parameters:
#PrevWeek = "ON"
#FourWeeks = "ON"
#PrevMonth = "ON"
#YTD = "OFF"

#Loops through all Pages and all Visualizations names
for page in Document.Pages:
	for vis in page.Visuals:
		if vis.Title == 'NavPanel_2':
			# Each line finds and replaces a part of the visualization's HTML code
			HTMLcode = vis.As[HtmlTextArea]().HtmlContent
			
			if PrevWeek == "ON":
				HTMLcode = HTMLcode.replace('id=PrevWeekButton_ON style="DISPLAY: none;','id=PrevWeekButton_ON style="DISPLAY: inline-block;') 
				HTMLcode = HTMLcode.replace('id=PrevWeekButton_OFF style="DISPLAY: inline-block;','id=PrevWeekButton_OFF style="DISPLAY: none;') 
				
			elif PrevWeek == "OFF":
				HTMLcode = HTMLcode.replace('id=PrevWeekButton_ON style="DISPLAY: inline-block;','id=PrevWeekButton_ON style="DISPLAY: none;') 
				HTMLcode = HTMLcode.replace('id=PrevWeekButton_OFF style="DISPLAY: none;','id=PrevWeekButton_OFF style="DISPLAY: inline-block;') 

			if FourWeeks == "ON":
				HTMLcode = HTMLcode.replace('id=FourWeeksButton_ON style="DISPLAY: none;','id=FourWeeksButton_ON style="DISPLAY: inline-block;') 
				HTMLcode = HTMLcode.replace('id=FourWeeksButton_OFF style="DISPLAY: inline-block;','id=FourWeeksButton_OFF style="DISPLAY: none;') 
				
			elif FourWeeks == "OFF":
				HTMLcode = HTMLcode.replace('id=FourWeeksButton_ON style="DISPLAY: inline-block;','id=FourWeeksButton_ON style="DISPLAY: none;') 
				HTMLcode = HTMLcode.replace('id=FourWeeksButton_OFF style="DISPLAY: none;','id=FourWeeksButton_OFF style="DISPLAY: inline-block;') 
			
			if PrevMonth == "ON":
				HTMLcode = HTMLcode.replace('id=PrevMonthButton_ON style="DISPLAY: none;','id=PrevMonthButton_ON style="DISPLAY: inline-block;') 
				HTMLcode = HTMLcode.replace('id=PrevMonthButton_OFF style="DISPLAY: inline-block;','id=PrevMonthButton_OFF style="DISPLAY: none;') 
				
			elif PrevMonth == "OFF":
				HTMLcode = HTMLcode.replace('id=PrevMonthButton_ON style="DISPLAY: inline-block;','id=PrevMonthButton_ON style="DISPLAY: none;') 
				HTMLcode = HTMLcode.replace('id=PrevMonthButton_OFF style="DISPLAY: none;','id=PrevMonthButton_OFF style="DISPLAY: inline-block;') 
			
			if YTD == "ON":
				HTMLcode = HTMLcode.replace('id=YTD_Button_ON style="DISPLAY: none;','id=YTD_Button_ON style="DISPLAY: inline-block;') 
				HTMLcode = HTMLcode.replace('id=YTD_Button_OFF style="DISPLAY: inline-block;','id=YTD_Button_OFF style="DISPLAY: none;') 
				
			elif YTD == "OFF":
				HTMLcode = HTMLcode.replace('id=YTD_Button_ON style="DISPLAY: inline-block;','id=YTD_Button_ON style="DISPLAY: none;') 
				HTMLcode = HTMLcode.replace('id=YTD_Button_OFF style="DISPLAY: none;','id=YTD_Button_OFF style="DISPLAY: inline-block;') 


			vis.As[HtmlTextArea]().HtmlContent = HTMLcode
