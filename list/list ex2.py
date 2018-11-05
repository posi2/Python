fname=input("Enter file name")
try:
  fhand=open(fname)
except:
  print("file can't open",fname)
count=0
for line in fhand:
  if line.startswith('From'):
    words=line.split()
    count=count+1
    print(words[1])
print("There were",count,"lines in the file with From as the first word")
