from application import app
from flask_mysqldb import MySQL
from MySQLdb.cursors import Cursor

app.config['MYSQL_HOST'] =  'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'coltis_movie_flask'
app.config['MYSQL_PORT'] =  3308
mysql = MySQL(app)

#crear un metodo llamada execute para la biblioteca  que ejecute el cursor, ya sea para devolver un dato o eliminar. 
def execute(sql: str) -> Cursor:
    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    return cursor
#
def commit() -> None:
    mysql.connection.commit()