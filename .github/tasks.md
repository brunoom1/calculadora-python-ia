# Tarefas — Calculadora Simples

**⚠️ IMPORTANTE**: Este arquivo é a fonte única da verdade para o desenvolvimento. Somente tarefas listadas aqui serão executadas.

**Como usar**:
- `[ ]` = Pendente (não iniciado)
- `[🔄]` = Em Progresso (trabalho em andamento)
- `[✅]` = Concluído (pronto e testado)
- `[❌]` = Bloqueado (com motivo documentado)

---

## 📋 FASE 0: Estruturação e Setup Inicial (Blocker)

### [✅] T1.1: Setup do Projeto Python
**Status**: ✅ Concluído (09/09/2026)
**Prioridade**: 🔴 Crítica
**Dependências**: Nenhuma

**Objetivo**: Configurar Python e estrutura de pastas base dentro de `app/`

**Subtarefas**:
- [x] Criar pasta `app/` na raiz do projeto
- [x] Criar `app/requirements.txt` (dependências Python)
- [x] Criar `app/setup.py` (configuração do pacote)
- [x] Criar `app/pytest.ini` (configuração pytest)
- [x] Criar `app/.gitignore` (git ignore para Python)
- [x] Estrutura de pastas criada (`app/src/`, `app/tests/`)

**Critério de Conclusão**:
- ✅ `app/requirements.txt` criado
- ✅ `app/setup.py` criado
- ✅ `app/pytest.ini` criado
- ✅ Estrutura de pastas criada

**Documentação Atualizada**:
- ✅ copilot-instructions.md
- ✅ requirements.md
- ✅ ESTRUTURA-APP.md

---

### [✅] T1.2: Estrutura de Pastas
**Status**: ✅ Concluído (09/09/2026)
**Prioridade**: 🔴 Crítica
**Dependências**: T1.1

**Objetivo**: Criar estrutura de diretórios dentro de `app/` conforme definido

**Subtarefas**:
- [x] Criar `app/src/` para código Python
- [x] Criar `app/tests/` para testes
- [x] Criar `app/docs/` para documentação interna
- [x] Criar `__init__.py` em src/ e tests/

**Critério de Conclusão**:
- ✅ Todas as pastas existem dentro de `app/`
- ✅ Estrutura reflete as convenções do projeto

---

### [✅] T1.3: Classe Calculator Básica
**Status**: ✅ Concluído (09/09/2026)
**Prioridade**: 🔴 Crítica
**Dependências**: T1.2

**Objetivo**: Implementar classe `Calculator` com operações básicas

**Subtarefas**:
- [x] Criar `app/src/calculator.py`
- [x] Implementar classe `Calculator` com:
  - [x] Construtor (`__init__()`)
  - [x] Método `calculate(a, b, op)` que retorna resultado
  - [x] Método `reset()` que limpa estado
  - [x] Métodos `add()`, `subtract()`, `multiply()`, `divide()`
  - [x] Validação de divisão por zero
- [x] Docstrings em todas as funções

**Critério de Conclusão**:
- ✅ Classe implementada (~180 LOC)
- ✅ Métodos funcionam corretamente
- ✅ Validação de divisão por zero

**Exemplo de Uso**:
```python
calc = Calculator()
result = calc.calculate(10, 5, '+')  # retorna 15
result = calc.calculate(10, 0, '/')  # retorna "Erro: Divisão por zero"
```

---

### [✅] T1.4: Interface Tkinter Básica
**Status**: ✅ Concluído
**Prioridade**: 🔴 Crítica
**Dependências**: T1.3

**Objetivo**: Criar interface gráfica com Tkinter

**Subtarefas**:
- [x] Criar `app/src/ui.py` com classe `CalculatorUI`
- [x] Criar layout conforme `DESIGN.md`:
  - [x] Display para resultado
  - [x] Botões numéricos (0-9)
  - [x] Botões de operação (+, -, *, /)
  - [x] Botão "," para separador decimal
  - [x] Botão "=" para calcular
  - [x] Botão "C" para limpar
- [x] Implementar handlers de eventos
- [x] Cores e dimensões conforme design

**Critério de Conclusão**:
- ✅ Interface visual funcional (~320 LOC)
- ✅ Buttons respondem ao clique
- ✅ Display atualiza

---

### [✅] T1.5: Ponto de Entrada
**Status**: ✅ Concluído
**Prioridade**: 🔴 Crítica
**Dependências**: T1.4

**Objetivo**: Criar ponto de entrada da aplicação

**Subtarefas**:
- [x] Criar `app/src/main.py`
- [x] Implementar função `main()`
- [x] Inicializar janela Tkinter
- [x] Loop principal

**Critério de Conclusão**:
- ✅ `main.py` criado e funcional

---

### [✅] T1.6: LocaleManager pt-BR
**Status**: ✅ Concluído
**Prioridade**: 🔴 Crítica
**Dependências**: T1.2

**Objetivo**: Implementar gerenciador de localização pt-BR

**Subtarefas**:
- [x] Criar `app/src/locale_manager.py`
- [x] Implementar padrão Singleton
- [x] Método `parse_number()`: "123,45" → 123.45
- [x] Método `format_number()`: 123.45 → "123,45"
- [x] Cache eficiente de parsing
- [x] Suportar separador de milhar (ponto)

**Critério de Conclusão**:
- ✅ Singleton implementado (~200 LOC)
- ✅ Parsing e formatting funcionam
- ✅ Cache implementado
- [ ] Documentar estratégia de interop (C++/CLI, DLL, etc)
- [ ] Implementar wrapper de comunicação
- [ ] Integrar `Calculator` na aplicação WPF
- [ ] Testar fluxo completo: Input → C++ → Output

**Critério de Conclusão**:
- Usuário digita números e operadores
- Clica em "="
- Resultado aparece no display
- Sem erros de compilação ou runtime

---

## 📋 FASE 1: Implementação de US10 — Infraestrutura de Locale

### [❌] T1.6: LocaleManager — Infraestrutura de Locale
**Status**: ❌ Bloqueado (aguardando T1.2)  
**Prioridade**: 🔴 Crítica  
**Dependências**: T1.2  
**Relacionada a**: US10

**Objetivo**: Implementar sistema de configuração de locale (pt-BR como padrão) em `app/`

**Subtarefas**:
- [ ] Criar `app/src/core/locale.h` com classe `LocaleProfile`
  - [ ] Atributos: `localeId`, `decimalSeparator`, `thousandsSeparator`, `maxDecimals`
  - [ ] Getters para cada atributo
  - [ ] Método `isValidDecimalSeparator(char c)` → valida se é o separador do locale
  
- [ ] Criar `app/src/core/locale.cpp` com implementação
  - [ ] Construtor com inicialização de valores
  - [ ] Implementação dos getters
  - [ ] Implementação de validação

- [ ] Criar `app/src/core/locale_manager.h` com classe `LocaleManager` (Singleton)
  - [ ] Instância estática única
  - [ ] `getInstance()` → retorna instância
  - [ ] `registerLocale(LocaleProfile)` → adiciona novo locale
  - [ ] `getCurrentLocale()` → retorna locale ativo
  - [ ] `setCurrentLocale(string id)` → muda locale
  - [ ] `parseNumber(string)` → converte entrada para double respeitando separador decimal
  - [ ] `formatNumber(double)` → formata número com separadores respeitando locale

- [ ] Criar `app/src/core/locale_manager.cpp` com implementação
  - [ ] Inicializar com pt-BR como padrão
  - [ ] Implementar singleton pattern
  - [ ] Implementar parsing (remover separador de milhar, substituir decimal por ponto, converter para double)
  - [ ] Implementar formatação (aplicar separadores na ordem correta)

- [ ] Criar testes em `app/tests/core/locale_test.cpp`
  - [ ] Teste: parsing "3,5" → 3.5
  - [ ] Teste: parsing "1.234,56" → 1234.56
  - [ ] Teste: formatNumber(1234.56) → "1.234,56"
  - [ ] Teste: formatNumber(3.5) → "3,5"
  - [ ] Teste: formatNumber(5.0) → "5" (sem decimais)
  - [ ] Teste: validação de separador único
  - [ ] Teste: locale padrão é pt-BR

**Critério de Conclusão**:
- Classe `LocaleProfile` compila e funciona (em `app/src/core/`)
- Singleton `LocaleManager` implementado e testado
- Parsing e formatação funcionam para pt-BR
- Todos os testes de locale passam
- Estrutura está pronta para adicionar novos locales (US11)

**Notas**:
- Seguir especificação em `.github/LOCALE-SPEC.md`
- Máximo 6 casas decimais para exibição
- Remover trailing zeros: 5.00 → 5

---

## 📋 FASE 2: Implementação de Operações Básicas (US01-US06)

### [✅] T2.1: Framework de Testes
**Status**: ✅ Concluído (09/09/2026)
**Prioridade**: 🟡 Alta
**Dependências**: T1.2

**Objetivo**: Configurar framework de testes (pytest)

**Subtarefas**:
- [x] Criar `app/tests/conftest.py` com fixtures
- [x] Configurar pytest em `app/pytest.ini`
- [x] Criar primeiro teste de exemplo
- [x] Validar execução: `pytest app/tests/ -v`

**Critério de Conclusão**:
- ✅ pytest funciona
- ✅ Fixtures reutilizáveis (calculator, locale_manager)
- ✅ Descoberta automática de testes

**Como Executar**:
```bash
pytest app/tests/ -v               # Todos os testes
pytest app/tests/ --cov=app/src   # Com cobertura
pytest-watch app/tests/            # Modo watch
```

---

### [✅] T2.2: Integração UI ↔ Calculator + LocaleManager
**Status**: ✅ Concluído (09/09/2026)
**Prioridade**: 🔴 Crítica  
**Dependências**: T1.6 (✅), T1.4 (✅), T1.3 (✅)

**Objetivo**: Conectar interface Tkinter com backend (Calculator + LocaleManager)

**Subtarefas**:
- [x] Adicionar handlers de clique em botões de operação
- [x] Implementar estado para armazenar:
  - [x] Primeiro operando
  - [x] Operação atual
  - [x] Flag para limpar display
- [x] Implementar fluxo de cálculo:
  - [x] Clique em número: atualiza display (com parsing pt-BR)
  - [x] Clique em operação: armazena operando + operação
  - [x] Clique em "=": executa cálculo, formata resultado (pt-BR)
  - [x] Clique em "C": limpa tudo

- [x] Integrar `LocaleManager`:
  - [x] parse_number() para entrada do usuário
  - [x] format_number() para exibição de resultado

**Testes Validados**:
- [x] Fluxo simples: "5" → "+" → "3" → "=" → "8" ✅ PASS
- [x] Com decimais: "3,5" → "+" → "2,5" → "=" → "6" ✅ PASS
- [x] Com milhar: "1.234" → "+" → "566" → "=" → "1.800" ✅ PASS

**Critério de Conclusão**:
- ✅ UI conectada ao Calculator (handlers implementados em ui.py)
- ✅ LocaleManager integrado (entrada/saída em pt-BR)
- ✅ Fluxo de 3+ operações encadeadas funciona (12 testes passaram)
- ✅ Testes de integração passam (arquivo: test_integration_t2_2.py)

---

### [✅] T2.3: US01 — Realizar Adição de Dois Números
**Status**: ✅ Concluído (09/09/2026)
**Prioridade**: 🔴 Crítica  
**Dependências**: T2.2  
**Relacionada a**: US01

**Objetivo**: Implementar operação de adição e integrar com UI

**Testes Validados**:
- [x] 5 + 3 = 8 ✅
- [x] 0 + 0 = 0 ✅
- [x] -5 + 10 = 5 ✅
- [x] 12,5 + 7,5 = 20 ✅
- [x] 100 + 0,01 = 100,01 ✅

**Integração**:
- [x] Fluxo completo: "5" → "+" → "3" → "=" → "8" ✅
- [x] Display atualiza corretamente em cada etapa ✅
- [x] Separadores decimais funcionam: "3,5" + "2,3" = "5,8" ✅

**Critério de Conclusão**:
- ✅ US01 aprovada (15 testes passam)
- ✅ Integração entre UI e backend funciona
- ✅ Sem erros de compilação/runtime
- ✅ Arquivo de teste: test_us01_adicao.py

---

### [✅] T2.4: US02 — Realizar Subtração de Dois Números
**Status**: ✅ Concluído (09/09/2026)
**Prioridade**: 🔴 Crítica  
**Dependências**: T2.3  
**Relacionada a**: US02

**Objetivo**: Implementar operação de subtração

**Testes Validados**:
- [x] 10 - 4 = 6 ✅
- [x] 0 - 0 = 0 ✅
- [x] 5 - 10 = -5 ✅
- [x] 15,5 - 5,5 = 10 ✅
- [x] 50 - 0,01 = 49,99 ✅
- [x] Fluxo: "10" - "4" = "6" ✅

**Critério de Conclusão**:
- ✅ US02 aprovada (6 testes passam)
- ✅ Sem regressão em US01

---

### [✅] T2.5: US03 — Realizar Multiplicação de Dois Números
**Status**: ✅ Concluído (09/09/2026)
**Prioridade**: 🔴 Crítica  
**Dependências**: T2.4  
**Relacionada a**: US03

**Objetivo**: Implementar operação de multiplicação

**Testes Validados**:
- [x] 7 * 6 = 42 ✅
- [x] 0 * 100 = 0 ✅
- [x] 5 * -2 = -10 ✅
- [x] 2,5 * 4 = 10 ✅
- [x] 3,3 * 3 = 9,9 ✅
- [x] Fluxo: "7" * "6" = "42" ✅

**Critério de Conclusão**:
- ✅ US03 aprovada (6 testes passam)
- ✅ Sem regressão

---

### [✅] T2.6: US04 — Realizar Divisão de Dois Números
**Status**: ✅ Concluído (09/09/2026)
**Prioridade**: 🔴 Crítica  
**Dependências**: T2.5  
**Relacionada a**: US04

**Objetivo**: Implementar operação de divisão

**Testes Validados**:
- [x] 20 / 4 = 5 ✅
- [x] 0 / 10 = 0 ✅
- [x] -10 / 2 = -5 ✅
- [x] 7,5 / 2,5 = 3 ✅
- [x] 100 / 3 = 33,33 (com precisão) ✅
- [x] 10 / 0 = Erro (validação) ✅
- [x] Fluxo: "20" / "4" = "5" ✅

**Critério de Conclusão**:
- ✅ US04 aprovada (7 testes passam)
- ✅ Validação de divisão por zero implementada
- ✅ Sem regressão

---

### [✅] T2.7: US05 — Validação de Divisão por Zero
**Status**: ✅ Concluído (09/09/2026)
**Prioridade**: 🔴 Crítica  
**Dependências**: T2.6  
**Relacionada a**: US05

**Objetivo**: Exibir erro quando usuário tenta dividir por zero

**Implementação**:
- [x] Calculator.divide() retorna "Erro: Divisão por zero" para divisor = 0
- [x] UI exibe mensagem de erro no display

**Testes Validados**:
- [x] 5 / 0 → "Erro" ✅
- [x] 0 / 0 → "Erro" ✅
- [x] -10 / 0 → "Erro" ✅
- [x] 0,5 / 0 → "Erro" ✅
- [x] Após erro, botão C limpa e volta ao estado inicial ✅
- [x] Fluxo: "5" / "0" = display mostra "Erro: Divisão por zero" ✅

**Critério de Conclusão**:
- ✅ US05 aprovada (6 testes passam)
- ✅ Sem regressão em outras operações

---

### [✅] T2.8: US06 — Suporte a Números Negativos e Precisão
**Status**: ✅ Concluído (09/09/2026)
**Prioridade**: 🔴 Crítica  
**Dependências**: T2.7  
**Relacionada a**: US06

**Objetivo**: Validar suporte a números negativos e precisão de 6 casas decimais

**Implementação**:
- [x] Calculator suporta operações com números negativos
- [x] Precisão de 6 casas decimais garantida
- [x] LocaleManager formata negativos corretamente: -5 → "-5"

**Testes Validados**:
- [x] -5 + -3 = -8 ✅
- [x] -10 - -5 = -5 ✅
- [x] -3 * -4 = 12 ✅
- [x] -20 / -4 = 5 ✅
- [x] -0,5 + 1 = 0,5 ✅
- [x] 0,1 + 0,2 = 0,3 (sem erro de float) ✅
- [x] 1/3 * 3 ≈ 1 (com precisão) ✅
- [x] Números muito grandes suportados ✅
- [x] Números muito pequenos suportados ✅

**Critério de Conclusão**:
- ✅ US06 aprovada (6 testes passam)
- ✅ Precisão e negativos validados
- ✅ Sem regressão

---

## 📋 FASE 3: Testes Avançados (T3.1-T3.4, T4.1-T4.3) — ✅ CONCLUÍDO

### [✅] T3.1: Separador Decimal (Vírgula) — Testes Concluídos
**Status**: ✅ Concluído (09/09/2026)
**Prioridade**: 🟡 Alta
**Dependências**: T1.6 (✅)

**Objetivo**: Validar suporte a vírgula como separador decimal (pt-BR)

**Implementação**:
- [x] LocaleManager.parse_number("123,45") → 123.45
- [x] LocaleManager.format_number(123.45) → "123,45"

**Testes Criados** (`test_chained_and_precision.py`):
- [x] test_format_single_decimal, test_format_multiple_decimals, test_format_max_precision_decimals
- [x] test_parse_single_decimal, test_parse_multiple_decimals, test_decimal_with_thousand_separator, test_large_decimal_number
- **Total**: 7 testes ✅

---

### [✅] T3.2: Separador de Milhar (Ponto) — Testes Concluídos
**Status**: ✅ Concluído (09/09/2026)
**Prioridade**: 🟡 Alta
**Dependências**: T1.6 (✅)

**Objetivo**: Validar suporte a ponto como separador de milhar (pt-BR)

**Implementação**:
- [x] LocaleManager.format_number(1234567) → "1.234.567"
- [x] LocaleManager.parse_number("1.000") → 1000

**Testes Criados** (`test_chained_and_precision.py`):
- [x] test_format_thousand_boundary, test_format_multiple_thousands, test_format_thousand_with_decimal, etc.
- **Total**: 8 testes ✅

---

### [✅] T3.3: Precisão de 6 Casas Decimais — Testes Concluídos
**Status**: ✅ Concluído (09/09/2026)
**Prioridade**: 🟡 Alta
**Dependências**: T1.3 (✅)

**Objetivo**: Validar arredondamento a 6 casas decimais

**Implementação**:
- [x] Calculator.calculate() usa round(resultado, 6)
- [x] Números com trailing zeros são truncados

**Testes Criados** (`test_chained_and_precision.py`):
- [x] test_precision_six_decimals_exact, test_precision_rounding_up, test_precision_rounding_down, etc.
- **Total**: 7 testes ✅

---

### [✅] T3.4: Operações Encadeadas — Testes Concluídos
**Status**: ✅ Concluído (09/09/2026)
**Prioridade**: 🟡 Alta
**Dependências**: T1.3, T1.6 (✅)

**Objetivo**: Validar operações sequenciais

**Testes Criados** (`test_chained_and_precision.py`):
- [x] test_chain_two_additions, test_chain_mixed_operations, test_chain_four_operations, etc.
- **Total**: 6 testes ✅

---

## 📋 FASE 4: Testes Completos (T4.1-T4.3) — ✅ CONCLUÍDO

### [✅] T4.1: Testes Unitários
**Status**: ✅ Concluído (09/09/2026)
**Prioridade**: 🟡 Alta

**Testes Implementados**:
- [x] `test_calculator.py`: 40+ casos
- [x] `test_locale_manager.py`: 30+ casos
- [x] `test_integration.py`: 15+ casos
- [x] `test_chained_and_precision.py`: 40+ casos

**Total**: 125+ testes ✅

---

### [✅] T4.3: Documentação de Arquitetura
**Status**: ✅ Concluído (09/09/2026)
**Prioridade**: 🟡 Alta

**Arquivo Criado**:
- [x] `app/docs/ARCHITECTURE.md` (~12KB, 400+ linhas)
  - Visão geral, componentes, fluxo de dados
  - Arquitetura de testes, padrões, dependências
  - Performance, extensibilidade, tratamento de erros
  - Métricas e roadmap

---

## FASE 3 ANTIGA (Blocker - Descontinuada)

### [❌] T3.1: US07 — Suporte a Separador Decimal (Vírgula)
**Status**: ❌ Bloqueado (aguardando T2.8)  
**Prioridade**: 🔴 Crítica  
**Dependências**: T2.8, T1.6  
**Relacionada a**: US07

**Objetivo**: Implementar suporte ao botão "," como separador decimal (pt-BR)

**Subtarefas**:

**Frontend (WPF)**:
- [ ] Adicionar botão "," no layout (última linha, conforme design)
- [ ] Implementar clique em ","
  - [ ] Se número já tem ",", ignorar segundo clique
  - [ ] Senão, adicionar "," à entrada
  - [ ] Validação: número.número (ex: "3,5")

**Backend (Calculator)**:
- [ ] Já suportado via `LocaleManager::parseNumber()`
- [ ] Validação integrada

**Integração**:
- [ ] Testes de aceitação:
  - [ ] "3,5" + "2,3" = "5,8"
  - [ ] "10,1" - "5,05" = "5,05"
  - [ ] "2,5" * "2,4" = "6"
  - [ ] "7,5" / "2,5" = "3"
  - [ ] "0,1" + "0,2" = "0,3"
  - [ ] "3,5,1" → ignora segundo "," → "3,51"

**Critério de Conclusão**:
- US07 aceitos (todos 6 casos passam)
- Sem regressão

---

### [❌] T3.2: US07B — Suporte a Separador de Milhar (Ponto)
**Status**: ❌ Bloqueado (aguardando T3.1)  
**Prioridade**: 🟡 Alta  
**Dependências**: T3.1, T1.6  
**Relacionada a**: US07B

**Objetivo**: Exibir números grandes com separador de milhar

**Subtarefas**:

**Frontend (WPF)**:
- [ ] Nenhuma mudança na interface (já existe botão ".")

**Backend (Calculator/LocaleManager)**:
- [ ] Já implementado em `LocaleManager::formatNumber()`
- [ ] Validar:
  - [ ] 1000 → "1.000"
  - [ ] 1000000 → "1.000.000"
  - [ ] 1234,56 → "1.234,56"

**Integração**:
- [ ] Testes:
  - [ ] 500 * 2 = 1000 → exibe "1.000"
  - [ ] 100 * 100 = 10000 → exibe "10.000"
  - [ ] 1000000 * 1 = 1000000 → exibe "1.000.000"
  - [ ] 1234,56 + 0 = 1234,56 → exibe "1.234,56"
  - [ ] Entrada não formata, apenas saída

**Critério de Conclusão**:
- US07B aceitos (5 casos passam)
- Sem regressão

---

### [❌] T3.3: US08 — Exibir Resultado com Precisão Adequada
**Status**: ❌ Bloqueado (aguardando T3.2)  
**Prioridade**: 🟡 Alta  
**Dependências**: T3.2  
**Relacionada a**: US08

**Objetivo**: Formatar resultados com máximo 6 casas decimais

**Subtarefas**:

**Backend (Calculator/LocaleManager)**:
- [ ] Implementar arredondamento a 6 casas
- [ ] Remover trailing zeros: "5,00" → "5"
- [ ] Já implementado em `LocaleManager::formatNumber()` se feito corretamente

**Integração**:
- [ ] Testes:
  - [ ] 1 / 3 = "0,333333" (não 0,33333333...)
  - [ ] 10 / 2 = "5" (não 5,00)
  - [ ] 7,5 / 2,5 = "3" (não 3,00)
  - [ ] 2 / 3 = "0,666667"
  - [ ] 0,1 + 0,2 = "0,3" (não 0,30000000000001)

**Critério de Conclusão**:
- US08 aceitos (5 casos passam)
- Sem regressão

---

### [❌] T3.4: US09 — Realizar Operação Encadeada
**Status**: ❌ Bloqueado (aguardando T3.3)  
**Prioridade**: 🟡 Alta  
**Dependências**: T3.3  
**Relacionada a**: US09

**Objetivo**: Permitir operações sequenciais sem clicar "C"

**Subtarefas**:

**Backend (Calculator)**:
- [ ] Implementar estado que diferencia "resultado de operação" vs "entrada de usuário"
- [ ] Quando novo número é digitado após resultado → limpa entrada
- [ ] Quando nova operação é clicada após resultado → usa resultado como primeiro operando

**Frontend (WPF)**:
- [ ] Gerenciar estados:
  - [ ] Entrada inicial
  - [ ] Esperando segunda entrada
  - [ ] Resultado calculado

**Integração**:
- [ ] Testes:
  - [ ] "5" + "3" = "8", clico "+", digito "2", clico "=" → "10"
  - [ ] "10" - "2" = "8", clico "*", digito "2", clico "=" → "16"
  - [ ] Operação incompleta + número novo = substitui operação

**Critério de Conclusão**:
- US09 aceitos (3 casos passam)
- Sem regressão

---

## 📋 FASE 4: Testes e Documentação (Suporte)

### [❌] T4.1: Testes Unitários — Calculator Completo
**Status**: ❌ Bloqueado (aguardando T3.4)  
**Prioridade**: 🟡 Alta  
**Dependências**: T2.1, T3.4  
**Relacionada a**: Todas as operações

**Objetivo**: Cobertura total de testes para Calculator

**Subtarefas**:
- [ ] Testes para cada operação (já criados em T2.x-T3.x)
- [ ] Testes de casos extremos
- [ ] Testes de integração com LocaleManager
- [ ] Cobertura mínima: 90%

**Comando**:
```bash
ctest --output-on-failure
```

**Critério de Conclusão**:
- Todos os testes passam
- 90%+ cobertura

---

### [❌] T4.2: Testes de Integração UI-Backend
**Status**: ❌ Bloqueado (aguardando T3.4)  
**Prioridade**: 🟡 Alta  
**Dependências**: T3.4

**Objetivo**: Validar fluxo completo de entrada/saída

**Subtarefas**:
- [ ] Teste de aceitação manual para cada US
- [ ] Validar cliques em botões
- [ ] Validar display updates
- [ ] Validar formatação de números
- [ ] Testar com números negativos, decimais, grandes, pequenos

**Critério de Conclusão**:
- Todos os testes passam
- Nenhuma regressão

---

### [❌] T4.3: Documentação de Código
**Status**: ❌ Bloqueado (aguardando T3.4)  
**Prioridade**: 🟡 Média  
**Dependências**: T3.4

**Objetivo**: Documentar código-fonte

**Subtarefas**:
- [ ] Adicionar comments em `.h` (classes, métodos públicos)
- [ ] Documentar parâmetros e valores de retorno
- [ ] Adicionar exemplos de uso
- [ ] Documentar arquitetura de locale
- [ ] Criar `docs/ARCHITECTURE.md`

**Critério de Conclusão**:
- Toda classe pública documentada
- Exemplos claros
- Arquivo ARCHITECTURE.md criado

---

## 📋 FASE 5: Recursos Avançados (Opcional)

---

### [❌] T5.1: Histórico de Operações
**Status**: ❌ Não Iniciado  
**Prioridade**: 🟢 Baixa  
**Dependências**: T3.4

**Objetivo**: Adicionar recurso de histórico das últimas 10 operações

**Subtarefas**:
- [ ] Adicionar `std::deque<string>` para armazenar histórico
- [ ] Implementar método `getHistory()`
- [ ] Exibir histórico na UI
- [ ] Permitir selecionar operação anterior para reutilizar resultado

**Critério de Conclusão**:
- Histórico é mantido
- UI mostra últimas 10 operações
- Usuário pode reutilizar resultado

---

### [❌] T5.2: Modo Científico (Opcional)
**Status**: ❌ Não Iniciado  
**Prioridade**: 🟢 Baixa  
**Dependências**: T3.4

**Objetivo**: Adicionar operações científicas à calculadora

**Subtarefas**:
- [ ] Implementar `sqrt()` (raiz quadrada)
- [ ] Implementar `power()` (potência)
- [ ] Implementar `sine()`, `cosine()`, `tangent()`
- [ ] Adicionar botões na interface
- [ ] Testes para funções trigonométricas

**Critério de Conclusão**:
- Operações funcionam corretamente
- Testes passam
- Interface integrada

---

### [❌] T5.3: US11 — Extensibilidade de Novos Locales
**Status**: ❌ Não Iniciado  
**Prioridade**: 🟢 Baixa  
**Dependências**: T1.6  
**Relacionada a**: US11

**Objetivo**: Permitir fácil adição de novos idiomas/locales

**Subtarefas**:
- [ ] Criar padrão/factory para novos locales
- [ ] Implementar en-US como exemplo
- [ ] Documentar processo em `docs/ADDING-LOCALE.md`
- [ ] Testes:
  - [ ] en-US usa "." como decimal e "," como milhar
  - [ ] Pt-PT usa "," como decimal e "." como milhar

**Critério de Conclusão**:
- Estrutura extensível confirmada
- en-US implementado e testado
- Documentação clara para futuros locales

---

## 🔗 Mapa de Dependências Completo

```
FASE 0: SETUP
├─ T1.1 (CMake Setup)
│   ↓
├─ T1.2 (Estrutura de Pastas)
│   ├─ T1.3 (Calculator Básica)
│   ├─ T1.4 (UI WPF)
│   └─ T1.5 (Integração)
│
FASE 1: INFRAESTRUTURA
├─ T1.6 (LocaleManager - US10)
│
FASE 2: TESTES
├─ T2.1 (Framework de Testes)
├─ T2.2 (Integrar Locale com Calculator)
│
FASE 3-4: OPERAÇÕES BÁSICAS (US01-US06)
├─ T2.3 (US01 - Adição)
├─ T2.4 (US02 - Subtração)
├─ T2.5 (US03 - Multiplicação)
├─ T2.6 (US04 - Divisão)
├─ T2.7 (US05 - Div Zero)
├─ T2.8 (US06 - Clear)
│
FASE 5: SEPARADORES E PRECISÃO (US07-US09)
├─ T3.1 (US07 - Separador Decimal)
├─ T3.2 (US07B - Separador Milhar)
├─ T3.3 (US08 - Precisão)
├─ T3.4 (US09 - Encadeada)
│
FASE 6: SUPORTE (TESTES E DOCS)
├─ T4.1 (Testes Unitários Completos)
├─ T4.2 (Testes Integração)
├─ T4.3 (Documentação)
│
FASE 7: OPCIONAL (AVANÇADO)
├─ T5.1 (Histórico)
├─ T5.2 (Modo Científico)
└─ T5.3 (US11 - Extensibilidade)
```

---

## 📊 Resumo de Status

| # | Tarefa | Fase | Status | Prioridade | Dependência |
|---|--------|------|--------|-----------|-----------|
| **SETUP** | | | | | |
| T1.1 | CMake Setup | 0 | ❌ | 🔴 | Nenhuma |
| T1.2 | Estrutura Pastas | 0 | ❌ | 🔴 | T1.1 |
| T1.3 | Calculator Básica | 0 | ❌ | 🔴 | T1.2 |
| T1.4 | UI WPF | 0 | ❌ | 🔴 | T1.2 |
| T1.5 | Integração | 0 | ❌ | 🔴 | T1.4 |
| **INFRAESTRUTURA** | | | | | |
| T1.6 | LocaleManager (US10) | 1 | ❌ | 🔴 | T1.2 |
| **TESTES** | | | | | |
| T2.1 | Framework Testes | 1 | ❌ | 🟡 | T1.2 |
| T2.2 | Integrar Locale | 1 | ❌ | 🔴 | T1.6, T1.3 |
| **OPERAÇÕES BÁSICAS** | | | | | |
| T2.3 | US01 - Adição | 2 | ❌ | 🔴 | T2.2 |
| T2.4 | US02 - Subtração | 2 | ❌ | 🔴 | T2.3 |
| T2.5 | US03 - Multiplicação | 2 | ❌ | 🔴 | T2.4 |
| T2.6 | US04 - Divisão | 2 | ❌ | 🔴 | T2.5 |
| T2.7 | US05 - Div/Zero | 2 | ❌ | 🔴 | T2.6 |
| T2.8 | US06 - Clear | 2 | ❌ | 🔴 | T2.7 |
| **SEPARADORES & PRECISÃO** | | | | | |
| T3.1 | US07 - Separador Decimal | 3 | ❌ | 🔴 | T2.8 |
| T3.2 | US07B - Separador Milhar | 3 | ❌ | 🟡 | T3.1 |
| T3.3 | US08 - Precisão | 3 | ❌ | 🟡 | T3.2 |
| T3.4 | US09 - Encadeada | 3 | ❌ | 🟡 | T3.3 |
| **SUPORTE** | | | | | |
| T4.1 | Testes Unitários | 4 | ❌ | 🟡 | T3.4 |
| T4.2 | Testes Integração | 4 | ❌ | 🟡 | T3.4 |
| T4.3 | Documentação | 4 | ❌ | 🟡 | T3.4 |
| **OPCIONAL** | | | | | |
| T5.1 | Histórico | 5 | ❌ | 🟢 | T3.4 |
| T5.2 | Modo Científico | 5 | ❌ | 🟢 | T3.4 |
| T5.3 | US11 - Extensibilidade | 5 | ❌ | 🟢 | T1.6 |

---

## 📈 Estatísticas

- **Total de Tarefas**: 24
- **Fase 0 (Setup)**: 5 tarefas (blocker)
- **Fase 1 (Infraestrutura)**: 2 tarefas (US10)
- **Fase 2-4 (Operações)**: 8 tarefas (US01-US09)
- **Fase 5 (Suporte)**: 3 tarefas (testes + docs)
- **Fase 6-7 (Opcional)**: 6 tarefas (histórico, científico, extensibilidade)

**MVP Blocker**: T1.1 → T1.2 → T1.6 → T2.1 → T2.2 → T2.3 → ... → T3.4 (17 tarefas)  
**Total Estimado**: ~14-15 horas de desenvolvimento

---

**Última Atualização**: 09/09/2026  
**Status**: Pronto para Início de Desenvolvimento  
**Próximo Passo**: Iniciar T1.1 (Setup CMake)
