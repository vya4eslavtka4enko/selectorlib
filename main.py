import requests
import selectorlib


URL = 'http://programmer100.pythonanywhere.com/tours/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    response = requests.get(url,headers=HEADERS)
    source = response.text
    return source
def read(extracted):
    with open("data.txt",'r') as file:
        return file.read()
def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)['tours']
    return value


def send_email():
    print("Email send")

def store(extracted):
    with open("data.txt",'w') as file:
        file.write(extracted+'\n')


if __name__ == "__main__":
    scalped = scrape(URL)
    extracted = extract(scalped)
    print(extracted)
    store(extracted)
    content = read(extracted)
    if extracted != "No upcoming tours":
        if extracted not in "data.txt":
            send_email()
