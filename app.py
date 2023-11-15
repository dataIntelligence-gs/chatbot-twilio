from database_module import create_records_from_file, update_initial_message_received, update_location_selection, update_usage_interest, get_all_records, get_number_of_records_by_filter, filter_by_column
from twilio.base.exceptions import TwilioRestException
from flask import Flask, request, jsonify
from twilio.rest import Client
from dotenv import load_dotenv
from waitress import serve
import datetime as dt
import os
import time
import random
import json
#from front import *
import datetime as dt


load_dotenv()

app = Flask(__name__)

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client()

pool_number = ['numbers']

eleccion = None

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

        pool_sales_mendoza = ['number']
        pool_sales_cordoba = ['number']
        pool_sales_general = ['number']
        
        if incoming_msg == "contactar con asesor":
        
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']
            client = Client(account_sid, auth_token)
            a = random.choices(pool_sales_mendoza)

            client.messages.create(
                                from_=to,
                                body=f"¡Hola! El número {number} de {name} desea más información. Por favor, contactar a la brevedad, presionando el siguiente link https://wa.me/{number}. ¡Saludos!",
                                to='whatsapp:+54'+a[0]
            )
            update_usage_interest(str(number), str(incoming_msg))
            with open(f"conversations_interesed/interesados/{str(number)}.txt", "a", encoding='utf-8') as f:
                f.write(f"{str(name)}: {str(incoming_msg)} - {str(now_time)}"+'\n')
        
        else:
            update_initial_message_received(str(number), str(incoming_msg))
            with open(f"conversations_interesed/{str(number)}.txt", "a", encoding='utf-8') as f:
                f.write(f"{str(name)}: {str(incoming_msg)} - {str(now_time)}"+'\n')
            
        print(f'Mensaje: {incoming_msg}, nombre: {name}, hora: {now_time}')

        return str('Done')
    except TwilioRestException as twilio_error:
        if twilio_error.status == 404 and 'No valid template found' in twilio_error.msg:
            print(f'Plantilla dada de baja - detalles:{twilio_error}')
            
        else:
            print(f'Error al momento de enviar mensaje - Detalles: TwilioRestException - {twilio_error}')

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
                                body="insert_template",
                                to='whatsapp:+54'+number,
            )
            time.sleep(random.randint(18, 20))

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

@app.route('/get-column-data', methods=['GET'])
def get_column_data():
    column = request.json.get('column')

    if column == None:
        return jsonify({'error': 'Missing column'})
    
    return jsonify(filter_by_column(column))

@app.route('/twilio-errors', methods=['POST'])
def twilio_errors():
    try:
        data = request.form

        parent_account_sid = data.get('ParentAccountSid')
        payload = data.get('Payload')
        level = data.get('Level')
        timestamp = data.get('Timestamp')
        payload_type = data.get('PayloadType')
        account_sid = data.get('AccountSid')
        sid = data.get('Sid')

        payload_dict = json.loads(payload)

        response_data = {
            #'ParentAccountSid': parent_account_sid,
            'Payload': payload_dict['more_info'],
            'Level': level,
            'Timestamp': timestamp,
            'PayloadType': payload_type,
            # 'AccountSid': account_sid,
            # 'Sid': sid
        }

        print(response_data)
        return jsonify(response_data)

    except Exception as e:
        print(f'Error general en la funcion twilio_errors - Detalles: {e}')
    

if __name__ == '__main__':
    from waitress import serve
    serve(app, port=5000)
