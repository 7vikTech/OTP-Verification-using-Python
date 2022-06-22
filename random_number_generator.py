import os
import math
import random
import smtplib

# generate random number and storing it in a variable which I will be # using while sending email to users

digits="0123456789"
OTP=""
for iterate_variable in range(6):
    OTP += digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
message = otp