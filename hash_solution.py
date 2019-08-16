# importing our library of hashing algorithms
import hashlib
from hashlib import md5
FIND='1c215fc1acf3ee6c9d0dc527d5b9cb62'
import os
for filename in os.listdir(os.getcwd() + '/suspicious_files/'):
 print("file: " + filename)
 with open('suspicious_files/' + filename, 'rb') as afile:
  # read the selected file
  buf = afile.read()
  print("contents: " + buf)
  # assigning the hash value to a new varible
  hash = md5(buf).hexdigest()
  if hash == FIND:
   print("\033[5;31;38mhash: " + hash + '\n  	' + FIND + '\n \033[0m ')
   print("MATCH!")
   break
