from database.BancoBD import Banco

class Produto(object):

    def __init__(self, id=0,nome="",unidade="",status="",imagem=""):
        self.info = {}
        self.id = id
        self.nome = nome
        self.unidade = unidade
        self.status = status
        self.imagem = imagem


    def selectALL(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("select id, nome, unidade, status, CONVERT(imagem USING utf8) from produto")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do produto"


    def selectONE(self, id):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("select id, nome, unidade, status, CONVERT(imagem USING utf8) from produto where id = %s" , (id))
            
            for linha in c:
                self.id = linha[0]
                self.nome = linha[1]
                self.unidade = linha[2]
                self.status = linha[3]
                self.imagem = linha[4]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do produto"


    def insert(self):
        banco = Banco()
        try:
            print(self.imagem)
            c = banco.conexao.cursor()
            c.execute("insert into produto(nome, unidade, imagem, status) values (%s,%s,%s,%s)" , (self.nome,self.unidade,self.imagem, '1'))
            banco.conexao.commit()
            c.close()

            return "Produto cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do produto"

    
    def update(self):

        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("update produto set nome=%s,unidade=%s,imagem=%s where id = %s" , (self.nome,self.unidade,self.imagem,self.id))
            banco.conexao.commit()
            c.close()

            return "Produto atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do produto"

    
    def delete(self, id):

        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("delete from produto where id = %s" , (id))
            banco.conexao.commit()
            c.close()

            return "Produto excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do Produto"
