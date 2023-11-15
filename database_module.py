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
        phone_number = line.strip()
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

# Función para actualizar el campo 'initial_message'
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

def get_all_records():
    try:
        conn = sqlite3.connect('chatbot_database.db')
        query = 'SELECT * FROM interactions'
        result = conn.execute(query).fetchall()
        conn.close()
        return result
    except Exception as e:
        print(f'Error en get_all_records - Detalles: {e}')

def filter_by_value_and_column(value, column):
    try:
        conn = sqlite3.connect('chatbot_database.db')
        query = f'SELECT * FROM interactions WHERE {column} = ?'
        result = conn.execute(query, (value,)).fetchall()
        conn.close()
        return result
    except Exception as e:
        print(f'Error en filter_by_value_and_column - Detalles: {e}')

def filter_by_column(column):
    try:
        conn = sqlite3.connect('chatbot_database.db')
        query = f'SELECT COUNT({column}) FROM interactions WHERE {column} IS NOT NULL'
        result = conn.execute(query).fetchall()
        conn.close()
        return result
    except Exception as e:
        print(f'Error en filter_by_value_and_column - Detalles: {e}')

def get_number_of_records():
    conn = sqlite3.connect('chatbot_database.db')
    query = 'SELECT COUNT(*) FROM interactions'
    result = conn.execute(query).fetchone()[0]
    conn.close()
    return result

def get_number_of_records_by_filter(value, column):
    records = filter_by_value_and_column(value, column)
    print(f'records: {records}')
    return records
