# Copilot instructions for this repository ✅

**Propósito:** Comparar y evaluar dos sistemas G2P en muchos idiomas: **DEEPphonemizer** y **Phonetisaurus**. Los scripts se centran en preparación de datos, entrenamiento (DEEP), inferencia, y cálculo de métricas (PER/WER) por idioma.

## Arquitectura y flujos principales 🔧
- DEEPphonemizer/
  - `training.py`: prepara `train_data` desde `data.txt`, llama a `dp.preprocess` y `dp.train` usando `config.yaml`. Nota: imprime `train_data` y hace `input()` (pausa) antes de entrenar.
  - `chec.py`: carga un checkpoint con `Phonemizer.from_checkpoint('checkpoints/best_model.pt')`, procesa una lista de palabras (archivo uno por línea) y escribe predicciones en `DEEPreult{lang}.txt`.
  - `KalkulatorDeep.py`: calcula métricas (Levenshtein, WER/PER) leyendo `DEEPreult*.txt` y comparando con archivos de referencia (`fasit/guidewf*.txt`). Usa `TruDistance.txt` para pesos de sustitución.
- Phonetisaurus/
  - `Kalkulator.py`: flujo equivalente para salidas de Phonetisaurus (`Result*.txt`), misma lógica de evaluación.
- Scripts de ayuda:
  - `Dataprep.py`: convierte IPA→ASJP y escribe `guide*.txt` y `guidewf*.txt` usados como test y facit.
  - `Mach.py`, `langfinder.py`: utilidades de limpieza, búsqueda de coincidencias y conteo de idiomas.

## Convenciones del proyecto (importantes) 📎
- Muchas rutas y nombres están **codificados** (no hay CLI genérica). Ejecuta scripts desde el directorio donde esperan los archivos.
- Archivos de resultados siguen patrones: `DEEPreult{lang}.txt`, `Result{lang}.txt` y archivos de facit `guidewf{lang}.txt`.
- Muchos scripts **abren en modo append** (`'a'`) — borra o mueve los archivos de salida antes de re-ejecutar para evitar duplicados.
- Codificación: UTF-8 asumida en todos los scripts.
- Notas de formato: Phonetisaurus espera tokens fonémicos separados por espacios (ver `Mach.py`).

## Dependencias observadas (instalación esperada) 📦
- Python packages: `dp` (DeepPhonemizer module), `asjp`, `pywer`, `weighted_levenshtein`, `python-Levenshtein`, `regex`, `numpy`.
- Archivos de datos requeridos: `TruDistance.txt`, `data.txt`, `config.yaml`, además de los `guide*.txt` y los `Result*/DEEPreult*` que alimentan los cálculos.

## Comandos y ejemplos (rápidos) ▶️
- Preparar test data (ajusta `Files` en `Dataprep.py`):
  - cd repo root && python Dataprep.py
- Entrenar DEEPphonemizer (desde `DEEPphonemizer`):
  - cd DEEPphonemizer && python training.py  # revisa la pausa y config.yaml
- Generar inferencias con un checkpoint:
  - cd DEEPphonemizer && python chec.py
- Calcular métricas:
  - cd DEEPphonemizer && python KalkulatorDeep.py
  - cd Phonetisaurus && python Kalkulator.py

## Puntos de fragilidad y consejos para depuración ⚠️
- Si el entrenamiento/`dp.preprocess` falla, revisa `data.txt` — `training.py` espera tripletas y hace slicing (`[2][:-2]`), lo que sugiere un formato específico por línea.
- Verifica la presencia de `checkpoints/best_model.pt` antes de ejecutar `chec.py`.
- `TruDistance.txt` define pesos críticos para la métrica ponderada; modificarlo cambia las comparaciones.
- Scripts usan arreglos y variables globales por idioma (duplicación de código). Para cambios globales en evaluación, modifique `KalkulatorDeep.py` y `Phonetisaurus/Kalkulator.py` en paralelo.
- Atención a escrituras en modo append: limpiar archivos de salida (`DEEPreult*.txt`, `Result*.txt`) entre corridas.

## Qué puede pedirte Copilot / agente AI 💡
- Añadir una CLI para `training.py` y `chec.py` (aceptar argumentos de archivo, checkpoint y salida).
- Centralizar las funciones de evaluación en una utilidad compartida para evitar duplicación entre `KalkulatorDeep.py` y `Phonetisaurus/Kalkulator.py`.
- Añadir un script de validación que verifique la existencia y tamaño de los archivos críticos (`TruDistance.txt`, `guidewf*.txt`, `data.txt`) y que limpie archivos de salida antes de ejecutar.

---

Si quieres, puedo: (1) abrir una PR con esta nueva `/.github/copilot-instructions.md`, (2) añadir un pequeño script `tools/validate_inputs.py` que verifique y limpie archivos de salida, o (3) ajustar el lenguaje (más/menos técnico). ¿Qué prefieres? ✅