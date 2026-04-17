

# Funciones de activacion, costo y optimizadores

# Funciones de activación, costo y optimizadores para

dummies

# Función de activación

* Es una función matemática que se le aplica a la salida (neta) de cada neurona para decir cuanto contribuye a la siguiente capa*
* Introduce la no linealidad
* Si yo tuviera una capa con función de activación lineal (o lo mismo, que salga neta derecho), y mi modelo no hace buenos cortes, entonces mi pensamiento sería agregar otra capa
* Sin embargo, si agrego capas lineales sigue siendo transformaciones lineales, ya que lo unico que hago es "multiplicar" los valores, por lo que sería igual a seguir teniendo una capa pero cambiando otras cosas (hiperparametros diferentes, mismo resultado pobre de no hacer buenos cortes)
* Pensa que lo que hace un ejemplo (que en realidad es un vector de valores numéricos) al pasar por la red es ser multiplicada por los pesos de la capa (que es una matriz en si)
* Entonces, un ejemplo al pasar por la red lo que hace es ser multiplicado por matrices en cada capa
* Si tengo tres capas lineales, multiplique tres veces
* Pero, las multiplicaciones con matrices lineales son asociativas, entonces la capacidad "de corte" de cada capa en realidad sigue siendo un corte lineal
* Las funciones de activación son
* Sigmoide => Explicación aqui
* tanh => Explicación aquí
* Softmax => Explicación aquí
* ReLU => Brevemente explicada aquí
# Función de costo

* Es la que uno usa para derivar para calcular el gradiente
* Por ejemplo, no es la misma si uso estocastico puro o por lotes (en esta, hay que promediar con el tamaño del lote)
* ¿Qué necesita una función de costo para ser una buena función de costo?
* Depende para que, se necesita que sea derivable. Pero como NOSOTROS SIEMPRE USAMOS GRADIENTE, DEBE SER DERIVABLE
* Tener valor positivo SIEMPRE
* Valer 0 cuando la función neta se acerca al valor correcto :)
* Alejarse de 0 (es decir, agrandar la groseridad del error) cuando la función esta mal

<table><tbody><tr><td>Tipo de problema</td><td>Función de costo típica</td></tr><tr><td>Clasificación binaria</td><td>Binary Cross-Entropy Aquí</td></tr><tr><td>Clasificación multiclase</td><td>Categorical Cross-Entropy Ag</td></tr><tr><td>Regresión</td><td>Mean Squared Error (MSE)</td></tr></tbody></table>

Clasificación multiclase Categorical Cross-Entropy Aquí

# Función de error

* Es la diferencia entre la respuesta que se quería y lo que se predijo
# Optimizador

* Es el algoritmo que ajusta los pesos de la red para minimizar la función de costo
* Sirve de guía para el aprendizaje modificando los parametros en la función del gradiente
* Si vez a la función de costo como el grafico en 3D donde hay un "pozo" al que se quiere llegar, el optimizador es la que le dice como moverse a "la pelota" para llegar a ese pozo* Ejemplos comunes:

<table><tbody><tr><td>Gradient Descent) Momentum</td><td>Acelera el aprendizaje acumulando gradientes</td><td>descenso de gradiente Clase 7 &gt; Momento</td></tr><tr><td>RMSProp</td><td>Ajusta el paso según la magnitud de los gradientes</td><td>Clase 7 &gt; RMSprop</td></tr><tr><td>Adam</td><td>Combina Momentum + RMSProp,</td><td>Clase 7 &gt; ADAM</td></tr></tbody></table>

# Relación entre función de activación y función de costo


<table><thead><tr><th>de costo | / Activación</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>Entropia</td><td>A, No ideal</td><td>X No —</td><td>MX No —</td><td>X No —</td></tr><tr><td>cruzada</td><td>— salida en</td><td>ReLU no está</td><td>Softmax es</td><td>salida sin</td></tr><tr><td>binaria</td><td>[-1,1], no representa bien probabilidades.</td><td>acotada; no sirve para probabilidades.</td><td>para multiclase, no binaria.</td><td>límites, no probabilística.</td></tr></tbody></table>


<table><thead><tr><th>Función de costo | |</th><th>Sigmoid</th><th>Tanh</th><th>ReLU</th><th>Softmax</th><th>Lineal</th></tr></thead><tbody><tr><td>Activación &gt; Entropia cruzada categorica</td><td>A, Posible pero rara — para 2 clases se puede usar sigmoid, pero no para multiclase.</td><td>MX No — salida en [—1,1], no tiene sentido como probabilidad.</td><td>MX No — salida no normalizada, no representa distribución.</td><td>Sí — Softmax genera una distribución de probabilidad sobre las</td><td>MX No — no limita ni normaliza las salidas.</td></tr><tr><td></td><td></td><td></td><td></td><td>clases.</td><td></td></tr><tr><td>Error cuadrático medio</td><td>A, Se puede, pero no ideal — funciona, pero el gradiente es lento para clasificación.</td><td>A, SÍ, pero poco eficiente — históricamente usada, pero converge peor.</td><td>A, Sí en regresión (no en clasificación) — puede saturar.</td><td>X No — Softmax con MSE no refleja bien las diferencias probabilísticas.</td><td>Sí — ideal en regresión, salida lineal sin límites.</td></tr><tr><td>Error</td><td>A, Posible — pero menos sensible que MSE.</td><td>A, SÍ, pero lenta convergencia.</td><td>Sí (regresión) — útil si hay outliers.</td><td>MX No — Softmax con MAE no tiene sentido.</td><td>Sí (regresión) predicciones</td></tr></tbody></table>

saturación.

# Resumen de cuando y donde usarla


<table><thead><tr><th></th><th></th><th></th><th>Activación (Salida)</th></tr></thead><tbody><tr><td>Clasificación Binaria</td><td>1 neurona</td><td>Entropía Cruzada Binaria</td><td>Sigmoid</td></tr><tr><td>Clasificación Multiclase</td><td>N neuronas (una por clase)</td><td>Entropía Cruzada Categórica</td><td>Softmax</td></tr><tr><td>Regresión</td><td>10N neuronas</td><td>Error Cuadrático Medio (MSE)</td><td>Lineal (Ninguna)</td></tr><tr><td>Regresión Robusta a Outliers</td><td>10 N neuronas</td><td>Error Absoluto Medio (MAE)</td><td>Lineal (Ninguna)</td></tr></tbody></table>

# Para las capas ocultas, usa ReLU (o Leaky ReLU / PReLU) en la gran mayoría de los casos.
