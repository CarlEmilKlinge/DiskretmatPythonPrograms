import math

def FindCommonPrimeFactor(a, m):
    Primes = FindPrimesBelow(min(a,m))
    for i in Primes:
        if(a%i==0 and m%i==0):
            return(i)
        
def find_smallest_common_prime_factor(a,m):
    return FindCommonPrimeFactor(a,m)
        

def FindPrimesBelow(number):
    Primtal = [2]
    for i in range(3, number, 2):
        isPrimtal = True
        for j in Primtal:
            if i%j==0:
                isPrimtal = False
                break
        if isPrimtal:
            Primtal.append(i)
    return Primtal
    
if __name__ == "__main__":
    while(True):
        # a is congruent to 1 mod m    a \equiv 1 \text{ mod } m
        try:
            a = int(input("Select a: "))        
            m = int(input("Select m: "))
        except:
            continue
        AnswerFound = False


        mIsNegative = m<0

        for i in range(abs(m)):
            if mIsNegative:
                if a*i%m != 1+m:
                    continue
            elif a*i%m != 1:
                continue

            s = i
            t = -math.floor((a*i)/m)
            if mIsNegative:
                t-=1

            print(f"s = {s}")
            print(f"t = {t}")
            print()
            print("sa+tm=1")
            print(f"({s}*{a})+({t}*{m})=1")
            AnswerFound = True
            break
        if not AnswerFound:
            print("No answer")
            print(f"The common primefactor is: {FindCommonPrimeFactor(a,m)}")
        print()


def find_primes_below(number):
    return FindPrimesBelow(number)
