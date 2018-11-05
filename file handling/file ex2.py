import re
fname=input("Enter file name")
try:
  fhand=open(fname)
except:
  print("file can't open",fname)
  quit()
sum=0
count=0
for line in fhand:
  line=line.rstrip()
  if line.startswith('X-DSPAM-Confidence:'):
    s=re.findall(r'-?\d+\.?\d*',line)
    count=count+1
    sum=sum+float(s[0]) 
average=sum/count
print('Average Spam Confidence:',average)
