import telebot
from functions import func_cep
from functions import func_ip
from conectores import mostra_token

bot = telebot.TeleBot(mostra_token())

@bot.message_handler(commands=['relatoriopdf'])
def resposta_pdf(mensagem):
    file_path = 'teste.pdf'
    with open(file_path, 'rb') as pdf_file:
        bot.send_document(mensagem.chat.id, pdf_file)

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
/relatoriopdf
Escolha uma opção:
    """
    bot.send_message(mensagem.chat.id, texto_menu)

bot.polling()
