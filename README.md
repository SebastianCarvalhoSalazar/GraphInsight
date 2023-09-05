# GraphInsight

## Tabla de Contenidos
- [Creación de un Dataset Sintético](#Creación-de-un-Dataset-Sintético)
- [Descripción del Problema](#descripción-del-problema)
- [Componentes Clave](#componentes-clave)
  - [Grafo Bipartito](#grafo-bipartito)
  - [Clase: RecomendationSystem](#clase-recomendationsystem)
- [Dependencias](#Dependencias)

## Creación de un Dataset Sintético

En esta sección, se explica cómo crear un dataset sintético utilizando Python y Pandas. Este dataset se puede utilizar para pruebas y experimentación en proyectos de recomendación u otros escenarios donde se requiera un conjunto de datos ficticio.

## Creación de un Dataset Sintético

```python
import pandas as pd
import random

# Crear una lista de clientes y productos aleatorios
clientes = [f'Cliente{i}' for i in range(1, 1001)]  # Generar 1000 clientes
productos = [f'Producto{i}' for i in range(1, 21)]  # Generar 20 productos

# Generar relaciones aleatorias
relaciones = []
for _ in range(5000):
    cliente = random.choice(clientes)
    producto = random.choice(productos)
    relaciones.append((cliente, producto))

# Crear un DataFrame de pandas
df = pd.DataFrame(relaciones, columns=['source', 'target'])

# Guardar el DataFrame en un archivo CSV
df.to_csv('dataset.csv', index=False, sep=';')
```

## Descripción del Problema

El problema que se busca resolver con este sistema de recomendación es proporcionar a los usuarios una lista de productos recomendados en función de su similitud con otros usuarios. El sistema se basa en un grafo bipartito en el que los nodos se dividen en dos particiones: usuarios y productos. La similitud entre usuarios se calcula mediante la cantidad de productos que comparten en común. Luego, se recomiendan productos a un usuario en función de la similitud con otros usuarios que tienen productos que el usuario aún no ha utilizado.

## Componentes Clave

### Grafo Bipartito
El sistema utiliza la biblioteca NetworkX para crear y manipular un grafo bipartito. En este grafo, los nodos se dividen en dos particiones: usuarios y productos. Cada nodo en el grafo representa un usuario o un producto, y las aristas conectan usuarios con los productos que han interactuado.

### Clase `RecomendationSystem`
La clase `RecomendationSystem` contiene los principales métodos para construir el grafo bipartito, calcular la similitud entre usuarios y generar recomendaciones de productos. Estos métodos incluyen:

- `_setPartitions(G, df)`: Este método establece las particiones de los nodos del grafo bipartito en función de los datos proporcionados en un DataFrame de entrada.

- `_buildGraph(df)`: Construye el grafo bipartito a partir de los datos de interacción proporcionados en un DataFrame. Además, asigna las particiones a los nodos del grafo.

- `_shared_partition_nodes(G, node1, node2)`: Calcula los nodos compartidos entre dos nodos de la misma partición (ya sea usuarios o productos).

- `_user_similarity(G, user1, user2, proj_nodes)`: Calcula la similitud entre dos usuarios en función de los proyectos (productos) compartidos. Esta similitud se utiliza para identificar usuarios similares.

- `_most_similar_users(G, user, user_nodes, proj_nodes)`: Encuentra los usuarios más similares a un usuario dado en función de sus interacciones con productos similares.

- `_recommend(G, from_user, to_user)`: Genera recomendaciones de productos para un usuario en función de las diferencias en sus interacciones con productos.

- `_predict(df, G)`: Realiza recomendaciones para los usuarios utilizando el grafo bipartito construido y los datos de interacción proporcionados en un DataFrame.

## Dependencias

Este código depende de las siguientes bibliotecas de Python:

- **collections**: Utilizada para `defaultdict` y `Counter`.
- **networkx**: Usada para la construcción y análisis del grafo bipartito.
- **numpy**: Necesaria para realizar operaciones numéricas.
- **pandas**: Utilizada en la manipulación de datos.
- **statistics**: Usada para calcular la moda.
