# Previous Quarter Start and End Date 
#=====================================
from datetime import datetime,timedelta, date

current_date = datetime.now()
input_date = current_date - timedelta(days=91)

currQuarter = int((input_date.month - 1) / 3 + 1)

dtFirstDay = datetime(current_date.year, 3 * currQuarter - 2, 1)
dtLastDay = datetime(current_date.year, 3 * currQuarter + 1, 1) - timedelta(days=1)

# Previous Month Start and End Date
#===================================
from datetime import date, timedelta, date
from Spotfire.Dxp.Data.DataType import Date

def get_first_day(dt, d_years=0, d_months=-1): # d_years & d_months are "deltas" to apply to dt
    y, m = dt.year + d_years, dt.month + d_months
    a, m = divmod(m-1, 12)
    return date(y+a, m+1, 1)

def get_last_day(dt):
    return get_first_day(dt, 0, 0) - timedelta(1)

dtFirstDay = get_first_day(date.today())
dtLastDay = get_last_day(date.today())

# Used in a Range Filter
LowVal = Date.Formatter.Parse(str(dtFirstDay))
HighVal = Date.Formatter.Parse(str(dtLastDay))

# Previous Fiscal Quarter Start and End Date
#============================================
# Code for determining Previous Fiscal Quarter with Fiscal Start Date in November
# ex. Q1 - Nov 01 2018 to Jan 31 2019

from datetime import datetime,timedelta, date

current_date = datetime.now()
input_date = current_date - timedelta(days=91)

quart = ((input_date.month + 1) / 3 + 1) # Create Fiscal Quarter
d_annee, restants = divmod(quart,5) # Normalise to 1 to 4 quarters
currQuarter = int(max(d_annee, restants)) 

def q_start_end(quarter): # Create veriables and define Quarter's Start and End dates
    global q_start #month when the quarter starts
    global q_end #the month when the next quarter starts
    global d_year #delta year - change in the year if required
    
    if quarter == 1:
        q_start, q_end, d_year = (11, 2, -1)
    elif quarter == 2:
        q_start, q_end, d_year = (2, 5, 0)
    elif quarter == 3:
        q_start, q_end, d_year = (5, 8, 0)
    elif quarter == 4:
        q_start, q_end, d_year = (8, 11, 0)    

q_start_end(currQuarter)

dtFirstDay = datetime(input_date.year + d_year + int(d_annee), q_start, 1)
dtLastDay = datetime(input_date.year + int(d_annee), q_end, 1) - timedelta(days=1)

# YTD
#========================================
from datetime import datetime,timedelta, date

current_date = datetime.now()

if current_date.month <= 10:
    high = datetime(current_date.year, 10, 31)
    low = datetime(current_date.year - 1, 11, 1)
elif current_date.month > 10:
    high = datetime(current_date.year + 1, 10, 31)
    low = datetime(current_date.year, 11, 1)
    
print(high)
print(low)
