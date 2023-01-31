# This is a sample Python script.
# import telebot
import random
import time

import requests
#
#import botFunction
import botFunctionAiogram
import checkMac
import dbPostgres
import loger
import readWriteExcel
import logging
import checkVisa


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    loger
    print_hi('PyCharm')

    #botFunction.bot()
    botFunctionAiogram.main()
    #checkMac.start()

    #dbPostgres.connection2PostgresSelect('insert into public.carfuel VALUES (\'text55\', \'text55\', \'comments55\');')





    #readWriteExcel.write2Excel()



    #checkVisa.main('OAM-70324-4/ZM-2022')
    #time.sleep(random.randint(50, 150))
    #checkVisa.main('OAM-42474-3/DP-2022')



