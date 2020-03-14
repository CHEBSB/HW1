# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107061110.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      if row['TEMP'] == '-99' or row['TEMP'] == '-999':
         row['TEMP'] = None   # remove data
      if row['station_id'] == 'C0A880' or row['station_id'] == 'C0F9A0' or row['station_id'] == 'C0G640' or row['station_id'] == 'C0R190' or row['station_id'] == 'C0X260' :
         data.append(row)    
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

MaxTemp = {'C0A880':0, 'C0F9A0':0, 'C0G640':0, 'C0R190':0, 'C0X260':0}
ListOfID =['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
n = len(data)     # length of data
for i in range(n):
   if data[i]['TEMP'] != None:
      data[i]['TEMP'] = (float)(data[i]['TEMP'])
      MaxTemp[data[i]['station_id']] = max(data[i]['TEMP'], MaxTemp[data[i]['station_id']])
for str in ListOfID:  
   if MaxTemp[str] == 0:
      MaxTemp[str] = 'None'
NewData = [None] * 5   # list for output, whose length must be 5
for i in range(5):
   NewData[i] = {}      # initialize
for i in range(5):
   NewData[i]['station_id'] = ListOfID[i]
   NewData[i]['TEMP'] =  MaxTemp[ListOfID[i]]
#---------sorting-------#
def sort(list, k, str): # the work horse
   while list[k][str] < list[k - 1][str]: # lexicographical
      temp = list[k]     # swapping
      list[k] = list[k - 1]
      list[k - 1] = temp
      if k <= 1:
         return
      k = k - 1      
def Sort(list, n, str): # the driver
   for i in range(n - 1):
      sort(list, i + 1, str)
Sort(NewData, 5, 'station_id')
#=======================================

# Part. 4
#=======================================
# Print result  
print(NewData)
#========================================

