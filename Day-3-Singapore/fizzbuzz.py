#import pdb
user_input_int=int(input("Enter n:"))

def cout(output):
    print(output, end='\n')
    
for i in range(1,user_input_int+1):
    if i%5==0 and i%3==0 :
        #pdb.set_trace()
        cout("fizzbuzz")
    elif i%3 ==0:
        #pdb.set_trace()
        cout("fizz")
    elif i%5==0 :
        #pdb.set_trace()
        cout("buzz")
    else:
        #pdb.set_trace()
        cout(i)
