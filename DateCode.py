# Previous Quarter Start and End Date 
#====================================
from datetime import datetime,timedelta, date

current_date = datetime.now()
input_date = current_date - timedelta(days=91)

currQuarter = int((input_date.month - 1) / 3 + 1)

dtFirstDay = datetime(current_date.year, 3 * currQuarter - 2, 1)
dtLastDay = datetime(current_date.year, 3 * currQuarter + 1, 1) - timedelta(days=1)

# Previous Month Start adn End Date
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
