#Simulate OTP/PIN/PASSWORD Verification system
import random 
actual_otp = random.randint(1000,9999)
print(actual_otp)

attempts = 3

while attempts:
    (user_otp)=int(input("Enter the OTP"))
    if len(str(user_otp)) !=4:
        print("OTP must be four digits")
    if user_otp==actual_otp:
        print("Correct OTP- Transaction Successfull")
        break
    attempts=attempts-1

else:
    print("Maximum attempts reached,Try after 24 hrs")

