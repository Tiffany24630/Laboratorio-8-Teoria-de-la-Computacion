import argparse
from profiling import ejecutar_todos, profiling

parser = argparse.ArgumentParser(
    description="Profiling de los problemas 1, 2 y 3 del Laboratorio 8."
)

parser.add_argument(
    "problema",
    nargs="?",
    type=int,
    choices=[1, 2, 3],
    help="Problema que se desea medir. Si se omite, se ejecutan los tres.",
)

args = parser.parse_args()

if args.problema:
    profiling(args.problema)

else:
    ejecutar_todos()