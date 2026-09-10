"""
Configuração compartilhada de pytest.

Define fixtures e configurações globais para testes.
"""

import pytest
import sys
from pathlib import Path

# Adicionar src ao path para imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from calculator import Calculator
from locale_manager import LocaleManager


@pytest.fixture
def calculator():
    """Fixture que fornece uma instância limpa de Calculator."""
    calc = Calculator()
    yield calc
    calc.reset()


@pytest.fixture
def locale_manager():
    """Fixture que fornece a instância singleton de LocaleManager."""
    mgr = LocaleManager.get_instance()
    mgr.clear_cache()
    yield mgr
    mgr.clear_cache()
