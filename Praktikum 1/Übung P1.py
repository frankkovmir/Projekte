import datetime

#convert string to datetime

dt_str = 'October 01, 2022'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y') #needs to be told the format
print(dt)