import random
import time
import os
print("<<=======<<TicTac>>=======>>")
print("1.play")
print("2.readme")
menu = int(input("выбери [1/2]: "))
if menu == 2:
  print("привет!. это консольная игра базирована на крестиках ноликах, правила простые выбераешь цифру под которую будешь ставить крестик|нолик")
elif menu == 1:
  os.system("clear")
  os.system("cls")
  a = "[__]"
  b = "[__]"
  c = "[__]"
  a1 = "[__]"
  b1 = "[__]"
  c1 = "[__]"
  a2 = "[__]"
  b2 = "[__]"
  c2 = "[__]"
  while True:
    print(a + b + c)
    print(a1 + b1 + c1)
    print(a2 + b2 + c2)
    vibor = int(input("выбери от 1, 9: "))
    if vibor == 1:
      if a == "[X]" or a == "[0]":
        print("ошибка: вы уже ставили  тут крест.")
        time.sleep(2)
        os.system("clear")
        os.system("cls")
        continue
      else:
        a = "[X]"
    elif vibor == 2:
      if b == "[X]" or b == "[0]":
        print("ошибка: вы уже ставили тут крест.")
        time.sleep(2)
        os.system("clear")
        os.system("cls")
        continue
      else:
        b = "[X]"
    elif vibor == 3:
      if c == "[X]" or c == "[0]":
        print("ошибка: вы уже ставили тут крест.")
        time.sleep(2)
        os.system("clear")
        os.system("cls")
        continue
      else:
        c = "[X]"
    elif vibor == 4:
      if a1 == "[X]" or a1 == "[0]":
        print("ошибка: вы уже ставили тут крест.")
        time.sleep(2)
        os.system("clear")
        os.system("cls")
        continue
      else:
        a1 = "[X]"
    elif vibor == 5:
      if b1 == "[X]" or b1 == "[0]":
        print("ошибка: вы уже ставили тут крест.")
        time.sleep(2)
        os.system("clear")
        os.system("cls")
        continue
      else:
        b1 = "[X]"
    elif vibor == 6:
      if c1 == "[X]" or c1 == "[0]":
        print("ошибка: вы уже ставили тут крест.")
        time.sleep(2)
        os.system("clear")
        os.system("cls")
        continue
      else:
        c1 = "[X]"
    elif vibor == 7:
      if a2 == "[X]" or a2 == "[0]":
        print("ошибка: вы уже ставили тут крест.")
        time.sleep(2)
        os.system("clear")
        os.system("cls")
        continue
      else:
        a2 = "[X]"
    if vibor == 8:
      if b2 == "[X]" or b2 == "[0]":
        print("ошибка: вы уже ставили тут крест.")
        time.sleep(2)
        os.system("clear")
        os.system("cls")
        continue
      else:
        b2 = "[X]"
    elif vibor == 9:
      if c2 == "[X]" or c2 == "[0]":
        print("ошибка: вы уже ставили тут крест.")
        time.sleep(2)
        os.system("clear")
        os.system("cls")
        continue
      else:
        c2 = "[X]"
    os.system("clear")
    os.system("cls")
    print(a + b + c)
    print(a1 + b1 + c1)
    print(a2 + b2 + c2)
    print("подождите...")
    time.sleep(2)
    os.system("clear")
    os.system("cls")
    while True:
      null = True
      bot = random.randint(1, 9)
      if bot == 1:
        if a != "[__]":
          null = False
        else:
          a = "[0]"
      elif bot == 2:
        if b != "[__]":
          null = False
        else:
          b = "[0]"
      elif bot == 3:
        if c != "[__]":
          null = False
        else:
          c = "[0]"
      elif bot == 4:
        if a1 != "[__]":
          null == False
        else:
          a1 = "[0]"
      elif bot == 5:
        if b1 != "[__]":
          null = False
        else:
          b1 = "[0]"
      elif bot == 6:
        if c1 != "[__]":
          null = False
        else:
          c1 = "[0]"
      elif bot == 7:
        if a2 != "[__]":
          null = False
        else:
          a2 = "[0]"
      elif bot == 8:
        if b2 != "[__]":
          null = False
        else:
          b2 = "[0]"
      elif bot == 9:
        if c2 != "[__]":
          null = False
        else:
          c2 = "[0]"
      if a == "[0]" or b == "[0]" or c == "[0]" or a1 == "[0]" or b1 == "[0]" or c1 == "[0]" or a2 == "[0]" or b2 == "[0]" or c2 == "[0]":
        os.system("clear")
        os.system("cls")
        break
    if a == "[X]" and b == "[X]"   and c == "[X]":
      print("вы выиграли!.")
      break
    elif a1 == "[X]" and b1 == "[X]" and c1 == "[X]":
      print("вы выиграли!.")
      break
    elif a2 == "[X]" and b2 == "[X]" and c2 == "[X]":
      print("вы выиграли!.")
      break
    elif a == "[X]" and a1 == "[X]" and a2 == "[X]":
      print("вы выиграли!.")
      break
    elif b == "[X]" and b1 == "[X]" and b2 == "[X]":
      print("вы выиграли!.")
      break
    elif c == "[X]" and c1 == "[X]" and c2 == "[X]":
      print("вы выиграли!.")
      break
    elif a == "[X]" and b1 == "[X]" and c2 == "[X]":
      print("вы выиграли!.")
      break
    elif a2 == "[X]" and b1 == "[X]" and c == "[X]":
      print("вы выиграли!.")
      break
    elif a == "[0]" and b == "[0]" and c == "[0]":
      print("вы проиграли =(")
      break
    elif a1 == "[0]" and b1 == "[0]" and c1 == "[0]":
      print("вы проиграли =(")
      break
    elif a2 == "[0]" and b2 == "[0]" and c2 == "[0]":
      print("вы проиграли =(")
      break
    elif a == "[0]" and a1 == "[0]" and a2 == "[0]":
      print("вы проиграли =(")
      break
    elif b == "[0]" and b1 == "[0]" and b2 == "[0]":
      print("вы проиграли =(")
      break
    elif c == "[0]" and c1 == "[0]" and c2 == "[0]":
      print("вы проиграли =(")
      break
    elif a == "[0]" and b1 == "[0]" and c2 == "[0]":
      print("вы проиграли =(")
      break
    elif a2 == "[0]" and b1 == "[0]" and c == "[0]":
      print("вы проиграли =(")
      break