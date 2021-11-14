# ---<=> MODULOS <=>---
import ssl
import smtplib
import getpass
import argparse
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# ---<=> ARGUMENTOS <=>---
parser = argparse.ArgumentParser()
parser.add_argument('--transmitter', dest = 'emisor', default = '', help = 'Correo Electronico del Emisor del Mensaje')
parser.add_argument('--password', dest = 'contraseña', default = '', help = 'Contraseña del Emisor del Mensaje')
parser.add_argument('--receiver', dest = 'destino', default = '',  help = 'Correo Electronico del Destino del Mensaje')
parser.add_argument('--subject', dest = 'asunto', default= '', help = 'Asunto del Correo Electronico')
parser.add_argument('--message', dest = 'mensaje', default = '', help = 'Mensaje del Correo Electronico')
params = parser.parse_args()

# ---<=> SCRIPT <=>---
if __name__ == '__main__':
    try: 
        correo = MIMEMultipart()
        correo["From"] = params.emisor
        correo["Subject"] = params.asunto
        correo["To"] = params.destino
        correo["body"] = params.mensaje

        correo.attach(MIMEText(params.mensaje, "plain"))

        context = ssl.create_default_context()
        with smtplib.SMTP("outlook.office365.com", 587) as server:
            server.ehlo()
            server.starttls(context=context)
            server.login(params.emisor, params.contraseña)
            server.sendmail(
                params.emisor, params.destino, correo.as_string()
            )
        print("*** CORREO ENVIADO EXITOSAMENTE ***")
        
    except Exception as e:
        print("Error", e)