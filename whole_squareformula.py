def square_formula(a,b):
   if (a + b)**2 == pow(a,2)+ 2 * a* b + pow(b,2):
        print("It is valid if {:d}={:d}".format(a,b))

num_1=int(input("Enter the value for a: "))
num_2=int(input("Enter the value for b: "))

square_formula(num_1,num_2)