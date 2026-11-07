# -*- coding: utf-8 -*-
"""Preguntas de refuerzo sobre los temas que comparte el curso con CS207
(Fundamentals of Machine Learning, Saylor University), la actividad opcional
de bonificación. Todas caen dentro de lo dictado en 2026-3."""
import json
F = "Curso 2026-3 · refuerzo CS207"

Q = [
 ("Regresión", "En una regresión lineal ajustada por mínimos cuadrados, ¿qué cantidad se minimiza exactamente?",
  ["La suma de los residuales",
   "La suma de los cuadrados de los residuales",
   "El residual más grande",
   "La suma de los valores absolutos de los residuales"], 1,
  "Mínimos cuadrados minimiza Σ(yᵢ − ŷᵢ)². No se minimiza la suma de los residuales a secas porque los positivos y los negativos se cancelan. Minimizar la suma de valores absolutos es otro método (regresión por mínima desviación absoluta), más robusto a atípicos pero sin solución cerrada."),

 ("Regresión", "Tiene una regresión lineal con 5 características y 2000 muestras. ¿Qué ventaja tiene resolverla con la ecuación normal en lugar de descenso de gradiente?",
  ["Siempre es más rápida, sin importar el número de características",
   "Da la solución exacta de una vez, sin escoger tasa de aprendizaje ni iterar",
   "Es la única forma de incluir el término independiente",
   "Permite usar regularización, cosa que el descenso de gradiente no"], 1,
  "La ecuación normal resuelve θ = (XᵀX)⁻¹Xᵀy en un paso: no hay que elegir α ni decidir cuándo parar. Su límite es el costo de invertir XᵀX, que crece con el cubo del número de características; con pocas características como aquí, no es problema."),

 ("Datos", "¿Por qué conviene escalar las características antes de usar KNN o SVM, pero no hace falta para un árbol de decisión?",
  ["Porque los árboles solo aceptan variables categóricas",
   "Porque KNN y SVM dependen de distancias, y el árbol parte cada característica por un umbral propio",
   "Porque el árbol escala los datos internamente",
   "Porque los árboles no usan todas las características"], 1,
  "KNN y SVM miden distancias entre puntos: una característica con rango grande domina la distancia solo por su escala. El árbol evalúa cada característica por separado buscando un umbral de corte, y ese corte no cambia si la variable se multiplica por una constante."),

 ("Clasificación", "En una regresión logística baja el umbral de decisión de 0,5 a 0,3. ¿Qué le pasa típicamente a la precisión y a la exhaustividad (recall)?",
  ["Las dos suben",
   "Las dos bajan",
   "Sube la exhaustividad y baja la precisión",
   "Sube la precisión y baja la exhaustividad"], 2,
  "Con un umbral más bajo se marcan como positivos más casos: se escapan menos positivos reales (sube la exhaustividad) pero entran más falsos positivos (baja la precisión). Mover el umbral no mejora el modelo, solo recorre el compromiso entre las dos métricas; eso es justamente lo que dibuja la curva ROC."),

 ("No supervisado", "¿Qué cantidad minimiza el algoritmo K-medias en cada iteración?",
  ["La distancia entre los centroides",
   "La suma de las distancias al cuadrado de cada punto al centroide de su grupo",
   "El número de grupos necesarios",
   "La varianza total del conjunto de datos"], 1,
  "K-medias minimiza la inercia: Σ‖xᵢ − μ_{c(i)}‖². Por eso alterna dos pasos que nunca la aumentan: asignar cada punto a su centroide más cercano y recalcular cada centroide como el promedio de sus puntos. Garantiza llegar a un mínimo local, no al global, y de ahí que convenga repetir con varias inicializaciones."),

 ("Métricas", "Está construyendo un tamizaje que detecta una enfermedad grave pero tratable. ¿Qué métrica conviene priorizar y por qué?",
  ["La precisión, porque hay que evitar alarmar a gente sana",
   "La exactitud (accuracy), porque resume todo el desempeño",
   "La exhaustividad (recall), porque dejar pasar un enfermo cuesta más que una falsa alarma",
   "La especificidad, porque la mayoría de las personas están sanas"], 2,
  "La métrica se escoge según el costo de cada tipo de error. Un falso negativo deja sin tratamiento a alguien enfermo; un falso positivo lleva a un examen de confirmación. La exactitud además engaña con clases desbalanceadas: si solo el 1 % está enfermo, decir «sano» siempre da 99 % de exactitud y no detecta a nadie."),

 ("Validación", "¿Por qué se separa un conjunto de validación además del de prueba, si ya hay validación cruzada?",
  ["Porque la validación cruzada no sirve para clasificación",
   "Para entrenar el modelo final con más datos",
   "Para tomar las decisiones de modelo y de hiperparámetros sin mirar nunca la prueba",
   "Porque así se reduce el sobreajuste del modelo automáticamente"], 2,
  "Todo lo que se escoja mirando unos datos hace que esos datos dejen de ser una estimación imparcial. Las decisiones (qué modelo, qué hiperparámetros, qué imputación) se toman con validación —sea un conjunto aparte o los pliegues de la validación cruzada— y la prueba se mira una sola vez, al final, para reportar."),

 ("No supervisado", "Corre K-medias dos veces sobre los mismos datos con el mismo K y obtiene dos agrupamientos distintos. ¿Cuál es la forma correcta de proceder?",
  ["Fijar siempre la misma semilla y quedarse con ese resultado",
   "Repetir con varias inicializaciones distintas y quedarse con la de menor inercia",
   "Repetir con varias inicializaciones y quedarse con el agrupamiento que más se repita",
   "Aumentar K hasta que el resultado deje de cambiar"], 1,
  "K-medias solo garantiza llegar a un mínimo local, y a cuál llega depende de dónde arranquen los centroides. La salida es repetir con inicializaciones distintas y quedarse con la corrida de menor inercia, que es la suma de distancias al cuadrado de cada punto a su centroide. Es lo que hace el parámetro n_init de scikit-learn. Fijar la semilla hace el resultado reproducible, pero no mejor; y quedarse con el que más se repita no es el criterio, porque un mínimo malo puede repetirse muchas veces."),

 ("Fundamentos", "K-vecinos más cercanos y K-medias se parecen en el nombre y los dos exigen fijar K de antemano. ¿Cuál es la diferencia de fondo?",
  ["KNN es no supervisado y K-medias es supervisado",
   "KNN predice la etiqueta de una muestra usando datos ya etiquetados; K-medias busca grupos en datos sin etiqueta",
   "KNN solo sirve para regresión y K-medias solo para clasificación",
   "En KNN la K es el número de grupos y en K-medias es el número de vecinos"], 1,
  "El nombre y la K son lo único que comparten. KNN es supervisado: necesita un conjunto etiquetado y clasifica una muestra nueva por mayoría entre sus K vecinos más cercanos. K-medias es no supervisado: no hay etiquetas y busca K grupos agrupando por cercanía. En KNN la K son vecinos; en K-medias, grupos."),

 ("Regularización", "¿Qué distingue a la regularización L1 (lasso) de la L2 (ridge)?",
  ["L1 penaliza los coeficientes al cuadrado y L2 en valor absoluto",
   "L1 puede dejar coeficientes exactamente en cero, así que también sirve para seleccionar características",
   "L2 solo se puede usar en clasificación y L1 solo en regresión",
   "L1 aumenta la varianza del modelo y L2 aumenta el sesgo"], 1,
  "L1 penaliza la suma de los valores absolutos de los coeficientes y L2 la suma de sus cuadrados. Esa diferencia hace que L1 pueda llevar coeficientes exactamente a cero, lo que equivale a descartar esa característica; L2 los encoge hacia cero sin anularlos. Las dos combaten el sobreajuste y las dos aumentan el sesgo para reducir la varianza."),
]

if __name__ == "__main__":
    banco = [{"id": f"S-{i+1}", "tema": t, "enunciado": e, "opciones": o, "correcta": c,
              "explicacion": x, "fuente": F}
             for i, (t, e, o, c, x) in enumerate(Q)]
    json.dump(banco, open("banco_refuerzo.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("preguntas de refuerzo:", len(banco))
