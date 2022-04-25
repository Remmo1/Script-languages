import re


# =========================================== Numer telefonu ================================================

def check_phone_number(number):
    phone_pattern = re.compile(r'(\+\d\d )?[1-9]\d{2}[ -.]?\d{3}[ -.]?\d{3}')
    matches = phone_pattern.finditer(number)

    for match in matches:
        if match.group(1) is None:
            return True
        else:
            return match.group(1) == '+48 '
    return False


result = check_phone_number(input('Podaj polski numer telefonu: '))

if result:
    print('Poprawny')
else:
    print('Niepoprawny')


# ========================================== Email PWR ================================================

def take_date_from_email(address):
    email_pattern = \
        re.compile(r'((\d{6})?([a-zA-Z]+\.[a-zA-Z]+)?([a-zA-Z]+\.[a-zA-Z]+-[a-zA-Z]+)?)@([a-zA-Z]+\.)?(pwr.edu.pl)')
    matches = email_pattern.finditer(address)

    for m in matches:
        data = m.group(1)
        if data is not None:
            if data.isdigit():
                return data
            else:
                data = data.split('.')
                return data[0], data[1]
        else:
            return data


print(take_date_from_email(input('Podaj adress email pwr: ')))

"""
te proby bardzo mi pomogly

emails_to_search = '''
12345@pwr.edu.pl
12345@student.pwr.edu.pl
marian.kowalski@pwr.edu.pl
adrianna.nowak-wolska@pwr.edu.pl

12345@gmail.com
@pwr.edu.pl
12eda2e312e@onet.pl
'''


def take_data_from_email(mail_address):
    email_pattern = \
        re.compile(r'((\d{5})?([a-zA-Z]+\.[a-zA-Z]+)?([a-zA-Z]+\.[a-zA-Z]+-[a-zA-Z]+)?)@([a-zA-Z]+\.)?(pwr.edu.pl)')
    matches = email_pattern.finditer(mail_address)

    for m in matches:
        if m.group(1).isdigit():
            print('numer', m.group(1))
        else:
            print('imime', m.group(1))

    return matches


take_data_from_email(emails_to_search)


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


"""
