import logging
import time
import requests


#import pyautogui

statusViza = ''
cisloJednaniGlob = ''
part1CJ = ''
part2CJ = ''
part3CJ = ''
part4CJ = ''
part5CJ = ''


def main(cisloJednani):
    global cisloJednaniGlob
    cisloJednaniGlob = cisloJednani
    parsCisloJednani(cisloJednani)
    #starChrome()
    createPost(part2CJ, part3CJ, part4CJ, part5CJ)
    print('END')


def parsCisloJednani(cisloJednani):
    global part1CJ
    global part2CJ
    global part3CJ
    global part4CJ
    global part5CJ
    part1CJNum = cisloJednani.find('-')
    part1CJ = cisloJednani[:part1CJNum]
    logging.info('part1 => ' + part1CJ)
    part2CJNum = cisloJednani.find('-', part1CJNum + 1)
    if cisloJednani[part1CJNum + 1: part1CJNum + 2] == '0':
        part2CJ = cisloJednani[part1CJNum + 2: part2CJNum]
        print('part2CJ - ' + str(part2CJ))
    else:
        part2CJ = cisloJednani[part1CJNum + 1: part2CJNum]
        print('part2CJ - ' + str(part2CJ))
    logging.info('part2 => ' + part2CJ)
    part3CJNum = cisloJednani.find('/', part2CJNum + 1)
    part3CJ = cisloJednani[part2CJNum + 1: part3CJNum]
    logging.info('part3 => ' + part3CJ)
    part4CJNum = cisloJednani.find('-', part3CJNum + 1)
    part4CJ = cisloJednani[part3CJNum + 1: part4CJNum]
    logging.info('part4 => ' + part4CJ)
    part5CJ = cisloJednani[part4CJNum + 1:]
    logging.info('part5 => ' + part5CJ)


def createPost(part2CJ, part3CJ, part4CJ, part5CJ):
    global statusViza
    r = requests.post('https://frs.gov.cz/cs/ioff/application-status', data={
        'ioff_application_number' : part2CJ,
        'ioff_application_number_fake' : part3CJ,
        'ioff_application_code' : part4CJ,
        'ioff_application_year' : part5CJ,
        'ioff_zov' : '',
        'op':'Ověřit',
        'form_build_id' : 'form-mgZs5aBXbiZnBFuMWtT4XdFoWJHCh2UmTIY_j1lYykE',
        'form_id': 'ioff_application_status_form',
        'honeypot_time': '1674998278|JFIcFp5Kk4lQE8RjmJwRmHjfipGSqYoTWUS1OZh-xug',
        'surname': ''})
    #print(r.text)


    # r = requests.post('https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html')
    #
    #print(r.text)
    # request2file.write(r.text)
    logging.info('request is writed to file')
    NumVisa = part1CJ + "-" + part2CJ + "/" + part4CJ + "-" + part5CJ
    print('NumVisa - ' + NumVisa)
    statusNum = r.text.find(NumVisa)
    print('statusNum - ' + str(statusNum))
    statusZpracovává = r.text.find('Zpracovává se', statusNum, statusNum + 200)     #find word 'Zpracovává se' (if NO -1 / if YES - number start word)
    statusVyřízeno = r.text.find('Vyřízeno – POVOLENO', statusNum, statusNum + 200)            #find word 'Vyřízeno' (if NO -1 / if YES - number start word)
    print('statusZpracovává - ' + str(statusZpracovává))
    print('statusVyřízeno - ' + str(statusVyřízeno))

    #print('statusPart1 - ' + statusPart1)
    if statusZpracovává != -1:
        #status = r.text[statusZpracovává: statusZpracovává + 13]   # Zpracovává se
        #print('Zpracovává se')
        status = 'Zpracovává se'
    elif statusVyřízeno != -1:
        #status = r.text[statusNum + 100: statusNum + 119]   # Vyřízeno – POVOLENO
        #print('Vyřízeno – POVOLENO')
        status = 'Vyřízeno – POVOLENO'
    else:
        print('else')
        print(r.text[statusNum : statusNum + 300])
    #print( cisloJednaniGlob + ' - status = ', status)
    #statusNum = r.text.find('<span class="alert alert-warning"><strong>')
    statusViza = cisloJednaniGlob + ' - status = ' + status
    logging.info('statusViza - '+ statusViza)
    #return (cisloJednaniGlob + ' - status = ', status)

# def starChrome():
#     pyautogui.keyDown("win")
#     pyautogui.press("r")
#     pyautogui.keyUp("win")
#     #pyautogui.write("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe https://frs.gov.cz/cs/ioff/application-status")
#     pyautogui.write("chrome https://frs.gov.cz/cs/ioff/application-status")
#     time.sleep(0.2)
#     pyautogui.press("enter")
#
#
#     pyautogui.moveTo(957, 503, duration=0.25)
#     time.sleep(0.5)
#     pyautogui.leftClick()
#     pyautogui.write(part2CJ)
#
#     pyautogui.moveTo(1050, 503, duration=0.25)
#     pyautogui.leftClick()
#     pyautogui.write(part3CJ)
#
#     pyautogui.moveTo(1150, 503, duration=0.25)
#     pyautogui.leftClick()
#     if part4CJ == "ZM":
#         pyautogui.press("z")
#         time.sleep(0.2)
#         pyautogui.press("z")
#         pyautogui.press("enter")
#     elif part4CJ == "DP":
#         pyautogui.press("d")
#         pyautogui.press("enter")
#     elif part4CJ == "DP":
#         pyautogui.press("d")
#         time.sleep(0.2)
#         pyautogui.press("d")
#         pyautogui.press("enter")
#
#     pyautogui.moveTo(1300, 503, duration=0.25)
#     pyautogui.leftClick()
#
#     if part5CJ == "2022":
#         pyautogui.press("2")
#         pyautogui.press("enter")
#     elif part5CJ == "2021":
#         pyautogui.press("2")
#         time.sleep(0.2)
#         pyautogui.press("2")
#         pyautogui.press("enter")
#
#     pyautogui.moveTo(850, 753, duration=0.25)
#     pyautogui.leftClick()
#
#     pyautogui.moveTo(790, 434, duration=0.25)
#     pyautogui.dragTo(1500, 439, 1, button='left')
    #pyautogui.leftClick

#Point(x=782, y=433)
#Point(x=1485, y=435)

#<span class="alert alert-warning"><strong>Zpracovává se</strong></span>

#Vaše řízení OAM-70324/ZM-2022 je dne 15. 10. 2022, 18:15 ve stavu Zpracovává se.
