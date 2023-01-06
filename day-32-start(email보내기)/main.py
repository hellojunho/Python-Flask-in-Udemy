# import smtplib
# from email.mime.text import MIMEText
#
# my_email = "junho991026@naver.com"
# password = "jun991026"
#
# connection = smtplib.SMTP(host="smtp.naver.com", port=465)
# connection.ehlo()
# connection.starttls()
# connection.login(user=my_email, password=password)
#
# # msg = MIMEText('본문 테스트 메시지')
# # msg['Subject'] = 'Hello Test!'
# # msg['To'] = "junho991026@naver.com"
# connection.sendmail(from_addr=my_email, to_addrs="junho991026@naver.com", msg="Hello")
# connection.quit()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "내이메일"
my_password = r"내비밀번호"
you = "상대이메일"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Alert"
msg['From'] = me
msg['To'] = you

html = '<html><body><p>Hi, I have the following alerts for you!</p></body></html>'
part2 = MIMEText(html, 'html')

msg.attach(part2)

# Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
s = smtplib.SMTP_SSL('smtp.naver.com')
# uncomment if interested in the actual smtp conversation
# s.set_debuglevel(1)
# do the smtp auth; sends ehlo if it hasn't been sent already
s.login(me, my_password)

s.sendmail(me, you, msg.as_string())
s.quit()

# 잘 안되네..