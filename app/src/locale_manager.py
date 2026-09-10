"""
Módulo LocaleManager - Gerenciador de localização (pt-BR).

Responsável por parsing e formatação de números conforme locale pt-BR.
Padrão: vírgula como separador decimal, ponto para milhar.
"""

from typing import Optional
from decimal import Decimal, InvalidOperation


class LocaleManager:
    """Gerenciador de localização - Singleton.

    Trata parsing (string → número) e formatação (número → string)
    conforme padrão pt-BR.
    """

    _instance: Optional['LocaleManager'] = None

    # Configurações de locale pt-BR
    DECIMAL_SEPARATOR = ','
    THOUSAND_SEPARATOR = '.'
    MAX_PRECISION = 6

    def __new__(cls) -> 'LocaleManager':
        """Implementa padrão Singleton."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        """Inicializa o gerenciador de locale."""
        if self._initialized:
            return
        
        self._cache: dict[str, float] = {}
        self._initialized = True

    @classmethod
    def get_instance(cls) -> 'LocaleManager':
        """Obtém a instância singleton.

        Returns:
            Instância do LocaleManager
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def parse_number(self, value: str) -> float:
        """Converte string (pt-BR) para float.

        Aceita:
        - "123" → 123.0
        - "123,45" → 123.45
        - "1.234,56" → 1234.56
        - "-123,45" → -123.45

        Args:
            value: String com número em formato pt-BR

        Returns:
            Número como float

        Raises:
            ValueError: Se string não é um número válido
        """
        if not value:
            raise ValueError("Valor vazio")

        # Verificar cache
        if value in self._cache:
            return self._cache[value]

        # Limpar espaços
        value = value.strip()

        try:
            # Remover separadores de milhar (ponto)
            value = value.replace(self.THOUSAND_SEPARATOR, '')
            
            # Substituir vírgula por ponto (padrão Python)
            value = value.replace(self.DECIMAL_SEPARATOR, '.')
            
            # Converter para float
            result = float(value)
            
            # Guardar em cache
            self._cache[value] = result
            
            return result
        except ValueError:
            raise ValueError(f"'{value}' não é um número válido")

    def format_number(self, value: float) -> str:
        """Formata float para string em padrão pt-BR.

        Exemplos:
        - 123.0 → "123"
        - 123.45 → "123,45"
        - 1234.56 → "1.234,56"
        - -123.45 → "-123,45"

        Args:
            value: Número como float

        Returns:
            String formatada conforme padrão pt-BR
        """
        # Limitar precisão
        value = round(value, self.MAX_PRECISION)

        # Se é inteiro, retornar sem casas decimais
        if value == int(value):
            formatted = self._format_thousands(int(value))
            return formatted

        # Converter para string e separar parte inteira e decimal
        str_value = f"{value:.{self.MAX_PRECISION}f}"
        parts = str_value.split('.')
        
        integer_part = int(parts[0])
        decimal_part = parts[1].rstrip('0')  # Remove zeros à direita

        # Formatar parte inteira com separador de milhar
        formatted_integer = self._format_thousands(integer_part)

        # Combinar
        if decimal_part:
            return f"{formatted_integer}{self.DECIMAL_SEPARATOR}{decimal_part}"
        else:
            return formatted_integer

    def _format_thousands(self, value: int) -> str:
        """Formata número inteiro com separador de milhar.

        Args:
            value: Número inteiro (pode ser negativo)

        Returns:
            String formatada com separador de milhar
        """
        is_negative = value < 0
        value = abs(value)
        
        # Formatar com separador
        formatted = format(value, ',').replace(',', self.THOUSAND_SEPARATOR)
        
        if is_negative:
            formatted = f"-{formatted}"
        
        return formatted

    def clear_cache(self) -> None:
        """Limpa o cache de parsing."""
        self._cache.clear()

    def get_cache_size(self) -> int:
        """Retorna o tamanho do cache.

        Returns:
            Número de entradas em cache
        """
        return len(self._cache)
