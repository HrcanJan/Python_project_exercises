def snowflake(bob, lengthSide, levels): 
    if levels == 0: 
        bob.forward(lengthSide) 
        return
    lengthSide /= 3.0
    snowflake(bob, lengthSide, levels-1) 
    bob.left(60) 
    snowflake(bob, lengthSide, levels-1) 
    bob.right(120) 
    snowflake(bob, lengthSide, levels-1) 
    bob.left(60) 
    snowflake(bob, lengthSide, levels-1) 
  
import turtle
bob=turtle.Turtle()
bob.speed(0)                    
length = 450.0   
bob.penup()                      
bob.backward(length/2.0) 
bob.pendown()            
for i in range(3):    
    snowflake(bob, length, 4) 
    bob.right(120)
