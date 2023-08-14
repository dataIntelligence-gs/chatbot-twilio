from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from twilio.rest import Client
from dotenv import load_dotenv
from datetime import datetime
from waitress import serve
import requests
import os
import datetime as dt
import ast 
import time
import random
import os


load_dotenv()

app = Flask(__name__)

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client()
pool_number = ['3518725311', '3518725310', '3518725309', '1178983221', '1178981923']
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

    pool_sales_mendoza = ['2604406536']
    pool_sales_cordoba = ['3547500771']
    pool_sales_general = ['2604406536', '3547500771']
    
    if incoming_msg == 'en otro momento':
        account_sid = 'ACce7b9301a1718047284a251f66781145'
        auth_token = '9eea91c9d052bfbc81cc3a1a672186ae'
        client = Client(account_sid, auth_token)
        client.messages.create(
                            from_=to,
                            body='Desde EVI desarrollos agradecemos tu tiempo. Te compartimos nuestro sitio web, cualquier consulta no dudes en escribirnos. \n\n*EVI DESARROLLOS*',
                            to='whatsapp:+54'+number
                        )
        time.sleep(random.randint(10, 15))

    elif incoming_msg == "sí, me encantaría":
        account_sid = 'ACce7b9301a1718047284a251f66781145'
        auth_token = '9eea91c9d052bfbc81cc3a1a672186ae'
        client = Client(account_sid, auth_token)
        client.messages.create(
                            from_=to,
                            body="*QUE BUENO QUE SIGAMOS CONVERSANDO* 😁 \n\nTodos nuestros proyectos cuentan con: \n\n- Financiación propia. \n- Cuotas fijas. \n\nHoy tenemos para ofrecerte dos opciones irresistibles: \n\n- *Córdoba* donde descubrirás la belleza natural propia de las sierras 🏞️ \n- *Mendoza* donde te sumergirás en la magia de los Andes y sus viñedos 🏔️ \n\n¿Sobre qué lugar te gustaría recibir más información?",
                            to='whatsapp:+54'+number
        )

    elif incoming_msg == "córdoba" or incoming_msg == "mendoza" or incoming_msg == "me interesan ambos":
        account_sid = 'ACce7b9301a1718047284a251f66781145'
        auth_token = '9eea91c9d052bfbc81cc3a1a672186ae'
        client = Client(account_sid, auth_token)
        client.messages.create(
                            from_=to,
                            body="Excelente elección, antes de derivarte con un especialista, te voy a hacer una última pregunta. \n\n¿Qué opción te interesa?",
                            to='whatsapp:+54'+number
        )
        eleccion = incoming_msg
    
    elif incoming_msg == "uso turístico" or incoming_msg == "uso residencial" or incoming_msg == "inversión":
        account_sid = 'ACce7b9301a1718047284a251f66781145'
        auth_token = '9eea91c9d052bfbc81cc3a1a672186ae'
        client = Client(account_sid, auth_token)
        
        if now_time.hour >= 9 and now_time.hour <= 17:
            if eleccion == "mendoza":
                a = random.choices(pool_sales_mendoza)
                client.messages.create(
                            from_=to,
                            body=f"¡Hola! El número {number} de {name} eligió la opción {incoming_msg} de {eleccion}, por lo que desea más información. Por favor, contactar a la brevedad, presionando el siguiente link https://wa.me/{number}. ¡Saludos!",
                            to='whatsapp:+54'+a[0]
                        )

                client.messages.create(
                                    from_=to,
                                    body="¡Genial! 😁 Un asesor de EVI Desarrollos se pondrá en contacto con vos muy pronto para darte toda la información que necesitas para dar el siguiente paso hacia tu nuevo lugar en el mundo. \n\nMientras aguardas la comunicación te comparto nuestro sitio web.",
                                    to='whatsapp:+54'+number
                )
        
            elif eleccion == "córdoba":
                a = random.choices(pool_sales_cordoba)
                client.messages.create(
                            from_=to,
                            body=f"¡Hola! El número {number} de {name} eligió la opción {incoming_msg} de {eleccion}, por lo que desea más información. Por favor, contactar a la brevedad, presionando el siguiente link https://wa.me/{number}. ¡Saludos!",
                            to='whatsapp:+54'+a[0]
                        )

                client.messages.create(
                                    from_=to,
                                    body="¡Genial! 😁 Un asesor de EVI Desarrollos se pondrá en contacto con vos muy pronto para darte toda la información que necesitas para dar el siguiente paso hacia tu nuevo lugar en el mundo. \n\nMientras aguardas la comunicación te comparto nuestro sitio web.",
                                    to='whatsapp:+54'+number
                )
            
            elif eleccion == "me interesan ambos":
                a = random.choices(pool_sales_general)
                client.messages.create(
                            from_=to,
                            body=f"¡Hola! El número {number} de {name} eligió la opción {incoming_msg} de {eleccion}, por lo que desea más información. Por favor, contactar a la brevedad, presionando el siguiente link https://wa.me/{number}. ¡Saludos!",
                            to='whatsapp:+54'+a[0]
                        )

                client.messages.create(
                                    from_=to,
                                    body="¡Genial! 😁 Un asesor de EVI Desarrollos se pondrá en contacto con vos muy pronto para darte toda la información que necesitas para dar el siguiente paso hacia tu nuevo lugar en el mundo. \n\nMientras aguardas la comunicación te comparto nuestro sitio web.",
                                    to='whatsapp:+54'+number
                )
        else:
            client.messages.create(
                            from_=to,
                            body="¡Disculpa! Todos nuestros asesores se encuentran fuera de horario laboral. Mañana durante el transcurso de la mañana serás contactado. ¡Muchas gracias por tu tiempo!",
                            to='whatsapp:+54'+number
                        )
            
            with open(f'offline.txt', 'a', encoding='utf-8') as file:
                file.write(f'Número: {str(number)}, Nombre: {str(name)}\n')
        
    elif incoming_msg == "ir con asistente":
        a = random.choices(pool_sales_general)
        client.messages.create(
                    from_=to,
                    body=f"¡Hola! El número {number} de {name} eligió la opción {incoming_msg} de {eleccion}, por lo que desea más información. Por favor, contactar a la brevedad, presionando el siguiente link https://wa.me/{number}. ¡Saludos!",
                    to='whatsapp:+54'+a[0]
                )

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

    with open(f"conversations_interesed/{str(number)}.txt", "a", encoding='utf-8') as f:
        f.write(f"{str(name)}: {str(incoming_msg)} - {str(now_time)}"+'\n')

    return str('Done')

@app.route('/send/campaign1', methods=['POST'])
def send():
    with open("clients_1.txt", "r") as f:
        number_list = f.readlines()

    account_sid = 'ACce7b9301a1718047284a251f66781145'
    auth_token = '9eea91c9d052bfbc81cc3a1a672186ae'
    client = Client(account_sid, auth_token)

    for number in number_list:
        try:
            print(number)
            a = random.choice(pool_number)
            message = client.messages.create(
                                from_='whatsapp:+549'+a,
                                body="Hola! 👋 ¿Cómo estás? \n\nMi nombre es Lautaro 👦🏻, Asesor comercial de Evi Desarrollos, empresa líder en el mercado inmobiliario dedicada a hacer realidad el sueño de tener tu propio lote. \n\n¿Querés conocernos un poco más?",
                                to='whatsapp:+54'+number,
            )
            time.sleep(random.randint(10, 15))

            print(message.sid)
        except Exception as e:
            print(f'Ocurrio un error en la funcion send - Detalles: {e}')
            continue
        
    return str('Done')

if __name__ == '__main__':
    from waitress import serve
    serve(app, port=5000)
