def remove (inputlist, itemtoremove, outputlist):
  whensomethingisremoved = False
  for i in inputlist:
    if i == itemtoremove and whensomethingisremoved == False :
      whensomethingisremoved = True
    else:
      outputlist.append(i)

n = [1, 2, 3, 4, 5, 6, 7, 8,4, 4]
output = []

userinput = input("Enter the number you want removed: ")
usernumber = int(userinput)
remove (n, usernumber, output)
print (n)
print (output)
