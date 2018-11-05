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
        # print(words)
         if(len(words)>2):
               word=words[5].split(':')
               counts[word[0]]=counts.get(word[0],0)+1

print(sorted([(value,key) for key,value in counts.items()],reverse=True))

