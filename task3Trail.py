A1=["ele11","ele2","ele9","ele7","ele12","ele9","ele4","ele5","ele10","ele13","ele8"]

A2=["ele1","ele3","ele2","ele11","ele7","ele10"]
A2, A1 = zip(*sorted(zip(A2, A1)))

print(A1)
print(A2)
