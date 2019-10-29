from database.BancoBD import Banco

class Usuario(object):

    def __init__(self, id=0, nome="", cpf="", data_nasc="", sexo="", email="", telefone="", celular="", username="", senha="", setor="", permissao="", status=""):
        self.info = {}
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc
        self.sexo = sexo
        self.email = email
        self.telefone = telefone
        self.celular = celular
        self.username = username
        self.senha = senha
        self.setor = setor
        self.permissao = permissao
        self.status = status

    def selectUserALL(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("select * from usuario where status = 1")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do usuário"


    def selectUser(self, id):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("select * from usuario where id = %s" , (id))
            
            for linha in c:
                self.id=linha[0]
                self.nome=linha[1]
                self.cpf = linha[2]
                self.telefone = linha[3]
                self.celular = linha[4]
                self.sexo = linha[5]
                self.username = linha[6]
                self.senha = linha[7]
                self.status = linha[8]
                self.email = linha[9]
                self.data_nasc = linha[10]
                self.setor = linha[11]
                self.permissao = linha[12]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"


    def insertUser(self):

        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT INTO usuario(nome, cpf, data_nasc, sexo, email, telefone, celular, username, senha, setor, permissao, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" , (self.nome, self.cpf, self.data_nasc, self.sexo, self.email, self.telefone, self.celular, self.username, self.senha, self.setor, self.permissao, '1' ))
            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"


    def updateUser(self):

        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("UPDATE usuario SET nome = %s , cpf = %s , data_nasc = %s , sexo = %s , email = %s , telefone = %s , celular = %s , username = %s , senha = %s , setor = %s , permissao = %s  WHERE id = %s " , (self.nome, self.cpf, self.data_nasc, self.sexo, self.email, self.telefone, self.celular, self.username, self.senha, self.setor, self.permissao, self.id))
            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"


    # def deleteUser(self):

    #     banco=Banco()
    #     try:

    #         c=banco.conexao.cursor()
    #         c.execute("delete from usuario where id = %s" , (self.id))
    #         banco.conexao.commit()
    #         c.close()

    #         return "Usuário excluído com sucesso!"
    #     except:
    #         return "Ocorreu um erro na exclusão do usuário"

    def deleteUser(self, id):

        banco=Banco()
        try:

            c=banco.conexao.cursor()
            c.execute("delete from usuario where id = %s" , (id))
            banco.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectLogin(self, username, password):

        banco=Banco()
        try:

            c=banco.conexao.cursor()
            c.execute("select * from usuario where username = %s and senha = %s" , (username, password))

            for linha in c:
                self.id=linha[0]
                self.nome=linha[1]
                self.cpf = linha[2]
                self.telefone = linha[3]
                self.celular = linha[4]
                self.sexo = linha[5]
                self.username = linha[6]
                self.senha = linha[7]
                self.status = linha[8]
                self.email = linha[9]
                self.data_nasc = linha[10]
                self.setor = linha[11]
                self.permissao = linha[12]
                
            c.close()

            return "Login efetuado com sucesso!"
        except:
            return "Ocorreu um erro ao efetuar o login"
