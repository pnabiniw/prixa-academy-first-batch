hour = int(input("Enter total work hour "))
rate = float(input("Enter hourly rate in Rs. "))

if hour <= 40:
    pay = hour * rate

else:
    overtime = hour - 40
    normal_pay = 40 * rate
    ot_pay = overtime * rate * 1.5
    pay = normal_pay + ot_pay

print("Gross payment is ", pay)