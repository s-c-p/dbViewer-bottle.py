<!DOCTYPE html>
<html>
<head>
	<title>Errors</title>
	<style type="text/css">
table, th, td {
    border: 1px solid black;
}
	</style>
</head>
<body>
	<button {{disabled}} type="button" formaction="?frm={{  }}&to={{  }}">Previous</button>
	<button {{disabled}} type="button" formaction="?frm={{  }}&to={{  }}">Next</button>
	<table>
		<thead>
			<td>#</td>
			<td>Type</td>
			<td>File</td>
			<td>Error</td>
		</thead>
		<tbody>
		<!-- FOR LOOP -->
			<tr>
				<td>{{  }}</td>
				<td>{{  }}</td>
				<td>{{  }}</td>
				<td>{{  }}</td>
			</tr>
		<!-- END FOR LOOP -->
		</tbody>
	</table>
</body>
</html>
