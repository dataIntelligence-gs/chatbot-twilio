import subprocess
from database_module import create_records_from_file, update_initial_message_received, update_location_selection, update_usage_interest, get_all_records, get_number_of_records_by_filter
from twilio.base.exceptions import TwilioRestException
from flask import Flask, request, jsonify
from twilio.rest import Client
from dotenv import load_dotenv
from waitress import serve
import datetime as dt
import os
import time
import random
from front import *
import datetime as dt
from apscheduler.schedulers.background import BackgroundScheduler
import streamlit as st


load_dotenv()

app = Flask(__name__)

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client()
pool_number = ['2604516691', '2604417534', '2604417531', '2604417524', '2604417522']
eleccion = None

def actualizar_informe():

    subprocess.Popen(['streamlit', 'run', 'front.py'])

    hora = dt.datetime.now()
    print(f'Informe Actualizado a las {hora.hour}:{hora.minute}')

scheduler = BackgroundScheduler()
scheduler.add_job(actualizar_informe, 'cron', hour=9, minute=39)  # Cambia la hora a la que deseas que se ejecute
scheduler.start()

@app.route('/bot', methods=['POST'])
def bot():
    try:
        global eleccion
        to = request.values.get('To')
        incoming_msg = request.values.get('Body').lower()
        person = request.values.get('From').lower()
        number = person.split(':+549')[1]
        name = request.values.get('ProfileName').lower()
        now_time = dt.datetime.now()

        pool_sales_mendoza = ['2942693075']
        pool_sales_cordoba = ['2942693075']
        pool_sales_general = ['2942693075']
        
        if incoming_msg == 'en otro momento':
            update_initial_message_received(str(number), str(incoming_msg))
            account_sid = 'ACce7b9301a1718047284a251f66781145'
            auth_token = '9eea91c9d052bfbc81cc3a1a672186ae'
            client = Client(account_sid, auth_token)
            client.messages.create(
                                from_=to,
                                body='Desde EVI desarrollos agradecemos tu tiempo. Te compartimos nuestro sitio web, cualquier consulta no dudes en escribirnos. \n\n*EVI DESARROLLOS*',
                                to='whatsapp:+54'+number
                            )
            time.sleep(random.randint(10, 15))

        elif incoming_msg == "si, me encantaria":
            update_initial_message_received(str(number), str(incoming_msg))
            account_sid = 'ACce7b9301a1718047284a251f66781145'
            auth_token = '9eea91c9d052bfbc81cc3a1a672186ae'
            client = Client(account_sid, auth_token)
            client.messages.create(
                                from_=to,
                                body="*QUE BUENO QUE SIGAMOS CONVERSANDO* 😁 \n\nTodos nuestros proyectos cuentan con: \n\n- Financiación propia. \n- Cuotas fijas. \n\nHoy tenemos para ofrecerte dos opciones irresistibles: \n\n- *Córdoba* donde descubrirás la belleza natural propia de las sierras 🏞️ \n- *Mendoza* donde te sumergirás en la magia de los Andes y sus viñedos 🏔️ \n\n¿Sobre qué lugar te gustaría recibir más información?",
                                to='whatsapp:+54'+number
            )

        elif incoming_msg == "córdoba" or incoming_msg == "mendoza" or incoming_msg == "me interesan ambos":
            update_location_selection(str(number), str(incoming_msg))
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
            update_usage_interest(str(number), str(incoming_msg))
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
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']
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
    except TwilioRestException as twilio_error:
        if twilio_error.status == 404 and 'No valid template found' in e.msg:
            print(f'Plantilla dada de baja - detalles:{e}')
            
        else:
            print(f'Error al momento de enviar mensaje - Detalles: TwilioRestException - {e}')

    except Exception as e:
        print(f'Error general en la funcion bot - Detalles: {e}')

@app.route('/send/campaign1', methods=['POST'])
def send():
    create_records_from_file('clients_1.txt')
    with open("clients_1.txt", "r") as f:
        number_list = f.readlines()

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    for number in number_list:
        try:
            print(number)
            a = random.choice(pool_number)
            message = client.messages.create(
                                from_='whatsapp:+549'+a,
                                body="Hola me comunico desde Evi Desarrollos para informarles los precios de nuestros lotes",
                                to='whatsapp:+54'+number,
            )
            time.sleep(random.randint(10, 15))

            print(message.sid)
        
        except TwilioRestException as twilio_error:
            if twilio_error.status == 404 and 'No valid template found' in twilio_error.msg:
                print(f'Plantilla de saludo de bot dada de baja - detalles: {twilio_error}')
                continue
            else:
                print(f'Error al momento de enviar mensaje - Detalles: TwilioRestException - {twilio_error}')
                continue

        except Exception as e:
            print(f'Error general en la funcion send - Detalles: {e}')
            continue
        
    return str('Done')

@app.route('/get-all-data', methods=['GET'])
def get_all_data():
    return jsonify(get_all_records())

@app.route('/get-filter-data', methods=['GET'])
def get_filter_data():
    value = request.json.get('value')
    column = request.json.get('column')

    if value == None or column == None:
        return jsonify({'error': 'Missing value or column'})
    
    return jsonify(get_number_of_records_by_filter(value, column))
    

if __name__ == '__main__':
    from waitress import serve
    serve(app, port=5000)
