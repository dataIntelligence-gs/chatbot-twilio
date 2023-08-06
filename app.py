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
eleccion = None

@app.route('/bot', methods=['POST'])
def bot():
    global eleccion
    to = request.values.get('To')
    incoming_msg = request.values.get('Body').lower()
    person = request.values.get('From').lower()
    number = person.split(':+549')[1]
    name = request.values.get('ProfileName').lower()
    now_time = dt.datetime.now()

    pool_sales_morning = ['2604017664']#['3547589941']
    pool_sales_afternoon = ['2604017664']#['3547589941']
    
        
    if incoming_msg == 'en otro momento':
        account_sid = 'ACce7b9301a1718047284a251f66781145'
        auth_token = '9eea91c9d052bfbc81cc3a1a672186ae'
        client = Client(account_sid, auth_token)
        #gret = random.choice(grettings)
        client.messages.create(
                            from_=to,
                            body='Desde EVI desarrollos agradecemos tu tiempo. Te compartimos nuestro sitio web, cualquier consulta no dudes en escribirnos. \n\n*EVI DESARROLLOS*',
                            to='whatsapp:+54'+number
                        )
        time.sleep(random.randint(1, 10))

    elif incoming_msg == "si, me encantaria":
        account_sid = 'ACce7b9301a1718047284a251f66781145'
        auth_token = '9eea91c9d052bfbc81cc3a1a672186ae'
        client = Client(account_sid, auth_token)
        client.messages.create(
                            from_=to,
                            body="*QUE BUENO QUE SIGAMOS CONVERSANDO* 😁 \n\nTodos nuestros proyectos cuentan con: \n\n- Financiación propia \n- Cuotas fijas \n\nHoy tenemos para ofrecerte dos opciones irresistibles: \n\n- *Córdoba* dónde descubrirás la belleza natural propia de las sierras 🏞️ \n- *Mendoza* dónde te sumergirás en la magia de los Andes y sus viñedos 🏔️ \n\n¿Sobre qué lugar te gustaría recibir más información?",
                            to='whatsapp:+54'+number
        )

    elif incoming_msg == "cordoba" or incoming_msg == "mendoza" or incoming_msg == "me interesan ambos":
        account_sid = 'ACce7b9301a1718047284a251f66781145'
        auth_token = '9eea91c9d052bfbc81cc3a1a672186ae'
        client = Client(account_sid, auth_token)
        client.messages.create(
                            from_=to,
                            body="Excelente elección, antes de derivarte con un especialista, te voy a hacer una ultima pregunta. \n\n¿Qué opción te interesa?",
                            to='whatsapp:+54'+number
        )
        eleccion = incoming_msg
    
    elif incoming_msg == "uso turistico" or incoming_msg == "uso residencial" or incoming_msg == "inversion":
        account_sid = 'ACce7b9301a1718047284a251f66781145'
        auth_token = '9eea91c9d052bfbc81cc3a1a672186ae'
        client = Client(account_sid, auth_token)
        
        if now_time.hour >= 8 and now_time.hour < 15:
            a = random.choices(pool_sales_morning)
            client.messages.create(
                        from_=to,
                        body=f"¡Hola! El número {number} de {name} eligió la opción {incoming_msg} de {eleccion}, por lo que desea más información. Por favor, contactar a la brevedad, presionando el siguiente link https://wa.me/{number}. ¡Saludos!",
                        to='whatsapp:+54'+a[0]
                    )

            client.messages.create(
                                from_=to,
                                body="¡Excelente! 😁 Un asesor de EVI Desarrollos se pondrá en contacto con vos muy pronto para darte toda la información que necesitas para dar el siguiente paso hacia tu nuevo lugar en el mundo. \n\nMientras aguardas la comunicación te comparto nuestro sitio web",
                                to='whatsapp:+54'+number
            )
        if now_time.hour >=15 and now_time.hour < 21:
            a = random.choices(pool_sales_afternoon)
            client.messages.create(
                        from_=to,
                        body=f"¡Hola! El número {number} de {name} eligió la opción {incoming_msg} de {eleccion}, por lo que desea más información. Por favor, contactar a la brevedad, presionando el siguiente link https://wa.me/{number}. ¡Saludos!",
                        to='whatsapp:+54'+a[0]
                    )

            client.messages.create(
                                from_=to,
                                body="¡Excelente! 😁 Un asesor de EVI Desarrollos se pondrá en contacto con vos muy pronto para darte toda la información que necesitas para dar el siguiente paso hacia tu nuevo lugar en el mundo. \n\nMientras aguardas la comunicación te comparto nuestro sitio web",
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
            # message = client.messages.create(
            #                     from_='whatsapp:+549'+a,
            #                     media_url=['https://evidesarrollos.com/wp-content/uploads/2022/10/10-2.jpg'],
            #                     to='whatsapp:+54'+number,
            # )
            # time.sleep(random.randint(3, 6))
            message = client.messages.create(

                                from_='whatsapp:+549'+a,
                                body="Hola! 👋 ¿Cómo estás? \n\nMi nombre es Tobías 👦🏻, Asistente Virtual de EVI DESARROLLOS, empresa líder en el mercado inmobiliario dedicada a hacer realidad el sueño de tener tu propio lote \n\n¿Queres conocernos un poco mas?",
                                to='whatsapp:+54'+number,

                                

                            )
            #
            time.sleep(random.randint(5, 10))
    
            print(message.sid)
        except:
            continue
        
    return str('Done')

if __name__ == '__main__':
    # app.run()
    from waitress import serve
    serve(app, port=5000)

