import psycopg2
import json
import requests
from cred import CredencialDW
from datetime import datetime


# FUNÇÃO DE API QUE BUSCA O SEU CEP
def func_cep(cep):
    vcep = str(cep)
    cep = vcep.replace("-", "").replace(".", "").replace(" ", "")
    url = f"https://cep.awesomeapi.com.br/json/{cep}"
    response = requests.get(url)
    dict_json = json.loads(response.text)
    return dict_json

# FUNÇÃO DE API QUE BUSCA O ATUAL IP DA SUA REDE
def func_ip():
    response = requests.get('https://api.ipify.org?format=json')
    if response.status_code == 200:
        dados = json.loads(response.content)
        response2 = requests.get(f"https://ipinfo.io/{dados['ip']}/geo")
        if response2.status_code == 200:
            data = json.loads(response2.content)
            return f"ip: {data['ip']}\nhostname: {data['hostname']}\ncity: {data['city']}\nregion: {data['region']}\ncountry: {data['country']}\nloc: {data['loc']}\norg: {data['org']}\npostal: {data['postal']}\ntimezone: {data['timezone']}"
        else:
            return f'conexao nao estabelecidad {response2.status_code}'
    else:
        return f'conexao nao estabelecidad {response.status_code}'
