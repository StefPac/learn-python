passwords = ["cat", "dog", "1234", "password", "leo"]
real_password = "leo"
for guess in passwords:
    print("Trying:", guess)
if guess == real_password:
    print("🚨 CRACKED:", guess)
    break
