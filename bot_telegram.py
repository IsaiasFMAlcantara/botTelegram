import telebot
from functions import func_cep
from functions import func_ip
from cred import mostra_token

bot = telebot.TeleBot(mostra_token())


@bot.message_handler(commands=['clima'])
def resposta_cep(mensagem):
    cidade = bot.send_message(mensagem.chat.id, 'INFORME SUA CIDADE: ')
    #informacoes = func_clima(fun_c())
    bot.send_message(mensagem.chat.id, dados)

@bot.message_handler(commands=['mylocation'])
def resposta_cep(mensagem):
    bot.send_message(mensagem.chat.id, 'Digite seu CEP:')
    def valida_cep(mensagem):
        vcep = func_cep(mensagem.text)
        cep_format = f'CEP: {vcep["cep"]}\nENDEREÇO: {vcep["address"]}\nESTADO: {vcep["state"]}\nBAIRRO: {vcep["district"]}\nCIDADE: {vcep["city"]}\nDDD: {vcep["ddd"]}\nCÓDIGO IBGE: {vcep["city_ibge"]}\nLATITUDE: {vcep["lat"]}\nLONGETUDE: {vcep["lng"]}'
        bot.send_message(mensagem.chat.id, cep_format)
        bot.send_message(mensagem.chat.id, 'Pressione /init\npara voltar pro menu')
    bot.register_next_step_handler(mensagem, valida_cep)

@bot.message_handler(commands=['myip'])
def resposta_ip(mensagem):
    texto_ip = func_ip()
    mensage_return = 'Pressione /init\npara voltar pro menu'
    bot.send_message(mensagem.chat.id, texto_ip)
    bot.send_message(mensagem.chat.id, mensage_return)
    

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def respostapadrao(mensagem):
    texto_menu = """
Segue o MENU do BOT
/mylocation
/myip
Escolha uma opção:
    """
    bot.send_message(mensagem.chat.id, texto_menu)

bot.polling()