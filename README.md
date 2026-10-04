# Laboratorio 8

## Requisitos

- Python 3.10 o superior
- matplotlib

Instalar:

```bash
pip install matplotlib
```

## Archivos

- `problema1.py` — implementación del problema 1.
- `problema2.py` — implementación del problema 2.
- `problema3.py` — implementación del problema 3.
- `profiling.py` — medición, tablas CSV y gráficas.
- `main.py` — ejecuta el profiling.
- `ANALISIS.md` — procedimiento de complejidad de los problemas 1–3.
- `resultados/` — archivos generados por el profiling.

## Profiling

Ejecutar los tres problemas:

```bash
python main.py
```

Ejecutar solamente uno:

```bash
python main.py 1
python main.py 2
python main.py 3
```

Los valores utilizados son exactamente los solicitados por el laboratorio:

```text
1, 10, 100, 1000, 10000, 100000, 1000000
```

Cada problema genera:

- un `.csv` con tamaño de input, tiempo y estado;
- un `.png` con la gráfica de tamaño de input vs. tiempo.

## Casos demasiado grandes

Los problemas 1 y 3 crecen demasiado para algunos de los valores grandes. Por ejemplo, para `n = 1,000,000`, el problema 1 requiere aproximadamente 5 × 10¹² ejecuciones del cuerpo interno y el problema 3 aproximadamente 8.33 × 10¹⁰.

Por seguridad, el profiling no inicia mediciones que superen 20 millones de operaciones estimadas. Estos casos aparecen como `SKIPPED` en el CSV y en la tabla de consola, en lugar de bloquear el equipo durante una ejecución impracticable.

En los problemas 2 y 3, la salida `Sequence` se descarta durante el profiling para no llenar la terminal; los ciclos del algoritmo sí se ejecutan.