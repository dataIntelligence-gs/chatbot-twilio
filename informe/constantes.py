

cantidad_mensajes = 500
responde = 130
si = 25
por_si = si/responde
por_no = 1-por_si
no_en_otro_momento = responde-si
no = cantidad_mensajes-responde
porcentaje_si = "{:.2f}".format(por_si)
porcentaje_no = "{:.2f}".format(por_no)