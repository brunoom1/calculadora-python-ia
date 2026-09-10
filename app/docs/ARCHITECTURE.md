# Arquitetura — Calculadora Python

**Data**: 09/09/2026  
**Versão**: 1.0.0  
**Stack**: Python 3.10+ + Tkinter + pytest

---

## 📐 Visão Geral de Alto Nível

A Calculadora segue uma **arquitetura em camadas** com separação estrita entre apresentação, lógica e localização:

```
┌─────────────────────────────────────────┐
│         UI Layer (ui.py)                │
│  Tkinter - Apresentação + Eventos       │
└──────────────────────────────────────────┘
            ↓ Chamadas
┌─────────────────────────────────────────┐
│       Logic Layer (calculator.py)       │
│  Operações Matemáticas + Validações     │
└──────────────────────────────────────────┘
            ↓ Uses
┌─────────────────────────────────────────┐
│     Locale Layer (locale_manager.py)    │
│  Parser pt-BR + Formatter pt-BR         │
└──────────────────────────────────────────┘
```

---

## 🏗️ Componentes Principais

### 1. **Camada de Apresentação (UI)**

**Arquivo**: `src/ui.py`  
**Classe**: `CalculatorUI`

#### Responsabilidades:
- Criar widgets Tkinter (botões, display, layout)
- Capturar eventos de clique
- Formatar entrada/saída usando LocaleManager
- Orquestrar fluxo: entrada → cálculo → exibição

#### Estrutura Interna:
```python
class CalculatorUI:
    # Configurações de design (cores, dimensões)
    WINDOW_WIDTH = 280
    BUTTON_NUMBERS = [0, 1, 2, ..., 9]
    BUTTON_OPERATIONS = ['+', '-', '*', '/']
    
    # Estado da interface
    display_value: str          # Valor no display
    accumulated_value: float    # Valor acumulado para operação
    current_operation: str      # Operação em progresso
    
    # Métodos principales
    _on_number_click()          # Handle clique em número
    _on_operation_click()       # Handle clique em operação
    _on_equals_click()          # Handle clique em igual
    _on_clear_click()           # Handle clique em limpar
```

#### Fluxo de Entrada:
```
Usuário clica em número
    ↓
_on_number_click()
    ↓
Valida entrada (máx 15 caracteres, ponto decimal)
    ↓
Atualiza display_value
    ↓
_update_display()
    ↓
Label.config(text=display_value)
```

#### Fluxo de Operação:
```
Usuário clica em operação (+, -, *, /)
    ↓
_on_operation_click()
    ↓
locale_manager.parse_number(display_value) → float
    ↓
Se operação pendente: calculator.calculate(acc, current, op)
    ↓
Se sucesso: formato com locale_manager.format_number()
    ↓
Armazena operação e acumulador
    ↓
_update_display()
```

---

### 2. **Camada de Lógica (Calculator)**

**Arquivo**: `src/calculator.py`  
**Classe**: `Calculator`

#### Responsabilidades:
- Executar operações matemáticas (+, -, *, /)
- Validar operações (ex: divisão por zero)
- Manter precisão de 6 casas decimais
- Contar operações realizadas

#### Métodos Principais:

```python
def calculate(a: float, b: float, op: str) -> Union[float, str]
    """Calcula resultado ou retorna erro"""
    
def add(a: float, b: float) -> float
    """Soma dois números"""
    
def subtract(a: float, b: float) -> float
    """Subtrai"""
    
def multiply(a: float, b: float) -> float
    """Multiplica"""
    
def divide(a: float, b: float) -> Union[float, str]
    """Divide com validação de zero"""
    
def reset() -> None
    """Reseta estado"""
```

#### Características:
- **Sem estado persistente**: Cada operação é independente
- **Imutável em relação ao display**: Não formata, retorna float/str de erro
- **Testável isoladamente**: Nenhuma dependência de UI ou Locale

#### Precisão:
```python
MAX_PRECISION = 6

# Todos os resultados são arredondados
return round(a + b, self.MAX_PRECISION)
```

---

### 3. **Camada de Localização (LocaleManager)**

**Arquivo**: `src/locale_manager.py`  
**Classe**: `LocaleManager` (Singleton)

#### Responsabilidades:
- Fazer parse de entrada pt-BR ("1.234,56" → 1234.56)
- Formatar output pt-BR (1234.56 → "1.234,56")
- Manter cache para performance

#### Padrão pt-BR:
- **Separador decimal**: `,` (vírgula)
- **Separador de milhar**: `.` (ponto)
- **Exemplo**: "1.234.567,89" = um bilhão, duzentos e trinta e quatro mil, quinhentos e sessenta e sete vírgula oitenta e nove

#### Métodos:

```python
@classmethod
def get_instance() -> LocaleManager
    """Obtém instância singleton"""

def parse_number(value: str) -> float
    """"123,45" → 123.45"""
    """Remover pontos (milhar), substituir vírgula por ponto, converter float"""

def format_number(value: float) -> str
    """123.45 → "123,45" """
    """Separar inteira e decimal, aplicar formatação, reconverter"""

def clear_cache() -> None
    """Limpa cache de parsing"""
```

#### Implementação de Singleton:

```python
class LocaleManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

**Por quê Singleton?**
- Garante uma única instância em toda a aplicação
- Cache compartilhado de parsing
- Evita múltiplas configurações

---

## 🔄 Fluxo de Dados Completo

### Exemplo: Usuário calcula "5,5 + 2,5 ="

```
1. ENTRADA (UI)
   Usuário digita "5" → display = "5"
   Usuário digita "," → display = "5,"
   Usuário digita "5" → display = "5,5"

2. OPERAÇÃO (UI → LocaleManager → Calculator)
   Usuário clica "+" →
      a) parse_number("5,5") → 5.5 [LocaleManager]
      b) Armazenar: accumulated = 5.5, operation = '+'
      c) Limpar display para próximo número
   
3. SEGUNDA ENTRADA (UI)
   Usuário digita "2" → display = "2"
   Usuário digita "," → display = "2,"
   Usuário digita "5" → display = "2,5"

4. RESULTADO (UI → Calculator → LocaleManager → UI)
   Usuário clica "=" →
      a) parse_number("2,5") → 2.5 [LocaleManager]
      b) calculate(5.5, 2.5, '+') → 8.0 [Calculator]
      c) format_number(8.0) → "8" [LocaleManager]
      d) display = "8" [UI]
      e) accumulated = 0, operation = None
```

---

## 🧪 Arquitetura de Testes

### Pirâmide de Testes

```
        ╱╲
       ╱  ╲  Integration Tests (test_integration.py)
      ╱────╲ Testes UI ↔ Backend completos
     ╱      ╲
    ╱────────╲ Unit Tests (test_calculator.py, test_locale_manager.py)
   ╱          ╲ Testes isolados de cada classe
```

### Estrutura:

```
tests/
├── conftest.py                          # Fixtures compartilhadas
├── test_calculator.py                   # Calculator unitário
├── test_locale_manager.py               # LocaleManager unitário
├── test_integration.py                  # Integration UI ↔ Backend
└── test_chained_and_precision.py       # Operações encadeadas
```

### Exemplo de Fixture (conftest.py):

```python
@pytest.fixture
def calculator():
    """Fornece Calculator limpo para cada teste"""
    calc = Calculator()
    yield calc
    calc.reset()  # Cleanup

@pytest.fixture
def locale_manager():
    """Fornece LocaleManager (singleton) com cache limpo"""
    mgr = LocaleManager.get_instance()
    mgr.clear_cache()
    yield mgr
    mgr.clear_cache()  # Cleanup
```

### Tipos de Teste:

| Tipo | Arquivo | Exemplos | Propósito |
|------|---------|----------|-----------|
| Unit - Calculator | test_calculator.py | test_add_positive_numbers | Validar cada operação |
| Unit - Locale | test_locale_manager.py | test_parse_decimal_comma | Validar parsing/formatting |
| Integration | test_integration.py | test_workflow_simple_addition | Fluxo completo |
| Chained | test_chained_and_precision.py | test_chain_two_additions | Operações em sequência |

---

## 🔐 Padrões e Decisões Arquiteturais

### ADR-001: Separação UI-Lógica
**Decisão**: Calculator e LocaleManager NÃO dependem de Tkinter  
**Benefício**: Testáveis sem GUI, reutilizáveis (CLI, web)  
**Implementação**: UI chama métodos, recebe resultado float/str

### ADR-002: Singleton para LocaleManager
**Decisão**: Única instância com cache  
**Benefício**: Performance (cache de parsing), estado consistente  
**Implementação**: `__new__()` controla instância

### ADR-003: Resultado de Error como String
**Decisão**: `divide(a, 0)` retorna `"Erro: Divisão por zero"`  
**Benefício**: Distinção clara entre erro e resultado válido  
**Alternativa**: Usar exceção (rejeitado para manter simplicidade UI)

### ADR-004: Precisão de 6 Casas
**Decisão**: `round(resultado, 6)` em todas operações  
**Benefício**: Evita acúmulo de erro de ponto flutuante  
**Trade-off**: Limita precisão (aceitável para calculadora desktop)

### ADR-005: Cache em LocaleManager
**Decisão**: LRU dict para armazenar parsing  
**Benefício**: Mesmos valores não re-parseados  
**Limite**: Sem limpeza automática (clearCache() manual)

---

## 📊 Dependências

### Internas:
```
ui.py
    ↓ imports
    calculator.py
    locale_manager.py

calculator.py
    (nenhuma dependência interna)

locale_manager.py
    (nenhuma dependência interna)

main.py
    ↓ imports
    ui.py
```

### Externas:
```
Standard Library (built-in):
  - tkinter (para UI)
  - typing (para type hints)
  - decimal (não usada, futuro)

Third-party:
  - pytest (para testes, não necessário para rodar app)
```

---

## 🚀 Performance

### Complexity Analysis

| Operação | Time | Space | Notas |
|----------|------|-------|-------|
| calculate() | O(1) | O(1) | Operação simples |
| parse_number() | O(n) | O(1) | n = comprimento string |
| format_number() | O(n) | O(n) | n = dígitos do número |
| Singleton get_instance() | O(1) | O(1) | Lazyload única vez |
| Cache lookup | O(1) | - | Dict hash |

### Otimizações:
- **Cache em LocaleManager**: Evita re-parsing de valores repetidos
- **Singleton**: Uma única instância de LocaleManager
- **Round vs Decimal**: `round()` é mais rápido que Decimal para 6 casas

---

## 🔌 Extensibilidade

### Como adicionar novo operador:

1. Adicionar método em `Calculator`:
```python
def power(self, a: float, b: float) -> float:
    return round(a ** b, self.MAX_PRECISION)
```

2. Adicionar em `calculate()`:
```python
elif op == '^':
    return self.power(a, b)
```

3. Adicionar botão em UI:
```python
('√', self.BUTTON_OPERATION_BG, 1),
```

4. Adicionar handler:
```python
btn.config(command=lambda: self._on_operation_click('^'))
```

5. Adicionar testes:
```python
def test_power(self, calculator):
    assert calculator.calculate(2, 3, '^') == 8
```

### Como adicionar novo locale (en_US):

1. Criar classe `LocaleManager_EN`:
```python
class LocaleManagerEN(LocaleManager):
    DECIMAL_SEPARATOR = '.'
    THOUSAND_SEPARATOR = ','
```

2. Factory method:
```python
@staticmethod
def get_instance(locale='pt_BR'):
    # Retornar LocaleManager_EN() ou LocaleManager()
```

---

## 🐛 Tratamento de Erros

| Cenário | Manipulação | Resultado |
|---------|-------------|-----------|
| Divisão por zero | `if b == 0: return "Erro: ..."` | String erro |
| Entrada inválida | Try-except ValueError | Display "Erro: entrada inválida" |
| Número muito grande | Python handle automaticamente | Pode ter overflow (raro) |
| Operação inválida | ValueError em `_validate_operation()` | Exceção capturada em UI |

---

## 📈 Métricas de Código

```
Linhas de código (LOC)
├─ calculator.py:         ~180
├─ locale_manager.py:     ~200
├─ ui.py:                 ~320
├─ main.py:               ~20
└─ Total:                 ~720 LOC

Testes
├─ test_calculator.py:        ~180 LOC, 40 casos
├─ test_locale_manager.py:    ~240 LOC, 30 casos
├─ test_integration.py:       ~300 LOC, 15 casos
├─ test_chained_and_precision.py: ~300 LOC, 40 casos
└─ Total:                     ~1000 LOC, 125 casos

Ratio teste/código: 1.39:1 (excelente)
```

---

## 🎯 Roadmap de Melhorias

### Curto Prazo
- [ ] Implementar histórico de operações (T5.1)
- [ ] Modo científico com √, x², etc (T5.2)
- [ ] Support multi-locale com factory (T5.3)

### Médio Prazo
- [ ] Converter para PyQt6 (UI mais avançada)
- [ ] Versão web (Flask + frontend)
- [ ] Versão mobile (Kivy)

### Longo Prazo
- [ ] Salvar histórico em arquivo
- [ ] Temas dark/light
- [ ] Suporte a teclado completo

---

**Documento Pronto**: Arquitetura clara, extensível e bem-testada! 🚀
