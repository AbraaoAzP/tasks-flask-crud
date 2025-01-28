from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete.

tasks = [] 
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    # global vai permitir que a variável criada fora do escopo seja reconhecida.
    data = request.get_json()
    # request: vai ser utilizado para recuperar as informações que precisam ser passadas.
    # get_json(): vai recuperar o que o cliente enviou.
    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", "")) # Foi definido um valor padrão de string vazia caso o usuário não passe a descrição.
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso!"})
    # vai retornar a mensagem no formato json, graças ao jsonify.

if __name__ == "__main__":
    app.run(debug=True)