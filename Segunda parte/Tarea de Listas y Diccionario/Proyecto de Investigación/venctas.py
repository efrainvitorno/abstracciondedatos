import numpy as np
from sklearn.linear_model import LinearRegression

# Datos históricos
X = np.array([
    [2000, 3000, 1000, 200, 3000],
    [2500, 2800, 1200, 220, 2900],
    [3000, 3500, 1500, 250, 3200],
    # Se pueden agregar más filas de datos según sea necesario
])

Y = np.array([5000, 4800, 5500])

# Crear el modelo
model = LinearRegression()

# Ajustar el modelo con los datos
model.fit(X, Y)

# Valores proyectados para las variables independientes
X_new = np.array([[3500, 3200, 1800, 300, 3500]])

# Realizar la predicción
Y_pred = model.predict(X_new)

# Calcular el presupuesto total de marketing
presupuesto_marketing = np.sum(X_new)

# Calcular el porcentaje del presupuesto en relación con las ventas proyectadas
porcentaje_presupuesto = (presupuesto_marketing / Y_pred[0]) * 100

# Resultados
print("Ventas proyectadas:", Y_pred[0])
print("Presupuesto de marketing proyectado:", presupuesto_marketing)
print("Porcentaje del presupuesto sobre las ventas proyectadas:", porcentaje_presupuesto)
