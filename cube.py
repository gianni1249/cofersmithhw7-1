# Function cb()

def cb(x):
    x = x*x*x
    print x 
    return;

# Calling function cb() for odd numbers 

for i in range(20):
    if i%2 == 0: 
        print i
    else:
        cb(i)
