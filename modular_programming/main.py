# import operators Module
import operators
import others
import trig

#build a better calculator
x=others.cube(9)
y=operators.divide(7,8)

print(x)

operator=input("Enter sign:")

if operator=="cube":
    num=eval(input("Enter number:"))
    x=others.cube(num)
    print(x)

elif operator=="sin":
    angle=eval(input("Enter angle in degrees:"))
    x=trig.get_sine(angle)
    print(x)

elif operator=='tan':
    angle1=eval(input("Enter angle in degrees here:"))
    y=trig.get_tan(angle1)  
    print(y) 

elif operator =='cos':
    angle2=eval(input("Enter angle in degrees here:"))
    v=trig.get_cos(angle2)
    print(v)    

else:
    num1=eval(input("Enter number1:"))
    num2=eval(input("Enter number2:"))    
 
    if operator =="+":
        x=operators.add(num1,num2)
        print(x)

    elif operator=="-":
        y=operators.subtract(num1,num2)  
        print(y)  

    elif operator=="/":
        z=operators.divide(num1,num2)
        print(z)    

    elif operator=='*' or "x" or "X":
        w=operators.multiply(num1,num2)
        print(w)    

   



