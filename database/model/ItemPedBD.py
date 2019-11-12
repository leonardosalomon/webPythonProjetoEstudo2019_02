from database.BancoBD import Banco

class ItemPed(object):

    def __init__(self, id=0,quantidade="",quantidade_aprovada="",id_pedido="",id_produto=""):
        self.info = {}
        self.id = id
        self.quantidade = quantidade
        self.quantidade_aprovada = quantidade_aprovada
        self.id_pedido = id_pedido
        self.id_produto = id_produto
        self.nomeprod = None
        self.uniprod = None
        self.imgprod = None


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
            c.execute("SELECT itens_pedido.id_pedido, itens_pedido.id_produto, itens_pedido.quantidade, produto.nome, produto.unidade, CONVERT(produto.imagem USING utf8), itens_pedido.quantidade_aprovada FROM itens_pedido LEFT JOIN produto ON itens_pedido.id_produto = produto.id WHERE itens_pedido.id_pedido = %s" , (id))

            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do produto"

    

    def insert(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into itens_pedido(quantidade, quantidade_aprovada, id_pedido, id_produto) values (%s,%s,%s,%s)" , (self.quantidade,self.quantidade_aprovada,self.id_pedido, self.id_produto))
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
