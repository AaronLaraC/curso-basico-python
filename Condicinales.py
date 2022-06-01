def califacionAzure():
    calificaciones = int(input('Introduce tu calificacion de la AZ-900: '))
    # preguntamos si la calificación es mayor a 700
    if (calificaciones > 700 and calificaciones <= 1000):
        print('bien hecho')
    elif (calificaciones < 700):
        print('Ves por no estudiar.')
    else:
        print('Mentiroso')


def mayorEdad():
    edad = int(input('introduce tu edad: '))
    if(edad >= 18):
        print(f'Eres mayor edad y tu edad es: {edad}')
    elif(edad >= 100):
        print('si vienes acompañad@ de tus abuelitos, si te podemos fiar')
    elif(edad < 0):
        print('Ni que fueras viajero del tiempo')
    else:
        print('No puedes llevarte cigarros')


mayorEdad()
