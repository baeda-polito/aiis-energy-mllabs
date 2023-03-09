import matplotlib.pyplot as plt
import numpy as np

# Generiamo dei dati di esempio
x = np.linspace(0, 10, 100) # generiamo 100 valori equidistanti tra 0 e 10
y = 2*x + 1 # la funzione lineare y = 2x + 1

# Creiamo il plot
plt.plot(x, y)

# Aggiungiamo delle etichette agli assi e un titolo
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funzione Lineare')

# Mostriamo il plot
plt.show()