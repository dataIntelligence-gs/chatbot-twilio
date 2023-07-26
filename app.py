from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import os
from twilio.rest import Client
from dotenv import load_dotenv
from waitress import serve
from datetime import datetime
import datetime as dt

load_dotenv()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

app = Flask(__name__)
client = Client()
pool_number = ['3518725311']

@app.route('/bot', methods=['POST'])
def bot():
    to = request.values.get('To')
    incoming_msg = request.values.get('Body').lower()
    person = request.values.get('From').lower()
    number = person.split(':+549')[1]
    name = request.values.get('ProfileName').lower()
    now_time = dt.datetime.now()

    pool_sales_morning = ['3547589941']
    pool_sales_afternoon = ['3547589941']
        
    if incoming_msg == 'no me interesa' or incoming_msg == 'no' or incoming_msg == 'no, muchas gracias':
        account_sid = 'ACce7b9301a1718047284a251f66781145'
        auth_token = '9eea91c9d052bfbc81cc3a1a672186ae'
        client = Client(account_sid, auth_token)
        #gret = random.choice(grettings)
        client.messages.create(
                            from_=to,
                            body='Desde Evi Desarrollos agradecemos tu tiempo. Te compartimos nuestro sitio web, cualquier consulta no dudes en escribirnos.\n_EVI DESARROLLOS_',
                            to='whatsapp:+54'+number
                        )
        time.sleep(random.randint(1, 10))

    elif incoming_msg == "mendoza" or incoming_msg == "córdoba" or incoming_msg == "cordoba" or incoming_msg == "ir con asistente":
        account_sid = 'ACce7b9301a1718047284a251f66781145'
        auth_token = '9eea91c9d052bfbc81cc3a1a672186ae'
        client = Client(account_sid, auth_token)
        if now_time.hour >= 8 and now_time.hour < 15:
            a = random.choices(pool_sales_morning)
            client.messages.create(
                            from_=to,
                            body=f"¡Hola! El número {number} de {name} eligió la opción {incoming_msg}, por lo que desea más información. Por favor, contactar a la brevedad, presionando el siguiente link https://wa.me/+549{number}. ¡Saludos!",
                            to='whatsapp:+54'+a[0]
                        )
            client.messages.create(
                            from_=to,
                            body="¡Excelente elección! 😄 Un asesor de Evi Desarrollos se pondrá en contacto con vos muy pronto para darte toda la información que necesitas para dar el siguiente paso hacia tu nuevo lugar en el mundo.",
                            to='whatsapp:+54'+number
                        )
        if now_time.hour >= 15 and now_time.hour < 21:
            a = random.choices(pool_sales_afternoon)
            client.messages.create(
                            from_=to,
                            body=f"¡Hola! El número {number} de {name} eligió la opción {incoming_msg}, por lo que desea más información. Por favor, contactar a la brevedad, presionando el siguiente link https://wa.me/+549{number}. ¡Saludos!",
                            to='whatsapp:+54'+a[0]
                        )
            client.messages.create(
                            from_=to,
                            body="¡Excelente elección! 😄 Un asesor de Evi Desarrollos se pondrá en contacto con vos muy pronto para darte toda la información que necesitas para dar el siguiente paso hacia tu nuevo lugar en el mundo.",
                            to='whatsapp:+54'+number
                        )
        else:
            client.messages.create(
                            from_=to,
                            body="¡Disculpa! Todos nuestros asesores se encuentran fuera de horario laboral. Mañana durante el transcurso de la mañana serás contactado. ¡Muchas gracias por tu tiempo!",
                            to='whatsapp:+54'+number
                        )
            file = open(f'offline.txt', 'a', encoding='utf-8')
            file.write(f'Número: {str(number)}, Nombre: {str(name)}\n')
            file.close()

    else:
        account_sid = 'ACce7b9301a1718047284a251f66781145'
        auth_token = '9eea91c9d052bfbc81cc3a1a672186ae'
        client = Client(account_sid, auth_token)
        client.messages.create(
                            from_=to,
                            body="El mensaje no pudo ser interpretado por nuestro asistente virtual. Te pido por favor que selecciones una de las alternativas disponibles o ingreses *IR CON ASISTENTE* para que uno de nuestros agentes pueda colaborarte en lo que necesites. Muchas gracias por tu tiempo.",
                            to='whatsapp:+54'+number
                        )
    
    print(incoming_msg, person, name)
    f = open(f"conversations_interesed/{str(number)}.txt", "a", encoding='utf-8')
    f.write(f"{str(name)}: {str(incoming_msg)}"+'\n')
    f.close()
    return str('Done')
    
import ast 
import time
import random

@app.route('/send/campaign1', methods=['POST'])
def send():
    number_list = []
    f = open("clients_1.txt", "r")
    lines = f.readlines()
    number_list = lines
    # Download the helper library from https://www.twilio.com/docs/python/install
    import os
    from twilio.rest import Client
    # print(number_list)
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = 'ACce7b9301a1718047284a251f66781145'
    auth_token = '9eea91c9d052bfbc81cc3a1a672186ae'
    client = Client(account_sid, auth_token)

    for number in number_list:
        try:
            print(number)
            a = random.choice(pool_number)
            message = client.messages.create(

                                from_='whatsapp:+549'+a,
                                body="Hola! 👋 ¿Cómo estás? \nMi nombre es Matias 👦🏻, Asistente Virtual de EVI DESARROLLOS, empresa líder en el mercado inmobiliario dedicada a hacer realidad el sueño de tener tu propio lote. \n\n• Financiación propia. \n• Cuotas fijas. \n• Loteos turísticos y residenciales.\n\nHoy tenemos para ofrecerte dos opciones irresistibles:\n\n1️⃣ Córdoba dónde descubrirás la belleza natural propia de las sierras cordobesas. 🏞️\n2️⃣ Mendoza dónde te sumergirás en la magia de los Andes y sus viñedos. 🏔️\n¿Sobre qué lugar te gustaría recibir más información?",
                                to='whatsapp:+54'+number

                            )
            #
            time.sleep(random.randint(5, 10))
    
            print(message.sid)
        except:
            continue
        
    return str('Done')

if __name__ == '__main__':
    #app.run()
    from waitress import serve
    serve(app, port=5000)

