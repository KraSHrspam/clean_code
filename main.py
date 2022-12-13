import os
import smtplib
import textwrap as tw


def readfile(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text


if __name__ == '__main__':
    headers_template = """
    From: fuzedizeli@yandex.ru
    To: fuzedizeli@yandex.ru
    Subject: invite
    Content-type: text/plain; charset="UTF-16";"""

    password = os.getenv('password')
    login = os.getenv('login')
    finished_headers_template = tw.dedent(headers_template)
    unfinished_letter = readfile('text.txt')
    my_name, website = readfile('to_replace.txt').split('\n')
    finished_letter_sending = f'''\
    {finished_headers_template}

    {unfinished_letter}
    '''.replace('%my_name%', 'Илья').replace('%website%', 'dvmn.org')

    finished_letter_sending = finished_letter_sending.encode('utf-16')
    server = smtplib.SMTP_SSL('smtp.yandex.com:465')
    server.login(login, password)
    server.sendmail(login, login, finished_letter_sending)
    server.quit()
    print('Письмо отправлено!')
