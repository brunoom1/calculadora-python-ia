# Referência Rápida de Tarefas

**Data**: 09/09/2026  
**Total**: 24 tarefas  
**MVP Blocker**: 17 tarefas (T1.1 → T3.4)  
**Status**: Pronto para Desenvolvimento

---

## 🚀 Caminho Crítico (MVP - O que não pode pular)

```
T1.1 CMake Setup (COMEÇA AQUI)
  ↓
T1.2 Estrutura Pastas
  ↓
T1.3 Calculator Básica
  ↓
T1.4 UI WPF + T1.5 Integração (paralelos)
  ↓
T1.6 LocaleManager (US10)
  ↓
T2.1 Framework Testes
  ↓
T2.2 Integrar Locale com Calculator
  ↓
T2.3 US01 - Adição
  ↓
T2.4 US02 - Subtração
  ↓
T2.5 US03 - Multiplicação
  ↓
T2.6 US04 - Divisão
  ↓
T2.7 US05 - Div/Zero
  ↓
T2.8 US06 - Clear
  ↓
T3.1 US07 - Decimal (,)
  ↓
T3.2 US07B - Milhar (.)
  ↓
T3.3 US08 - Precisão
  ↓
T3.4 US09 - Encadeada
  ↓
✅ MVP PRONTO
```

---

## 📊 Tarefas por Prioridade

### 🔴 CRÍTICA (Deve fazer)
- T1.1, T1.2, T1.3, T1.4, T1.5 (Setup)
- T1.6 (LocaleManager)
- T2.1, T2.2 (Testes + Integração)
- T2.3, T2.4, T2.5, T2.6, T2.7, T2.8 (Operações)
- T3.1 (Separador Decimal)

### 🟡 ALTA (Muito importante)
- T3.2, T3.3, T3.4 (Separadores + Precisão)
- T4.1, T4.2 (Testes)

### 🟢 MÉDIA (Importante, mas pode adiar)
- T4.3 (Documentação)

### 🟢 BAIXA (Opcional, não bloqueia MVP)
- T5.1 (Histórico)
- T5.2 (Modo Científico)
- T5.3 (US11 - Extensibilidade)

---

## 📈 Tarefas por Estimativa

### < 30 minutos
- T1.2 (Estrutura)
- T2.7 (Validação Div Zero)
- T2.8 (Clear)
- T3.2 (Milhar)
- T4.3 (Documentação)

### 30 min - 1h
- T1.1 (CMake)
- T1.3 (Calculator)
- T2.1 (Framework)
- T2.6 (Divisão)
- T3.1 (Decimal)
- T3.3 (Precisão)
- T4.1 (Testes Unit)

### 1 - 2h
- T1.4 (UI WPF)
- T1.5 (Integração)
- T1.6 (LocaleManager)
- T2.2 (Integrar)
- T2.3 (Adição)
- T2.4 (Subtração)
- T2.5 (Multiplicação)
- T3.4 (Encadeada)

### 2+ horas
- T4.2 (Testes Integração)
- T5.1 (Histórico)
- T5.2 (Científico)
- T5.3 (Extensibilidade)

---

## 🎯 Tarefas por Fase

| Fase | Tarefas | Estimativa | Status |
|------|---------|-----------|--------|
| 0 (Setup) | T1.1-T1.5 | ~5h | ❌ Bloqueado |
| 1 (Locale) | T1.6, T2.1 | ~2h | ❌ Bloqueado |
| 2 (Integração) | T2.2 | ~1.5h | ❌ Bloqueado |
| 3 (Operações) | T2.3-T2.8 | ~5.5h | ❌ Bloqueado |
| 4 (Separadores) | T3.1-T3.4 | ~2h | ❌ Bloqueado |
| 5 (Testes) | T4.1-T4.2 | ~2h | ❌ Bloqueado |
| 6 (Docs) | T4.3 | ~0.5h | ❌ Bloqueado |
| 7 (Opcional) | T5.1-T5.3 | ~3h | ❌ Não Iniciado |

**Total MVP**: ~18-19 horas  
**Com Opcional**: ~21-22 horas

---

## 📋 Tarefas por História de Usuário

### US01 (Adição)
- T2.3: Implementação completa

### US02 (Subtração)
- T2.4: Implementação completa

### US03 (Multiplicação)
- T2.5: Implementação completa

### US04 (Divisão)
- T2.6: Implementação completa

### US05 (Validação Div/Zero)
- T2.7: Implementação completa

### US06 (Clear - Botão C)
- T2.8: Implementação completa

### US07 (Separador Decimal ",")
- T3.1: Implementação completa

### US07B (Separador Milhar ".")
- T3.2: Implementação completa

### US08 (Precisão)
- T3.3: Implementação completa

### US09 (Operação Encadeada)
- T3.4: Implementação completa

### US10 (Locale pt-BR)
- T1.6: LocaleManager (infrastructure)
- T2.2: Integração com Calculator

### US11 (Extensibilidade)
- T5.3: Implementação completa (opcional)

---

## ✅ Checklist Rápido

**Antes de iniciar desenvolvimento:**
- [ ] Ler `.github/copilot-instructions.md` (como trabalhar no projeto)
- [ ] Ler `.github/user-stories.md` (o que precisa ser feito)
- [ ] Ler `.github/tasks.md` (como fazer)
- [ ] Ler `.github/LOCALE-SPEC.md` (especificação de locale)
- [ ] Ler `.github/DESIGN.md` (especificação visual)
- [ ] Confirmar que `design/projeto.pen` está aberto e viável

**Para cada tarefa:**
- [ ] Ler objetivo
- [ ] Ler subtarefas (copiar para seu workflow)
- [ ] Ler critério de conclusão
- [ ] Executar subtarefas em ordem
- [ ] Testar com casos específicos
- [ ] Validar critério de conclusão
- [ ] Marcar como [✅] no tasks.md
- [ ] Passar para próxima tarefa

**Após cada tarefa crítica (T1.x-T3.x):**
- [ ] Executar testes relacionados
- [ ] Validar sem regressão em tarefas anteriores
- [ ] Atualizar `handover.md` com progresso
- [ ] Commit com mensagem clara

---

## 🔗 Matriz de Dependências

```
Sem dependências:
├─ T1.1

Depende de T1.1:
├─ T1.2
└─ T2.1

Depende de T1.2:
├─ T1.3
├─ T1.4
└─ T1.6

Depende de T1.3:
└─ T1.5

Depende de T1.5:
└─ (nenhuma, vai em paralelo com T1.6)

Depende de T1.6:
├─ T2.2
└─ T5.3

Depende de T1.6 + T1.3:
└─ T2.2

Depende de T2.1:
└─ (nenhuma, integração com T2.2)

Depende de T2.2:
└─ T2.3

Depende de T2.3:
└─ T2.4

Depende de T2.4:
└─ T2.5

Depende de T2.5:
└─ T2.6

Depende de T2.6:
├─ T2.7
└─ T2.8

Depende de T2.8:
└─ T3.1

Depende de T3.1:
├─ T3.2
└─ (T5.3, opcional)

Depende de T3.2:
└─ T3.3

Depende de T3.3:
└─ T3.4

Depende de T3.4:
├─ T4.1
├─ T4.2
├─ T4.3
├─ T5.1
└─ T5.2
```

---

## 🎓 Referência Rápida de Cada Tarefa

### T1.1 - CMake Setup
```bash
# Criar CMakeLists.txt na raiz
# Configurar project("Calculadora")
# Testar: cmake .. && cmake --build .
```

### T1.2 - Estrutura
```
src/
├─ core/    (lógica C++)
├─ ui/      (WPF)
└─ wrapper/ (interop)

tests/
├─ core/    (testes C++)
└─ ui/      (testes UI)
```

### T1.3 - Calculator
```cpp
class Calculator {
  double calculate(double a, double b, char op);
  double add(double a, double b);
  double subtract(double a, double b);
  // ... etc
  void reset();
};
```

### T1.4 - WPF
```xaml
<Display>...</Display>
<NumberButtons 0-9>...</NumberButtons>
<OperationButtons +, -, *, />...</OperationButtons>
<EqualButton>=</EqualButton>
<ClearButton>C</ClearButton>
```

### T1.5 - Integração
Conectar cliques de botões WPF a Calculator C++

### T1.6 - LocaleManager
```cpp
class LocaleManager {
  static LocaleManager& getInstance();
  double parseNumber(string input);  // "3,5" → 3.5
  string formatNumber(double value); // 1234.56 → "1.234,56"
};
```

### T2.1 - Testes
Escolher framework (Google Test, Catch2)

### T2.2 - Integração
Calculator usa LocaleManager para entrada/saída

### T2.3-T2.8 - Operações
Implementar cada operação: add, sub, mul, div, div/0, clear

### T3.1-T3.4 - Separadores
Suporte a "," decimal e "." milhar, precisão 6 casas, encadeamento

### T4.1-T4.3 - Suporte
Testes unitários, integração, documentação

### T5.1-T5.3 - Opcional
Histórico, modo científico, extensibilidade de locales

---

**Última Atualização**: 09/09/2026  
**Versão**: 1.0  
**Status**: Pronto para Desenvolvimento
