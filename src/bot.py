from twilio.rest import Client
from telebot import types, TeleBot
import json
import time
import config


def botMessage(message, text, markup=False):
    if not markup:
        bot.send_message(chat_id=message.chat.id, text=text)
    else:
        markup = types.ForceReply(selective=False)
        bot.send_message(chat_id=message.chat.id,
                         text=text, reply_markup=markup)
    time.sleep(1)

def createJSON(message):
    chat_id = message.chat.id
    message_text = message.text

    with open('data.json', 'w') as f:
        data = {'{}'.format(chat_id):{'aula_nome':message_text}}
        json.dump(data, f)

def appendJSON(message, key, value):
    chat_id = message.chat.id
    json_data = {}
    with open('data.json', 'r+') as f:
        json_data = json.load(f)
    
    json_data[str(chat_id)][key] = value
    json_data.update(json_data)
    
    with open('data.json', 'w') as f:
        json.dump(json_data, f)

def parseJSON():
    NOME_DA_ULA = URL_TO_PLAY = ''
    with open('data.json', 'r+') as f:
        json_data = json.load(f)
        for keys in json_data:
            session = json_data[keys]
            NOME_DA_ULA = session['aula_nome']
            URL_TO_PLAY = session['aula_url']

    return NOME_DA_ULA, URL_TO_PLAY

def sendSMS(message, number):
    
    TWILIO_SID = config.credentials['TWILIO_SID']
    TWILIO_TOKEN  = config.credentials['TWILIO_TOKEN']
    TWILIO_NUMBER = '+17064938737'
    RECIPENT_NUMBER = '+5581997660099'
    SMS_MESSAGE = message

    client = Client(TWILIO_SID, TWILIO_TOKEN)

    message = client.messages.create(
        to=RECIPENT_NUMBER, 
        from_=TWILIO_NUMBER,
        body=SMS_MESSAGE)

TWILIO_NUMBER = '+17064938737'

TELEGRAM_TOKEN = config.credentials['TELEGRAM_TOKEN']
DOWNLOAD_URL = 'https://api.telegram.org/file/bot{}/'.format(TELEGRAM_TOKEN)
bot = TeleBot(TELEGRAM_TOKEN)

BOT_INTERACOES = {
    'start': 'Olá, eu sou a Duda! Tudo bem com você? Estou aqui para disponibilizar suas aulas com conteúdos programáticos para o enem aos seus alunos, tudo pelo telefone e gratuito 🤗',
    'start_2': 'Vamos lá?',
    
    'nome_aula': 'Digite, por favor, o nome da sua aula:',
    'nome_aula_reply': 'Muito bem! Agora seus alunos saberão do que se trata a sua aula.',
    'nome_aula_reply_2': 'Essa é a sua primeira aula que está inserida no seu primeiro plano de aula. Envie seu arquivo .mp3 para mim agora.',
    'nome_aula_reply_3': 'Caso você não tenha uma plataforma para gravar seu áudio, sugerimos essas abaixo:\nhttps://www.audacityteam.org/\nhttps://free-pc-audio-recorder.br.softonic.com/.',
    'nome_aula_reply_4': 'Está pronta para enviar o arquivo?',

    'envie_arquivo': 'Por favor faça o upload do arquivo:',
    'envie_arquivo_reply':'Que bom! A sua aula já está disponível no número de telefone {}.'.format(TWILIO_NUMBER),
    'envie_arquivo_reply_2':'lembrando que seus alunos podem ligar gratuitamente, não vão pagar nada por isso.',

    'envie_sms': 'Agora digite os números de telefone (Incluindo DDD) de seus alunos que você gostaria que fossem avisados por SMS sobre o código com o número em que sua aula está inserida.',
    'envie_sms_2': 'Digite 1 número por linha:',

    'envie_sms_reply': 'Pronto! O número de sua aula ja foi enviado para seus alunos, muito obrigado.',
    'envie_sms_reply_2': 'lembrando que seus alunos podem ouvir quantas aulas quiserem! e gratuitamente! Grande abraço, até a próxima aula.',

    'mp3_error':'Por favor, envie um audio no formato .mp3.'
}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print('[BOT] Bot has started.')
    chat_id = message.chat.id

    botMessage(message, BOT_INTERACOES['start'])
    botMessage(message, BOT_INTERACOES['start_2'])
    botMessage(message, BOT_INTERACOES['nome_aula'], True)


# Handles all sent documents and audio files
@bot.message_handler(content_types=['audio','voice'])
def handle_docs_audio(message):
    print('[BOT] Audio file was sent.')

    file_id = ''

    if message.audio:
        file_id = message.audio.file_id
    else:
        botMessage(message, BOT_INTERACOES['mp3_error'])
        botMessage(message, BOT_INTERACOES['envie_arquivo'], True)
        return

    audio_path = bot.get_file(file_id).file_path
    audio_download_url = DOWNLOAD_URL+audio_path

    appendJSON(message,'aula_url',audio_download_url)

    botMessage(message, BOT_INTERACOES['envie_arquivo_reply'])
    botMessage(message, BOT_INTERACOES['envie_arquivo_reply_2'])
    botMessage(message, BOT_INTERACOES['envie_sms'])
    botMessage(message, BOT_INTERACOES['envie_sms_2'], True)



@bot.message_handler(func=lambda message: True)
def echo_questions(message):
    context = message.reply_to_message.text

    # Nome da Aula
    if context == BOT_INTERACOES['nome_aula']:
        print("[BOT] Classe's name was sent.")
        botMessage(message, BOT_INTERACOES['nome_aula_reply'])
        botMessage(message, BOT_INTERACOES['nome_aula_reply_2'])
        botMessage(message, BOT_INTERACOES['nome_aula_reply_3'])
        botMessage(message, BOT_INTERACOES['nome_aula_reply_4'])

        createJSON(message)

        botMessage(message, BOT_INTERACOES['envie_arquivo'], True)

    if context == BOT_INTERACOES['envie_sms_2']:
        print('[BOT] SMS numbers were sent.')
        print('-----------------------------')
        sms_numbers = message.text.split('\n')
        nome_aula,_ = parseJSON()
        for number in sms_numbers:
            number = '+55{}'.format(number)
            message_value = 'Olá! A aula {} está dispónivel no número de telefone {}, basta ligar e estudar!'.format(nome_aula, TWILIO_NUMBER)
            sendSMS(message_value, number)

        botMessage(message, BOT_INTERACOES['envie_sms_reply'])
        botMessage(message, BOT_INTERACOES['envie_sms_reply_2'])

if __name__ == "__main__":
    print('[SERVER] Running...')
    bot.infinity_polling(True)