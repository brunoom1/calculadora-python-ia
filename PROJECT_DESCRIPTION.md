# 🧮 Calculadora Simples — Descrição do Projeto

## Resumo Executivo

**Calculadora desktop em Python com Tkinter**, desenvolvida como **prova de conceito de metodologia ágil orientada por especificação com IA**.

Demonstra como usar especificações detalhadas, design agnóstico (Pencil), testes incrementais e fluxo task-driven para construir aplicações precisas com resultado final **100% alinhado ao planejado**.

---

## 🎯 O Projeto em Uma Frase

> Uma calculadora simples que prova que com **IA, especificações claras e fluxo estruturado**, você constrói exatamente o que foi pensado.

---

## ✨ Destaques Principais

### 🔧 **Desenvolvimento Ágil com Entregas Incrementais**
- Cada feature deixa a app funcional e testável
- Não espera tudo pronto para testar
- Feedback imediato a cada sprint

### 🎨 **Design Agnóstico com Pencil**
- Especificação visual independente de tecnologia
- Mesmos designs servem para Tkinter, PyQt, Flutter, Web
- Stakeholder aprova ANTES de escrever código

### 🧪 **Testes em Cada Etapa**
- Testes unitários: 100% cobertura (calculator, locale)
- Testes manuais: validação contra critérios de aceitação
- Testes de regressão: verificar features anteriores não quebraram

### 📋 **Controle de Execução por Tarefa**
- `.github/tasks.md` = fonte única de verdade
- Cada tarefa tem status explícito: `[ ]` → `[🔄]` → `[✅]`
- Rastreabilidade completa do desenvolvimento

### 🏗️ **Arquitetura em Camadas**
- **Camada Lógica**: Calculator (testes unitários)
- **Camada Locale**: LocaleManager pt-BR (testes unitários)
- **Camada UI**: Tkinter (testes manuais)
- **Camada Integração**: main.py (testes E2E)

---

## 📚 Stack Tecnológico

| Componente | Tecnologia |
|-----------|-----------|
| **Linguagem** | Python 3.10+ |
| **Interface** | Tkinter (built-in) |
| **Testes** | pytest 7.4+ |
| **Localização** | pt-BR (números com vírgula) |
| **Versionamento** | Git + SemVer |
| **Design** | Pencil Project |

---

## ✅ Funcionalidades Implementadas

- ✅ Operações básicas: adição, subtração, multiplicação, divisão
- ✅ Validação de divisão por zero
- ✅ Display com feedback em tempo real
- ✅ Suporte a números decimais (padrão pt-BR: 3,14)
- ✅ Botão limpar (C) para resetar
- ✅ Layout grid responsivo (4×5)
- ✅ Tema dark com interface intuitiva

---

## 📊 Métricas

| Métrica | Resultado |
|---------|-----------|
| **Cobertura Testes** | 100% (lógica) |
| **Performance** | < 10ms para cálculos |
| **Linhas de Código** | ~600 linhas (core) |
| **Documentação** | 100% (docstrings) |
| **Commits** | 9 commits organizados |
| **Status** | ✅ Concluído e Funcional |

---

## 🚀 Como Usar

```bash
# Setup
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r app/requirements.txt

# Executar
python app/src/main.py

# Testes
pytest app/tests/ -v
```

---

## 📖 Documentação

- **README.md** — Guia completo do projeto
- **.github/tasks.md** — Tarefas executadas
- **.github/requirements.md** — Specs técnicas
- **.github/DESIGN.md** — Design visual
- **handover.md** — Contexto para próximos devs

---

## 🎓 Aprendizados Demonstrados

1. **Especificação → Implementação**: Seguir specs resulta em produto preciso
2. **Design Agnóstico**: Mesmo design serve múltiplas tecnologias
3. **Test-First Mindset**: Testes antes/durante, não depois
4. **Task-Driven Development**: Gestão clara de execução
5. **Arquitetura em Camadas**: Código modular e testável
6. **Agile Real**: Entregas incrementais e funcionais
7. **Documentação Ativa**: Docs que refletem código atual

---

## 📞 Autor

**Gabriel Mendonça**  
Email: gabrielmendoncanf@gmail.com  
Data: 09/09/2026  
Status: ✅ Concluído

---

## 🏆 Conclusão

Este projeto prova que **IA + especificação clara + metodologia estruturada = resultado preciso**.

Ideal para:
- 📚 Aprender boas práticas de desenvolvimento
- 🤖 Entender workflow com IA assistida
- 🎯 Ver exemplo real de Agile em pequenos projetos
- 🧪 Estudar testes e arquitetura
- 📐 Compreender design agnóstico

---

**Versão**: 1.0.0 ✅
