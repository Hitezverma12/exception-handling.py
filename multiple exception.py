try:
    num1, num2 = eval(input("enter two numbers, seperated but comma : "))
    result = num1/num2
    print("Result is",result)

except ZeroDivisionError :
    print("division by zero is error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


except SyntaxError:
    print("comma is missing. print numbers like 1, 2")

except:
    print("wrong input")

else:
    print("no exceptions")

finally:
    print("this will euxecute no matter what")
