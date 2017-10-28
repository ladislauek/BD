from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'root',
  'password': '1234',
  'host': '127.0.0.1',
  'database': 'AULA_BD',
  'raise_on_warnings': True,
}

try:
  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  add_aluno = ("INSERT INTO ALUNO "
              "(NOME, DT_NASCIMENTO) "
              "VALUES (%s, %s)")
  data_aluno = ('Rudy', date(1980, 5, 15))
  cursor.execute(add_aluno, data_aluno)
  cnx.commit()
  print(':::: EXECUTADO ::::')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor.close()
  cnx.close()
