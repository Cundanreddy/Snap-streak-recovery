import webbrowser
import pyautogui
import time


s = """_______"""  #snap ID of the lost streaks
l = s.split("\n")
k = []
Snap_id=input("enter the snap id of the user : ")
email_id=input("enter the email id : ")
ph_num=input("enter the mobile number of the user")
dev_name=input("enter the device name snap is installed (ex: IPhone, oppo, vivo etc.) : ")
for i in l:
    temp = i.split("\t")
    k.append(temp)
time.sleep(10)
for i in range(len(k)):
    pyautogui.typewrite(Snap_id)  #snap ID of the user
    pyautogui.press('tab')
    pyautogui.typewrite(email_id)   # email id of the user
    pyautogui.press('tab')
    pyautogui.typewrite(ph_num)   # phone number of the user
    pyautogui.press('tab')
    pyautogui.typewrite(dev_name)      # device name of the user
    pyautogui.press('tab')
    pyautogui.typewrite(k[i][0])
    pyautogui.press('tab')
    pyautogui.typewrite("today")
    pyautogui.press('tab')
    pyautogui.typewrite("500")
    pyautogui.press('tab')
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.typewrite("back")
    pyautogui.scroll(-50000)
    pyautogui.click(779,528)
    time.sleep(10)

