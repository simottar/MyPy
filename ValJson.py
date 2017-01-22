# Author simottar@gmail.com
# Validates a JSON file
# If it fails validation, it is posted into jsonlint
# takes in the name of the file as parameter. E.g. RemCarRet.py asdf.txt
import json,sys,os

#Checks if json is valid or not
def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError:
    return False
  return True

#We can either take a file or the clipboard
fileName = sys.argv[1]
readFile = open(os.path.join(os.getcwd(),fileName)).read()


if is_json(readFile):
  print('All good')
else: #If the file is fucked we open up the default browser and paste in http://jsonlint.com/ and validate json
  print('shit is fucked yo')

