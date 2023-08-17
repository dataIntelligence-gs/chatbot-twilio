import sqlite3


def create_db():
    conn = sqlite3.connect('chatbot_database.db')  # Cambia el nombre del archivo según tus preferencias

    # Crear la tabla si no existe
    conn.execute('''
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone_number TEXT,
            initial_message TEXT,
            location_selection TEXT,
            usage_interest TEXT
        );
    ''')

    conn.close()

def create_records_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        phone_number = line.strip()  # Elimina saltos de línea y espacios
        create_record(phone_number)

def create_record(phone_number):
    try:
        conn = sqlite3.connect('chatbot_database.db')
        query = '''
            INSERT INTO interactions (phone_number, initial_message, location_selection, usage_interest)
            VALUES (?, ?, ?, ?)
        '''
        conn.execute(query, (phone_number, None, None, None))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f'Error en create_record - Detalles: {e}')

# Función para actualizar el campo 'initial_message_received'
def update_initial_message_received(phone_number, initial_message):
    try:
        conn = sqlite3.connect('chatbot_database.db')
        query = '''
            UPDATE interactions
            SET initial_message = ?
            WHERE phone_number = ?
        '''
        conn.execute(query, (initial_message, phone_number))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f'Error en update_initial_message_received - Detalles: {e}')

# Función para actualizar el campo 'location_selection'
def update_location_selection(phone_number, location):
    try:
        conn = sqlite3.connect('chatbot_database.db')
        query = '''
            UPDATE interactions
            SET location_selection = ?
            WHERE phone_number = ?
        '''
        conn.execute(query, (location, phone_number))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f'Error en update_location_selection - Detalles: {e}')

# Función para actualizar el campo 'usage_interest'
def update_usage_interest(phone_number, usage):
    try:
        conn = sqlite3.connect('chatbot_database.db')
        query = '''
            UPDATE interactions
            SET usage_interest = ?
            WHERE phone_number = ?
        '''
        conn.execute(query, (usage, phone_number))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f'Error en update_usage_interest - Detalles: {e}')

if __name__ == '__main__':
    create_db()
    create_records_from_file('clients.txt')
    update_initial_message_received('2942693075', 'si, me encantaria')
    update_location_selection('2942693075', 'mendoza')
    update_usage_interest('2942693075', 'turistico')