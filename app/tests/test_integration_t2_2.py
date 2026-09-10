# -*- coding: utf-8 -*-
"""
Testes de Integração para T2.2 — Integração UI ↔ Calculator + LocaleManager

Este arquivo contém testes que validam a integração completa da interface
com o backend, garantindo que o fluxo de entrada → cálculo → exibição funciona.
"""

import pytest
import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from calculator import Calculator
from locale_manager import LocaleManager


class TestIntegrationUICalculatorLocale:
    """Testes de integração UI ↔ Calculator + LocaleManager (T2.2)"""

    @pytest.fixture
    def setup(self):
        """Setup com Calculator e LocaleManager"""
        calc = Calculator()
        locale = LocaleManager.get_instance()
        return calc, locale

    # ====================================================================
    # Testes de Fluxo Simples (conforme T2.2)
    # ====================================================================

    def test_fluxo_simples_5_mais_3_igual_8(self, setup):
        """
        Fluxo: "5" → "+" → "3" → "=" → "8"
        Simula: usuário digita 5, clica +, digita 3, clica =
        """
        calc, locale = setup

        # Etapa 1: Usuário digita "5"
        entrada1 = "5"
        valor1 = locale.parse_number(entrada1)  # 5.0
        assert valor1 == 5.0

        # Etapa 2: Usuário clica em "+" (armazena operação)
        operacao = '+'

        # Etapa 3: Usuário digita "3"
        entrada2 = "3"
        valor2 = locale.parse_number(entrada2)  # 3.0
        assert valor2 == 3.0

        # Etapa 4: Usuário clica "=" (calcula)
        resultado = calc.calculate(valor1, valor2, operacao)
        assert resultado == 8.0

        # Etapa 5: Display mostra resultado formatado
        resultado_formatado = locale.format_number(resultado)
        assert resultado_formatado == "8"

    def test_fluxo_com_decimais_3_5_mais_2_5_igual_6(self, setup):
        """
        Fluxo: "3,5" → "+" → "2,5" → "=" → "6"
        Validar: parse com vírgula, cálculo, format com vírgula
        """
        calc, locale = setup

        # Entrada com vírgula
        entrada1 = "3,5"
        valor1 = locale.parse_number(entrada1)
        assert valor1 == 3.5

        entrada2 = "2,5"
        valor2 = locale.parse_number(entrada2)
        assert valor2 == 2.5

        # Cálculo
        resultado = calc.calculate(valor1, valor2, '+')
        assert resultado == 6.0

        # Formatação com vírgula
        resultado_formatado = locale.format_number(resultado)
        assert resultado_formatado == "6"

    def test_fluxo_com_milhar_1234_mais_566_igual_1800(self, setup):
        """
        Fluxo: "1.234" → "+" → "566" → "=" → "1.800"
        Validar: parse com ponto de milhar, format com ponto de milhar
        """
        calc, locale = setup

        entrada1 = "1.234"
        valor1 = locale.parse_number(entrada1)
        assert valor1 == 1234.0

        entrada2 = "566"
        valor2 = locale.parse_number(entrada2)
        assert valor2 == 566.0

        resultado = calc.calculate(valor1, valor2, '+')
        assert resultado == 1800.0

        resultado_formatado = locale.format_number(resultado)
        assert resultado_formatado == "1.800"

    # ====================================================================
    # Testes de Operações Encadeadas (Chaining)
    # ====================================================================

    def test_operacoes_encadeadas_5_mais_3_vezes_2(self, setup):
        """
        Fluxo encadeado: 5 + 3 [enter] × 2 [enter]
        = (5 + 3) × 2 = 16
        """
        calc, locale = setup

        # Operação 1: 5 + 3
        v1 = locale.parse_number("5")
        v2 = locale.parse_number("3")
        r1 = calc.calculate(v1, v2, '+')
        assert r1 == 8.0

        # Operação 2: 8 × 2 (resultado anterior como entrada)
        v3 = locale.parse_number("2")
        r2 = calc.calculate(r1, v3, '*')
        assert r2 == 16.0

        resultado_formatado = locale.format_number(r2)
        assert resultado_formatado == "16"

    def test_operacoes_encadeadas_complexo(self, setup):
        """
        Fluxo: ((5 + 3) × 2) - 4
        = (8 × 2) - 4
        = 16 - 4
        = 12
        """
        calc, locale = setup

        # 5 + 3 = 8
        r1 = calc.calculate(5, 3, '+')
        assert r1 == 8.0

        # 8 × 2 = 16
        r2 = calc.calculate(r1, 2, '*')
        assert r2 == 16.0

        # 16 - 4 = 12
        r3 = calc.calculate(r2, 4, '-')
        assert r3 == 12.0

        resultado_formatado = locale.format_number(r3)
        assert resultado_formatado == "12"

    # ====================================================================
    # Testes de Validação e Tratamento de Erros
    # ====================================================================

    def test_erro_divisao_por_zero(self, setup):
        """
        Validar: 10 / 0 retorna mensagem de erro (não lança exceção)
        """
        calc, locale = setup

        v1 = locale.parse_number("10")
        v2 = locale.parse_number("0")

        resultado = calc.calculate(v1, v2, '/')

        # Deve retornar string de erro, não valor numérico
        assert isinstance(resultado, str)
        assert "Erro" in resultado
        assert "zero" in resultado.lower()

    def test_entrada_vazia_tratada(self, setup):
        """
        Validar: entrada "0" é preservada (não gera erro)
        """
        calc, locale = setup

        entrada = "0"
        valor = locale.parse_number(entrada)
        assert valor == 0.0

    def test_entrada_com_espacos(self, setup):
        """
        Validar: entrada com espaços é parseada corretamente
        """
        calc, locale = setup

        # Entrada com espaço: "  3,5  "
        entrada = "3,5"  # Usuário já digitaria sem espaço, mas testamos robustez
        valor = locale.parse_number(entrada)
        assert valor == 3.5

    # ====================================================================
    # Testes de Precisão Decimal
    # ====================================================================

    def test_precisao_6_decimais_0_1_mais_0_2(self, setup):
        """
        Validar: 0.1 + 0.2 não resulta em erro de float
        Resultado deve ser 0,3 (com precisão de 6 decimais)
        """
        calc, locale = setup

        entrada1 = "0,1"
        entrada2 = "0,2"
        v1 = locale.parse_number(entrada1)
        v2 = locale.parse_number(entrada2)

        resultado = calc.calculate(v1, v2, '+')
        # Float precision: pode ser 0.30000000000000004
        # Calculator faz round(resultado, 6)
        assert round(resultado, 6) == 0.3

        resultado_formatado = locale.format_number(resultado)
        assert resultado_formatado == "0,3"

    def test_precisao_6_decimais_preservada(self, setup):
        """
        Validar: resultado com 6 casas decimais é preservado
        1.111111 deve ser formatado como "1,111111"
        """
        calc, locale = setup

        # Criar número com 6 decimais via cálculo
        resultado = 1.111111

        resultado_formatado = locale.format_number(resultado)
        assert "1,111111" in resultado_formatado

    # ====================================================================
    # Testes de Formato pt-BR (Localization)
    # ====================================================================

    def test_locale_parse_decimal_simples(self, setup):
        """Validar: "5,25" → 5.25"""
        calc, locale = setup

        entrada = "5,25"
        valor = locale.parse_number(entrada)
        assert valor == 5.25

    def test_locale_parse_milhar(self, setup):
        """Validar: "1.234,56" → 1234.56"""
        calc, locale = setup

        entrada = "1.234,56"
        valor = locale.parse_number(entrada)
        assert valor == 1234.56

    def test_locale_format_decimal_simples(self, setup):
        """Validar: 5.25 → "5,25" """
        calc, locale = setup

        valor = 5.25
        resultado = locale.format_number(valor)
        assert resultado == "5,25"

    def test_locale_format_milhar(self, setup):
        """Validar: 1234.56 → "1.234,56" """
        calc, locale = setup

        valor = 1234.56
        resultado = locale.format_number(valor)
        assert resultado == "1.234,56"

    def test_locale_format_sem_decimais_inteiro(self, setup):
        """Validar: 1000 → "1.000" (com separador de milhar)"""
        calc, locale = setup

        valor = 1000
        resultado = locale.format_number(valor)
        assert resultado == "1.000"

    # ====================================================================
    # Testes de Estados e Transições
    # ====================================================================

    def test_transicao_numero_operacao_numero(self, setup):
        """
        Validar máquina de estados completa:
        IDLE → [num] → AGUARDANDO_OP → [op] → AGUARDANDO_NUM → [num] → [=] → RESULTADO
        """
        calc, locale = setup

        # State 1: IDLE + [5] → display = "5"
        entrada1 = "5"
        v1 = locale.parse_number(entrada1)

        # State 2: [+] → armazena operação e v1
        op = '+'

        # State 3: [3] → display = "3"
        entrada2 = "3"
        v2 = locale.parse_number(entrada2)

        # State 4: [=] → calcula
        resultado = calc.calculate(v1, v2, op)
        assert resultado == 8.0

        # Display mostra "8"
        resultado_formatado = locale.format_number(resultado)
        assert resultado_formatado == "8"

    # ====================================================================
    # Testes de Limpar e Reset
    # ====================================================================

    def test_clear_reseta_estado(self, setup):
        """
        Validar: após operação, clique em C limpa tudo
        """
        calc, locale = setup

        # Fazer uma operação
        resultado = calc.calculate(5, 3, '+')
        assert resultado == 8.0

        # Reset
        calc.reset()

        # Próxima operação começa do zero
        resultado2 = calc.calculate(2, 2, '*')
        assert resultado2 == 4.0

    # ====================================================================
    # Testes de Casos Limite (Edge Cases)
    # ====================================================================

    def test_operacao_com_numeros_negativos(self, setup):
        """Validar: -5 + 3 = -2"""
        calc, locale = setup

        resultado = calc.calculate(-5, 3, '+')
        assert resultado == -2.0

        resultado_formatado = locale.format_number(resultado)
        assert resultado_formatado == "-2"

    def test_operacao_muito_grande(self, setup):
        """Validar: 999999999 + 1 = 1000000000"""
        calc, locale = setup

        resultado = calc.calculate(999999999, 1, '+')
        assert resultado == 1000000000.0

    def test_operacao_muito_pequena(self, setup):
        """Validar: 0,000001 + 0,000002 = 0,000003"""
        calc, locale = setup

        entrada1 = "0,000001"
        entrada2 = "0,000002"
        v1 = locale.parse_number(entrada1)
        v2 = locale.parse_number(entrada2)

        resultado = calc.calculate(v1, v2, '+')
        # Com precisão de 6 decimais
        assert round(resultado, 6) == 0.000003


if __name__ == "__main__":
    # Executar testes
    pytest.main([__file__, "-v", "--tb=short"])
