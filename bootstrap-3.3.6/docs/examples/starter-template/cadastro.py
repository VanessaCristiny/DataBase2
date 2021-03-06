#!C:/Users/Vanessa/AppData/Local/Programs/Python/Python35/python.exe -u 
import cx_Oracle
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage()

con = cx_Oracle.connect('system/Admin1234@localhost/TrabalhoBD2')
cur = con.cursor()

idprimeiro_nome = form.getvalue('idprimeiro_nome')
idnome_do_meio = form.getvalue('idnome_do_meio')
idultimo_nome = form.getvalue('idultimo_nome')
idlogin = form.getvalue('idlogin')
idsenha = form.getvalue('idsenha')
idsexo = form.getvalue('idsexo')
id_email = form.getvalue('id_email')
idcpf = form.getvalue('idcpf')
idrua = form.getvalue('idrua')
idnumero = form.getvalue('idnumero')
idcomplemento = form.getvalue('idcomplemento')
idbairro = form.getvalue('idbairro')
idcidade = form.getvalue('idcidade')
idestado = form.getvalue('idestado')
idcep = form.getvalue('idcep')
idtelefone = form.getvalue('idtelefone')
idcelular = form.getvalue('idcelular')

str = "INSERT INTO USUARIOS VALUES(T_NOME('" + idprimeiro_nome + "','" + idnome_do_meio + "','" + idultimo_nome + "'), '" + idlogin +  "','" + idsenha + "','" + idcpf + "','" + idsexo + "','" + id_email + "', T_ENDERECO('" + idrua + "'," + idnumero + ",'" + idcomplemento + "','" + idbairro + "','" + idcidade + "','" + idestado + "','" + idcep + "'), LISTA_TELS(T_TELEFONE('" + idtelefone[0:2] + "','" + idtelefone[2:] + "', 'residencial'), T_TELEFONE('" + idcelular[0:2] + "','" + idcelular[2:] + "', 'celular')))"

print('Content-type:text/html\r\n\r\n')
print('<head>')
print('<meta charset="utf-8">')
print('<meta http-equiv="X-UA-Compatible" content="IE=edge">')
print('<meta name="viewport" content="width=device-width, initial-scale=1">')
print('<!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->')
print('<meta name="description" content="">')
print('<meta name="author" content="">')
print('<link rel="icon" href="../../favicon.ico">')

print('<title>Mercado das Pulgas</title>')

print('<!-- Bootstrap core CSS -->')
print('<link href="../../dist/css/bootstrap.min.css" rel="stylesheet">')

print('<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->')
print('<link href="../../assets/css/ie10-viewport-bug-workaround.css" rel="stylesheet">')

print('<!-- Custom styles for this template -->') 
print('<link href="dashboard.css" rel="stylesheet">')

print('<!-- Just for debugging purposes. Dont actually copy these 2 lines! -->')
print('<!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->')
print('<script src="../../assets/js/ie-emulation-modes-warning.js"></script>')

print('<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->')
print('<!--[if lt IE 9]>')
print('<script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>')
print('<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>')
print('<![endif]-->')
print('</head>')

print('<nav class="navbar navbar-inverse navbar-fixed-top">')
print('<div class="container">')
print('<div class="navbar-header">')
print('<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">')
print('<span class="sr-only">Toggle navigation</span>')
print('<span class="icon-bar"></span>')
print('<span class="icon-bar"></span>')
print('<span class="icon-bar"></span>')
print('</button>')
print('<a class="navbar-brand" href="home.html">Mercado das Pulgas</a>')
print('</div>')
print('<div id="navbar" class="collapse navbar-collapse">')
print('<ul class="nav navbar-nav">')
print('<li class="active"><a href="home.html">Home</a></li>')
print('<li><a href="vender.html">Vender</a></li>')
print('<li><a href="login.html">Login</a></li>')
print('</ul>')
print('</div><!--/.nav-collapse -->')
print('</div>')
print('</nav>')

try:
	cur.execute(str)
	con.commit()
except cx_Oracle.DatabaseError as e:
	print ("<body>")
	print ("<h2>Nao foi possivel cadastrar novo usuario</h2>")
	print ("</body>")
	cur.close()
	con.close()
else:
	print ("<body>")
	print ("<h2>Usuario cadastrado com sucesso</h2>")
	print ("</body>")
	cur.close()
	con.close()