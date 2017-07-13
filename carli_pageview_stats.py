import urllib2
import csv
import json


w = raw_input("Input year: ")
filename = w + '_pageviews.csv'
dates = []
# Gets current list of collections
cdm = urllib2.urlopen("https://collections.carli.illinois.edu:8443/dmwebservices/index.php?q=dmGetCollectionList/json")
aliases = json.load(cdm)
nbycoll = []
#for other collections 'nby_' has to be changed to collection prefix
for a in aliases:
	if "nby_" in a['alias']:
		alias = a['alias'].replace("/","")
		nbycoll.append(alias)
for m in range(1,13):
	mylist = []
	n = str(m)
	date = str(w) + '-' + n.zfill(2)
	dates.append(date)
with open(filename, 'wb') as myfile:
		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		wr.writerow([""] + dates)
for t in nbycoll:
	mylist = [t]
	for x in dates:
		# print x
		coll = None
		try:
			data = urllib2.urlopen("https://www.carli.illinois.edu/sites/files/digital_collections/output/" + x + "/collection_homepages_" + x + ".txt")
		
			for line in data:
				if t in line:
					coll = line.replace(t,"").replace("|","").replace("\n","")			
					mylist.append(coll)		
	
		except urllib2.HTTPError, e:
			error_message = e.read()
		if coll == None:
			mylist.append("")
	with open(filename, 'a') as myfile:
		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		wr.writerow(mylist)
	

	
