import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import configparser

# 讀取config.ini中的配置
config = configparser.ConfigParser()
config.read('config.ini')

sender_email = config['EMAIL']['SENDER_EMAIL']
receiver_email = config['EMAIL']['RECEIVER_EMAIL']
password = config['EMAIL']['PASSWORD']
subject = "測試郵件"
body = "這是一封由姚奕碩發送的測試郵件。"

# 建立 MIMEText 物件
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

# 附加郵件內容
msg.attach(MIMEText(body, "plain"))

# 設定 SMTP 伺服器並發送郵件
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)  # 使用正確的TLS端口
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()
    print("郵件發送成功！")
except Exception as e:
    print(f"郵件發送失敗：{e}")
