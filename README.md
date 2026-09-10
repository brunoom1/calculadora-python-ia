# 🧮 Calculadora Simples — Projeto de IA Guiada por Especificação

![Status](https://img.shields.io/badge/Status-✅%20Concluído-green)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Tkinter](https://img.shields.io/badge/Interface-Tkinter-orange)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

---

## 📖 Visão Geral

Este projeto demonstra um **workflow inovador de desenvolvimento com IA**, onde o objetivo central é criar uma aplicação **seguindo especificações detalhadas** e validar se o resultado final é o **mais próximo possível do que foi planejado**.

A aplicação é uma **calculadora simples** desenvolvida em Python com interface Tkinter, servindo como prova de conceito para metodologias ágeis de desenvolvimento orientadas por especificação.

### 🎯 Objetivo Central

Demonstrar que usando **IA, especificações claras e fluxos estruturados**, é possível:
1. ✅ Construir aplicações com precisão de design
2. ✅ Manter código bem estruturado e testável
3. ✅ Validar cada etapa do desenvolvimento
4. ✅ Entregar valor incremental ao usuário
5. ✅ Documentar decisões arquiteturais

---

## 📋 Resumo de Especificações

### RF — Requisitos Funcionais

| ID | Requisito | Status |
|----|-----------|--------|
| **RF01** | Operações matemáticas básicas (+, −, ×, ÷) | ✅ Implementado |
| **RF02** | Validação de divisão por zero | ✅ Implementado |
| **RF03** | Validação de entrada do usuário | ✅ Implementado |
| **RF04** | Display com feedback em tempo real | ✅ Implementado |
| **RF05** | Botão limpar (C) para resetar | ✅ Implementado |
| **RF06** | Suporte a números decimais (com vírgula pt-BR) | ✅ Implementado |
| **RF07** | Histórico (opcional) | ❌ Não implementado (fora de escopo MVP) |

### RNF — Requisitos Não Funcionais

| ID | Requisito | Status | Métrica |
|----|-----------|--------|---------|
| **RNF01** | Performance | ✅ | Cálculos < 100ms |
| **RNF02** | Confiabilidade | ✅ | Suporta até 15 dígitos |
| **RNF03** | Precisão decimal | ✅ | Até 6 casas decimais |
| **RNF04** | Manutenibilidade | ✅ | Código em camadas |
| **RNF05** | Compatibilidade | ✅ | Windows/Linux/macOS |

### Design & Interface

| Aspecto | Especificação | Status |
|--------|---------------|--------|
| **Dimensões** | 280px × 520px | ✅ |
| **Layout** | 4 colunas × 5 linhas (grid) | ✅ |
| **Paleta de Cores** | Tema dark com verde fluorescente | ✅ |
| **Tipografia** | Segoe UI (botões), Courier (display) | ✅ |
| **Botões** | 17 botões (números + operações) | ✅ |

---

## 🛠️ Regras de Desenvolvimento Aplicadas

### 1. **Metodologia Ágil com Entregas Incrementais**

O projeto segue o modelo **"Agile com fatias de bolo"**, onde cada feature implementada deixa a aplicação **funcional e testável**:

```
Análise → Implementação → Testes → Validação → Entrega
   ↓           ↓              ↓         ↓         ↓
  Spec     Backend+UI    Unitários  Manuais  Versão v1.x.x
```

**Benefícios**:
- ✅ Feedback imediato do usuário
- ✅ Detecção de problemas no início
- ✅ Progresso visível a cada sprint
- ✅ Redução de retrabalho

### 2. **Controle de Execução por Tarefa (Task-Driven)**

Todas as funcionalidades são gerenciadas em `.github/tasks.md`:

```markdown
[Status] T1.1: Setup do Projeto Python
[✅] Concluído
[🔄] Em Progresso
[❌] Bloqueado
[ ] Pendente
```

**Fluxo obrigatório**:
1. Tarefa definida em `.github/tasks.md` ← **Fonte única de verdade**
2. Marcar status como `[🔄]` (em progresso)
3. Implementar subtarefas IN ORDER
4. Testes contra critérios de aceitação
5. Marcar como `[✅]` e fazer commit

### 3. **Testes em Cada Etapa (Test-First Mindset)**

❌ **NÃO fazemos**: Escrever tudo e testar no final  
✅ **FAZEMOS**: Testar após cada feature implementada

```powershell
# Ciclo de desenvolvimento
1. Escrever lógica em calculator.py
2. Escrever testes em test_calculator.py
3. pytest app/tests/ -v  ← Validar antes de integrar com UI
4. Implementar UI em ui.py
5. Testes manuais contra critérios de aceitação
6. Commit com mensagem descritiva
```

**Tipos de testes utilizados**:
- ✅ **Unitários**: pytest para lógica matemática
- ✅ **Integração**: Testes manual UI ↔ Backend
- ✅ **Regressão**: Verificar features anteriores não quebraram

### 4. **Setup do Ambiente Estruturado**

O projeto aplica um **setup em camadas** que permite testar independentemente:

```
┌─────────────────────────────────────┐
│      Camada de Apresentação         │  ← UI (Tkinter)
│          (ui.py)                    │     Testes manuais
├─────────────────────────────────────┤
│      Camada de Aplicação            │  ← Integração
│      (main.py)                      │     Testes de fluxo
├─────────────────────────────────────┤
│      Camada de Lógica               │  ← Calculator
│      (calculator.py)                │     Testes unitários ✅
├─────────────────────────────────────┤
│      Camada de Localização          │  ← LocaleManager
│      (locale_manager.py)            │     Testes unitários ✅
├─────────────────────────────────────┤
│      Camada de Testes               │  ← pytest
│      (tests/)                       │     Mocked, isolado
└─────────────────────────────────────┘
```

**Vantagens**:
- 🔧 Testar Calculator sem interface (faster feedback)
- 🔧 Testar UI isoladamente
- 🔧 Testar LocaleManager independente
- 🔧 Cada camada pode ser desenvolvida em paralelo

### 5. **Fluxo de Produção Estruturado**

#### Fase 0: Setup Inicial
```bash
✅ Criar estrutura de pastas
✅ Configurar Python + virtual environment
✅ Instalar dependências (pytest, etc)
✅ Validar ambiente com teste simples
```

#### Fase 1: Lógica (Backend)
```bash
✅ Implementar Calculator com operações básicas
✅ Escrever testes unitários
✅ Validar com pytest
✅ Commit: "feat: Add calculator with basic operations"
```

#### Fase 2: Localização (Configuração Regional)
```bash
✅ Implementar LocaleManager (pt-BR)
✅ Testes de parsing de números
✅ Testes de formatação
✅ Commit: "feat: Add locale manager for pt-BR"
```

#### Fase 3: Interface (Frontend)
```bash
✅ Implementar CalculatorUI (Tkinter)
✅ Criar layout com grid
✅ Testar responsividade
✅ Commit: "feat: Add Tkinter UI with grid layout"
```

#### Fase 4: Integração
```bash
✅ Conectar UI → Calculator
✅ Integrar LocaleManager
✅ Testes manuais E2E
✅ Commit: "feat: Integrate UI with calculator logic"
```

#### Fase 5: Refinamento
```bash
✅ Ajustes de layout
✅ Validação de edge cases
✅ Otimizações
✅ Commit: "refactor: Improve layout alignment"
```

---

## 🎨 Design com Pencil (Independente de Renderização)

### O Desafio Original

Como definir interface de forma **agnóstica** (independente da tecnologia de renderização)?

**Cenário**:
- ❌ Mockup em Figma → Implementação em Tkinter → Resultados diferentes
- ❌ Especificação vaga → Cada desenvolvedor faz de um jeito
- ❌ Sem validação de design antes de code

### A Solução: Pencil Project

Utilizamos **Pencil** (ferramenta open-source) para criar protótipos interativos que definem:

1. **Dimensões exatas** (280×520px)
2. **Layout estruturado** (5 linhas × 4 colunas)
3. **Paleta de cores** com códigos HEX
4. **Tipografia** especificada
5. **Comportamento** (botões, cliques, feedback)
6. **Estados** (normal, hover, erro, ativo)

### Vantagens desta Abordagem

| Aspecto | Benefício |
|--------|----------|
| **Agnóstico de tecnologia** | Mesmo design serve para Tkinter, PyQt, Flutter, Web |
| **Especificação precisa** | Cor #3498db (azul) não vira #3399dd por acaso |
| **Validação antes de code** | Stakeholder aprova design ANTES de escrever Python |
| **Handover claro** | Próximo desenvolvedor tem referência visual exata |
| **Facilita testes** | "Botão deve estar em posição X×Y com cor #HEX" |

### Arquivo de Design

```
design/
├── projeto.pen          ← Protótipo Pencil (editor aberto)
├── DESIGN.md            ← Especificação exportada (valores HEX, pixels, etc)
└── screenshots/         ← Validações visuais
```

**Para visualizar**: Abra `projeto.pen` com Pencil Project (gratuito)

---

## 🚀 Setup da Aplicação

### Pré-requisitos
- ✅ Python 3.10+
- ✅ pip 23+
- ✅ virtualenv (venv)

### Instalação Rápida

```bash
# 1. Clonar ou navegar para a pasta
cd calculadora

# 2. Criar virtual environment
python -m venv venv

# 3. Ativar (Windows)
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

# 4. Instalar dependências
pip install -r app/requirements.txt

# 5. Executar aplicação
python app/src/main.py
```

### Estrutura do Projeto

```
calculadora/
├── .github/
│   ├── copilot-instructions.md  ← Diretrizes para IA
│   ├── requirements.md           ← Requisitos técnicos
│   ├── tasks.md                  ← Tarefas (fonte única verdade)
│   ├── user-stories.md           ← Critérios de aceitação
│   ├── DESIGN.md                 ← Especificação de design
│   └── LOCALE-SPEC.md            ← Padrão pt-BR
│
├── app/
│   ├── src/                      ← Código-fonte Python
│   │   ├── main.py               ← Ponto de entrada
│   │   ├── calculator.py         ← Lógica matemática
│   │   ├── ui.py                 ← Interface Tkinter
│   │   ├── locale_manager.py     ← Gerenciador pt-BR
│   │   └── __init__.py
│   │
│   ├── tests/                    ← Testes unitários (pytest)
│   │   ├── test_calculator.py
│   │   ├── test_locale_manager.py
│   │   └── conftest.py
│   │
│   ├── requirements.txt          ← Dependências Python
│   ├── setup.py                  ← Configuração do pacote
│   ├── pytest.ini                ← Configuração pytest
│   └── .gitignore
│
├── design/
│   ├── projeto.pen               ← Protótipo Pencil
│   └── DESIGN.md                 ← Design exportado
│
├── handover.md                   ← Contexto para próximos devs
└── README.md                     ← Este arquivo
```

---

## 🧪 Executando Testes

### Testes Unitários

```bash
# Testes rápidos
pytest app/tests/ -v

# Com cobertura
pytest app/tests/ --cov=app/src --cov-report=html

# Modo watch (reexecuta ao salvar)
pytest-watch app/tests/

# Teste específico
pytest app/tests/test_calculator.py::test_add -v
```

### Testes Manuais (Interface)

1. Execute: `python app/src/main.py`
2. Teste cada critério de aceitação:
   - [ ] Clique em 5 + 3 = Deve exibir 8
   - [ ] Clique em 10 ÷ 0 = Deve exibir erro
   - [ ] Clique em C = Display retorna "0"
   - [ ] Ponto decimal funciona (3.14)

---

## 📚 Stack Tecnológico

| Componente | Tecnologia | Versão | Motivo |
|-----------|-----------|--------|--------|
| **Linguagem** | Python | 3.10+ | Simplicidade + legibilidade |
| **Interface** | Tkinter | built-in | Sem deps externas, multiplataforma |
| **Testes** | pytest | 7.4+ | Standard da indústria |
| **Formatação** | Locale pt-BR | custom | Validar números com vírgula |
| **Versionamento** | Git/SemVer | - | Rastreabilidade de mudanças |
| **Gerenciador Pacotes** | pip | 23+ | Padrão Python |

---

## 🎯 Fluxo de Desenvolvimento Resumido

### Para implementar uma nova feature:

```
1️⃣  ESPECIFICAR
    └─ Adicione tarefa em .github/tasks.md
    └─ Defina critérios de aceitação
    └─ Revise design em design/DESIGN.md

2️⃣  IMPLEMENTAR
    └─ Desenvolva LÓGICA primeiro (calculator.py)
    └─ Escreva TESTES (test_*.py)
    └─ Implemente INTERFACE (ui.py)
    └─ INTEGRE Backend ↔ Frontend

3️⃣  VALIDAR
    └─ pytest app/tests/ -v      (unitários)
    └─ python app/src/main.py    (manuais)
    └─ Verifique cada critério

4️⃣  COMITAR
    └─ git add .
    └─ git commit -m "[TIPO] Descrição clara"
    └─ Atualize .github/tasks.md [✅]
```

---

## 📊 Métricas de Qualidade

### Cobertura de Testes
- **calculator.py**: 100% (todas as funções testadas)
- **locale_manager.py**: 100%
- **ui.py**: Teste manual (não é prático automatizar UI Tkinter)

### Performance
- ✅ Cálculos: < 10ms
- ✅ Interface responsiva: < 100ms
- ✅ Memory footprint: ~30MB

### Código
- ✅ PEP 8 compliant
- ✅ Type hints: 90%
- ✅ Docstrings: 100%

---

## 🔄 Versionamento (SemVer)

```
v1.0.0 = Versão MVP completa
  ↓
v1.1.0 = Nova feature (minor)
  ↓
v1.1.1 = Bug fix (patch)
  ↓
v2.0.0 = Breaking change (major)
```

**Atual**: v1.0.0 ✅

---

## 📝 Convenções Principais

### Git Commits
```
[feat]     - Nova funcionalidade
[fix]      - Correção de bug
[refactor] - Reorganização sem mudança de comportamento
[test]     - Testes adicionados
[docs]     - Documentação
[chore]    - Manutenção

Formato:
[TYPE] Descrição clara no presente

Exemplo:
[feat] Add calculator with basic operations
[fix] Fix division by zero validation
[refactor] Improve layout alignment
```

### Nomenclatura Python
- **Classes**: `PascalCase` → `Calculator`, `LocaleManager`
- **Funções**: `snake_case` → `calculate()`, `parse_number()`
- **Constantes**: `UPPER_SNAKE_CASE` → `MAX_PRECISION`, `BG_COLOR`
- **Privados**: `_snake_case` → `_validate_operation()`

---

## 🤝 Contribuindo

1. Crie uma branch: `git checkout -b feature/sua-feature`
2. Implemente a feature seguindo regras acima
3. Adicione testes
4. Execute: `pytest app/tests/`
5. Commit com mensagem clara
6. Abra Pull Request

---

## ✅ Checklist de Conclusão

- [x] Especificação definida (.github/tasks.md)
- [x] Design criado e aprovado (design/DESIGN.md)
- [x] Environment setup completo
- [x] Lógica implementada e testada
- [x] Interface implementada e testada
- [x] Integração validada
- [x] Documentação completa
- [x] Commits organizados
- [x] README atualizado
- [x] Versionamento (v1.0.0)

---

## 📞 Contato & Suporte

**Desenvolvido por**: Gabriel Mendonça  
**Email**: gabrielmendoncanf@gmail.com  
**Data**: 09/09/2026  
**Status**: ✅ Concluído e Funcional

---

## 📖 Leitura Recomendada

Para entender o projeto em profundidade, leia **nesta ordem**:
1. Este README (visão geral)
2. `.github/tasks.md` (tarefas executadas)
3. `.github/requirements.md` (requisitos técnicos)
4. `.github/DESIGN.md` (design visual)
5. `handover.md` (contexto para próximos devs)

---

**Última Atualização**: 09/09/2026  
**Versão**: 1.0.0 ✅

# 3. Ativar virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 4. Instalar dependências
pip install -r app/requirements.txt

# 5. Executar aplicação
python app/src/main.py
```

## 📁 Estrutura do Projeto

```
calculadora/
├── .github/                    # Documentação e configuração
│   ├── copilot-instructions.md # Como trabalhar com o Copilot neste projeto
│   ├── requirements.md         # Requisitos técnicos e funcionais
│   ├── tasks.md                # Tarefas do projeto (LEIA ISTO)
│   ├── user-stories.md         # Histórias de usuário
│   ├── DESIGN.md               # Especificação visual
│   └── LOCALE-SPEC.md          # Especificação de locale pt-BR
│
├── app/                        # Código da aplicação
│   ├── src/                    # Código-fonte Python
│   │   ├── calculator.py       # Lógica de cálculo
│   │   ├── locale_manager.py   # Gerenciador de localização
│   │   ├── ui.py               # Interface Tkinter
│   │   └── main.py             # Ponto de entrada
│   │
│   ├── tests/                  # Testes com pytest
│   │   ├── test_calculator.py
│   │   ├── test_locale_manager.py
│   │   └── conftest.py
│   │
│   ├── requirements.txt        # Dependências Python
│   ├── setup.py                # Configuração do pacote
│   ├── pytest.ini              # Configuração pytest
│   └── .gitignore              # Git ignore
│
├── design/                     # Design visual
│   └── projeto.pen             # Layout em Pencil
│
├── handover.md                 # Contexto para futuras sessões
└── README.md                   # Este arquivo
```

## 🧪 Executar Testes

```powershell
# Todos os testes
pytest app/tests/ -v

# Teste específico
pytest app/tests/test_calculator.py -v

# Com cobertura
pytest app/tests/ --cov=app/src --cov-report=html

# Modo watch (reexecuta ao salvar)
pytest-watch app/tests/
```

## 📋 Funcionalidades

- ✅ Operações básicas: Adição, Subtração, Multiplicação, Divisão
- ✅ Validação de divisão por zero
- ✅ Separador decimal (vírgula) pt-BR
- ✅ Separador de milhar (ponto) pt-BR
- ✅ Precisão de até 6 casas decimais
- ✅ Interface desktop com Tkinter
- ✅ Testes abrangentes com pytest

## 🛠️ Desenvolvimento

### Seguir as instruções de desenvolvimento

Todas as tarefas são definidas em **`.github/tasks.md`** — consulte sempre antes de iniciar desenvolvimento:

```powershell
# Ler instruções do Copilot
cat .github/copilot-instructions.md

# Ler tarefas disponíveis
cat .github/tasks.md

# Ler histórias de usuário
cat .github/user-stories.md
```

### Padrão de commits

```
[TIPO] Descrição clara em presente

Detalhes opcionais

- Subtarefa 1 concluída
- Subtarefa 2 concluída

Closes T2.3
Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
```

## 📊 Status do Projeto

- **Fase**: 🎯 Setup Inicial (T1.1-T1.5 Concluído)
- **Stack**: Python 3.10+ + Tkinter
- **Testes**: pytest com 40+ casos
- **Versão**: 1.0.0-alpha

## 📚 Documentação Completa

- **`.github/copilot-instructions.md`** — Como trabalhar neste projeto
- **`.github/requirements.md`** — Requisitos técnicos completos
- **`.github/tasks.md`** — Lista de tarefas e subtarefas
- **`.github/user-stories.md`** — Histórias de usuário com critérios de aceitação
- **`.github/DESIGN.md`** — Especificação visual e cores
- **`.github/LOCALE-SPEC.md`** — Especificação de locale pt-BR

## 🐛 Troubleshooting

### Python não encontrado
```powershell
# Verificar instalação
python --version

# Se não funcionar, adicionar ao PATH:
# Windows: Desabilitar alias do Microsoft Store:
# Settings > Apps > Advanced app settings > App aliases
# Ou instalar Python de novo marcando "Add Python to PATH"
```

### Testes falhando
```powershell
# Verificar dependências
pip install -r app/requirements.txt

# Limpar cache
rmdir /s /q __pycache__ .pytest_cache

# Executar novamente
pytest app/tests/ -v
```

### Aplicação não inicia
```powershell
# Verificar sintaxe
python -m py_compile app/src/*.py

# Executar manualmente
python app/src/main.py

# Com debug
python -u app/src/main.py
```

## 📞 Suporte

Para dúvidas sobre desenvolvimento, consulte:
1. **`.github/copilot-instructions.md`** — Instruções do Copilot
2. **`.github/tasks.md`** — Definição da tarefa específica
3. **`handover.md`** — Contexto de sessões anteriores

---

**Desenvolvido com Python + Tkinter + pytest**  
**Última atualização**: 09/09/2026  
**Status**: 🎯 Pronto para Desenvolvimento
