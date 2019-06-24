# Previous Quarter Start and End Date 

from datetime import datetime,timedelta, date

current_date = datetime.now()
input_date = current_date - timedelta(days=91)

currQuarter = int((input_date.month - 1) / 3 + 1)

dtFirstDay = datetime(current_date.year, 3 * currQuarter - 2, 1)
dtLastDay = datetime(current_date.year, 3 * currQuarter + 1, 1) - timedelta(days=1)
