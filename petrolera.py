import numpy as np
import random

def simular_exploracion(n_simulaciones=10, costo_exploracion=1_000_000, barriles=300_000, precio_barril=150):
    prob_exito = 0.4  # Probabilidad de encontrar petróleo
    porcentaje_empresa = 0.6  # Porcentaje de ganancia para la empresa
    
    exitos = 0
    fracasos = 0
    ganancias = []
    
    for _ in range(n_simulaciones):
        exito = random.random() < prob_exito  # Determinar si se encuentra petróleo
        if exito:
            ganancia = (barriles * precio_barril * porcentaje_empresa) - costo_exploracion
            exitos += 1
        else:
            ganancia = -costo_exploracion
            fracasos += 1
        
        ganancias.append(ganancia)
    
    ganancias = np.array(ganancias)
    promedio = np.mean(ganancias)
    desviacion = np.std(ganancias)
    
    reporte = f'''
    Simulaciones realizadas: {n_simulaciones}
    Veces que se encontró petróleo: {exitos}
    Veces que no se encontró nada: {fracasos}
    Ganancias netas por expediciones exitosas: {exitos * (barriles * precio_barril * porcentaje_empresa)} USD
    Pérdidas totales de las expediciones fallidas: {fracasos * costo_exploracion} USD
    Ganancias totales: {sum(ganancias)} USD
    Umbral de éxito: {exitos / n_simulaciones:.2%}
    Desviación estándar: {desviacion:,.2f} USD
    '''
    print(reporte)
    
    return ganancias

# Ejecutar la simulación
resultados = simular_exploracion(n_simulaciones=1000)
