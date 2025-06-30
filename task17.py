baho = int(input("Bahoingizni kiriting:"))
if baho >=90 and baho <= 100:
    print("A'lo")
elif baho >=80 and baho <= 89:
    print("Yaxshi")
elif baho >=70 and baho <= 79:
    print("Qoniqarli")
elif baho >=60 and baho <= 69:
    print("Qoniqarsiz")
elif baho >=0 and baho <= 59:
    print("Yomon")
else:
    print("Ball 0-100 oralig'ida bo'lishi kerak!")
