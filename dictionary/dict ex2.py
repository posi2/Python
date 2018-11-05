fname=input("Enter file name")
try:
  fhand=open(fname)
except:
  print("file can't open",fname)
counts=dict()
words=list()
for line in fhand:
   if line.startswith('From'):
         words=line.split()
         if words[1] not in counts:
            counts[words[1]] = 1
         else:
            counts[words[1]] += 1

print(counts)
              
