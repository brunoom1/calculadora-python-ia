"""
Módulo UI - Interface gráfica com Tkinter.

Responsável pela apresentação visual e captura de eventos do usuário.
Integrado com Calculator e LocaleManager.
"""

import tkinter as tk
from tkinter import font as tkFont
from typing import Callable, Optional

from calculator import Calculator
from locale_manager import LocaleManager


class CalculatorUI:
    """Interface gráfica da Calculadora com Tkinter."""

    # Configurações de design
    WINDOW_WIDTH = 280
    WINDOW_HEIGHT = 520
    PADDING = 12
    GAP = 8
    BUTTON_HEIGHT = 45

    # Cores
    BG_COLOR = '#2c3e50'
    DISPLAY_BG = '#000000'
    DISPLAY_FG = '#00ff00'
    BUTTON_NUMBER_BG = '#34495e'
    BUTTON_OPERATION_BG = '#3498db'
    BUTTON_CLEAR_BG = '#e74c3c'
    BUTTON_EQUALS_BG = '#27ae60'
    TEXT_COLOR = '#ecf0f1'
    BORDER_COLOR = '#2c3e50'

    def __init__(self, root: tk.Tk) -> None:
        """Inicializa a interface.

        Args:
            root: Janela raiz Tkinter
        """
        self.root = root
        self.root.title("Calculadora v1.0")
        self.root.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.root.configure(bg=self.BG_COLOR)
        self.root.resizable(False, False)

        # Backend
        self.calculator = Calculator()
        self.locale_mgr = LocaleManager.get_instance()

        # Estado da interface
        self.display_value = "0"
        self.accumulated_value = 0.0
        self.current_operation: Optional[str] = None
        self.should_clear_display = False

        # Criar widgets
        self._create_widgets()

    def _create_widgets(self) -> None:
        """Cria todos os widgets da interface."""
        # Main frame com padding
        main_frame = tk.Frame(
            self.root,
            bg=self.BG_COLOR,
            padx=self.PADDING,
            pady=self.PADDING
        )
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título
        title_label = tk.Label(
            main_frame,
            text="Calculadora v1.0",
            font=("Segoe UI", 14, "bold"),
            fg=self.TEXT_COLOR,
            bg=self.BG_COLOR
        )
        title_label.pack(pady=(0, self.GAP))

        # Display
        self.display = tk.Label(
            main_frame,
            text=self.display_value,
            font=("Courier New", 32, "bold"),
            fg=self.DISPLAY_FG,
            bg=self.DISPLAY_BG,
            relief=tk.SUNKEN,
            anchor="e",
            padx=15,
            pady=15,
            width=20,
            height=2
        )
        self.display.pack(fill=tk.BOTH, pady=(0, self.GAP))

        # Botões - usar grid em um frame
        buttons_frame = tk.Frame(main_frame, bg=self.BG_COLOR)
        buttons_frame.pack(fill=tk.BOTH, expand=True)

        # Define layout dos botões (coluna, linha, colspan, rowspan)
        buttons_layout = [
            # Linha 0: C ÷
            ('C', 0, 0, 2, 1, self.BUTTON_CLEAR_BG),
            ('÷', 2, 0, 2, 1, self.BUTTON_OPERATION_BG),
            # Linha 1: 7 8 9 ×
            ('7', 0, 1, 1, 1, self.BUTTON_NUMBER_BG),
            ('8', 1, 1, 1, 1, self.BUTTON_NUMBER_BG),
            ('9', 2, 1, 1, 1, self.BUTTON_NUMBER_BG),
            ('×', 3, 1, 1, 1, self.BUTTON_OPERATION_BG),
            # Linha 2: 4 5 6 −
            ('4', 0, 2, 1, 1, self.BUTTON_NUMBER_BG),
            ('5', 1, 2, 1, 1, self.BUTTON_NUMBER_BG),
            ('6', 2, 2, 1, 1, self.BUTTON_NUMBER_BG),
            ('−', 3, 2, 1, 1, self.BUTTON_OPERATION_BG),
            # Linha 3: 1 2 3 +
            ('1', 0, 3, 1, 1, self.BUTTON_NUMBER_BG),
            ('2', 1, 3, 1, 1, self.BUTTON_NUMBER_BG),
            ('3', 2, 3, 1, 1, self.BUTTON_NUMBER_BG),
            ('+', 3, 3, 1, 1, self.BUTTON_OPERATION_BG),
            # Linha 4: 0 , =
            ('0', 0, 4, 2, 1, self.BUTTON_NUMBER_BG),
            (',', 2, 4, 1, 1, self.BUTTON_NUMBER_BG),
            ('=', 3, 4, 1, 1, self.BUTTON_EQUALS_BG),
        ]

        # Criar botões
        for text, col, row, colspan, rowspan, color in buttons_layout:
            btn = tk.Button(
                buttons_frame,
                text=text,
                font=("Segoe UI", 16, "bold"),
                bg=color,
                fg=self.TEXT_COLOR,
                activebackground=color,
                activeforeground=self.TEXT_COLOR,
                relief=tk.RAISED,
                bd=2,
                height=2
            )
            btn.grid(
                row=row,
                column=col,
                sticky="nsew",
                padx=self.GAP // 2,
                pady=self.GAP // 2,
                columnspan=colspan,
                rowspan=rowspan
            )

            # Bind eventos
            if text in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',']:
                btn.config(command=lambda t=text: self._on_number_click(t))
            elif text == 'C':
                btn.config(command=self._on_clear_click)
            elif text == '=':
                btn.config(command=self._on_equals_click)
            else:
                # Operações: converter símbolos para operadores
                op_map = {'÷': '/', '×': '*', '−': '-'}
                op = op_map.get(text, text)
                btn.config(command=lambda o=op: self._on_operation_click(o))

        # Configurar pesos das colunas e linhas para grid responsivo
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)

    def _on_number_click(self, digit: str) -> None:
        """Handler para cliques em números e ponto decimal.

        Args:
            digit: Dígito ou ponto pressionado
        """
        if self.should_clear_display:
            self.display_value = ""
            self.should_clear_display = False

        # Validar entrada de ponto
        if digit == ',':
            if ',' in self.display_value:
                return
            if not self.display_value:
                self.display_value = "0"
            self.display_value += digit
        else:
            # Limitar tamanho da entrada
            if len(self.display_value) < 15:
                if self.display_value == "0" and digit != ",":
                    self.display_value = digit
                else:
                    self.display_value += digit

        self._update_display()

    def _on_operation_click(self, op: str) -> None:
        """Handler para cliques em operações (+, -, *, /).

        Args:
            op: Operação selecionada
        """
        try:
            # Parse do valor atual usando LocaleManager
            current = self.locale_mgr.parse_number(self.display_value)

            # Se já há operação acumulada, calcular resultado
            if self.current_operation and not self.should_clear_display:
                result = self.calculator.calculate(
                    self.accumulated_value,
                    current,
                    self.current_operation
                )
                
                if isinstance(result, str):  # Erro
                    self.display_value = result
                else:
                    self.accumulated_value = result
                    # Formatar com LocaleManager
                    self.display_value = self.locale_mgr.format_number(result)
            else:
                self.accumulated_value = current

            # Armazenar operação
            self.current_operation = op
            self.should_clear_display = True
            self._update_display()

        except ValueError:
            self.display_value = "Erro: entrada inválida"
            self._update_display()

    def _on_equals_click(self) -> None:
        """Handler para clique no botão de igualdade (=)."""
        if not self.current_operation:
            return

        try:
            # Parse usando LocaleManager
            current = self.locale_mgr.parse_number(self.display_value)
            
            # Calcular
            result = self.calculator.calculate(
                self.accumulated_value,
                current,
                self.current_operation
            )

            if isinstance(result, str):  # Erro
                self.display_value = result
            else:
                # Formatar com LocaleManager
                self.display_value = self.locale_mgr.format_number(result)

            # Limpar estado
            self.accumulated_value = 0.0
            self.current_operation = None
            self.should_clear_display = True
            self._update_display()

        except ValueError:
            self.display_value = "Erro: entrada inválida"
            self._update_display()

    def _on_clear_click(self) -> None:
        """Handler para clique no botão de limpar (C)."""
        self.calculator.reset()
        self.display_value = "0"
        self.accumulated_value = 0.0
        self.current_operation = None
        self.should_clear_display = False
        self._update_display()

    def _update_display(self) -> None:
        """Atualiza o texto do display."""
        self.display.config(text=self.display_value)

    def run(self) -> None:
        """Inicia o loop principal da interface."""
        self.root.mainloop()

