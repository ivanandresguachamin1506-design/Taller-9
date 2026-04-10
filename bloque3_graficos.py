import pandas as pd
import matplotlib.pyplot as plt
datos = {
'reactor': ['R1','R1','R1','R2','R2','R2','R3','R3'],
'turno': ['mañana','tarde','noche','mañana','tarde','noche','mañana','tarde'],
'temperatura': [85, 92, 78, 95, 88, 91, 76, 83],
'eficiencia': [91.2, 87.5, 94.1, 83.3, 89.7, 85.0, 96.4, 92.8],
'incidentes': [0, 1, 0, 2, 0, 1, 0, 0]
}
#Separación para obtener distinta respuesta 
promedio_temp = df.groupby('reactor')['temperatura'].mean()
plt.figure(figsize=(7, 4))
plt.bar(promedio_temp.index, promedio_temp.values, color='brown')
plt.title('Temperatura promedio por reactor')
plt.xlabel('Reactor')
plt.ylabel('Temperatura (C)')
plt.tight_layout()
plt.show()
#Separación para obtener distinta respuesta 
plt.figure(figsize=(7, 4))
ream = df.groupby('temperatura')['eficiencia'].mean()
plt.scatter( ream.index, ream.values , color='coral', s=80)
plt.title('Temperatura vs Eficiencia')
plt.xlabel('Temperatura (C)')
plt.ylabel('Eficiencia (%)')
plt.tight_layout()
plt.show()
#Función extra para poder unir los puntos de la grafica antes determinada. 
plt.figure(figsize=(8, 4))
plt.plotream = df.groupby('temperatura')['eficiencia'].mean()
plt.plot( ream.index, ream.values , color='coral',)
plt.title('Eficiencia por medicion')
plt.xlabel('Numero de medicion')
plt.ylabel('Eficiencia (%)')
plt.tight_layout()
plt.show()
#Separación para obtener distinta respuesta 
plt.figure(figsize=(8, 4))
plt.plot( df.index , df['eficiencia'])
plt.title('Eficiencia por medicion')
plt.xlabel('Numero de medicion')
plt.ylabel('Eficiencia (%)')
plt.tight_layout()
plt.show()
