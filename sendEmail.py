import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def send_mail(string):
	print("具体设置，参考 https://zhuanlan.zhihu.com/p/33192111")
	sender = input("请输入发件人邮箱(默认QQ邮箱)")
	auth_code = input("请输入授权码(不包含空格)")
	host = input("请输入服务器地址(QQ-->smtp.qq.com)")
	port = int(input("请输入服务器端口号(QQ-->465、587，默认465)"))
	receiver = input("请输入接收人地址")

	msg = MIMEMultipart()
	# 主题
	msg['Subject'] = input("请输入邮件主题")
	# 发送人
	msg['From'] = sender
	# 添加正文
	msg.attach(MIMEText(string, 'plain', 'utf-8'))

	# 登录并发送
	try:
		s = smtplib.SMTP_SSL(host, port)
		s.set_debuglevel(1)
		s.login(sender, auth_code)
		msg['To'] = receiver
		s.sendmail(sender, receiver, msg.as_string())
		s.quit()
	except smtplib.SMTPException as ex:
		print("error, %s", ex)


