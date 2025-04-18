from flask import Flask, request, jsonify
from models.task import Aluno

app = Flask(__name__)

alunos = []
aluno_id_control = 1


# Criar uma nova tarefa
@app.route('/Alunos', methods=['POST'])
def create_aluno():
 global aluno_id_control # Variável global
 data = request.get_json()
 new_aluno = Aluno(id=aluno_id_control, nome=data['nome'],
 description=data.get("description", ""))
 aluno_id_control += 1
 alunos.append(new_aluno)
 print(alunos)
 return jsonify({"message": "Nova tarefa criada com sucesso"})

# listar todas as tarefas
@app.route('/Alunos', methods=['GET'])
def get_alunos():
 aluno_list = [aluno.to_dict() for aluno in alunos]
 output = {
 "alunos": aluno_list,
 "total_alunos": len(aluno_list)
 }
 return jsonify(output)

# Listar uma tarefa específica por id
@app.route('/Alunos/<int:id>', methods=['GET'])
def get_aluno(id):
    for t in alunos:
        if t.id == id:
            return jsonify(t.to_dict())
    
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404 

# Listar uma tarefa específica por title
@app.route('/Alunos/<string:nome>', methods=['GET'])
def get_nome(nome):
    for t in alunos:
        if t.nome == nome:
            return jsonify(t.to_dict())
    
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404 


# Editar Tarefa
@app.route('/Alunos/<int:id>', methods=["PUT"])
def update_task(id):
    aluno = None

    for t in alunos:
        if t.id == id:
            aluno = t

    if aluno == None:
        return jsonify({"message": "Não foi possível encontrar aatividade"}), 404
    data = request.get_json()
    aluno.nome = data['nome']
    aluno.description = data['description']
    aluno.completed = data['completed']

    return jsonify({"message": "Tarefa atualizada com sucesso"})
        


# Deletar tarefa
@app.route('/Alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
 aluno = None
 for t in alunos:
    if t.id == id:
     aluno = t
    break
 if not aluno:
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

 alunos.remove(aluno)
 return jsonify({"message": "Tarefa deletada com sucesso"})
   


if __name__ == "__main__":
    app.run(debug=True)
