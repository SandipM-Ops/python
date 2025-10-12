password="Sandip"
length = len(password)
if length<6:
    so="week"
elif length<10:
    so="Medium"
else:
    so="Strong"
print("your Password is",so)