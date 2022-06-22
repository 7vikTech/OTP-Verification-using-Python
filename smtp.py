import os
import math
import random
import smtplib

# you need to have your Google app password to be able to send emails  # using your Gmail account
# Copy that key and paste in the code below

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("Your Gmail Account", "You app password")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")