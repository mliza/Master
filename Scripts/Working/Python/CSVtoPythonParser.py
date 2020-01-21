import csv 
import os 
import sys
import shutil

path = '/this/is/the/path/where/files/will/be'
templateName = 'Name of File to be copied.py' 
csvName  = 'Name of the CSV file that will be copied into template.csv'
Linux = 'Linux command to run'
templatePath = os.path.join(path, template) 


#open the CSV that will be copy to python 
with open(csvName,'r') as f:
	csvData = []
	csvReader = csv.read(f) 
	for row in csvReader:
	  csvData.append(row)

#Append data into templateName.py and run bash 
lineNum = 0
for item in csvData:
  dataIndx = 0
  if not lineNum == 0: 
    tempFile = os.path.join(path,templateName)
    shutil.copy2(templatePath, tempFile)
    with open(tempFile,'a') as tmp: 
      for value in item:
	try:
	  value = eval(value) 
          dataString = "{var} = {value}\n".format(var=csvData[0][dataIndx],value=csvData[lineNum][dataIndx])
	except: 
	  dataString = "{var} = '{value}'\n".format(var=csvData[0][dataIndx],value=csvData[lineNum][dataIndx])
	tmp.write(dataString)
	dataIndx += 1
      
      os.system(Linux)
   lineNum += 1
