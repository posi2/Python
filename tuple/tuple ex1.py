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
         counts[words[1]]=counts.get(words[1],0)+1

words=sorted([(value,key) for key,value in counts.items()],reverse=True)
print(words[0])

