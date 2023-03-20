import pyodbc

# configuração da conexão com o banco de dados
server = 'nome_do_servidor'
database = 'nome_do_banco'
username = 'usuario'
password = 'senha'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
