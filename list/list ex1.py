fname=input("Enter file name")
try:
  fhand=open(fname)
except:
  print("file can't open",fname)
final_list=list()
for line in fhand:
    for i in line.split():
      if i not in final_list:
        final_list=final_list+[i]

final_list.sort()
print(final_list)
#store only one copy of each word in file
