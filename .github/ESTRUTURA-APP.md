# Estrutura do Projeto - Calculadora v1.0 (Python)

**Organização**: Código da aplicação em pasta `app/` separada da documentação  
**Data**: 09/09/2026  
**Stack**: Python 3.10+ com Tkinter/PyQt6  
**Status**: ✅ Pronto para Desenvolvimento

---

## 📁 Árvore Completa

```
calculadora/                          (raiz do repositório)
│
├─ .github/                           (documentação e configuração)
│  ├─ copilot-instructions.md         (como desenvolver no projeto)
│  ├─ requirements.md                 (requisitos técnicos)
│  ├─ user-stories.md                 (11 histórias de usuário)
│  ├─ tasks.md                        (24 tarefas detalhadas)
│  ├─ LOCALE-SPEC.md                  (especificação de locale)
│  ├─ DESIGN.md                       (design visual)
│  ├─ TASKS-QUICK-REF.md              (referência rápida)
│  ├─ PROJECT-SUMMARY.md              (resumo executivo)
│  └─ ESTRUTURA-APP.md                (este arquivo)
│
├─ design/                            (design visual)
│  └─ projeto.pen                     (arquivo Pencil com layout)
│
├─ app/                               🆕 RAIZ DO CÓDIGO DA APLICAÇÃO
│  │
│  ├─ src/                            (código-fonte Python)
│  │  ├─ calculator.py                (T1.3 - lógica de cálculo)
│  │  ├─ locale_manager.py            (T1.6 - gerenciador de locale pt-BR)
│  │  ├─ ui.py                        (T1.4 - interface Tkinter/PyQt6)
│  │  ├─ main.py                      (T1.5 - ponto de entrada)
│  │  └─ __init__.py
│  │
│  ├─ tests/                          (testes com pytest)
│  │  ├─ test_calculator.py           (T2.1, T4.1 - testes de lógica)
│  │  ├─ test_locale_manager.py       (T1.6, T4.1 - testes de locale)
│  │  ├─ conftest.py                  (configuração pytest)
│  │  └─ __init__.py
│  │
│  ├─ docs/                           (documentação interna)
│  │  └─ ARCHITECTURE.md              (T4.3 - arquitetura)
│  │
│  ├─ requirements.txt                (dependências Python)
│  ├─ setup.py                        (configuração do pacote)
│  ├─ pytest.ini                      (configuração pytest)
│  └─ .gitignore                      (ignora arquivos Python)
│
├─ handover.md                        (contexto para futuras sessões)
├─ README.md                          (instruções de uso da calculadora)
└─ .gitignore                         (git ignore da raiz)
```

---

## 🎯 Mapeamento: Tarefas → Arquivos (PYTHON)

### Fase 0: Setup (T1.1-T1.5)

| Tarefa | Arquivos | Pasta |
|--------|----------|-------|
| T1.1 | requirements.txt, setup.py, pytest.ini | `app/` |
| T1.2 | Estrutura de pastas | `app/src/`, `app/tests/`, etc |
| T1.3 | calculator.py | `app/src/` |
| T1.4 | ui.py | `app/src/` |
| T1.5 | main.py | `app/src/` |

### Fase 1: Infraestrutura (T1.6, T2.1)

| Tarefa | Arquivos | Pasta |
|--------|----------|-------|
| T1.6 | locale_manager.py, test_locale_manager.py | `app/src/`, `app/tests/` |
| T2.1 | pytest.ini (configuração) | `app/` |

### Fase 2-5: Desenvolvimento e Testes

| Tarefa | Arquivos | Pasta |
|--------|----------|-------|
| T2.2-T3.4 | calculator.py, ui.py, locale_manager.py | `app/src/` |
| T2.1, T4.1 | test_*.py | `app/tests/` |
| T4.3 | ARCHITECTURE.md | `app/docs/` |

---

## 📂 Convenções de Nomes (PYTHON)

### Pastas
- `src/` → código-fonte Python
- `tests/` → testes com pytest
- `docs/` → documentação
- `__init__.py` → marca pastas como módulos Python

### Arquivos Python
- `*.py` → código-fonte
- `test_*.py` → arquivos de teste (pytest descobre automaticamente)
- `*_test.py` → alternativa para testes
- `conftest.py` → configuração compartilhada de pytest

### Nomes de Módulos/Funções/Classes
- **Classes**: `PascalCase` (ex: `Calculator`, `LocaleManager`)
- **Funções/Métodos**: `snake_case` (ex: `calculate()`, `parse_number()`)
- **Constantes**: `UPPER_SNAKE_CASE` (ex: `MAX_PRECISION`, `DEFAULT_LOCALE`)
- **Variáveis privadas**: `_snake_case` (ex: `_cache`, `_result`)

---

## 🔄 Fluxo de Desenvolvimento Típico

```
Ler tarefa em .github/tasks.md
    ↓
Localizar arquivo em app/ conforme indicado
    ↓
Implementar subtarefas em ordem
    ↓
Rodar testes (pytest app/tests/)
    ↓
Executar aplicação (python app/src/main.py)
    ↓
Validar critério de conclusão
    ↓
Marcar [✅] em .github/tasks.md
    ↓
Commit com referência
    ↓
Passar para próxima tarefa
```

---

## ✅ Checklist de Estrutura

Ao iniciar desenvolvimento, validar:

- [ ] Pasta `app/` existe
- [ ] Subpastas criadas:
  - [ ] `app/src/`
  - [ ] `app/tests/`
  - [ ] `app/docs/`
- [ ] Arquivos de configuração Python:
  - [ ] `app/requirements.txt` (será criado em T1.1)
  - [ ] `app/setup.py` (será criado em T1.1)
  - [ ] `app/pytest.ini` (será criado em T1.1)
- [ ] `.gitignore` configurado para Python
- [ ] Documentação em `.github/` está completa
- [ ] Design em `design/projeto.pen` aprovado

---

## 🚀 Próximas Etapas

1. **T1.1: Setup Python**
   - Criar `app/requirements.txt`
   - Criar `app/setup.py`
   - Criar `app/pytest.ini`
   - Testar: `pip install -r requirements.txt`

2. **T1.2: Confirmar Estrutura**
   - Validar pastas em `app/`
   - Criar `__init__.py` em `src/` e `tests/`

3. **T1.3+: Desenvolvimento**
   - Seguir tarefas em ordem
   - Cada arquivo referenciado com caminho completo
   - Todos em `app/`

---

**Versão**: 1.0 (Python)
**Status**: ✅ Pronto para Desenvolvimento  
**Data**: 09/09/2026

🎯 Stack Python escolhida, dependências definidas, caminho para desenvolvimento claro!
