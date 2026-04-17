Procesado en: 1 minuto 39 segundos

# **Funciones de activacion, costo y optimizadores**

## **Funciones de activación, costo y optimizadores para dummies**

#### **Función de activación**

- Es una función matemática que se le aplica a la salida (neta) de cada neurona para decir cuanto contribuye a la siguiente capa\*
- Introduce la no linealidad
  - Si yo tuviera una capa con función de activación lineal (o lo mismo, que salga neta derecho), y mi modelo no hace buenos cortes, entonces mi pensamiento sería agregar otra capa
  - Sin embargo, si agrego capas lineales sigue siendo transformaciones lineales, ya que lo unico que hago es "multiplicar" los valores, por lo que sería igual a seguir teniendo una capa pero cambiando otras cosas (hiperparametros diferentes, mismo resultado pobre de no hacer buenos cortes)
    - Pensa que lo que hace un ejemplo (que en realidad es un vector de valores numéricos) al pasar por la red es ser multiplicada por los pesos de la capa (que es una matriz en si)
    - Entonces, un ejemplo al pasar por la red lo que hace es ser multiplicado por matrices en cada capa
    - Si tengo tres capas lineales, multiplique tres veces
    - Pero, las multiplicaciones con matrices lineales son asociativas, entonces la capacidad "de corte" de cada capa en realidad sigue siendo un corte lineal
- Las funciones de activación son
  - Sigmoide => Explicación aqui
  - tanh => Explicación aquí
  - Softmax => Explicación aquí
  - ReLU => Brevemente explicada aquí

### **Función de costo**

- Es la que uno usa para derivar para calcular el gradiente
  - Por ejemplo, no es la misma si uso estocastico puro o por lotes (en esta, hay que promediar con el tamaño del lote)
- ¿Qué necesita una función de costo para ser una buena función de costo?
  - Depende para que, se necesita que sea derivable. Pero como NOSOTROS SIEMPRE USAMOS GRADIENTE, DEBE SER DERIVABLE
  - Tener valor positivo SIEMPRE
  - Valer 0 cuando la función neta se acerca al valor correcto :)
  - Alejarse de 0 (es decir, agrandar la groseridad del error) cuando la función esta mal

| Tipo de problema         | Función de costo típica        |  |
|--------------------------|--------------------------------|--|
| Clasificación binaria    | Binary Cross-Entropy Aquí      |  |
| Clasificación multiclase | Categorical Cross-Entropy Aquí |  |
| Regresión                | Mean Squared Error (MSE)       |  |

#### **Función de error**

Es la diferencia entre la respuesta que se quería y lo que se predijo

#### **Optimizador**

- Es el algoritmo que ajusta los pesos de la red para minimizar la función de costo
- Sirve de guía para el aprendizaje modificando los parametros en la función del gradiente
- Si vez a la función de costo como el grafico en 3D donde hay un "pozo" al que se quiere llegar, el optimizador es la que le dice como moverse a "la pelota" para llegar a ese pozo\* **Ejemplos comunes:**

| Optimizador                          | Características                                       | Explicación                                    |
|--------------------------------------|-------------------------------------------------------|------------------------------------------------|
| SGD (Stochastic<br>Gradient Descent) | Simple, puede ser lento                               | Clase 3 > Técnica del<br>descenso de gradiente |
| Momentum                             | Acelera el aprendizaje acumulando<br>gradientes       | Clase 7 > Momento                              |
| RMSProp                              | Ajusta el paso según la magnitud<br>de los gradientes | Clase 7 > RMSprop                              |
| Adam                                 | Combina Momentum + RMSProp,<br>el más usado           | Clase 7 > ADAM                                 |

### **Relación entre función de activación y función de costo**

| Función<br>de costo ↓<br>/<br>Activación<br>→ | Sigmoid                                                                                               | Tanh                                                                                 | ReLU                                                                       | Softmax                                                    | Lineal                                                     |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|
| Entropia<br>cruzada<br>binaria                | ✅ Sí —<br>ambas<br>producen<br>valores en [0,<br>1]<br>,<br>interpretables<br>como<br>probabilidades. | ⚠️<br>No ideal<br>— salida en<br>[-1,1], no<br>representa<br>bien<br>probabilidades. | ❌️<br>No —<br>ReLU no está<br>acotada; no<br>sirve para<br>probabilidades. | ❌️No —<br>Softmax es<br>para<br>multiclase, no<br>binaria. | ❌️<br>No —<br>salida sin<br>límites, no<br>probabilística. |

| Función<br>de costo ↓<br>/<br>Activación<br>→ | Sigmoid                                                                                                    | Tanh                                                                                     | ReLU                                                                        | Softmax                                                                                          | Lineal                                                                    |
|-----------------------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Entropia<br>cruzada<br>categorica             | ⚠️<br>Posible<br>pero rara —<br>para 2 clases<br>se puede usar<br>sigmoid, pero<br>no para<br>multiclase.  | ❌️<br>No —<br>salida en<br>1], no<br>[−1,<br>tiene sentido<br>como<br>probabilidad.      | ❌️No —<br>salida no<br>normalizada,<br>no representa<br>distribución.       | ✅<br>Sí —<br>Softmax<br>genera una<br>distribución<br>de<br>probabilidad<br>sobre las<br>clases. | ❌️No — no<br>limita ni<br>normaliza las<br>salidas.                       |
| Error<br>cuadrático<br>medio                  | ⚠️<br>Se puede,<br>pero no ideal<br>— funciona,<br>pero el<br>gradiente es<br>lento para<br>clasificación. | ⚠️<br>Sí, pero<br>poco<br>eficiente —<br>históricamente<br>usada, pero<br>converge peor. | ⚠️<br>Sí en<br>regresión (no<br>en<br>clasificación)<br>— puede<br>saturar. | ❌️<br>No —<br>Softmax con<br>MSE no<br>refleja bien<br>las diferencias<br>probabilísticas.       | ✅<br>Sí —<br>ideal en<br>regresión,<br>salida lineal<br>sin límites.      |
| Error                                         | ⚠️<br>Posible —<br>pero menos<br>sensible que<br>MSE.                                                      | ⚠️<br>Sí, pero<br>lenta<br>convergencia.                                                 | ✅<br>Sí<br>(regresión) —<br>útil si hay<br>outliers.                        | ❌️No —<br>Softmax con<br>MAE no tiene<br>sentido.                                                | ✅<br>Sí<br>(regresión)<br>—<br>predicciones<br>reales, sin<br>saturación. |

#### **Resumen de cuando y donde usarla**

| Problema                        | Capa de Salida                | Función de Costo                | Función de<br>Activación (Salida) |
|---------------------------------|-------------------------------|---------------------------------|-----------------------------------|
| Clasificación Binaria           | 1 neurona                     | Entropía Cruzada<br>Binaria     | Sigmoid                           |
| Clasificación<br>Multiclase     | N neuronas (una<br>por clase) | Entropía Cruzada<br>Categórica  | Softmax                           |
| Regresión                       | 1 o N neuronas                | Error Cuadrático<br>Medio (MSE) | Lineal (Ninguna)                  |
| Regresión Robusta a<br>Outliers | 1 o N neuronas                | Error Absoluto Medio<br>(MAE)   | Lineal (Ninguna)                  |

**Para las capas ocultas, usa ReLU (o Leaky ReLU / PReLU) en la gran mayoría de los casos.**