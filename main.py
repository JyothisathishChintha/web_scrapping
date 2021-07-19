import pyttsx3
import requests
from bs4 import BeautifulSoup

# Used to "convert text to speech".
# Initialization of "pyttsx".

engine = pyttsx3.init()
newVoiceRate = 100
newVolume = 100
engine.setProperty('rate', newVoiceRate)
engine.setProperty('volume', newVolume)


# Tata motor function later is used.

def tata_motors():
    engine.say('\nLoading to Tata Motors Indian Limited\n')
    engine.runAndWait()

# Getting contents from webpage.
# Using BeautifulSoup with parser lxml contents are loaded.

    web_page = requests.get('https://www.ndtv.com/business/stock/tata-motors-ltd_tatamotors/reports').text
    source = BeautifulSoup(web_page, 'lxml')
    content = source.find('div', class_='left-panel')
    exchanges = content.find_all('div', class_='num')
    print("\nTATA MOTORS INDIAN LIMITED\n")

    for exchange in exchanges:
        print(f"{exchange['id']}: {exchange.span.text}")

    para = source.find('div', class_='output dyn-data')
    sub_para = para.find('div', id="historyReport")
    sub_para = sub_para.find_all('ul')

# creating dictionary  to store keys as numbers and values are contents followed by sub_para.
# Manually inserting headdlines to extract data easier.

    d = {}
    ls = ['Passenger Cars:', 'Utility Vehicles:', 'Trucks:', 'Commercial Passenger Carriers:',
          'Subsidiaries of the company:',
          'Milestones:', 'Achievements/ recognition:', 'Advertising Awards:', 'Environ-international']

    for index, i in enumerate(sub_para, start=1):
        v = []
        if index != 7:
            for j in i.find_all('li'):
                v.append(j.text)
            if index > 7:
                d[index-1] = v
            else:
                d[index] = v

    while True:
        print('\nOptions\n')
        for ind, i in enumerate(ls, start=1):
            print(f'{ind}: {i}:')

        inp = input('\nSelect options or viewall(v) or exit(e)"\n')
        if inp.lower() == 'e':
            engine.say("exiting...")
            engine.runAndWait()
            break
        elif inp.lower() == 'v':
            engine.say('viewing...')
            engine.runAndWait()
            for key, val in d.items():
                print(ls[key-1])
                for i in val:
                    print(i)
                print('\n')

# Checking input is digit or not.If it is then checking it is inrange of length of list "ls".

        elif inp.isdigit() and int(inp) in range(1, len(ls)+1):
            engine.say('viewing...')
            engine.runAndWait()
            inp = int(inp)
            print(ls[inp-1])
            for i in d[inp]:
                print(i)
        else:
            engine.say("Not Understanding Try again...")
            engine.runAndWait()
        print('\n')

# Similar to above function "Tata Motors".
# Maruthi suziki function later is used.


def maruthi():
    engine.say('\nLoading to Maruthi Suziki Indian Limited\n')
    engine.runAndWait()
    web_page = requests.get('https://www.ndtv.com/business/stock/maruti-suzuki-india-ltd_maruti/reports').text
    source = BeautifulSoup(web_page, 'lxml')
    content = source.find('div', class_='left-panel')
    exchanges = content.find_all('div', class_='num')
    print('\nMARUTHI SUZIKI INDIAN LIMITED\n')

    for exchange in exchanges:
        print(f"{exchange['id']}: {exchange.span.text}")

    para = source.find('div', class_='output dyn-data')
    sub_para = para.find('div', id="historyReport")
    sub_para = sub_para.find_all('ul')

    d = {}
    ls = ['Product range of the company includes:', 'Achievements/ recognition:', 'Other Accolades:']
    for index, i in enumerate(sub_para, start=1):
        v = []
        for j in i.find_all('li'):
            v.append(j.text)
        d[index] = v

    while True:
        print('\nOptions\n')
        for ind, i in enumerate(ls, start=1):
            print(f'{ind}: {i}:')

        inp = input('\nSelect options or viewall(v) or exit(e)\n')
        if inp.lower() == 'e':
            engine.say("exiting...")
            engine.runAndWait()
            break
        elif inp.lower() == 'v':
            engine.say('viewing')
            engine.runAndWait()
            for key, val in d.items():
                print(ls[key-1])
                for i in val:
                    print(i)
                print('\n')
        elif inp.isdigit() and int(inp) in range(1, len(ls)):
            engine.say('viewing')
            engine.runAndWait()

            inp = int(inp)
            print(ls[inp-1])
            for i in d[inp]:
                print(i)
        else:
            engine.say("Not Understanding Try again...")
            engine.runAndWait()
        print('\n')


# Main Function to run above two functions.

if __name__ == "__main__":
    engine.say('Welcome to web scrapping')
    engine.runAndWait()
    while True:
        user = input("enter which data to view\n1.TataMotors\n2.MaruthiSuziki\n")
        if user == '1':
            tata_motors()
            break
        elif user == '2':
            maruthi()
            break
        else:
            engine.say("Not Understanding Try again...")
            engine.runAndWait()
