import yagmail,csv
from decouple import config


def horario_atencion(file,inicio,final):
        atencion=[]
        inicio_hora,inicio_minutos=inicio.split(":")
        final_hora,final_minutos=final.split(":")
        minutos_totales=(int(final_hora)-int(inicio_hora))*60+(int(final_minutos)-int(inicio_minutos))
        with open (file, newline="") as f:
                filereader=csv.reader(f,delimiter=";")
                counter=0
                for line in filereader:
                        counter+=1
        tiempo_por_persona=minutos_totales//counter
        atencion.append(inicio)
        conteo_minutos=int(inicio_minutos)
        conteo_horas=int(inicio_hora)
        for _ in range(counter):
                conteo_minutos+=tiempo_por_persona
                if conteo_minutos>=60:
                        conteo_horas+=1
                        conteo_minutos-=60
                atencion.append(f"{conteo_horas}:{conteo_minutos:02}")
        return atencion




archivo="C:/Users/gquintero/Desktop/python/correosDireccionGrupo - copia.csv"
horario=horario_atencion(archivo,"8:00","1:00")


yag = yagmail.SMTP("gquintero@colegionuevayork.edu.co",config("gquintero_mail_password"))
with open (archivo,newline="") as file:
    filereader=csv.reader(file,delimiter=";")   
    numero=0 
    for line in filereader:
        mail=[]
        nombre=""
        for i in line:
                if "@" in i:
                        mail.append(i)
                elif i=="":
                        pass
                else:
                        nombre=i

        body ='''
Apreciada papitos de {name}, cordial saludo con deseos de bienestar para todos.

Este lunes 5 de diciembre, tendremos nuestro Open Day de cierre del año escolar. La asistencia es de carácter obligatorio.
Los esperamos a las {hora} y como todos están con cita, agradecemos su puntualidad.

De igual manera, si por alguna razón justificable, no pudiera asistir a la hora determinada, solicite una cita al correo del director de grupo (o como respuesta a este). Es fundamental que reciba la información.

Cordialmente:
Gustavo Orlando Quintero Quintero
Docente Matemáticas
Colegio Nueva York
Tel:601684890 ext. 134.'''

        sub="Open day final"
        yag.send(to=mail,subject=sub,contents=body.format(name=nombre,hora=horario[numero]))
        print(f"email sent to {nombre} at {mail}")
        numero+=1
print("Done")