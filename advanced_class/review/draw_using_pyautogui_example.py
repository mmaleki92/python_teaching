import pyautogui
import time

time.sleep(3)

b = [[1, 1, 1, 1],
     [1, 0, 0, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 0, 0, 1],
     [1, 1, 1, 1]]

step = 10

for a in b:
    print(a)
    for n, i in enumerate(a):
        print(i)
        if i == 1:
            pyautogui.click()

        if n != len(a) - 1:
            for i in range(step):
                pyautogui.press("right")

    for _ in range(step):
        pyautogui.press("down")
    
    for _ in range((len(a)-1) * step):
        pyautogui.press("left")
