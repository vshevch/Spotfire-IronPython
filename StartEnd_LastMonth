import time
import datetime

now = time.localtime()

# Get the last day of last month by taking the first day of this month
# and subtracting 1 day.
last = datetime.date(now.tm_year, now.tm_mon, 1) - datetime.timedelta(1)

# Set the day to 1 gives us the start of last month
first = last.replace(day=1)

# The default string representation of these datetime instances is 
# YYYY-mm-dd format (which is what I usually need),
# so we can just print them out
print first, last
