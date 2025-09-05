import pickle
import os

ARQUIVO_MEMORIA = "./project_1_chatbot/bot_memory/chatbot_memory.txt"

# Function to load memory from file
def load_memory():
    """Carrega a memória do chatbot a partir de um arquivo."""

    if os.path.exists(ARQUIVO_MEMORIA):
        try:
            with open(ARQUIVO_MEMORIA, 'rb') as f:
                # The line `return pickle.load(f)` is loading the data stored in the file `f` using
                # the `pickle` module in Python. `pickle.load()` is used to deserialize a data stream
                # stored in a file object and reconstruct the original Python object that was stored
                # in that file.
                return pickle.load(f)
        except Exception as e:
            return {}
    return {}

def save_memory(memory):
    """Salva a memória do chatbot em um arquivo."""
    with open(ARQUIVO_MEMORIA, 'wb') as f:
        # `pickle.dump(memory, f)` is a line of code that is used to serialize the `memory` data
        # (Python object) and write it to the file object `f` using the `pickle` module in Python.
        pickle.dump(memory, f)
        

memoria = load_memory()

print("Chatbot - Aprende e Responde (digite 'sair' para encerrar)\n")
print("Digite 'apagar' para limpar a memória.\n")
print("Digite 'listar para ver todas as respostas aprendidas. \n")

while True:
    
    entrada = input("Você: ").strip().lower()

    if entrada == "sair":
        print("Encerrando o chatbot. Até mais!")
        break

    if entrada == "apagar":
        memoria.clear()
        print("Memória apagada.")
        continue

    if entrada == "listar":
        if memoria:
            print("Respostas aprendidas:")
            for pergunta in memoria.keys():
                print(f"- {pergunta}")
            print()
        else:
            print("Bot: Nenhuma resposta aprendida ainda.\n")
        continue

    if entrada in memoria:
        print("Bot:", memoria[entrada])

    else:
        print("Bot: Não sei responder isso.")
        if resposta := input("Me ensine: ").strip():
            memoria[entrada] = resposta
            save_memory(memoria)
            print("Obrigado! Aprendi algo novo.\n")        