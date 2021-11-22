import random
reqCheckList=[False,False,False,False,False]
specialCharacters=[33,35,36,37,38,40,41,64,94]
passwordList=[]
def randomizer():
  capitalLetterInput = input('Input Number of Capital Letters ')
  lowerLetterInput = input('Input Number of Lowercase Letters ')
  numberInput = input('Input Number of Numbers ')
  symbolInput = input('Input Number of Symbols ')
  letterDigit = ""
    #adds random items to the final output
  for count in range(int(capitalLetterInput)):
    letterDigit += chr(random.randint(65,91))
  lowerLetterDigit = ""
  for count2 in range(int(lowerLetterInput)):
    lowerLetterDigit += chr(random.randint(97,122))
  numberDigit = 0
  for count3 in range(int(numberInput)):
    numberDigit += (random.randint(0,9))
  symbolsDigit = ""
  for count4 in range(int(symbolInput)):
    symbolsDigit += chr(random.randint(33,42))
  ui[1].append([letterDigit, lowerLetterDigit, numberDigit, symbolsDigit])
loginUser=[]
loginPass=[]
passwordToCheckList=[]
loginTries=5
home=[[]]
work=[[]]
entertainment=[[]]
bills=[[]]
catagory=["home,work,entertainment,bills"]
newUser=input("Are you a new user y or n ")
if newUser=="y":
  firstName=input("What is your first name ")
  lastName=input("What is your last name ")
  username=input("What will your username be ")
  loginUser.append(username)
passwordToCheck=input("Put in a letter, number, or symbol ")
passwordList.append(passwordToCheck)
while passwordToCheck!="stop":
  passwordToCheck=input("Put in a letter, number, or symbol ")
  if passwordToCheck!= "stop":
    passwordList.append(passwordToCheck-1)
if (len(passwordList)>=6 and (len(passwordList)<=16)):
    reqCheckList[0]=True
    #iterate throught passwordToCheck
    for i in range(len(passwordList)):
      #print(passwordToCheck[i])
      #convert letters to numbers with ord() ordinance
      #a-z on ASCII is range(97,123)
      if(ord(passwordList[i])) in range(97,123):
        reqCheckList[1]=True
      #A-Z on ASCII is range(65,91)
      elif(ord(passwordList[i])) in range(65,91):
        reqCheckList[2]=True
      #0-9 on ASCII is range(48,58)
      elif(ord(passwordList[i])) in range(48,58):
        reqCheckList[3]=True
      elif(ord(passwordList[i])in specialCharacters):
        reqCheckList[4]=True
    if(False in reqCheckList):
      print("Password did not meet the requirements, try again")
      passwordToCheckList=[]
      passwordToCheck=input("Put in a letter, number, or symbol ")
    else:
      print("Your password met the requirements")
      loginPass.append(passwordToCheckList)
newUser=input("Are you a new user y or n ")
if newUser=="n":
  login=input("What is your username ")
  loginPassword=input("What is your password ")
  if login or loginPassword not in len(loginUser) and len(loginPass):
    loginTries-=1
    print("Input your information again",loginTries,"tries remaining")
    loginUser=input("What is your username ")
    loginPass=input("What is your password ")
if loginTries==0:
  print("No more tries")
print("Welcome",loginUser)
print(catagory)
add=input("Would you like to add a catagory or open a catagory ")
if add=="add":
  add=input("What would you like to call the catagory ")
  catagory.append(add)
  print (catagory)
elif add=="open":
  add=input("What catagory would you like to open ")
  if add=="home":
    print(home)
    ui=input("Would you like to add, redo or delete a password")
    if ui=="add":
      user=input("What is the username ")
      home[0].append(user)
      home[1].append(randomizer())
    elif ui=="redo":
        ui=int(input("Input the number of your password that you want to "))-1
        passwordToCheck=input("Put in a letter, number, or symbol ")
        passwordList.append(passwordToCheck)
        while passwordToCheck!="stop":
          passwordToCheck=input("Put in a letter, number, or symbol ")
        if passwordToCheck!= "stop":
          passwordList.append(passwordToCheck-1)
        if (len(passwordList)>=6 and (len(passwordList)<=16)):
          reqCheckList[0]=True
        #iterate throught passwordToCheck
        for i in range(len(passwordList)):
          #print(passwordToCheck[i])
          #convert letters to numbers with ord() ordinance
          #a-z on ASCII is range(97,123)
          if(ord(passwordList[i])) in range(97,123):
            reqCheckList[1]=True
          #A-Z on ASCII is range(65,91)
          elif(ord(passwordList[i])) in range(65,91):
            reqCheckList[2]=True
          #0-9 on ASCII is range(48,58)
          elif(ord(passwordList[i])) in range(48,58):
            reqCheckList[3]=True
          elif(ord(passwordList[i])in specialCharacters):
            reqCheckList[4]=True
        if(False in reqCheckList):
          print("Password did not meet the requirements, try again")
          passwordToCheckList=[]
          passwordToCheck=input("Put in a letter, number, or symbol ")
        else:
          print("Your password met the requirements")
          home[1].append(passwordToCheck)
    elif ui=="delete":
      ui=int(input("Input the number for the password you want to remove "))-1
      home.remove(ui)
elif add=="work":
  print(work)
  ui=input("Would you like to add, redo or delete a password")
  if ui=="add":
    user=input("What is the username ")
    work[0].append(user)
    work[1].append(randomizer())
  elif ui=="redo":
    ui=input("Input the number of your password that you want to ")-1 #gets the ui-1
    passwordToCheck=input("Put in a letter, number, or symbol ")
    passwordList.append(passwordToCheck)
    while passwordToCheck!="stop":
      passwordToCheck=input("Put in a letter, number, or symbol ")
    if passwordToCheck!= "stop":
      passwordList.append(passwordToCheck)
    if (len(passwordList)>=6 and (len(passwordList)<=16)):
      reqCheckList[0]=True
      #iterate throught passwordToCheck
      for i in range(len(passwordList)):
        #print(passwordToCheck[i])
        #convert letters to numbers with ord() ordinance
        #a-z on ASCII is range(97,123)
        if(ord(passwordList[i])) in range(97,123):
          reqCheckList[1]=True
        #A-Z on ASCII is range(65,91)
        elif(ord(passwordList[i])) in range(65,91):
          reqCheckList[2]=True
        #0-9 on ASCII is range(48,58)
        elif(ord(passwordList[i])) in range(48,58):
          reqCheckList[3]=True
        elif(ord(passwordList[i])in specialCharacters):
          reqCheckList[4]=True
      if(False in reqCheckList):
        print("Password did not meet the requirements, try again")
        passwordToCheckList=[]
        passwordToCheck=input("Put in a letter, number, or symbol ")
      else:
        print("Your password met the requirements")
  elif ui=="delete":
    ui=int(input("Input the number for the password you want to remove "))-1 #gets the ui-1
    work.remove(ui)
  elif add=="entertainment":
    print(entertainment)
    ui=input("Would you like to add, redo or delete a password")
    if ui=="add":
      user=input("What is the username ")
      entertainment[0].append(user)
      entertainment[1].append(randomizer())
    elif ui=="redo":
      ui=input("Input the number of your password that you want to ")-1
      passwordToCheck=input("Put in a letter, number, or symbol ")
      passwordList.append(passwordToCheck)
      while passwordToCheck!="stop":
        passwordToCheck=input("Put in a letter, number, or symbol ")
      if passwordToCheck!= "stop":
        passwordList.append(passwordToCheck)
      if (len(passwordList)>=6 and (len(passwordList)<=16)):
        reqCheckList[0]=True
      #iterate throught passwordToCheck
      for i in range(len(passwordList)):
        #print(passwordToCheck[i])
        #convert letters to numbers with ord() ordinance
        #a-z on ASCII is range(97,123)
        if(ord(passwordList[i])) in range(97,123):
          reqCheckList[1]=True
        #A-Z on ASCII is range(65,91)
        elif(ord(passwordList[i])) in range(65,91):
          reqCheckList[2]=True
        #0-9 on ASCII is range(48,58)
        elif(ord(passwordList[i])) in range(48,58):
          reqCheckList[3]=True
        elif(ord(passwordList[i])in specialCharacters):
          reqCheckList[4]=True
      if(False in reqCheckList):
        print("Password did not meet the requirements, try again")
        passwordToCheckList=[]
        passwordToCheck=input("Put in a letter, number, or symbol ")
      else:
        print("Your password met the requirements")
    elif ui=="delete":
      ui=int(input("Input the number for the password you want to remove "))-1#gets the ui-1
      entertainment.remove(ui)
  elif add=="bills":
    print(bills)
    ui=input("Would you like to add, redo or delete a password")
    if ui=="add":
      user=input("What is the username ")
      bills[0].append(user)
      bills[1].append(randomizer())
    elif ui=="redo":
      ui=int(input("Input the number of your password that you want to "))-1
      passwordToCheck=input("Put in a letter, number, or symbol ")
      passwordList.append(passwordToCheck)
      while passwordToCheck!="stop":
        passwordToCheck=input("Put in a letter, number, or symbol ")
      if passwordToCheck!= "stop":
        passwordList.append(passwordToCheck)
      if (len(passwordList)>=6 and (len(passwordList)<=16)):
        reqCheckList[0]=True
      #iterate throught passwordToCheck
      for i in range(len(passwordList)):
        #print(passwordToCheck[i])
        #convert letters to numbers with ord() ordinance
        #a-z on ASCII is range(97,123)
        if(ord(passwordList[i])) in range(97,123):
          reqCheckList[1]=True
        #A-Z on ASCII is range(65,91)
        elif(ord(passwordList[i])) in range(65,91):
          reqCheckList[2]=True
        #0-9 on ASCII is range(48,58)
        elif(ord(passwordList[i])) in range(48,58):
          reqCheckList[3]=True
        elif(ord(passwordList[i])in specialCharacters):
          reqCheckList[4]=True
        if(False in reqCheckList):
          print("Password did not meet the requirements, try again")
          passwordToCheckList=[]
          passwordToCheck=input("Put in a letter, number, or symbol ")
        else:
          print("Your password met the requirements")
          loginPass.append(passwordToCheckList)
    elif ui=="delete":
      ui=int(input("Input the number for the password you want to remove "))-1#gets the ui-1
      entertainment.remove(ui)
white_check_mark
eyes
raised_hands







Send a message to Mason Camp
















