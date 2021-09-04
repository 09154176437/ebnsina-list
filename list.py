nomarat = [20,19,20,12,15]
for ozv in nomarat:
    print(ozv)







nomarat = [20,19,20,12,15]
comp = int(input())
nomarat.append(comp)
print(nomarat)








nomarat = [20,19,20,12,15]
adad = int(input())
nomarat.insert(1,adad)
print(nomarat)




adadha = []

for adadhaye in range(100,1000):
    yekan= adadhaye %10
    dahgan=(adadhaye//10)%10
    sadgan=adadhaye //100
    if(yekan**3+dahgan**3+sadgan**3 == adadhaye):
            adadha.append(adadhaye)
print(adadha)

