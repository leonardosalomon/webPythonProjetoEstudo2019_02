from database.BancoBD import Banco

class Pedido(object):

    def __init__(self, id=0, data_solicita="", status="", data_aprovacao="", data_entrega="", id_usuario=""):
        self.info = {}
        self.id = id
        self.data_solicita = data_solicita
        self.status = status
        self.data_aprovacao = data_aprovacao
        self.data_entrega = data_entrega
        self.id_usuario = id_usuario

    def selectRequestALL(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT * FROM pedido LEFT JOIN usuario ON pedido.id_usuario = usuario.id")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do usuário"


    def selectRequest(self, id):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT * FROM pedido WHERE pedido.id = %s" , (id))
            
            for linha in c:
                self.id = linha[0]
                self.data_solicita = linha[1]
                self.status = linha[2]
                self.data_aprovacao = linha[3]
                self.data_entrega = linha[4]
                self.id_usuario = linha[5]

            c.close()

            return "Busca realizada com sucesso"
        except:
            return "Ocorreu um erro na busca do usuário"


    def insert(self):

        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT INTO pedido(data_solicita, status, id_usuario) VALUES (%s, %s, %s)" , (self.data_solicita, self.status, self.id_usuario))
            banco.conexao.commit()
            self.id = c.lastrowid
            c.close()

            return "Pedido cadastrado com sucesso!"
        except:
            return "Ocorreu um erro no cadastro do pedido"


    def update(self):

        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("UPDATE usuario SET nome = %s , cpf = %s , data_nasc = %s , sexo = %s , email = %s , telefone = %s , celular = %s , username = %s , senha = %s , setor = %s , permissao = %s  WHERE id = %s " , (self.nome, self.cpf, self.data_nasc, self.sexo, self.email, self.telefone, self.celular, self.username, self.senha, self.setor, self.permissao, self.id))
            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"


    def delete(self, id):

        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("delete from itens_pedido where id_pedido = %s" , (id))
            c.execute("delete from pedido where id = %s" , (id))
            banco.conexao.commit()
            c.close()

            return "Pedido excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do Pedido"


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
