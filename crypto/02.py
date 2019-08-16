import hashlib

message = "Learning Python 3, yea!!!"
h = hashlib.sha256()
h.update(message.encode('utf-8'))
print("MESSAGE:", message)
print(" SHA256:", h.hexdigest())

len(h.hexdigest()) * 4
