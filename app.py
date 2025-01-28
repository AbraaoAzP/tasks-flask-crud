from flask import Flask

# Sempre que executarmos de forma manual, o __name__ == "__main__", com isso sabemos que ela não está sindo implantada ou importada por outro arquivo.
app = Flask(__name__)

# Criando uma rota:
@app.route("/") # ("/") -> Rota inicial.
# Criando o que será executado a partir da rota:
def hello_world():
    return "Hello, world!"

@app.route("/about")
def about():
    return "Página sobre."

# Faz uma verificação para garantir que só vai ser possível subir o servidor se estivermos fazendo de forma manual, visto que quando fazemos de forma manual, o __name__ recebe "__main__"
if __name__ == "__main__":
    # Para executar:
    # Esse modo de execução é usado somente durante o desenvolvimento.
    app.run(debug=True)
    # debug -> vai permitir visualizar informações que nos ajudarão a entender o que está acontecendo no servidor web.