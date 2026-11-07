# Simulacro de examen final · Inteligencia Artificial

### 👉 [Abrir el simulacro](https://calderonf.github.io/simulacro-Examen-ia-PUJ/)

Práctica para el examen final del curso de **Inteligencia Artificial** del Departamento de
Electrónica de la Pontificia Universidad Javeriana.

No hay que instalar nada ni registrarse: se abre en el navegador, también desde el celular.

---

## Cómo funciona

Cada vez que empieza, el sitio arma un **examen distinto con 15 preguntas** tomadas al azar
de un banco de 101, repartidas entre las seis áreas del curso. Puede activar un **reloj de
una hora** si quiere practicar con la presión del tiempo, o dejarlo apagado para ir con calma.

Puede devolverse y cambiar respuestas antes de terminar. Al calificar verá:

- el puntaje y el porcentaje de aciertos,
- **en qué área le fue bien y en cuál no**, que es lo que le dice qué repasar,
- y la revisión pregunta por pregunta, con **la explicación de por qué** esa era la respuesta.

Puede repetirlo las veces que quiera. Cada intento trae preguntas diferentes.

## Qué entra

| Área | Preguntas en el banco | Temas |
|---|---|---|
| Evaluación y validación | 25 | Matriz de confusión, precisión y exhaustividad, F1, ROC, R², MAE, RMSE, MAPE, validación cruzada, fuga de datos, comparación de modelos, GridSearch y AutoML |
| Modelos supervisados | 20 | Regresión lineal y logística, KNN, Naive Bayes, árboles, bosque aleatorio, SVM, multiclase, regularización L1 y L2 |
| Datos y preprocesamiento | 17 | Datos faltantes e imputación, escalado y normalización, codificación, PCA y reducción de dimensionalidad |
| Fundamentos | 15 | Supervisado y no supervisado, sobreajuste y subajuste, sesgo y varianza, conjuntos de entrenamiento y prueba |
| No supervisado y series | 12 | K-medias, selección de K, coeficiente de silueta, series de tiempo |
| Redes neuronales | 12 | Perceptrón, capas ocultas, funciones de activación, softmax, descenso de gradiente, funciones de costo |

## Cómo sacarle provecho

Hágalo **antes** de repasar, no después. Un primer intento en frío le muestra dónde está
parado y le ahorra repasar lo que ya sabe.

Lea las explicaciones de las que acertó, no solo las de las que falló. A veces se acierta por
descarte y la explicación es la que enseña.

Mire la tabla por área más que el puntaje total. Un 10 sobre 15 con todos los errores
concentrados en una sola área dice algo muy distinto a un 10 con los errores repartidos.

Repítalo unos días después. Como el examen cambia en cada intento, la segunda vez le van a
salir preguntas que no vio.

> El simulacro es para practicar. No es el examen, ni una muestra de las preguntas que van a
> salir, ni cubre todo lo que puede entrar.

## De dónde salen las preguntas

De tres sitios: los exámenes finales de semestres anteriores del curso, preguntas escritas
sobre el material visto en clase en 2026-3, y preguntas traducidas y adaptadas de un banco
público de evaluaciones de aprendizaje automático. Todas tienen explicación.

También hay preguntas sobre los temas que el curso comparte con
[CS207: Fundamentals of Machine Learning](https://learn.saylor.org/course/view.php?id=1267)
de Saylor University, el curso de la actividad opcional de bonificación.

## Para el profesor

El banco se arma con los módulos de `banco/` y se regenera así:

```bash
cd banco && python3 generar.py
```

Eso valida cada pregunta (identificador único, al menos tres opciones, respuesta dentro de
rango y explicación no vacía) y reescribe `preguntas.json` y `preguntas.js`. **No se edita
`preguntas.js` a mano.**

Los archivos `banco/*_raw.json` son las fuentes sin procesar y **no se publican**: contienen
preguntas que no entraron al banco. Están en `.gitignore` y se conservan solo en el
computador. Sin ellos no se puede regenerar desde cero, pero el banco ya generado sí viaja en
el repositorio.

Para cambiar la duración o el número de preguntas, al comienzo del `<script>` de `index.html`:

```js
const TOTAL = 15;      // preguntas por simulacro
const SEGUNDOS = 3600; // duración del reloj
```

## Licencia

Preguntas de los exámenes y del material de clase por Francisco Carlos Calderón B., Ph.D.

Parte del banco está traducida y adaptada del repositorio
[linkedin-skill-assessments-quizzes](https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes)
de Ebazhanov, publicado bajo **AGPL-3.0**. Por esa razón este repositorio también se
distribuye bajo **AGPL-3.0** (ver `LICENSE`).
