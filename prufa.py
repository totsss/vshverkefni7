from bottle import *
from beaker.middleware import SessionMiddleware

@route('/')
def start():
	return template("innskra.tpl")

@post("/data")
def data():

	n = request.query.get("nafn")
	p = request.query.get("password")
	#response.set_cookie("kokunanf", "admin")
	#response.set_cookie("kokupassword", "admin")

	if n == "admin" and p == "1234":
		response.set_cookie("admin", "ok")
		redirect('/leyni')
	else:
		return ("Þú hefur ekki aðgang...")

@post("/leyni")
def leyno():

	if request.get_cookie("admin","ok"):
		return "Þú ert komin á leynisíðunna..."
	else:
		return ("Þú hefur ekki aðgang...")




run(host='localhost',port=8080,debug=True,reloader=True)
#
#
#
from bottle import *

@route('/static/<nafn>')
def static(nafn):
    return static_file(nafn,root='./static')

@route("/")
def kaka():
#	timi=datetime.datetime.now()+datetime.timedelta(days=1)
#	response.set_cookie("kaka","100", expires=timi)
	return ("kaka til")

@route("/datadel")
def kaka():
	response.set_cookie("sukkuladi","",expires="")
	return ("sukkuladi ekki til")






run(host='localhost',port=8080,debug=True,reloader=True)
