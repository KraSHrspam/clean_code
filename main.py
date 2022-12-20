import os
import smtplib
import textwrap as tw
from dotenv import load_dotenv


def readfile(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        text = file.read()
    return text


if __name__ == '__main__':
    load_dotenv()
    password = os.getenv('password')
    login = os.getenv('login')
    headers_template = f"""
    From: {login}
    To: {login}
    Subject: invite
    Content-type: text/plain; charset="UTF-8";"""

    headers = tw.dedent(headers_template)
    letter_template = readfile('text.txt')
    my_name, website = readfile('to_replace.txt').split('\n')
    finished_letter_sending = f'''\
    {headers}

    {letter_template}
    '''.replace('%my_name%', 'Илья').replace('%website%', 'dvmn.org')

    encoded_letter = finished_letter_sending.encode('utf-8')
    server = smtplib.SMTP_SSL('smtp.yandex.com:465')
    server.login(login, password)
    server.sendmail(login, login, encoded_letter)
    server.quit()
    print('Письмо отправлено!')
