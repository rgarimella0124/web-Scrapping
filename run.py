
filepath = 'test.txt'
substring = "reviewRating"
with open(filepath) as fp:  
   line = fp.readline()
   cnt = 1
   flag = False
   while line:
       if substring in line:
            print("string found in line {}".format(cnt))
            flag = True
            break
       line = fp.readline()
       cnt += 1
   if not flag:
       print("string not found in file")

"""
fname = "test.txt"
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)
"""


p = str(soup.find('script', {'type':'application/ld+json'}))