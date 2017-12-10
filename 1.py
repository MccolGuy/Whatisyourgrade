korean = input("국어 점수는 몇점입니까? ")
a =int(korean)
math = input("수학 점수는 몇점입니까? ")
b =int(math)
society = input("사회 점수는 몇점입니까? ")
c =int(society)
science = input("과학 점수는 몇점입니까? ")
d =int(science)
english = input("영어 점수는 몇점입니까? ")
e =int(english)
history = input("한국사 점수는 몇점입니까? ")
f =int(history)
giga = input("기가 점수는 몇점입니까? ")
g =int(giga)
h = (a + b + c + d + e + f + g)/7

print("평균은 %d 점 입니다"% h)

import win32clipboard

# set clipboard data
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText("점수는 %f점 입니다."% h)
win32clipboard.CloseClipboard()

# get clipboard data
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
import os
os.system('Pause')

