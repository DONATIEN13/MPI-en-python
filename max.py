# Dounia DOnatien

#programme sequentiel en pyhton qui fait la recherche du plus grang element dans une liste

# le temps d'execution est 2.67e-05 s

import time

data = [1, 2, 8, 4, 5, 6]

x = data[0]

start = time.time()

for i in range(1, len(data)):
	if x < data[i]:
		x = data[i]
print("La plus grande valeur de la liste est: ", x)

end = time.time()

print("Le temp d'execution est:", end-start)