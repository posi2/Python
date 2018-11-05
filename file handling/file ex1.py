fname=input("Enter file name")
try:
  fhand=open(fname)
except:
  print("file can't open",fname)
  quit()

count=0
for line in fhand:
   count=count+1
   line=line.rstrip() #remove whitespacce
   print(line.upper())

print('total number of lines',count)
