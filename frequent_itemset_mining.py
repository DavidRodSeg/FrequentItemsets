# Práctica 2: Maximal/Closed frequent itemsets (lenguaje de programación R o Python)

# Instrucciones:

# Utilice el dataset que se desee, puede ser uno creado por vosotros o cualquiera que descarguéis por internet. Tiene que ser en formato CSV. CONSEJO: utilizad un dataset pequeño en cuanto a numero de ítems y registros/transacciones
# Implemente un algoritmo que permita descubrir los maximal itemsets que existen en ese dataset.
# Implemente un algoritmo que permita descubrir los closed itemsets que existen en ese dataset.
# Entregue el código y el dataset, así como un fichero (txt, pdf) que explique cómo ejecutar el código. Debe incluir también una explicación a la metodología utilizada (explicación del algoritmo realizado).
# Importante: Se debe entregar un código con una implementación propia, sin invocar a librerías externas. Se permite el uso de una implementación externa para obtener previamente los frequent itemsets, pero en ese caso no se otorgará la máxima calificación.

# Evaluación: se analizará la limpieza y claridad del código. Se evaluará la eficiencia de los algoritmos cuando se ejecuten sobre un dataset modelo que se usará para todos los alumnos.

import csv
import matplotlib.pyplot as plt
from algorithms.fp_growth import fp_growth_algorithm
from algorithms.maximal_closed_itemsets import find_closed_maximal, find_frequent


#################### LOADING THE DATA SET ####################
dataset = []
with open("market.csv", mode="r") as file:
    csv_reader = csv.reader(file, delimiter=";")
    header = next(csv_reader)
    dataset.append(header)
    for row in csv_reader:
        dataset.append(row)

# plt.bar(support.index, support.values)
# plt.title("Soporte absoluto de cada característica")
# plt.xlabel("Características")
# plt.ylabel("Frecuencia")
# plt.show()


#################### FP-GROWTH ALGORITHM ####################
itemsets = fp_growth_algorithm(dataset)


#################### CLOSED AND MAXIMAL ITEMSETS ####################
closed, maximal = find_closed_maximal(itemsets, minimum_support=40)
print(f"CLOSED ITEMSETS: {closed}")
print(f"MAXIMAL ITEMSETS: {maximal}")