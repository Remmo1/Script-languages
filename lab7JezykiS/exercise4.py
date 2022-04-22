import re

text_to_search = '''
123-456-789
+48 123.456.789
123456789

12345
+49 987654321
+90 987654321
123a456 354
087654321
'''

phone_pattern = re.compile(r'(\+\d\d )?[1-9]\d{2}[ -.]?\d{3}[ -.]?\d{3}')

matches = phone_pattern.finditer(text_to_search)

for match in matches:
    if match.group(1) != None:
        if match.group(1) == '+48 ':
            print(match)
    else:
        print(match)



emails_to_search = '''
12345@pwr.edu.pl
12345@student.pwr.edu.pl
marian.kowalski@pwr.edu.pl

12345@gmail.com
@pwr.edu.pl
12eda2e312e@onet.pl
'''

def take_data_from_email(mail_address):
    email_pattern = re.compile(r'((\d{5})?([a-zA-Z]+\.[a-zA-Z]+)?)@([a-zA-Z]+\.)?(pwr.edu.pl)')
    matches = email_pattern.finditer(mail_address)

    for m in matches:
        print(m)

    return matches

take_data_from_email(emails_to_search)
