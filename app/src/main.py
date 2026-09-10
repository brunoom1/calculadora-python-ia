"""
Módulo main - Ponto de entrada da aplicação.

Inicializa a aplicação Calculadora.
"""

import tkinter as tk
from ui import CalculatorUI


def main() -> None:
    """Função principal - inicia a aplicação."""
    root = tk.Tk()
    app = CalculatorUI(root)
    app.run()


if __name__ == "__main__":
    main()
