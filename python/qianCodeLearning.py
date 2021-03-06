#轉換為四進制
def transQua(dec,fourList):
  i=0
  while(dec>=1):
    fourList.append(i)
    fourList[i]=int(dec%4)
    dec=dec/4
    i=i+1
  return fourList

#以自定義符號代替0123，用while loop
def transCode3(qianCode,fourList):
  j=0
  while(j<len(fourList)):
    qianCode.append(j)
    qianCode[j]=str(fourList[j])
    qianCode[j]=qianCode[j].replace("0","@")
    qianCode[j]=qianCode[j].replace("1","a")
    qianCode[j]=qianCode[j].replace("2","b")
    qianCode[j]=qianCode[j].replace("3","c")
    j = j+1

#以自定義符號代替0123，用for loop
def transCode5(qianCode,fourList):
  j=0
  for i in fourList:
    qianCode.append(j)
    qianCode[j]=str(i)
    qianCode[j]=qianCode[j].replace("0","@")
    qianCode[j]=qianCode[j].replace("1","a")
    qianCode[j]=qianCode[j].replace("2","b")
    qianCode[j]=qianCode[j].replace("3","c")
    j = j+1

#以自定義符號代替0123，用for loop2
def transCode2(qianCode,fourList):
  for j in range(len(fourList)):
    qianCode.append(j)
    qianCode[j]=str(fourList[j])
    qianCode[j]=qianCode[j].replace("0","@")
    qianCode[j]=qianCode[j].replace("1","a")
    qianCode[j]=qianCode[j].replace("2","b")
    qianCode[j]=qianCode[j].replace("3","c")

#第二種以自定義符號代替0123+output（但順序反了）
def transCode4(fourList):
  for i in fourList:
    number = str(i)
    for char in number:
      print(code[char.upper()],end='')

#第二種以自定義符號代替0123+output
def transCode(fourList):
  j=len(fourList)
  while(j>0):
    j=j-1
    number = str(fourList[j])
    for char in number:
      print(code[char.upper()],end='')
      
#以自定義符號代替0123 + output(簡化）
def transCode(fourList):
  j=len(fourList)
  while(j>0):
    j=j-1
    temp = str(fourList[j])
    print(code[temp],end='')
    
#輸出
def output(qianCode):
  print('qianCode is: ',end='')
  j=len(qianCode)
  while(j>0):
    j=j-1
    print(qianCode[j],end='')
  print()
  
  
#主程式
a = int(input('please enter a number:'))
myList =[]
myCode =[]
code={'0':'@', '1':'a', '2':'b', '3':'c'}
transQua(a,myList)
print('qianCode is: ',end='')
transCode(myList)
print()
transCode2(myCode,myList)
output(myCode)
