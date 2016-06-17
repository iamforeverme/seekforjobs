#!/usr/bin/python
parameters = r"dateRange=999&workType=0&industry=&occupation=&graduateSearch=false&salaryFrom=0&salaryTo=999999&salaryType=annual&companyID=&advertiserID=&advertiserGroup=&keywords=python&page=1&displaySuburb=&seoSuburb=&where=&whereId=&whereIsDirty=false&isAreaUnspecified=false&location=&area=&nation=&sortMode=KeywordRelevance&searchFrom=active+filters+clear+all+locations&searchType="
paraList = parameters.split("&")
paraDict = {}
for item in paraList:
	paraDict[item.split("=")[0]] = item.split("=")[-1]

print("{")
for key in paraDict:
	showStr = ""
	if("" == paraDict[key].strip()):
		showStr = ""
	else:
		showStr = paraDict[key]
	print("   \""+key + "\": \"" + showStr +"\",")
print("}")

