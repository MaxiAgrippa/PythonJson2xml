from json2xml import json2xml
# import json2xml.json2xml
# import json2xml.json2xml
#from json2xml.utils import readfromurl, readfromstring, readfromjson
from json2xml.utils import *

# get the xml from an URL that return json
data = readfromurl("https://coderwall.com/vinitcool76.json")
print(json2xml.Json2xml(data).to_xml())

# get the xml from a json string
data = readfromstring(
    '{"login":"mojombo","id":1,"avatar_url":"https://avatars0.githubusercontent.com/u/1?v=4"}'
)
print(json2xml.Json2xml(data).to_xml())

# get the data from an URL
# data = readfromjson("examples/licht.json")
# print(json2xml.Json2xml(data).to_xml())