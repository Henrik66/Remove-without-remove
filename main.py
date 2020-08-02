def remove (inputlist, itemtoremove, outputlist):
  whensomethingisremoved = False

  for i in inputlist:
    print ("before if", i)
    if i == itemtoremove:
      print ("removed an item")
      whensomethingisremoved = True
    else:
      print ("after if", i)
      outputlist.append(i)

n = [1, 2, 3, 4, 5, 6, 7, 8,1]
output = []

remove (n, 1, output)
print (n)
print (output)
