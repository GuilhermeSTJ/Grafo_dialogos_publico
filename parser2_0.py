import json
import string
import random
from tkinter import *
from tkinter import filedialog

#Guarda o nome dos scripts
nome_scripts= []

#Salva os dados referentes a links
linkos = [""]

nome = "script03"
conteudo = "speak@Teste02@true@true\nwait@1000\nvoice@command@trigger_asr"

entrada = '{"input":"Entrada um"},{"input":"Entrada dois"},{"input":"Entrada três"}'
saida = '{"output":"Resposta um","actions":"","emotions":"","parameters":[]},{"output":"Resposta 02","actions":"script:Script1","emotions":"","parameters":[]},{"output":"Resposta 03","actions":"script:Script2","emotions":"","parameters":[]}'
context = '{"name":"no.answer"},{"name":"context:script:Script2"},{"name":"context:script:Script1"}'

def trataScript(data):
    conteudo = []
    data = data.split(";")
    text = ""

    #Laço que passa por todas linhas de script
    for d in data:
        value = []
        #Retira todos \n
        d = d.replace('\n', '')

        #aqui começamos com os casos
        if "@voice" in d:
            print(d.strip('@voice'))

        if "@wait" in d:
            print("")

        if "@voice" in d:
            print("")

    #envia uma lista contendo todos scripts
    return conteudo

def criaDialogo(dialog):

    uid = '4770ac69-6bc0-45a7-a7ad-8672382be7aa'

    dialogo = '{"id":"'+ uid +'","mode":"-","inputs":['+ entrada +'],"outputs":['+ saida +'],"requires":[],"concepts":['+ context +'],"entities":['+ context+']}'
    f = open(uid + ".json", "w")
    f.write(dialogo)
    f.close()

def criaScript(scri):

    nome = scri['key'].strip('\n')
    conteudo = trataScript(scri['text'])
    uid = "52f2bc85-228e-477f-a2c4-c163aa1e8059"
    apid = "ae37d798-c643-495c-a9fc-7a42ced9f458"

    #script = '{"uid":"' + uid + '","applicationUid":"'+ apid +'","name":"'+ nome +'","content":"' + conteudo +'"}'

    #f = open("Scripts/" + nome + ".json", "w",encoding="utf-8")
    #f.write(script)
    #f.close()

def open_file():

    filepath = "saida2.json"
    f = open(filepath,'r')
    k = 0
    data = json.load(f)

    #Salva os dados referentes a links
    for i in data['linkDataArray']:
        linkos.append(i)

    #remove todos links que encaixam em um 1 nó
    for l in linkos[:]:
       if len(l) == 1:
           linkos.remove(l)

    #Salva em uma lista o nome de todos scripts
    for i in data['nodeDataArray']:
        keys,values = zip(*i.items())
        if(values[0] == "Script"):
            nome_scripts.append(values[1])

    #Separa aqueles que são script e aqueles que são dialogo
    for j in data['nodeDataArray']:        
        keys,values = zip(*j.items())
        if(values[0] == "Script"):
            criaScript(j)
        if(values[0] == "Dialogo"):
            criaDialogo(j) 
    
    f.close()

#criaScript(nome,conteudo)
#criaDialogo(entrada,saida,context)
open_file()

