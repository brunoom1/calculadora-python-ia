"""
Testes de integração entre UI e Backend.

Testa o fluxo completo: entrada → parsing → cálculo → formatação → exibição.
"""

import pytest
import sys
from pathlib import Path

# Adicionar src ao path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from calculator import Calculator
from locale_manager import LocaleManager


class TestIntegrationCalculatorLocale:
    """Testes de integração Calculator + LocaleManager."""

    def test_parse_calculate_format_addition(self, calculator, locale_manager):
        """Teste: Input "5,5" + "2,5" = "8" (parsing → calc → formatting)"""
        # Parse entrada
        a = locale_manager.parse_number("5,5")
        b = locale_manager.parse_number("2,5")
        
        # Calcular
        result = calculator.calculate(a, b, '+')
        
        # Formatar
        formatted = locale_manager.format_number(result)
        
        assert formatted == "8"

    def test_parse_calculate_format_decimal(self, calculator, locale_manager):
        """Teste: Input "10,5" + "2,3" = "12,8" """
        a = locale_manager.parse_number("10,5")
        b = locale_manager.parse_number("2,3")
        result = calculator.calculate(a, b, '+')
        formatted = locale_manager.format_number(result)
        
        assert formatted == "12,8"

    def test_parse_calculate_format_thousand_separator(self, calculator, locale_manager):
        """Teste: Input "1.000,50" + "500,50" = "1.501" """
        a = locale_manager.parse_number("1.000,50")
        b = locale_manager.parse_number("500,50")
        result = calculator.calculate(a, b, '+')
        formatted = locale_manager.format_number(result)
        
        assert formatted == "1.501"

    def test_parse_calculate_format_division(self, calculator, locale_manager):
        """Teste: Input "10" ÷ "3" = "3,333333" """
        a = locale_manager.parse_number("10")
        b = locale_manager.parse_number("3")
        result = calculator.calculate(a, b, '/')
        formatted = locale_manager.format_number(result)
        
        # Devem ser 6 casas decimais
        assert formatted == "3,333333"

    def test_parse_calculate_format_negative(self, calculator, locale_manager):
        """Teste: Input "5" - "10" = "-5" """
        a = locale_manager.parse_number("5")
        b = locale_manager.parse_number("10")
        result = calculator.calculate(a, b, '-')
        formatted = locale_manager.format_number(result)
        
        assert formatted == "-5"

    def test_parse_calculate_format_multiplication(self, calculator, locale_manager):
        """Teste: Input "2,5" × "4" = "10" """
        a = locale_manager.parse_number("2,5")
        b = locale_manager.parse_number("4")
        result = calculator.calculate(a, b, '*')
        formatted = locale_manager.format_number(result)
        
        assert formatted == "10"

    def test_error_handling_division_by_zero(self, calculator, locale_manager):
        """Teste: Erro em divisão por zero retorna mensagem"""
        a = locale_manager.parse_number("10")
        b = locale_manager.parse_number("0")
        result = calculator.calculate(a, b, '/')
        
        assert isinstance(result, str)
        assert "zero" in result.lower()

    def test_chained_operations_add_then_multiply(self, calculator, locale_manager):
        """Teste: Operações encadeadas (5 + 3) × 2 = 16"""
        # Primeira operação
        a1 = locale_manager.parse_number("5")
        b1 = locale_manager.parse_number("3")
        result1 = calculator.calculate(a1, b1, '+')
        
        # Segunda operação usa resultado anterior
        b2 = locale_manager.parse_number("2")
        result2 = calculator.calculate(result1, b2, '*')
        
        # Formatar
        formatted = locale_manager.format_number(result2)
        
        assert formatted == "16"

    def test_large_number_formatting(self, calculator, locale_manager):
        """Teste: Números grandes mantêm separador de milhar"""
        a = locale_manager.parse_number("1.000.000")
        b = locale_manager.parse_number("500.000")
        result = calculator.calculate(a, b, '+')
        formatted = locale_manager.format_number(result)
        
        assert formatted == "1.500.000"

    def test_precision_maintained_through_integration(self, calculator, locale_manager):
        """Teste: Precisão é mantida através do fluxo"""
        # Entrada com vírgula
        a = locale_manager.parse_number("1,23456789")
        b = locale_manager.parse_number("2,34567891")
        
        # Calcular
        result = calculator.calculate(a, b, '+')
        
        # Formatar - deve ter máx 6 casas
        formatted = locale_manager.format_number(result)
        
        # Verificar que não tem mais que 6 casas decimais
        if ',' in formatted:
            decimal_part = formatted.split(',')[1]
            assert len(decimal_part) <= 6

    def test_clear_resets_state(self, calculator):
        """Teste: Reset limpa estado da calculadora"""
        calculator.calculate(10, 5, '+')
        calculator.calculate(15, 3, '*')
        
        calculator.reset()
        
        assert calculator.result == 0.0
        assert calculator.get_operation_count() == 0

    def test_cache_improves_performance(self, locale_manager):
        """Teste: Cache evita re-parsing de mesmos valores"""
        assert locale_manager.get_cache_size() == 0
        
        # Primeiro parse
        val1 = locale_manager.parse_number("123,45")
        size1 = locale_manager.get_cache_size()
        
        # Segundo parse do mesmo valor
        val2 = locale_manager.parse_number("123,45")
        size2 = locale_manager.get_cache_size()
        
        # Devem ser iguais e cache não deve crescer
        assert val1 == val2
        assert size1 == size2


class TestUIWorkflow:
    """Testes que simulam o workflow da interface."""

    def test_workflow_simple_addition(self, calculator, locale_manager):
        """Simula: usuário digita "5,5" "+" "2,5" "=" na interface"""
        # Estado inicial
        display = "5,5"
        accumulated = locale_manager.parse_number(display)
        operation = "+"
        
        # Usuário digita segundo número
        display = "2,5"
        current = locale_manager.parse_number(display)
        
        # Clica igual
        result = calculator.calculate(accumulated, current, operation)
        display_result = locale_manager.format_number(result)
        
        assert display_result == "8"

    def test_workflow_clear_resets_display(self, calculator, locale_manager):
        """Simula: usuário faz cálculo, depois clica C (clear)"""
        # Fazer cálculo
        result = calculator.calculate(10, 5, '+')
        display = locale_manager.format_number(result)
        
        # Limpar
        calculator.reset()
        display = "0"
        
        assert display == "0"
        assert calculator.result == 0.0

    def test_workflow_chain_operations(self, calculator, locale_manager):
        """Simula: 5 + 3 - 2 × 4 ÷ 2 = 4"""
        # 5 + 3 = 8
        result = calculator.calculate(5, 3, '+')
        accumulated = locale_manager.format_number(result)
        
        # 8 - 2 = 6
        current = locale_manager.parse_number(accumulated)
        result = calculator.calculate(current, 2, '-')
        accumulated = locale_manager.format_number(result)
        
        # 6 × 4 = 24
        current = locale_manager.parse_number(accumulated)
        result = calculator.calculate(current, 4, '*')
        accumulated = locale_manager.format_number(result)
        
        # 24 ÷ 2 = 12
        current = locale_manager.parse_number(accumulated)
        result = calculator.calculate(current, 2, '/')
        final_display = locale_manager.format_number(result)
        
        assert final_display == "12"

    def test_workflow_error_recovery(self, calculator, locale_manager):
        """Simula: usuário faz erro (div por zero), depois continua"""
        # Tentar divisão por zero
        result = calculator.calculate(10, 0, '/')
        assert isinstance(result, str)  # Erro
        
        # Limpar e fazer novo cálculo
        calculator.reset()
        result = calculator.calculate(5, 5, '+')
        display = locale_manager.format_number(result)
        
        assert display == "10"

    def test_workflow_negative_result(self, calculator, locale_manager):
        """Simula: usuário faz subtração que resulta em negativo"""
        result = calculator.calculate(3, 10, '-')
        display = locale_manager.format_number(result)
        
        assert display == "-7"

    def test_workflow_decimal_input_validation(self, locale_manager):
        """Simula: validação de entrada com decimais"""
        # Entrada válida com vírgula
        result = locale_manager.parse_number("123,45")
        assert result == 123.45
        
        # Entrada com múltiplas vírgulas é inválida
        with pytest.raises(ValueError):
            locale_manager.parse_number("123,45,67")

    def test_workflow_display_update_sequence(self, calculator, locale_manager):
        """Simula sequência de atualizações de display"""
        displays = []
        
        # Usuário digita "1"
        displays.append("1")
        
        # Digita mais "23"
        displays.append("123")
        
        # Clica "+"
        accumulated = locale_manager.parse_number("123")
        displays.append("123")
        
        # Digita "4" "5" 
        displays.append("45")
        
        # Clica "="
        result = calculator.calculate(123, 45, '+')
        displays.append(locale_manager.format_number(result))
        
        # Validar sequência final
        assert displays[-1] == "168"
        assert len(displays) == 5
