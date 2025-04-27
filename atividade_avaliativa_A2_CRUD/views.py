from flask import Flask, request, jsonify, render_template
from models.task import Aluno
from database.conexao import conectar
import random

app = Flask(__name__)

# função para gerar ID único sem risco de repetições
def gerar_id_unico(cursor):
    while True:
        novo_id = random.randint(10000, 99999)
        cursor.execute("SELECT id_aluno FROM aluno_crud WHERE id_aluno = %s", (novo_id,))
        resultado = cursor.fetchone()
        if not resultado:
            return novo_id

# rota para 
@app.route("/cadastro.html")
def retornar_pagina():
        return render_template("cadastro.html")

@app.route("/segunda_pagina.html")
def pagina2():
    return render_template("segunda_pagina.html")

@app.route("/resultado.html")
def pagina_aluno():
    return render_template("resultado.html")

# CRIAR ALUNO
@app.route("/aluno", methods=['POST'])
def criar_aluno():
 data = request.get_json()
 print("Recebido do front-end:", data)
 try:
    conexao = conectar()
    with conexao:
        with conexao.cursor() as cursor:
             id = gerar_id_unico(cursor) # variável recebe id aleatório
             new_aluno = Aluno(id_aluno = id, nome=data['nome'], email=data['email'], senha= data['senha'])
             sql = "INSERT INTO aluno_crud (id_aluno, nome, email, senha) VALUES (%s, %s, %s, %s)"
             cursor.execute(sql, (
                new_aluno.id_aluno,
                new_aluno.nome,
                new_aluno.email,
                new_aluno.senha
            ))
        conexao.commit()
 except Exception as e:
    print("Erro ao inserir no banco:", e)
    return jsonify({"message": "Erro ao salvar no banco de dados"}), 500
 return jsonify({"message": "Aluno cadastrado com sucesso!"}), 201

# EXIBIR ALUNO
@app.route("/aluno", methods=['GET'])
def mostrar_aluno():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM aluno_crud")
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return jsonify(resultados)

# ATUALIZAR ALUNO
@app.route("/aluno/<int:id_aluno>", methods=['PUT'])
def atualizar_aluno(id_aluno):
    data = request.get_json()
    campos = {chave: data[chave] for chave in ['nome', 'email', 'senha'] if chave in data}

    if not campos:
        return jsonify({"message": "Nenhum dado fornecido para atualização"}), 400

    try:
        conexao = conectar()
        with conexao:
            with conexao.cursor() as cursor:
                sets = ", ".join(f"{k} = %s" for k in campos)
                valores = list(campos.values()) + [id_aluno]
                cursor.execute(f"UPDATE aluno_crud SET {sets} WHERE id_aluno = %s", valores)

                if cursor.rowcount == 0:
                    return jsonify({"message": "Aluno não encontrado"}), 404

            conexao.commit()

        return jsonify({"message": "Aluno atualizado com sucesso"}), 200

    except Exception as e:
        print("Erro ao atualizar aluno:", e)
        return jsonify({"message": "Erro ao atualizar aluno"}), 500


# DELETAR ALUNO
@app.route("/aluno/<int:id_aluno>", methods=['DELETE'])
def deletar_aluno(id_aluno):
    try:
        conexao = conectar()
        with conexao:
            with conexao.cursor() as cursor:
                sql = "DELETE FROM aluno_crud WHERE id_aluno = %s"
                cursor.execute(sql, (id_aluno,))
            conexao.commit()

        # Se nenhum registro foi afetado:
        if cursor.rowcount == 0:
            return jsonify({"message": "Aluno não encontrado"}), 404

        return jsonify({"message": f"Aluno com ID {id_aluno} foi deletado com sucesso"}), 200

    except Exception as e:
        print("Erro ao deletar:", e)
        return jsonify({"message": "Erro ao deletar aluno"}), 500

if __name__ == "__main__":
    app.run(debug=True)