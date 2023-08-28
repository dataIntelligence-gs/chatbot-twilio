from database_module import get_number_of_records, get_number_of_records_by_filter


class Constants:
    def __init__(self):
        self.cantidad_mensajes = None
        self.responde = None
        self.si = None
        self.por_si = None
        self.por_no = None
        self.no_en_otro_momento = None
        self.no = None
        self.porcentaje_si = None
        self.porcentaje_no = None


    def main(self):
        total = get_number_of_records()
        self.cantidad_mensajes = total
        responde_no = get_number_of_records_by_filter('en otro momento', 'initial_message')
        responde_si = get_number_of_records_by_filter('si, me encantaria', 'initial_message')
        responde = responde_si + responde_no
        self.responde = responde
        self.si = responde_si
        self.por_si = self.si/self.responde
        self.por_no = 1-self.por_si
        self.no_en_otro_momento = self.responde-self.si
        self.no = self.cantidad_mensajes-self.responde
        self.porcentaje_si = "{:.2f}".format(self.por_si)
        self.porcentaje_no = "{:.2f}".format(self.por_no)
        return self.cantidad_mensajes, self.responde, self.si, self.por_si, self.por_no, self.no_en_otro_momento, self.no, self.porcentaje_si, self.porcentaje_no



