"""
Módulo Calculator - Lógica de cálculo da aplicação.

Responsável por realizar operações matemáticas básicas com validações.
"""

from typing import Optional, Union


class Calculator:
    """Classe responsável por operações matemáticas."""

    MAX_PRECISION = 6
    SUPPORTED_OPERATIONS = {'+', '-', '*', '/'}

    def __init__(self) -> None:
        """Inicializa a calculadora em estado limpo."""
        self.result: float = 0.0
        self._last_operation: Optional[str] = None
        self._accumulated: float = 0.0
        self._operation_count = 0

    def calculate(self, a: float, b: float, op: str) -> Union[float, str]:
        """
        Calcula o resultado de uma operação entre dois números.

        Args:
            a: Primeiro operando
            b: Segundo operando
            op: Operação (+, -, *, /)

        Returns:
            Resultado da operação (float) ou mensagem de erro (str)

        Raises:
            ValueError: Se operação é inválida
        """
        if not self._validate_operation(op):
            raise ValueError(f"Operação inválida: {op}")

        try:
            if op == '+':
                result = self.add(a, b)
            elif op == '-':
                result = self.subtract(a, b)
            elif op == '*':
                result = self.multiply(a, b)
            elif op == '/':
                result = self.divide(a, b)
                if isinstance(result, str):  # Erro de divisão por zero
                    return result
            
            self.result = result
            self._operation_count += 1
            return result
        except Exception as e:
            return f"Erro: {str(e)}"

    def add(self, a: float, b: float) -> float:
        """Soma dois números.

        Args:
            a: Primeiro número
            b: Segundo número

        Returns:
            Resultado da soma
        """
        return round(a + b, self.MAX_PRECISION)

    def subtract(self, a: float, b: float) -> float:
        """Subtrai o segundo número do primeiro.

        Args:
            a: Minuendo
            b: Subtraendo

        Returns:
            Resultado da subtração
        """
        return round(a - b, self.MAX_PRECISION)

    def multiply(self, a: float, b: float) -> float:
        """Multiplica dois números.

        Args:
            a: Primeiro fator
            b: Segundo fator

        Returns:
            Resultado da multiplicação
        """
        return round(a * b, self.MAX_PRECISION)

    def divide(self, a: float, b: float) -> Union[float, str]:
        """Divide o primeiro número pelo segundo.

        Args:
            a: Dividendo
            b: Divisor

        Returns:
            Resultado da divisão ou mensagem de erro se divisão por zero

        Raises:
            ValueError: Se divisor for zero
        """
        if b == 0:
            return "Erro: Divisão por zero"
        
        return round(a / b, self.MAX_PRECISION)

    def reset(self) -> None:
        """Reseta a calculadora para estado inicial."""
        self.result = 0.0
        self._last_operation = None
        self._accumulated = 0.0
        self._operation_count = 0

    def get_result(self) -> float:
        """Retorna o resultado atual.

        Returns:
            Resultado armazenado
        """
        return self.result

    def get_operation_count(self) -> int:
        """Retorna quantas operações foram realizadas.

        Returns:
            Número de operações
        """
        return self._operation_count

    def _validate_operation(self, op: str) -> bool:
        """Valida se operação é suportada.

        Args:
            op: Símbolo da operação

        Returns:
            True se válida, False caso contrário
        """
        return op in self.SUPPORTED_OPERATIONS
