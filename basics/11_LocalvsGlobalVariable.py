def show():
    x = 5  #local
    print(x)

x = 10 #global
show()

#Local variable has precedence over global variable

print(x) # 10 is outside the function , for 5 we use return value