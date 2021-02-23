# adding datetime to the module using datetime library
from datetime import datetime
present_time = datetime.now()
'{:%H:%M:%S}'.format(present_time)
print(present_time)