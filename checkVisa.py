import logging
import time


import pyautogui

part1CJ = ''
part2CJ = ''
part3CJ = ''
part4CJ = ''
part5CJ = ''


def main(cisloJednani):
    parsCisloJednani(cisloJednani)
    starChrome()



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
    part2CJ = cisloJednani[part1CJNum + 1: part2CJNum]
    logging.info('part2 => ' + part2CJ)
    part3CJNum = cisloJednani.find('/', part2CJNum + 1)
    part3CJ = cisloJednani[part2CJNum + 1: part3CJNum]
    logging.info('part3 => ' + part3CJ)
    part4CJNum = cisloJednani.find('-', part3CJNum + 1)
    part4CJ = cisloJednani[part3CJNum + 1: part4CJNum]
    logging.info('part4 => ' + part4CJ)
    part5CJ = cisloJednani[part4CJNum + 1:]
    logging.info('part5 => ' + part5CJ)

def starChrome():
    pyautogui.keyDown("win")
    pyautogui.press("r")
    pyautogui.keyUp("win")
    pyautogui.write("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe https://frs.gov.cz/cs/ioff/application-status")
    time.sleep(0.2)
    pyautogui.press("enter")


    pyautogui.moveTo(957, 503, duration=0.25)
    time.sleep(0.5)
    pyautogui.leftClick()
    pyautogui.write(part2CJ)

    pyautogui.moveTo(1050, 503, duration=0.25)
    pyautogui.leftClick()
    pyautogui.write(part3CJ)

    pyautogui.moveTo(1150, 503, duration=0.25)
    pyautogui.leftClick()
    if part4CJ == "ZM":
        pyautogui.press("z")
        time.sleep(0.2)
        pyautogui.press("z")
        pyautogui.press("enter")
    elif part4CJ == "DP":
        pyautogui.press("d")
        pyautogui.press("enter")
    elif part4CJ == "DP":
        pyautogui.press("d")
        time.sleep(0.2)
        pyautogui.press("d")
        pyautogui.press("enter")

    pyautogui.moveTo(1300, 503, duration=0.25)
    pyautogui.leftClick()

    if part5CJ == "2022":
        pyautogui.press("2")
        pyautogui.press("enter")
    elif part5CJ == "2021":
        pyautogui.press("2")
        time.sleep(0.2)
        pyautogui.press("2")
        pyautogui.press("enter")

    pyautogui.moveTo(850, 753, duration=0.25)
    pyautogui.leftClick()

    pyautogui.moveTo(790, 434, duration=0.25)
    pyautogui.dragTo(1500, 439, 1, button='left')
    #pyautogui.leftClick

#Point(x=782, y=433)
#Point(x=1485, y=435)

#<span class="alert alert-warning"><strong>Zpracovává se</strong></span>

#Vaše řízení OAM-70324/ZM-2022 je dne 15. 10. 2022, 18:15 ve stavu Zpracovává se.
