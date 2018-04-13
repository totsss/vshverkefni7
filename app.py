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
            <a href='/byrja/0'>vara 1</a><br>
            <a href='/byrja/1'>vara 2</a><br>
            <a href='/byrja/2'>vara 3</a><br>
            <a href='/karfa'>karfa</a><br>
            <a href='/eyda'>Eyða Session</a><br>
         """
# Búum til session

@route('/byrja/<id>')
def byrja(id):
    breyta=id
    s = request.environ.get('beaker.session')
    s[breyta] = "gg"
    s.save()
    return """vara hefur verið sett i körfu <br><a href='/'>Heim</a>"""

# Athugum hvort tiltekið session sé til
@route('/karfa')
def karfa():
    s = request.environ.get('beaker.session')

    # Athugum hvort session-ið prufa sé til
    if s.get('gg'):
        return s,"vara til til <br><a href='/'>Heim</a>"
    else:
        return "ekkrt til í körfu <br><a href='/'>Heim</a>"

# Eyðum session
@route('/eyda')
def eyda():

    s = request.environ.get('beaker.session',)
    s.delete()

    return "Session (prufa) eytt!<br><a href='/'>Heim</a>"
    #else:
     #   return "Þessi vara var ekki til áður !"

# Muna eftir app=app í run fallinu
run(app=app)
