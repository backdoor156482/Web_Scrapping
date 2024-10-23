import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# URL del producto
url = 'https://ejemplo.com/producto'

# Realiza la solicitud HTTP
response = requests.get(url)

# Analiza el contenido HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Encuentra el valor numérico del producto (ajusta el selector según la estructura de la página)
precio = soup.find('span', {'class': 'precio'}).text

# Envía una notificación por correo electrónico
def enviar_notificacion(precio):
    remitente = 'tu_correo@gmail.com'
    destinatario = 'destinatario_correo@gmail.com'
    contraseña = 'tu_contraseña'

    # Configura el contenido del correo
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = 'Precio del Producto'

    cuerpo = f'El precio del producto es: {precio}'
    msg.attach(MIMEText(cuerpo, 'plain'))

    # Conexión y envío del correo
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(remitente, contraseña)
    texto = msg.as_string()
    server.sendmail(remitente, destinatario, texto)
    server.quit()

# Llama a la función para enviar la notificación
enviar_notificacion(precio)
