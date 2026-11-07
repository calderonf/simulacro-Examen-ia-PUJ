# -*- coding: utf-8 -*-
"""Banco a partir de los exámenes del profesor. Conserva el texto original."""
import json, re

raw = json.load(open("exams_raw.json", encoding="utf-8"))

def limpia(t):
    return re.sub(r"\s+", " ", t.replace("\xa0", " ")).strip()

# ---------- Examen 2023-1 (respuestas resaltadas en el archivo solucionado)
EXPL_2023 = {
 1:("Métricas","El coeficiente de silueta mide qué tan bien separados quedan los grupos en aprendizaje NO supervisado. R², la matriz de confusión y el AUC-ROC sí evalúan modelos supervisados."),
 2:("Validación","Es el menos confiable por dos razones a la vez: una sola partición (Holdout) da un número que depende del azar de esa partición, y la exactitud engaña cuando las clases están desbalanceadas. La validación cruzada con MCC o F1 es más robusta."),
 3:("No supervisado","Se busca el K con el MAYOR coeficiente de silueta (más alto es mejor) y se contrasta con el codo de la inercia. Los dos criterios deben apuntar al mismo K."),
 4:("Datos faltantes","Si las características están muy correlacionadas, las demás columnas contienen información sobre la que falta: una regresión la aprovecha. Rellenar con el promedio de la característica ignora esa correlación, y promediar la MUESTRA mezcla variables de unidades distintas."),
 5:("Validación","La validación cruzada es un método de EVALUACIÓN, no de regularización: no toca la tasa de aprendizaje ni penaliza los coeficientes del modelo."),
 6:("Regularización","λ pequeño o cero deja el modelo sin penalización, así que puede sobreajustar. Es al revés con λ grande: el modelo queda demasiado restringido y subajusta."),
 10:("Optimización","Si tras 1,5 millones de iteraciones el costo todavía baja de forma casi lineal, el descenso va demasiado lento: α es muy pequeño. Hay que aumentarlo y buscar que la curva se doble y se aplane."),
 12:("Fundamentos","Lo que define a un método no supervisado es justamente que NO necesita etiquetas. Las otras tres afirmaciones sí lo describen."),
 15:("Fundamentos","Sobreajuste: el modelo memoriza el entrenamiento y falla con datos nuevos. Subajuste: el modelo es demasiado simple y falla incluso en el entrenamiento."),
 16:("PCA","La maldición de la dimensionalidad se combate REDUCIENDO dimensiones, por ejemplo con PCA. Agregar características empeora el problema."),
 19:("PCA","PCA aprovecha la correlación entre características para resumirlas. Si hay poca correlación, cada componente aporta poco y no se gana casi nada al reducir."),
 20:("Regresión","Residual = real − predicho. Si los residuales son en promedio negativos, el predicho es mayor que el real: el modelo SOBRESTIMA."),
 7:("No supervisado","K-medias asigna cada punto al centroide más cercano. Se calcula la distancia del punto a (2,4), (6,8) y (10,12) y gana el segundo."),
 8:("No supervisado","K-medias se ve menos afectada por la ALTA DIMENSIONALIDAD que por las otras situaciones. Los atípicos corren los centroides, las densidades distintas y las formas no convexas rompen el supuesto de grupos esféricos."),
 9:("PCA","Se escoge el k MÁS PEQUEÑO que conserve al menos el 99 % de la varianza explicada: es el mínimo número de componentes que mantiene la información deseada."),
 11:("Clasificación","En regresión logística la hipótesis devuelve P(y = 1 | x; θ). Si vale 0,2, hay 20 % de probabilidad de que la clase sea 1 (y por tanto 80 % de que sea 0)."),
 13:("Optimización","Con descenso de gradiente por lotes completos, cada paso recorre todo el conjunto antes de actualizar, así que el orden de las filas no cambia el resultado."),
 14:("Optimización","Con descenso estocástico por lotes el orden SÍ importa: si no se mezcla, cada lote puede quedar sesgado (por ejemplo todo de una misma clase) y las actualizaciones dejan de ser representativas."),
 17:("Clasificación","Esa NO es una desventaja porque es falsa: en OvO cada clasificador binario se entrena solo con las muestras de dos clases, así que si el conjunto estaba balanceado los subproblemas también lo están. OvA sí sufre desbalance."),
 18:("Fundamentos","Agrupar documentos por contenido, sin etiquetas previas, es aprendizaje NO supervisado. Los otros tres tienen una etiqueta conocida que el modelo aprende a predecir."),
}
FIX_2023 = {14: 1}      # el archivo no resaltó la respuesta de la 14

def del_2023():
    out = []
    for q in raw["2023"]:
        n = q["n"]
        ops = [limpia(o) for o in q["opciones"]]
        cor = q["correcta"]
        if n == 14:                       # en el .docx la 14 y la 15 quedaron pegadas
            q15 = {"n": 15, "enunciado": "¿Cuál de las siguientes afirmaciones describe correctamente el sobreajuste (overfitting) y el subajuste (underfitting)?",
                   "opciones": ops[4:], "correcta": (cor - 4) if cor is not None and cor >= 4 else 0}
            ops, cor = ops[:4], FIX_2023[14]
            raw["2023"].append(q15) if False else None
            out.append(_arma(n, q["enunciado"], ops, cor, EXPL_2023, "Examen final 2023-1"))
            out.append(_arma(15, q15["enunciado"], q15["opciones"], q15["correcta"], EXPL_2023, "Examen final 2023-1"))
            continue
        if n == 15:
            continue
        if cor is None:
            continue
        out.append(_arma(n, q["enunciado"], ops, cor, EXPL_2023, "Examen final 2023-1"))
    return out

def _arma(n, enun, ops, cor, expl, fuente):
    tema, texto = expl.get(n, ("Fundamentos", ""))
    return {"id": f"{fuente.split()[-1]}-{n}", "tema": tema, "enunciado": limpia(enun),
            "opciones": ops, "correcta": cor, "explicacion": texto,
            "fuente": fuente}

# ---------- Examen 2022-3 (sin resaltar: respuestas propuestas, marcadas para revisión)
RESP_2022 = {
 1:(3,"Métricas","El coeficiente de silueta es una métrica de agrupamiento (no supervisado). R², RMSE y MSE sí evalúan regresiones."),
 2:(1,"Métricas","La matriz de confusión resume aciertos y errores por clase y de ella salen exactitud, precisión, sensibilidad, F1 y MCC."),
 3:(3,"Métricas","El coeficiente de silueta evalúa qué tan compactos y separados quedan los grupos, sin necesitar etiquetas."),
 4:(3,"Validación","Un buen conjunto de prueba debe ser grande para que el resultado sea estadísticamente significativo y debe contener TODAS las clases."),
 5:(0,"Validación","La validación cruzada estima el desempeño que tendría el modelo entrenado con todos los datos, usando varias particiones en vez de una sola."),
 6:(1,"Regularización","Es la afirmación FALSA: un λ grande restringe el modelo y produce subajuste, nunca sobreajuste."),
 12:(0,"Regresión","La regresión predice una variable dependiente CONTINUA. Si el conjunto de valores es discreto y finito, el problema es de clasificación."),
 16:(3,"Datos faltantes","La pregunta pide la opción que NO sirve. Promediar por FILAS mezcla variables de unidades distintas (humedad con pH, por ejemplo) y el promedio no significa nada. Las otras tres sí son razonables: el promedio por columnas es la imputación simple de siempre, hacerlo por clase la refina, y estimar el faltante con una regresión sobre las demás columnas es imputación multivariada. Ojo con esta última: es justamente la respuesta CORRECTA de la 2023-1-4, donde la pregunta está formulada al derecho."),
}

def del_2022():
    out = []
    for q in raw["2022"]:
        n = q["n"]
        if n not in RESP_2022:
            continue
        cor, tema, texto = RESP_2022[n]
        ops = [limpia(o) for o in q["opciones"]]
        if cor >= len(ops):
            continue
        out.append({"id": f"2022-3-{n}", "tema": tema, "enunciado": limpia(q["enunciado"]),
                    "opciones": ops, "correcta": cor, "explicacion": texto,
                    "fuente": "Examen final 2022-3"})
    return out

if __name__ == "__main__":
    banco = del_2023() + del_2022()
    json.dump(banco, open("banco_examenes.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("preguntas de los exámenes:", len(banco))
