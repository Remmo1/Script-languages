import smtplib

import Operations
import constst
from Operations import compress_file, delete_all, create_folder_for_extension

# compress_file('/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/pythonProject/others/covid_test.txt')
# Operations.decompress_file('/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/pythonProject/others/covid_test-compressed.bz2')

#Operations.compress_all_files(constst.OTHERS_FOLDER)
#f = Operations.search_for_folders('/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/pythonProject')
#for i in f:
#  print(i)

#for rule in f[1]:
#   print(rule)
#print(chr(1))
#print(ord(''))

#create_folder_for_extension('f1', 'ddd')

"""# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.

msg = MIMEText('Some text')

# me == the sender's email address
# you == the recipient's email address
me = 'remigiusz.pisarski@onet.pl'
you = 'remigiusz.pisarski@onet.pl'

msg['Subject'] = 'The contents of'
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
print('a')
s = smtplib.SMTP('smtp.poczta.onet.pl', 465)
print('b')
s.starttls()
s.sendmail(me, [you], msg.as_string())
s.quit()"""

