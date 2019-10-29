import pymysql

class Banco():

    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = ""
        db = "almoxarifado"
        self.conexao = pymysql.connect(host, user, password, db)
        
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS usuario (
                        id INT(11) NOT NULL primary key AUTO_INCREMENT,
                        nome VARCHAR(100) NOT NULL,
                        cpf CHAR(11) NOT NULL,
                        telefone VARCHAR(18) DEFAULT NULL,
                        celular VARCHAR(18) DEFAULT NULL,
                        sexo CHAR(1) DEFAULT NULL,
                        username VARCHAR(45) NOT NULL,
                        senha VARCHAR(256) NOT NULL,
                        status TINYINT(1) NOT NULL,
                        email VARCHAR(45) DEFAULT NULL,
                        data_nasc DATE DEFAULT NULL,
                        setor VARCHAR(45) NOT NULL,
                        permissao VARCHAR(45) NOT NULL
                )""")
        self.conexao.commit()
        c.close()
