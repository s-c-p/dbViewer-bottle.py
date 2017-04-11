"""
	The business logic, test is CLI based
"""

import sqlite3
from collections import namedtuple

TOTAL = "SELECT COUNT(uid) FROM {tableName};"
FETCH = "SELECT * FROM {tableName} WHERE uid BETWEEN ? AND ?;"
DB_FILE = "analyses.db"
DEFAULT_FETCH_SIZE = 10

anError = namedtuple("anError",
	[ "sr_num"
	, "dateType"
	, "filePath"
	, "errorMsg"])

fileRec = namedtuple("fileRec",
	[ "sr_num"
	, "dateType"
	, "filePath"
	, "timestamp"
	, "humanTime"])

lastPage = False
firstPage = True
workerFunc = None
dataStruct = None

def readDB(query, f, t, dataStruct):
	with sqlite3.connect(DB_FILE) as conn:
		cur = conn.cursor()
		x = cur.execute(    query, (f, t)    )
	ans = list()
	for anEntry in x:
		ans.append(dataStruct._make(anEntry))
	if len(ans) < (t-f+1):
		globals()["lastPage"] = True
	return ans

def getErrors(f, t):
	sq = FETCH.format(tableName="errors")
	return readDB(sq, f, t, anError)

def getFiles(f, t):
	sq = FETCH.format(tableName="files")
	return readDB(sq, f, t, fileRec)

def getPageNum(page_num, fetchSize):
	if page_num <= 0:
		raise StopIteration("Negative page number requested")
	firstPage = True if page_num == 1 else False
	multiplier = page_num
	t = fetchSize*multiplier
	f = t - (fetchSize-1)
	return workerFunc(f, t)

def setFetchSize():
	x = input("Enter size of one chunk: ")
	try:
		x = int(x)
	except:
		x = DEFAULT_FETCH_SIZE
	return x

def decideTableName():
	ch = input("Which table would you like to inspect?").lower()
	if ch.startswith("e"):
		table_name = "errors"
		globals()["workerFunc"] = getErrors
	else:
		table_name = "files"
		globals()["workerFunc"] = getFiles
	# globals()["N"] = sqlite3.connect(DB_FILE).cursor().execute(TOTAL.format(tableName=table_name)).fetchone()[0]
	return

def test():
	from pprint import pprint
	page_num = 1
	fetchSize = setFetchSize()
	decideTableName()
	pprint(getPageNum(page_num, fetchSize))
	while True:
		firstPage = True if page_num == 1 else False
		if lastPage:
			print("---------- End of database ----------")
			break
		ch = input("Press:\n\t[s]top\n\t[n]ext\n\t[p]revious\n\n>>> ")
		if ch == "s":
			break
		elif ch == "p":
			if firstPage:	input("you are already at the first page")
			page_num-= 1
			pprint(getPageNum(page_num, fetchSize))
		else:
			page_num+= 1
			pprint(getPageNum(page_num, fetchSize))
	return

if __name__ == '__main__':
	test()
