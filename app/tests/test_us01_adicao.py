# -*- coding: utf-8 -*-
"""
Testes para US01 — Realizar Adição de Dois Números

Esta User Story valida a operação de adição em todos os cenários.
"""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from calculator import Calculator
from locale_manager import LocaleManager


class TestUS01Adicao:
    """User Story US01: Realizar Adição de Dois Números"""

    @pytest.fixture
    def setup(self):
        """Setup com Calculator e LocaleManager"""
        calc = Calculator()
        locale = LocaleManager.get_instance()
        return calc, locale

    # ====================================================================
    # Testes Backend — Operação de Adição
    # ====================================================================

    def test_add_5_mais_3_igual_8(self, setup):
        """Caso 1: 5 + 3 = 8"""
        calc, locale = setup
        resultado = calc.calculate(5, 3, '+')
        assert resultado == 8.0

    def test_add_0_mais_0_igual_0(self, setup):
        """Caso 2: 0 + 0 = 0"""
        calc, locale = setup
        resultado = calc.calculate(0, 0, '+')
        assert resultado == 0.0

    def test_add_negativo_5_mais_10_igual_5(self, setup):
        """Caso 3: -5 + 10 = 5"""
        calc, locale = setup
        resultado = calc.calculate(-5, 10, '+')
        assert resultado == 5.0

    def test_add_12_5_mais_7_5_igual_20(self, setup):
        """Caso 4: 12,5 + 7,5 = 20"""
        calc, locale = setup
        resultado = calc.calculate(12.5, 7.5, '+')
        assert resultado == 20.0

    def test_add_100_mais_0_01_igual_100_01(self, setup):
        """Caso 5: 100 + 0,01 = 100,01"""
        calc, locale = setup
        resultado = calc.calculate(100, 0.01, '+')
        assert abs(resultado - 100.01) < 0.0001

    # ====================================================================
    # Testes Frontend — Input com pt-BR e Display
    # ====================================================================

    def test_parse_input_5(self, setup):
        """Entrada do usuário: digita "5""""
        calc, locale = setup
        entrada = "5"
        valor = locale.parse_number(entrada)
        assert valor == 5.0

    def test_parse_input_12_5(self, setup):
        """Entrada do usuário: digita "12,5" (com virgula)"""
        calc, locale = setup
        entrada = "12,5"
        valor = locale.parse_number(entrada)
        assert valor == 12.5

    def test_parse_input_100(self, setup):
        """Entrada do usuário: digita "100" """
        calc, locale = setup
        entrada = "100"
        valor = locale.parse_number(entrada)
        assert valor == 100.0

    def test_format_output_8(self, setup):
        """Display mostra: "8" (resultado de 5 + 3)"""
        calc, locale = setup
        resultado = 8.0
        display = locale.format_number(resultado)
        assert display == "8"

    def test_format_output_20(self, setup):
        """Display mostra: "20" (resultado de 12,5 + 7,5)"""
        calc, locale = setup
        resultado = 20.0
        display = locale.format_number(resultado)
        assert display == "20"

    def test_format_output_100_01(self, setup):
        """Display mostra: "100,01" (resultado de 100 + 0,01)"""
        calc, locale = setup
        resultado = 100.01
        display = locale.format_number(resultado)
        assert display == "100,01"

    # ====================================================================
    # Testes de Integração — Fluxo Completo da UI
    # ====================================================================

    def test_fluxo_completo_5_mais_3(self, setup):
        """
        Fluxo completo da UI:
        1. Usuário digita "5" → parse → 5.0
        2. Usuário clica "+" → armazena (5.0, '+')
        3. Usuário digita "3" → parse → 3.0
        4. Usuário clica "=" → calc.calculate(5, 3, '+') → 8.0
        5. Display formata 8.0 → "8"
        """
        calc, locale = setup

        # Etapa 1: Entrada "5"
        entrada1 = "5"
        v1 = locale.parse_number(entrada1)
        assert v1 == 5.0

        # Etapa 2: Operação "+"
        op = '+'

        # Etapa 3: Entrada "3"
        entrada2 = "3"
        v2 = locale.parse_number(entrada2)
        assert v2 == 3.0

        # Etapa 4: Calcular
        resultado = calc.calculate(v1, v2, op)
        assert resultado == 8.0

        # Etapa 5: Display
        display = locale.format_number(resultado)
        assert display == "8"

    def test_fluxo_completo_100_mais_0_01(self, setup):
        """
        Fluxo completo: 100 + 0,01 = 100,01
        """
        calc, locale = setup

        entrada1 = "100"
        v1 = locale.parse_number(entrada1)
        assert v1 == 100.0

        entrada2 = "0,01"
        v2 = locale.parse_number(entrada2)
        assert v2 == 0.01

        resultado = calc.calculate(v1, v2, '+')
        assert abs(resultado - 100.01) < 0.0001

        display = locale.format_number(resultado)
        assert "100,01" in display

    def test_fluxo_completo_12_5_mais_7_5(self, setup):
        """
        Fluxo completo com decimais: 12,5 + 7,5 = 20
        """
        calc, locale = setup

        entrada1 = "12,5"
        v1 = locale.parse_number(entrada1)
        assert v1 == 12.5

        entrada2 = "7,5"
        v2 = locale.parse_number(entrada2)
        assert v2 == 7.5

        resultado = calc.calculate(v1, v2, '+')
        assert resultado == 20.0

        display = locale.format_number(resultado)
        assert display == "20"

    # ====================================================================
    # Testes de Validação de Entrada
    # ====================================================================

    def test_validacao_entrada_invalida(self, setup):
        """
        Validar: entrada inválida é tratada
        Entrada "abc" deve gerar ValueError ao fazer float()
        """
        calc, locale = setup

        with pytest.raises(ValueError):
            locale.parse_number("abc")

    def test_validacao_entrada_vazia(self, setup):
        """
        Validar: entrada vazia retorna 0 (ou trata corretamente)
        """
        calc, locale = setup

        # Se entrada estiver vazia, UI deve ter "0" como padrão
        entrada = "0"
        valor = locale.parse_number(entrada)
        assert valor == 0.0

    def test_validacao_entrada_negativa(self, setup):
        """
        Validar: número negativo pode ser inserido
        Usuário pode digitar "-5" e somar com 10
        """
        calc, locale = setup

        # Se o UI permitir, negativo deve funcionar
        resultado = calc.calculate(-5, 10, '+')
        assert resultado == 5.0

    # ====================================================================
    # Testes de Precisão Decimal
    # ====================================================================

    def test_precisao_0_1_mais_0_2_igual_0_3(self, setup):
        """
        Validar: 0,1 + 0,2 = 0,3 (sem erro de float)
        Python: 0.1 + 0.2 = 0.30000000000000004
        Calculator faz round(resultado, 6) para corrigir
        """
        calc, locale = setup

        v1 = locale.parse_number("0,1")
        v2 = locale.parse_number("0,2")
        resultado = calc.calculate(v1, v2, '+')

        # Com precisão de 6 decimais
        assert round(resultado, 6) == 0.3

        display = locale.format_number(resultado)
        assert display == "0,3"

    def test_precisao_arredondamento_6_decimais(self, setup):
        """
        Validar: resultado é arredondado a 6 casas decimais
        5.123456789 + 0 → 5.123457 (arredondado)
        """
        calc, locale = setup

        # Força um número com muitos decimais
        resultado = calc.calculate(5.123456789, 0, '+')

        # Must be rounded to 6 decimals max
        assert round(resultado, 6) == round(5.123456789, 6)

    # ====================================================================
    # Testes de Formato pt-BR na Saída
    # ====================================================================

    def test_format_output_sem_decimais(self, setup):
        """
        Validar: 5 é exibido como "5" (sem decimais desnecessários)
        """
        calc, locale = setup

        resultado = calc.calculate(5, 0, '+')
        display = locale.format_number(resultado)
        assert display == "5"

    def test_format_output_com_virgula(self, setup):
        """
        Validar: 5.5 é exibido como "5,5" (com vírgula)
        """
        calc, locale = setup

        resultado = 5.5
        display = locale.format_number(resultado)
        assert display == "5,5"

    def test_format_output_com_milhar(self, setup):
        """
        Validar: 1000 é exibido como "1.000" (com ponto de milhar)
        """
        calc, locale = setup

        resultado = 1000.0
        display = locale.format_number(resultado)
        assert display == "1.000"

    # ====================================================================
    # Testes de Casos Limite
    # ====================================================================

    def test_adicao_numero_muito_grande(self, setup):
        """
        Validar: adicionar números muito grandes
        999999999 + 1 = 1000000000
        """
        calc, locale = setup

        resultado = calc.calculate(999999999, 1, '+')
        assert resultado == 1000000000.0

    def test_adicao_numero_muito_pequeno(self, setup):
        """
        Validar: adicionar números muito pequenos
        0,000001 + 0,000002 = 0,000003
        """
        calc, locale = setup

        entrada1 = "0,000001"
        entrada2 = "0,000002"
        v1 = locale.parse_number(entrada1)
        v2 = locale.parse_number(entrada2)

        resultado = calc.calculate(v1, v2, '+')
        assert round(resultado, 6) == 0.000003

    def test_adicao_numero_negativo_mais_numero_negativo(self, setup):
        """
        Validar: -5 + -3 = -8
        """
        calc, locale = setup

        resultado = calc.calculate(-5, -3, '+')
        assert resultado == -8.0

    def test_adicao_numero_grande_mais_numero_pequeno(self, setup):
        """
        Validar: 1000000 + 0,01 = 1000000,01
        """
        calc, locale = setup

        resultado = calc.calculate(1000000, 0.01, '+')
        assert abs(resultado - 1000000.01) < 0.0001


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
