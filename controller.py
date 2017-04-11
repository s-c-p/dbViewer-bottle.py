import bottle

@bottle.route("/files")
def files():
	dicn = bottle.request.query
	multiplier = int(dicn.page)
	fetchSize = int(dicn.chunk)

	from dbReader import getFiles
	t = fetchSize*multiplier
	f = t - (fetchSize-1)
	ans = getFiles(f, t)

	lastPage = True if len(ans) < t-f+1 else False
	firstPage = True if multiplier == 1 else False

	return bottle.template("files"
		, page=multiplier
		, chunk=fetchSize
		, data=ans
		, isThisFirstPage=firstPage
		, isThisLastPage=lastPage)

@bottle.route("/errors")
def errors():
	from dbReader import getErrors
	dicn = bottle.request.query
	multiplier = int(dicn.page)
	fetchSize = int(dicn.chunk)
	t = fetchSize*multiplier
	f = t - (fetchSize-1)
	ans = getErrors(f, t)
	return ans

if __name__ == '__main__':
	bottle.run(debug=True, reloader=True)
