<!DOCTYPE html>
<html>
<head>
	<title>Files</title>
	<style type="text/css">
table, th, td {
    border: 1px solid black;
}
thead {
	font-weight: bolder;
	text-align: center;
}

	</style>
</head>
<body>
	% if not isThisFirstPage:
		<a href="?chunk={{ chunk }}&page={{ page-1 }}">Previous</a>
	% end
	% if not isThisLastPage:
		<a href="?chunk={{ chunk }}&page={{ page+1 }}">Next</a>
	% end
	<table>
		<thead>
			<td>#</td>
			<td>Type</td>
			<td>File</td>
			<td>Time</td>
		</thead>
		<tbody>
		% for aRec in data:
			<tr>
				<td>{{ aRec.sr_num }}</td>
				<td>{{ aRec.dateType }}</td>
				<td>{{ aRec.filePath }}</td>
				<td>{{ aRec.humanTime }}</td>
			</tr>
		% end
		</tbody>
	</table>
</body>
</html>
