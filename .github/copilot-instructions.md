# Copilot instructions for this repository ✅

**Propósito (breve):** Evaluar y comparar dos sistemas G2P a escala: **DEEPphonemizer** y **Phonetisaurus**. El repo contiene scripts para preparar datos, entrenar, inferir y calcular métricas (PER/WER) por idioma.

## Resumen rápido 🔎
- DEEPphonemizer: `DEEPphonemizer/training.py`, `DEEPphonemizer/chec.py`, `DEEPphonemizer/KalkulatorDeep.py`
- Phonetisaurus: `Phonetisaurus/Kalkulator.py`, `Phonetisaurus/data.dict` and result folder
- Preparación: `Dataprep.py` → genera `guide*.txt` y `guidewf*.txt` (test/facit)
- Distancias fonémicas: `viktad fonem distanse/TruDistance.txt` (pesos de sustitución usados por los kalkulators)

## Cómo ejecutar (comandos prácticos) ▶️
- Preparar datos: from repo root
  - python Dataprep.py
- Entrenar (DEEPphonemizer): from `DEEPphonemizer/`
  - python training.py  # **nota:** el script imprime `train_data` y llama `input()` (pausa). Remove/comment for automated runs.
- Inferencia (usar checkpoint): from `DEEPphonemizer/`
  - python chec.py  # espera `checkpoints/best_model.pt`
- Calcular métricas:
  - cd DEEPphonemizer && python KalkulatorDeep.py
  - cd Phonetisaurus && python Kalkulator.py
- Validar inputs / limpiar salidas: `python tools/validate_inputs.py --check` or `--clean --yes`
- CI: `.github/workflows/validate_and_smoke.yml` runs the validator and a small smoke test that executes the kalkulator scripts on a subset of languages (`tools/smoke_kalkulators.py`).

## Convenciones y puntos importantes 📎
- Muchas rutas y archivos están **codificados** (sin CLI). Ejecuta cada script desde el directorio esperado.
- Archivos de salida usan patrones: `DEEPreult{lang}.txt`, `Result{lang}.txt` y facit `guidewf{lang}.txt`.
- Muchos scripts abren archivos en modo append (`'a'`) → **limpia** o mueve los archivos de salida antes de volver a ejecutar para evitar duplicados.
- Codificación: UTF-8 asumida en todo el repo.
- Formato: Phonetisaurus produce tokens fonémicos separados por espacios (ve `Mach.py`).

## Dependencias y entorno 🧰
- Paquetes Python observados: `dp` (DeepPhonemizer), `asjp`, `pywer`, `weighted_levenshtein`, `python-Levenshtein`, `regex`, `numpy`.
- No hay `requirements.txt` fijo; use un entorno virtual o el dev container (Ubuntu 24.04 LTS) provisto en el repo's devcontainer.

## Fragilidades conocidas & depuración ⚠️
- `training.py` pausa con `input()` — quita la pausa para CI/automatización.
- `training.py` procesa `data.txt` con slicing (`[2][:-2]`) → el formato de `data.txt` es estricto (tripletas); revisar fallos en `dp.preprocess` si falla.
- `TruDistance.txt` controla los pesos en las métricas; cambiarlo afecta resultados (útil para experiments).
- Duplicación: evaluación está en dos kalkulators (`KalkulatorDeep.py` y `Phonetisaurus/Kalkulator.py`). Cambios lógicos deben reflejarse en ambos.

## Qué pedirle a Copilot / agente AI 💡
- Añadir CLI a `DEEPphonemizer/training.py` y `DEEPphonemizer/chec.py` para parámetros `--data`, `--checkpoint`, `--out`.
- Extraer y centralizar la lógica de evaluación en `tools/eval_utils.py` para reutilización entre kalkulators.
- Añadir una tarea de CI (acción rápida) que ejecute `tools/validate_inputs.py --check`, y corra `Kalkulator*` en un subset de idiomas para detectar regresiones.
- Escriba pruebas pequeñas o scripts de humo que: limpien salidas, ejecuten `chec.py` con un checkpoint fijo y comparen contra `fasit/guidewf*.txt`.

## Archivo clave (referencia rápida) 🔧
- DEEPphonemizer/training.py — formateo de `data.txt` y pausa con `input()`
- DEEPphonemizer/chec.py — carga checkpoint `checkpoints/best_model.pt`
- DEEPphonemizer/KalkulatorDeep.py — cálculo PER/WER
- Phonetisaurus/Kalkulator.py — cálculo equivalente para Phonetisaurus
- Dataprep.py — genera `guide*.txt` / `guidewf*.txt`
- tools/validate_inputs.py — valida la existencia/tamaños y limpia salidas (usar con `--clean --yes`)
- viktad fonem distanse/TruDistance.txt — pesos para la métrica ponderada

---

Si algo no está claro o quieres que haga una PR con cambios sugeridos (CLI, centralizar evaluación, CI simple), dímelo y lo implemento en un branch y PR de ejemplo. ✅
