def remove (inputlist, itemtoremove, outputlist):
  for i in inputlist:
    if i!=itemtoremove:
      outputlist.append(i)

n = [1, 2, 3, 4, 5, 6, 7, 8,1]
output = []

remove (n, 1, output)
print (n)
print (output)
