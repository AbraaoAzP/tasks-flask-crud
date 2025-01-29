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
    # Sempre que formos utilizar uma variável e vamos realizar uma iteração com ela dentro do método, teremos que usar o Global.
    data = request.get_json()
    # request: vai ser utilizado para recuperar as informações que precisam ser passadas.
    # get_json(): vai recuperar o que o cliente enviou.
    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", "")) # Foi definido um valor padrão de string vazia caso o usuário não passe a descrição.
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso!"})
    # vai retornar a mensagem no formato json, graças ao jsonify.

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    # Cria uma nova lista e dentro um for está sendo executado iterando sobre todos os elementos da lista task e retornando a cada iteração o task.to_dict().

    # for task in tasks:
    #     task_list.append(task.to_dict())
    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
        
    return jsonify({"message": "Não foi possível encontrar a atividade."}), 404

if __name__ == "__main__":
    app.run(debug=True)