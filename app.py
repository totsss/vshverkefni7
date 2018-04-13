from bottle import *
from beaker.middleware import SessionMiddleware

# Kóði hér fyrir neðan nauðsinlegur...
session_opts = {
    'session.type': 'file',
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)

# Ósköp vejulegt route...

@route('/')
def index():
  return """
            <a href='/innskra'>liður a</a><br>
            <a href='/versla'>liður b</a><br>
         """

@route('/versla')
def index():
  return """
            <a href='/byrja/0'>vara 1</a><br>
            <a href='/byrja/1'>vara 2</a><br>
            <a href='/byrja/2'>vara 3</a><br>
            <a href='/karfa'>karfa</a><br>
            <a href='/eyda'>Eyða Session</a><br>
            <a href='/'>liðir</a><br>

         """
# Búum til session

@route('/byrja/<id>')
def byrja(id):
    breyta=id
    s = request.environ.get('beaker.session')
    s[breyta] = "gg"
    s.save()
    return """vara hefur verið sett i körfu <br> <a href='/versla'>Heim</a>"""


@route('/karfa')
def karfa():
    s = request.environ.get('beaker.session')
    vorulisti = str()
    # Athugum hvort session-ið prufa sé til
    for i in range(4):
        if s.get(str(i)):
            strengur = "vara" + str(i+1)
            vorulisti = vorulisti + strengur
    for s in vorulisti:
        return vorulisti,"<br><a href='/versla'>vorur</a>"



# Eyðum session
@route('/eyda')
def eyda():

    s = request.environ.get('beaker.session',)
    s.delete()

    return "Session (prufa) eytt!<br><a href='/versla'>Heim</a>"
    #else:
     #   return "Þessi vara var ekki til áður !"



from beaker.middleware import SessionMiddleware

@route('/innskra')
def start():
	return template("innskra.tpl")

@post("/data")
def data():

	n = request.forms.get("nafn")
	p = request.forms.get("password")
	#response.set_cookie("kokunanf", "admin")
	#response.set_cookie("kokupassword", "admin")
	print(n,p)

	if n == "admin" and p == "1234":
		response.set_cookie("admin", "ok")
		redirect("/leyni")
	else:
		return ("Þú hefur ekki aðgang...")

@route("/leyni")
def leyno():
	if request.get_cookie("admin","ok"):
		return "Þú ert komin á leynisíðunna..."




run(app=app,host='0.0.0.0',port=os.environ.get('PORT'))
