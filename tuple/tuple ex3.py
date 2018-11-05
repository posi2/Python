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
         for word in words:
                 word=word.lower()
               #  print(word)
		 for i in range(len(word)):
		       if word[i].isalpha():
		           counts[word[i]]=counts.get(word[i],0)+1
print(sorted(counts.items()))

