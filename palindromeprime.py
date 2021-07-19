start = eval(input("Enter the start point N: \n"))
end = eval(input("Enter the end point M: \n"))
print("The palindromic primes are: ")
# defining my functions
def neo(x):
    for y in range (2,x):
        if x%y == 0:
            return False
    return True
for z in range (start+1 , end):
    w=z
    reverse = 0
    while z>0:
        digit =z%10
        z = z//10
        reverse = reverse*10 +digit
    if w==reverse:
        if(neo(w)):
            print(w)