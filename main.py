import time
import requests
import selectorlib
import smtplib, ssl
import os
import sqlite3



URL = 'http://programmer100.pythonanywhere.com/tours/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect('data.db')

def scrape(url):
    respose = requests.get(url, headers=HEADERS)
    source = respose.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)['tours']
    return value


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "venedygait@gmail.com"
    password = os.environ['PASSWORD']

    receiver = "venedygait@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

def read(extracted):
    row = extracted.split(',')
    row = [item.strip() for item in row]
    band,city,date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?",(band,city,date))
    cursor.fetchall()
    print(row)
    return row

def store(extracted):
    row = extracted.split(',')
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VELUES(?,?,?)", row)
    connection.commit()


if __name__ == "__main__":
    while True:
        scalped = scrape(URL)
        extracted = extract(scalped)
        print(extracted)

        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                store(extracted)
                send_email(message="Hey, new event was found!")
        time.sleep(2)
