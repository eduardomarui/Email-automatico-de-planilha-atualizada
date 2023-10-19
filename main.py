import smtplib
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import schedule
import time

# Função para obter dados do Google Sheets
def obter_dados_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    
    # Obter os dados da planilha do Google Sheets
    sheet = client.open("Nome da Planilha").sheet1
    data = sheet.get_all_records()

    # Converter os dados para DataFrame do pandas
    df = pd.DataFrame(data)
    df.to_csv('planilha.csv', index=False)

# Função para enviar e-mail
def enviar_email():
    remetente = "SEU_EMAIL@gmail.com"
    senha = "SUA_SENHA"
    destinatario = "DESTINATARIO@gmail.com"
    
    # Criar a mensagem
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = 'Planilha Atualizada'
    
    # Anexar arquivo
    with open('planilha.csv', 'rb') as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="planilha.csv"')
        msg.attach(part)

    # Enviar e-mail
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(remetente, senha)
        server.send_message(msg)
        print("Email enviado com sucesso!")

# Agendar a tarefa
schedule.every().day.at("12:00").do(obter_dados_google_sheets)
schedule.every().day.at("12:00").do(enviar_email)

# Mantenha o script em execução
while True:
    schedule.run_pending()
    time.sleep(1)
