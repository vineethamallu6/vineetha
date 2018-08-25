#define the gen_primes function here
def genPrimes():
   num = 2
   prime = True
   while True:
       if prime == True:
           yield num
       num = num + 1
       for i in range(2,num):
           if num % i == 0:
               prime = False
               break
       else:
           prime = True
n = int(input())
primenum = genPrimes()
for i in range(n):
   print(primenum.__next__())

def main():
    data=input()
    l=data.split()
    a=int(l[0])
    b=int(l[1])
    primeGenerator = genPrimes()
    for i in range(a):
        p=primeGenerator.next()
        if(i%b==0):
            print(p)
    
if __name__== "__main__":
    main()
