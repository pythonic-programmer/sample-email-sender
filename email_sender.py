# email sender simple script

import smtplib
from email.message import EmailMessage

# credentials and message contents
sender_email = 'sender_adress@gmail.com'
receiver_email = 'receiver_address@gmail.com'
sender_password = 'pass_word12345'
message = EmailMessage()
message['Subject'] = "Hello There."
message['From'] = sender_email
message['To'] = receiver_email
text_message = "How are you?"
message.set_content(text_message)


def send_email(user_email, user_password):
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com",
                                  465)  # SSL stands for  secure socket  layer, to make security transformation;
        server.login(user_email, user_password)
        server.send_message(message)
        server.close()
        print(' Email sent successfully')
    except:
        print("Failed to send mail")


if __name__ == '__main__':
    send_email(sender_email, sender_password)

