#<\>!python3.11
#-------------------Dont Edit This Script-----------------#
import os,platform,time

bitt=platform.architecture()[0]

if bitt=="32bit":
    print('[!] Your Device is 32 bit');time.sleep(1);print('\n\n[!] Your Python Version :');time.sleep(1);os.system('python --version')
    time.sleep(2)
    import FIRE32.MAHIN


elif bitt=="64bit":
    os.system('clear');print('[!] Your Device is 64 bit');time.sleep(1);print('\n\n[!] Your Python Version :');time.sleep(1);os.system('python --version')
    time.sleep(2)
    import FIRE64.MAHIN

else:
    print('\nUNKNOWN DEVICE')

#---------------------------------------------------------#
#                    THIS TOOL OWNED BY
#                  • MAHIN KHAN
#---------------------------------------------------------#
