import hashlib,os

def hash_file(filePath):
   

   """"This function returns the SHA-1 hash
   of the file passed into it"""

#    h = hashlib.sha1()
   h = hashlib.sha256()

   with open(filePath,'rb') as file:

       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)

   return h.hexdigest()


