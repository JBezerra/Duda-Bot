from flask import Flask, render_template, Response
from twilio.twiml.voice_response import Play, VoiceResponse
import json
import requests


def parseJson():
    NOME_DA_ULA = URL_TO_PLAY = ''
    with open('data.json', 'r+') as f:
        json_data = json.load(f)
        for keys in json_data:
            session = json_data[keys]
            NOME_DA_ULA = session['aula_nome']
            URL_TO_PLAY = session['aula_url']

    return NOME_DA_ULA, URL_TO_PLAY


app = Flask(__name__, template_folder='template', static_url_path='')


@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    NOME_DA_ULA, _ = parseJson()
    AUDIO_URL = 'http://827fe24f.ngrok.io/audio'

    response = VoiceResponse()
    response.say("A aula de {} será reproduzida em instantes.".format(
        NOME_DA_ULA), language='pt-BR')
    response.play(url=AUDIO_URL)

    response = response.to_xml()
    
    return response, 200, {'Content-Type': 'text/xml; charset=utf-8'}


@app.route('/audio', methods=['GET', 'POST'])
def home():
    _, URL_TO_PLAY = parseJson()
    r = requests.get(URL_TO_PLAY, stream=True)
    return Response(r.iter_content(chunk_size=1024), mimetype='audio/mpeg')
    

if __name__ == "__main__":
    app.run(debug=True)
