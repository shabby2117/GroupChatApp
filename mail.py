import smtplib
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def send_mail_to(destination,obj_id):
   
    me = "shubhamsaurabh2117@gmail.com"
    you = destination
    link = "https://groupchatapp20.herokuapp.com/confirmation/{}".format(obj_id)


    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Link"
    msg['From'] = me
    msg['To'] = you

    text = "Hi!\nWelcome to chat application\nHere is the confiramation link you wanted:\nhttp://www.python.org"
    html = """\
    <html>
    <head></head>
    <body>
        <p>Hi!<br>
        HWelcome to chat application<br>
        Here is the <a href={} >confirmation link</a> you wanted.
        </p>
    </body>
    </html>
    """.format(link,link)
    try:
        part2 = MIMEText(html, 'html')
        msg.attach(part2)
        mailserver = smtplib.SMTP_SSL('smtp.googlemail.com',465)
        try:
            mailserver.login('groupchat2018@gmail.com', 'groupchat@2018')
            mailserver.sendmail(me, you, msg.as_string())
        finally:
            mailserver .quit()
    except Exception as exc:
        sys.exit( "mail failed; %s" % str(exc) )


if __name__ == "__main__":
    main()

