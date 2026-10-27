import matplotlib.pyplot as plt
import numpy as np

# Nicole Robles NC = 0120
cant_productos = [100, 150, 200, 300, 500]
precio = [4000, 7000, 9000, 12000, 18000]

# personalizar gradica
plt.plot(
    cant_productos,
    precio,
    color="pink",
    marker="o",
    linestyle="--",
    linewidth=2,
    markersize=12,
)
plt.title("Ventas de walmart 0120")
plt.xlabel("precios")
plt.ylabel("cant prod")
plt.show()