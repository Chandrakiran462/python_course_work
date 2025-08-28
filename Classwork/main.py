import EmailAutomation

res_mail = input("Enter Email: ")
subject = input("Enter Subject: ")
body = input("Enter Body: ")

EmailAutomation.send_email(res_mail,subject,body)
