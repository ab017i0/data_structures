x = float(input("Enter value for x: "))
c = int(input("Enter number of times x is repeated: "))

limit = c - 1
temp = x
counter = 0
def x_modifier(temp):
    
    global counter
    global x
    
    z = x + 1 / temp
    counter += 1
    
    if counter < limit:
        
        y = x + 1 / z
        return x_modifier(y)
        
    else:
        return 1 / z

y = x_modifier(x)
# Write your code here.

print("y =", y)