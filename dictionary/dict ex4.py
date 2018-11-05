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
         domain=words[1].split('@')
         if(len(domain)>1):
		 if domain[1] not in counts:
		    counts[domain[1]] = 1
		 else:
		    counts[domain[1]] += 1

print(counts)
#find domain name of the email condition mail start with FROM
