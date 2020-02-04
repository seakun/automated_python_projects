import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
type(conn)

conn

conn.ehlo() # Connect to SMTP server
conn.starttls()
conn.login('asweigart@gmail.com', 'password')

conn.sendmail('asweigart@gmail.com', 'asweigart@gmail.com', 'Subject: So long...\n\nDear Al, \nSo long, and thanks for all the fish.\n\n-Al')
#from, to, email body

conn.quit()
