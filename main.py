import requests
import getpass

def location():
    info = requests.get('https://freegeoip.app/json/').json()
    print('Your username is: ' + getpass.getuser())
    for key, value in info.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    location()
