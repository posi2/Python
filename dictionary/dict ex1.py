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
         if(len(words)>2):
             if words[2] not in counts:
                counts[words[2]] = 1
             else:
                counts[words[2]] += 1

print(counts)
              
#count Number of the time word come
