from strats import next_fit, fit_first, best_fit, waste

objects = [3, 4, 1, 2]
c = 5

print("Objects: "+str(objects)+", c: "+str(c)+"\n")

print("Next fit:")
next_fit(objects, c, pp = True)
print("waste: "+str(waste(next_fit, objects, c))+"\n")

print("Fit first:")
fit_first(objects, c, pp = True)
print("waste: "+str(waste(fit_first, objects, c))+"\n")

print("Best fit:")
best_fit(objects, c, pp = True)
print("waste: "+str(waste(best_fit, objects, c))+"\n")
