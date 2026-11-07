# -*- coding: utf-8 -*-
"""Junta las fuentes del banco y escribe preguntas.json y ../preguntas.js.

Uso:   python3 generar.py
"""
import json, collections, pathlib, subprocess, sys

AQUI = pathlib.Path(__file__).parent

for modulo in ("banco_examenes.py", "banco_linkedin.py", "banco_curso.py", "banco_refuerzo.py"):
    subprocess.run([sys.executable, str(AQUI / modulo)], cwd=AQUI, check=True)

banco = []
for f in ("banco_examenes.json", "banco_linkedin.json", "banco_curso.json", "banco_refuerzo.json"):
    banco += json.loads((AQUI / f).read_text(encoding="utf-8"))

vistos = set()
for q in banco:
    assert q["id"] not in vistos, f"id repetido: {q['id']}"
    vistos.add(q["id"])
    assert 0 <= q["correcta"] < len(q["opciones"]), f"respuesta fuera de rango en {q['id']}"
    assert len(q["opciones"]) >= 3, f"muy pocas opciones en {q['id']}"
    assert q["explicacion"].strip(), f"falta la explicación en {q['id']}"

(AQUI / "preguntas.json").write_text(
    json.dumps(banco, ensure_ascii=False, indent=1), encoding="utf-8")
(AQUI.parent / "preguntas.js").write_text(
    "// Generado por banco/generar.py. No editar a mano.\nconst PREGUNTAS = "
    + json.dumps(banco, ensure_ascii=False, indent=1) + ";\n", encoding="utf-8")

print(f"{len(banco)} preguntas")
print("por fuente:", dict(collections.Counter(q["fuente"] for q in banco)))
