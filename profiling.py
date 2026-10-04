import contextlib
import csv
import os
import time
from pathlib import Path
import matplotlib.pyplot as plt
from problema1 import problema1
from problema2 import problema2
from problema3 import problema3

VALORES = [1, 10, 100, 1000, 10000, 100000, 1000000]
RESULTADOS = Path(__file__).parent / "resultados"
MAX_OPERACIONES = 20_000_000

FUNCIONES = {
    1: problema1,
    2: problema2,
    3: problema3,
}

def operaciones_estimadas(problema, n):
    """Cantidad de operaciones relevantes de cada algoritmo."""
    if problema == 1:
        if n <= 0:
            return 0
        return (n - n // 2 + 1) * (n - n // 2) * n.bit_length()
    if problema == 2:
        return 0 if n <= 1 else n
    if problema == 3:
        return (n // 3) * ((n + 3) // 4)
    raise ValueError("Problema inválido")

def medir(problema, n):
    """Mide una ejecución real, descartando la salida de Sequence."""
    funcion = FUNCIONES[problema]
    inicio = time.perf_counter()

    with open(os.devnull, "w") as salida, contextlib.redirect_stdout(salida):
        funcion(n)

    return time.perf_counter() - inicio

def profiling(problema):
    nombre = f"Problema {problema}"
    tiempos = []
    estados = []

    print("\n" + "=" * 60)
    print(nombre)
    print("=" * 60)
    print(f"{'n':>10} | {'Tiempo (s)':>14} | Estado")
    print("-" * 48)

    for n in VALORES:
        operaciones = operaciones_estimadas(problema, n)

        if operaciones > MAX_OPERACIONES:
            tiempo = None
            estado = "SKIPPED"
        else:
            tiempo = medir(problema, n)
            estado = "OK"

        tiempos.append(tiempo)
        estados.append(estado)
        texto_tiempo = "-" if tiempo is None else f"{tiempo:.6f}"
        print(f"{n:>10} | {texto_tiempo:>14} | {estado}")

    RESULTADOS.mkdir(exist_ok=True)

    with (RESULTADOS / f"problema_{problema}.csv").open(
        "w", newline="", encoding="utf-8"
    ) as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([
            "Tamaño de input",
            "Tiempo (segundos)",
            "Estado",
            "Operaciones estimadas",
        ])
        for n, tiempo, estado in zip(VALORES, tiempos, estados):
            escritor.writerow([
                n,
                "" if tiempo is None else tiempo,
                estado,
                operaciones_estimadas(problema, n),
            ])

    x = [n for n, t in zip(VALORES, tiempos) if t is not None]
    y = [t for t in tiempos if t is not None]

    plt.figure(figsize=(8, 5))
    if x:
        plt.plot(x, y, marker="o")
    plt.xlabel("Tamaño de input (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title(f"{nombre}: tamaño de input vs tiempo")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(RESULTADOS / f"problema_{problema}.png", dpi=150)
    plt.close()

def ejecutar_todos():
    for problema in (1, 2, 3):
        profiling(problema)