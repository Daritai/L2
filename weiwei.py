x = int(input("數學："))
y = int(input("英文："))

if x >= 90 and y >= 90:
    print("有獎品")
elif x < 60 and y < 60:
    print("要處罰")
elif x < 60 or y < 60:
    print("要加油")
else:
    print("平凡")