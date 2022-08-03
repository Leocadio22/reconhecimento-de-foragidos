import smtplib
import email.message


def enviar():
    corpo_email = """
    <p>oláLuiz</p>
    <p>Segue_meu_e-mail automatico</p> 
    """
    msg = email.message.Message()
    msg['Subject'] = 'Assunto'
    msg['from'] = 'luiz.ferreira.leocadio@gmail.com'
    msg['to'] = 'luiz.ferreira.leocadio@gmail.com'
    password = 'suvxzagdfzxevoif'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    #login credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('email enviado')


enviar()
