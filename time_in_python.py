from datetime import datetime
import pytz

""" tabla de codigos de tiempo.
%Y Year
%m Month
%d Day
%H Hour
%M Minute
%S Second
"""
def run():

    """utilizar una zona horaria especifica con pytz.
    base de datos de zonas horarias: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones"""

    my_datetime = datetime.utcnow()
    print(my_datetime)

    my_str = my_datetime.strftime('%d/%m/%Y')
    print(f'Formato LATAM: {my_str}')

    my_str = my_datetime.strftime('%m/%d/%Y')
    print(f'Formato USA: {my_str}')

    my_str = my_datetime.strftime('Estamos en el año %Y') 
    # se puede modificar el string a mostrar.
    print(f'Formato Random: {my_str}')

#configurar zona horaria de Bogota.

#crear funcion que muestre hora y fecha segun alguna zona horaria solicitada

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogota: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)
print("Ciudad de Mexico: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

caracas_timezone = pytz.timezone("America/Caracas")
caracas_date = datetime.now(mexico_timezone)
print("Caracas: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))


if __name__ == '__main__':
    run()