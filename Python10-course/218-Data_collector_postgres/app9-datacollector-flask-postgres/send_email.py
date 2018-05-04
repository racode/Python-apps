from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    fromaddr=""
    from_password=""
    toaddrs=email

    subject="Height data"
    message="Hey there, your height is <strong>%s</strong>. <br> Average height of all is <strong>%s</strong> and that is calculated out of <strong>%s</strong> people. <br> Thanks!" % (height, average_height, count)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=toaddrs
    msg['From']=fromaddr

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.set_debuglevel(1)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(fromaddr, from_password)
    gmail.sendmail(fromaddr, toaddrs, msg.as_string())
    gmail.quit()

'''
# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
'''
