from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests, webbrowser


index_page_html_str = """
<!DOCTYPE html>
<html>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Books</title>
</head>
<body style="background-color: #B1DB34;">
<div>
	<center>
		<h1>Books</h1>
		<form method="post" action="">
			<input type="text" name="bookname" placeholder="Enter book name..." autofocus>
			<input type="submit" name="sm" value = "Search">
		</form>
		<hr>
	</center>
</div>
<div style="overflow-x: auto;overflow-y: auto;width: 98vw;height: 67vh;background-color: white">
	{datax}
</div>
<hr>
<div style="font-family: monospace;"><b>Developer's name</b>: Sandipan Chowdhury</div>

</body>
</html>
"""


app = Flask(__name__)

@app.route('/', methods=["get","post"])
def index():
	if request.method == "POST":
		try:
			bookname = request.form.get("bookname")
			myurl = f"http://libgen.is/search.php?req={bookname}&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def"
			req_obj = requests.get(myurl)
			soupObj = BeautifulSoup(req_obj.text,"lxml")
			tables = soupObj.select('table')
			data_table = tables[2]
			data = str(data_table)
		except:
			data = "<h1 style='font-family:roboto'> Try Checking Internet Connection...</h1>"
	else:
		data = ""
	return index_page_html_str.format(datax = data)



if __name__ == '__main__':
	webbrowser.open("http://localhost:5000/")
	app.run(debug = False)