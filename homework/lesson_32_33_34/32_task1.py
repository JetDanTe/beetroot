"""Task 1

Robots.txt

Download and save to file robots.txt from wikipedia, twitter websites etc. """
import requests
from requests import request
class Adv:
    def __init__(self, link):
        self.link = link

    def download_adv(self):
        with open('robots.txt', 'w') as robot:
            adv = requests.get(self.link)
            robot.writelines(str(adv.text))
            robot.close()

if __name__ == '__main__':
    dante_adv = Adv('https://www.olx.ua/d/obyavlenie/obuchayuschiy-nabor-arduino-starter-kit-na-baze-uno-r3-v-keyse-IDjgkJ0.html?sd=1#0baa891a48;promoted')
    dante_adv.download_adv()
