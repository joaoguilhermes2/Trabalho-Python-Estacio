from PyQt5 import uic, QtWidgets
import pymysql.connections

banco = pymysql.connect(
    host = "localhost",
    user="root",
    passwd="",
    database="cadastro_colaborador"
)

def cadastrar():
    codigo = cadastro.codigo.text()
    nome = cadastro.nome.text()
    email = cadastro.email.text()
    telefone = cadastro.telefone.text()

    categoria = ""

    if cadastro.adm.isChecked():
        print("categoria administrador Selecionada.")
        categoria = "Adminstrador"

    elif cadastro.colab.isChecked():
        print("Categoria Colaborador Selecionada.")
        categoria = "Colaborador"

    else:
        print("Categoria Terceirizada Selecionada")
        categoria = "Terceirizada"

    print("Codigo:", codigo)
    print("Nome:",nome)
    print("Email:",email)
    print("Telefone:", telefone)
    print("Categoria:", categoria)

    cursor = banco.cursor()

    sql = "INSERT INTO `colaborador`(`codigo`, `nome`, `email`, `telefone`, `categoria`)VALUES(%s,%s,%s,%s,%s)"
    dados = (str(codigo),str(nome),str(email),str(telefone), categoria)
    cursor.execute(sql,dados)
    banco.commit()
    
    #limpar campos
    cadastro.codigo.setText("")
    cadastro.nome.setText("")
    cadastro.email.setText("")
    cadastro.telefone.setText("")


def listarDados():
    listar.show()
    cursor = banco.cursor()
    sql = "SELECT * FROM colaborador"
    cursor.execute(sql)
    dadosLidos = cursor.fetchall()
    
    listar.tableWidget.setRowCount(len(dadosLidos))
    listar.tableWidget.setColumnCount(5)
    
    for linha in range(0,len(dadosLidos)):
        for coluna in range(0,4):
            listar.tableWidget.setItem(linha,coluna,QtWidgets.QTableWidgetItem(str(dadosLidos[linha][coluna])))

def excluir():
    linha_selecionada = listar.tableWidget.currentRow()
    if linha_selecionada >= 0:
        codigo = listar.tableWidget.item(linha_selecionada, 0).text()
        cursor = banco.cursor()
        sql = "DELETE FROM colaborador WHERE codigo = %s"
        cursor.execute(sql, (codigo,))
        banco.commit()
        listar.tableWidget.removeRow(linha_selecionada)
    else:
        print("Selecione uma linha para excluir.")

def editar():
    linha_selecionada = listar.tableWidget.currentRow()
    if linha_selecionada >= 0:
        codigo = listar.tableWidget.item(linha_selecionada, 0).text()
        nome = listar.tableWidget.item(linha_selecionada, 1).text()
        email = listar.tableWidget.item(linha_selecionada, 2).text()
        telefone = listar.tableWidget.item(linha_selecionada, 3).text()

        # Populate fields in edicao.ui
        edicao.codigo.setText(codigo)
        edicao.nome.setText(nome)
        edicao.email.setText(email)
        edicao.telefone.setText(telefone)

        edicao.show()
    else:
        print("Selecione uma linha para editar.")


# Function to save edited data back to the database
def salvarEdicao():
    codigo = edicao.codigo.text()
    nome = edicao.nome.text()
    email = edicao.email.text()
    telefone = edicao.telefone.text()

    cursor = banco.cursor()
    sql = "UPDATE colaborador SET nome=%s, email=%s, telefone=%s WHERE codigo=%s"
    dados = (nome, email, telefone, codigo)
    cursor.execute(sql, dados)
    banco.commit()

    # Refresh the table in listar.ui
    listarDados()
    edicao.close()

    
app = QtWidgets.QApplication([])
cadastro = uic.loadUi("cadastro.ui")
listar = uic.loadUi("listar.ui")
edicao = uic.loadUi("edicao.ui")

cadastro.btn_cadastrar.clicked.connect(cadastrar)
cadastro.btn_listar.clicked.connect(listarDados)
listar.excluir.clicked.connect(excluir)
listar.editar.clicked.connect(editar)  # Connect the edit button in listar.ui
edicao.btn_salvar.clicked.connect(salvarEdicao)  # Connect the save button in edicao.ui


cadastro.show()
app.exec()
