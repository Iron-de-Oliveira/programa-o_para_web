from flask import Flask, request, jsonify, render_template
from models.task import Aluno
from database.conexao import conectar

app = Flask(__name__)

alunos = []
aluno_id_control = 1

@app.route('/cadastro')
def retornar_pagina():
   return render_template('cadastro_aluno.html')

# Criar uma novo aluno
@app.route('/Alunos', methods=['POST'])
def criar_aluno():
 global aluno_id_control # Variável global
 data = request.get_json()
 data = request.get_json()
 print("Recebido do front-end:", data)

 new_aluno = Aluno(matricula=aluno_id_control, nome=data['nome'], email=data['email'], senha= data['senha'])
 try:
    conexao = conectar()
    with conexao:
        with conexao.cursor() as cursor:
            sql = "INSERT INTO aluno ( nome, email, matricula, senha) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (
                new_aluno.nome,
                new_aluno.email,
                new_aluno.matricula,
                new_aluno.senha
            ))
        conexao.commit()
 except Exception as e:
    print("Erro ao inserir no banco:", e)
    return jsonify({"message": "Erro ao salvar no banco de dados"}), 500

 aluno_id_control += 1
 alunos.append(new_aluno)
 print(alunos)
 return jsonify({"message": "Novo aluno criado com sucesso"})

# listar todos os alunos
@app.route('/Alunos', methods=['GET'])
def listar_alunos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM aluno")
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return jsonify(resultados)

# busca um aluno por matricula
@app.route('/Alunos/<string:matricula>', methods=['GET'])
def buscar_aluno_por_matricula(matricula):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM aluno WHERE matricula = %s"
    cursor.execute(sql, (matricula,))
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    if resultado:
        return jsonify(resultado)
    else:
        return jsonify({'erro': 'Aluno não encontrado'}), 404

# busca um aluno por nome
@app.route('/Alunos/nome/<string:nome>', methods=['GET'])
def buscar_aluno_nome(nome):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM aluno WHERE nome LIKE %s"
    like_param = f"%{nome}%"  # permite busca parcial
    cursor.execute(sql, (like_param,))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    if resultado:
        return jsonify(resultado)
    else:
        return jsonify({'erro': 'Aluno não encontrado'}), 404

if __name__ == "__main__":
    app.run(debug=True)
