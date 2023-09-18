import json
import requests
from cred import func_api_key

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

def kelvin_para_celsius(kelvin):
    celsius = kelvin - 273.15
    return round(celsius,2)

def func_clima(cidade, pais):
    api_key = func_api_key()
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={cidade},{pais}&appid={api_key}"
    )
    data = response.json()
    print(f"""
    temperatura: {kelvin_para_celsius(data['main']['temp'])}
    temp_minima: {kelvin_para_celsius(data['main']['temp_min'])}
    temp_maxima: {kelvin_para_celsius(data['main']['temp_max'])}
    pressao: {kelvin_para_celsius(data['main']['pressure'])}
    humidade: {kelvin_para_celsius(data['main']['humidity'])}
    """)