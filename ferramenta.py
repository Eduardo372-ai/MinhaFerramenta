# Biblioteca para Criar as Janelas
from tkinter import Tk

# Internet
import webbrowser as database1
import wikipedia as database2

# Biblioteca do Chat
import os

def CreateWindow(*args):
            janela = Tk()
            janela.geometry(*args)
            janela.mainloop()
def SystemPrint(*args):
            print(*args)
            
def OpenAI():
    database1.open('https://chat.openai.com/chat')
def SummaryAIOpenAI():
    database2.set_lang('pt')
    result = database2.summary('ChatGPT OpenAI', 2)
    print(result)

def GetResultWiki(*args):
    database2.set_lang('pt')
    wiki_result = database2.summary(*args, 2)
    print(wiki_result)
def NewChat():
    chat_server_file = "server.py"
    chat_client_file = "client.py"
    os.startfile(chat_server_file)
    os.startfile(chat_client_file)
# Descrição

# - SummaryAI(), Consegue as Informações da Maquina artificial: ChatGPT (OpenAI)

# - OpenAI(), Entra na Inteligencia Artificial ChatGPT (OpenAI)

# - SummaryAIOpenAI(), Busca pelo wikipedia por ChatGPT (OpenAI) ou Inteligencia atificial OpenAI

# - GetResultWiki(), Busca por Algo

# - SystemPrint(), Imprime algo.

# - CreateWindow(), Cria uma Janela com a Gemetricidade Fornecida Exemplo: "CreateWindow('200x200')"
