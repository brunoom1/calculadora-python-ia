# Instruções Copilot — Calculadora Simples (Python)

**Data**: 09/09/2026 | **Status**: 🎯 Pronto para Desenvolvimento | **Stack**: Python 3.10+ + Tkinter

## 🚀 COMECE AQUI: Leitura Essencial (5 minutos)

Antes de qualquer trabalho, ler **nesta ordem exata**:

1. **Este arquivo** (orientação geral)
2. **`.github/tasks.md`** (tarefas específicas — FONTE ÚNICA DE VERDADE)
3. **`.github/user-stories.md`** (critérios de aceitação detalhados)
4. **`.github/ESTRUTURA-APP.md`** (mapeamento de arquivos dentro de `app/`)
5. **`.github/requirements.md`** (requisitos técnicos e funcionais)

**Documentação de suporte** (consulte conforme necessário):
- `.github/DESIGN.md` — Especificação visual (cores, botões, layout)
- `.github/LOCALE-SPEC.md` — Especificação de localização pt-BR

## ⚠️ Gerenciamento de Tarefas — CRÍTICO

**Todas as tarefas DEVEM ser gerenciadas através de `.github/tasks.md`**

- ✅ **Somente tarefas** listadas em `.github/tasks.md` **serão executadas**
- ✅ Antes de criar qualquer funcionalidade, ela deve estar **definida e aprovada**
- ✅ Cada tarefa inclui: objetivo, subtarefas ordenadas, critério de conclusão específico
- ✅ Status: `[ ]` (pendente) → `[🔄]` (em progresso) → `[✅]` (concluído)
- ❌ **NÃO implemente trabalho fora de `.github/tasks.md`**

**Fluxo padrão para cada tarefa**:
```
1. Localizar tarefa em .github/tasks.md
2. Marcar como [🔄] (em progresso)
3. Implementar subtarefas IN ORDER (ordem importa!)
4. Testar contra critério de conclusão
5. Marcar como [✅] e fazer commit
6. Passar para próxima tarefa
```

---

## 🔧 Metodologia de Desenvolvimento — Agile

### 1️⃣ **Setup e Ambiente (Prioridade Máxima)**

Antes de iniciar qualquer desenvolvimento:

- **Setup completo**: Ambiente deve estar funcional com Python 3.10+
- **Verificação**: Confirmar que:
  - ✅ Python instalado (`python --version` mostra 3.10+)
  - ✅ Virtual environment criado e ativado
  - ✅ Dependências instaladas (`pip install -r app/requirements.txt`)
  - ✅ Testes configurados e descobertos (`pytest app/tests/`)
  - ✅ Aplicação executa (`python app/src/main.py`)
- **Não prosseguir** até que o setup básico esteja 100% operacional
- **Documentar**: Quaisquer issues de setup devem ser registradas para próximas sessões

### 2️⃣ **Entregas Incrementais por Feature**

Seguimos **metodologia Agile**: cada feature é uma "fatia de bolo" completa

- ✅ **Após cada feature implementada**: aplicação fica em estado funcional e testável
- ✅ **Não esperar** para testar tudo no final
- ✅ **Cada feature** adicionada = nova versão funcional da app (v1.0.0 → v1.1.0 → v1.2.0)
- ✅ **Deploy pronto**: ao final de cada feature, versão pode ser entregue para uso

**Fluxo por Feature**:
```
[Definir Feature] 
    ↓
[Implementar Lógica em Python]
    ↓
[Implementar Interface (Tkinter)]
    ↓
[Integração Backend ↔ Frontend]
    ↓
[Testes com pytest conforme Critérios de Aceitação]
    ↓
[Feature Completa ✅] → Nova versão funcional entregue
```

### 3️⃣ **Estrutura de Feature**

Cada feature deve considerar todos os componentes necessários:

| Componente | Descrição | Obrigatório? |
|-----------|-----------|-------------|
| **Lógica (Backend)** | Algoritmos, cálculos, regras de negócio em Python | Sim (sempre) |
| **Frontend** | Interface Tkinter, widgets, eventos | Sim (sempre) |
| **Integração** | Conexão Frontend ↔ Backend (chamadas de função) | Sim (sempre) |
| **Testes** | Testes unitários com pytest | Sim (sempre) |

**Exemplo de Feature Completa - "Operação de Adição"**:
```
✅ Lógica: Implementar Calculator.add(a, b) em calculator.py
✅ Frontend: Botões "1", "2", "3", "+", Display para resultado em ui.py
✅ Integração: Botões clicáveis → Calculator → Display atualizado
✅ Testes: test_calculator.py com casos de aceitação de US01
→ Feature pronta para entrega
```

**Exemplo de Feature Incompleta**:
```
✅ Lógica: Implementar subtract()
✅ Frontend: Botões numéricos adicionados
❌ Integração: Botões não disparam cálculos
→ Feature BLOQUEADA até integração funcionar
```

### 4️⃣ **Critérios de Aceitação**

**Cada feature DEVE ter critérios de aceitação claros** definidos no arquivo `tasks.md`

Critérios de Aceitação devem ser:
- ✅ **Específicos**: "Quando usuário clica em '+'" (não "funciona bem")
- ✅ **Mensuráveis**: "Display mostra resultado" (não "parece correto")
- ✅ **Testáveis**: Podem ser verificados manualmente ou automatizado
- ✅ **Quantificáveis**: "5 operações em < 100ms" (não "rápido")

**Template de Critério de Aceitação**:
```
Dado que: [estado inicial]
Quando: [ação do usuário]
Então: [resultado esperado]

Exemplos:
1. Dado que: Calculadora está aberta e limpa
   Quando: Usuário digita "5 + 3 =" 
   Então: Display mostra "8"

2. Dado que: Calculadora está aberta
   Quando: Usuário tenta "10 / 0"
   Então: Display mostra mensagem de erro "Divisão por zero"
```

### 5️⃣ **Testes por Feature**

Após cada feature, **testes OBRIGATÓRIOS**:

- **Teste Unitário**: pytest em `app/tests/test_*.py`
- **Teste Manual**: Validar contra cada Critério de Aceitação
- **Teste de Regressão**: Verificar se features anteriores continuam funcionando

**Checklist de Testes**:
```
Feature: [Nome da feature]

[ ] Testes unitários passam (pytest app/tests/)
[ ] Todos os critérios de aceitação validados manualmente
[ ] Nenhuma feature anterior foi quebrada
[ ] Código sem erros (python -m py_compile)
[ ] Aplicação executa sem crashes
```

---

## 🏗️ Arquitetura de Alto Nível

O projeto segue uma estrutura **modular em camadas**:

1. **Camada de Apresentação (UI)**: Interface Tkinter em `src/ui.py`
2. **Camada de Lógica**: Núcleo da calculadora em `src/calculator.py`
3. **Camada de Localização**: Gerenciador de locale em `src/locale_manager.py`
4. **Camada de Testes**: Testes unitários em `tests/`

**Fluxo de Dados**:
```
Usuário → Interface Tkinter → Calculator (lógica) → LocaleManager (formatação) → Resultado exibido
```

### Exemplo de Integração:

```python
# ui.py
from calculator import Calculator
from locale_manager import LocaleManager

locale_mgr = LocaleManager.get_instance()
calc = Calculator()

def on_button_click(number):
    display.append(number)

def on_equals_click():
    result = calc.calculate(a, b, operation)
    display_text = locale_mgr.format_number(result)
    display.set_text(display_text)
```

## Estrutura do Projeto

```
calculadora/
├── .github/
│   ├── copilot-instructions.md    ← Você está aqui
│   ├── requirements.md             ← Requisitos detalhados
│   └── tasks.md                    ← TAREFAS (LEIA PRIMEIRO!)
├── app/
│   ├── src/                        ← Código Python
│   │   ├── calculator.py           ← Lógica de cálculo
│   │   ├── locale_manager.py       ← Gerenciador de locale pt-BR
│   │   ├── ui.py                   ← Interface Tkinter
│   │   ├── main.py                 ← Ponto de entrada
│   │   └── __init__.py
│   ├── tests/                      ← Testes com pytest
│   │   ├── test_calculator.py
│   │   ├── test_locale_manager.py
│   │   ├── conftest.py
│   │   └── __init__.py
│   ├── docs/                       ← Documentação interna
│   │   └── ARCHITECTURE.md
│   ├── requirements.txt            ← Dependências Python
│   ├── setup.py                    ← Configuração do pacote
│   ├── pytest.ini                  ← Configuração pytest
│   └── .gitignore
├── handover.md                     ← Contexto para próximas sessões
└── README.md                       ← Instruções de uso
```

## Stack & Tecnologia

- **Linguagem**: Python 3.10+
- **Interface**: Tkinter (built-in) ou PyQt6 6.5+ (recomendado Tkinter para MVP)
- **Testes**: pytest 7.4+
- **Gerenciador de Pacotes**: pip 23+
- **Virtualenv**: venv (built-in)

---

## 🏗️ Comandos de Build, Testes e Execução

### Setup Inicial (Execute uma única vez)

```powershell
# 1. Verificar Python
python --version  # Deve ser 3.10+

# 2. Criar virtual environment
python -m venv venv

# 3. Ativar virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 4. Instalar dependências
pip install -r app/requirements.txt

# 5. Verificar instalação
pip list  # Deve listar pytest
```

### Executar a Aplicação

```powershell
# A partir do diretório raiz com venv ativado
python app/src/main.py
```

### Testes Unitários

```powershell
# Executar todos os testes
pytest app/tests/ -v

# Executar teste específico
pytest app/tests/test_calculator.py -v

# Executar com cobertura
pytest app/tests/ --cov=app/src --cov-report=html

# Executar e parar no primeiro erro
pytest app/tests/ -x

# Modo watch (reexecuta ao salvar arquivos)
pytest-watch app/tests/
```

### Validação Rápida Pós-Implementação

Após implementar qualquer tarefa, executar:

```powershell
# 1. Verificar sintaxe Python
python -m py_compile app/src/*.py

# 2. Executar todos os testes
pytest app/tests/ -v

# 3. Executar aplicação
python app/src/main.py
  # Validar manualmente contra critérios de aceitação
```

### Limpeza

```powershell
# Remover cache Python
rmdir /s /q __pycache__ .pytest_cache

# Remover virtual environment
rmdir /s /q venv

# Recriar do zero (após verificar requirements.txt)
python -m venv venv
venv\Scripts\activate
pip install -r app/requirements.txt
```

---

## Convenções Principais

### Nomenclatura em Python
- **Classes**: `PascalCase` (ex: `Calculator`, `LocaleManager`)
- **Funções/Métodos**: `snake_case` (ex: `calculate()`, `parse_number()`)
- **Variáveis**: `snake_case` (ex: `first_number`, `is_positive`)
- **Constantes**: `UPPER_SNAKE_CASE` (ex: `MAX_PRECISION`, `DEFAULT_LOCALE`)
- **Privados**: `_snake_case` (ex: `_cache`, `_result`)

### Estilo de Código Python
- Seguir PEP 8 (verificável com `pycodestyle` ou `flake8`)
- Linhas até 100 caracteres
- Docstrings em todas as funções/classes públicas
- Type hints onde apropriado (Python 3.10+)
- Imports organizados: stdlib → third-party → local

### Estrutura de Classes Python

```python
# calculator.py
from typing import Optional

class Calculator:
    """Classe responsável por operações matemáticas."""
    
    MAX_PRECISION = 6
    
    def __init__(self):
        """Inicializa a calculadora."""
        self.result: float = 0.0
        self._last_operation: Optional[str] = None
    
    def calculate(self, a: float, b: float, op: str) -> float:
        """
        Calcula o resultado de uma operação.
        
        Args:
            a: Primeiro operando
            b: Segundo operando
            op: Operação (+, -, *, /)
        
        Returns:
            Resultado da operação
        
        Raises:
            ValueError: Se operação é inválida ou divisão por zero
        """
        if op == '+':
            return self.add(a, b)
        # ... etc
    
    def add(self, a: float, b: float) -> float:
        """Soma dois números."""
        return a + b
    
    def _validate_operation(self, op: str) -> bool:
        """Valida se operação é suportada (privada)."""
        return op in ['+', '-', '*', '/']
```

### Padrões de Git
- **Branch principal**: `main`
- **Branch de desenvolvimento**: `develop` (opcional)
- **Padrão de branch**: `feature/nome-da-funcionalidade` ou `fix/nome-do-bug`
- **Formato de commits**: 
  ```
  [TIPO] Descrição clara em presente
  
  Detalhes opcionais (quebra de linhas no corpo)
  
  - Subtarefa 1 concluída
  - Subtarefa 2 concluída
  
  Closes T2.3
  Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
  ```
  - TIPO: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`

### Versionamento
- Use **SemVer** (MAJOR.MINOR.PATCH): ex: `1.0.0`, `1.2.3`
- Atualize em `app/setup.py` e tags Git

---

## Checklist para Novas Features

Ao implementar uma funcionalidade:
- [ ] **Tarefa definida em `.github/tasks.md`** (obrigatório!)
- [ ] **Critérios de Aceitação claros** definidos na tarefa
- [ ] Implemente **Lógica** em `app/src/`
  - [ ] Crie classe/função Python
  - [ ] Escreva docstrings
  - [ ] Teste lógica isoladamente
- [ ] Implemente **Frontend** em `app/src/ui.py`
  - [ ] Crie widgets Tkinter
  - [ ] Crie handlers de eventos
  - [ ] Teste interface
- [ ] Implemente **Integração** Backend ↔ Frontend
  - [ ] Conecte UI aos métodos do Calculator
  - [ ] Teste fluxo completo
- [ ] **Testes**: Valide contra Critérios de Aceitação
  - [ ] Testes unitários em `app/tests/test_*.py`
  - [ ] Teste manual de cada critério
  - [ ] Teste regressão (features anteriores funcionam?)
  - [ ] Código sem erros/warnings
- [ ] Atualize `app/requirements.txt` se novas dependências
- [ ] Faça commit com mensagem descritiva
- [ ] **Marque tarefa como concluída** em `.github/tasks.md`

---

## Notas Importantes
- Manter a lógica de cálculo (`calculator.py`) completamente separada da interface (`ui.py`)
- `LocaleManager` deve ser um singleton para cache eficiente
- Se adicionar dependências externas, atualizar `app/requirements.txt` E `.github/requirements.md`
- Para debug: adicionar `print()` ou usar pdb: `import pdb; pdb.set_trace()`
- **Lembre-se**: Ágil significa entregar valor frequentemente, não código incompleto

---

**Última Atualização**: 09/09/2026  
**Stack**: Python 3.10+ com Tkinter  
**Pronto para desenvolvimento!**
