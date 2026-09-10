# Requisitos — Calculadora Simples

## Visão Geral
Projeto de uma **calculadora simples** desenvolvida em C++ com interface desktop WPF. A aplicação deve realizar operações matemáticas básicas com interface clara e código bem estruturado.

## Requisitos Funcionais

### RF01: Operações Matemáticas Básicas
- [x] Adição de dois números
- [x] Subtração de dois números
- [x] Multiplicação de dois números
- [x] Divisão de dois números (com validação de divisão por zero)
- [x] Cálculo de percentual

### RF02: Interface de Usuário
- [x] Campo de entrada para números
- [x] Botões para operações matemáticas (+, -, *, /)
- [x] Botão de igual (=) para executar o cálculo
- [x] Display para mostrar resultado
- [x] Botão de limpar (C) para resetar a calculadora

### RF03: Validações
- [x] Detectar e prevenir divisão por zero
- [x] Validar entrada de usuário (apenas números)
- [x] Limpar estado anterior ao começar novo cálculo

### RF04: Histórico (Opcional)
- [ ] Manter histórico das últimas 10 operações
- [ ] Permite reutilizar resultado anterior

## Requisitos Não Funcionais

### RNF01: Performance
- Cálculos devem ser executados em menos de 100ms
- Interface responsiva durante operações

### RNF02: Confiabilidade
- Suportar números de até 15 dígitos significativos
- Precisão decimal de até 6 casas decimais

### RNF03: Manutenibilidade
- Código bem estruturado e comentado
- Lógica de cálculo separada da interface
- Estrutura de projeto padronizada em camadas

### RNF04: Compatibilidade
- Windows 7+
- Exige .NET Framework 4.5+ para WPF
- C++11 ou superior

## Stack Tecnológica Definida

| Componente | Tecnologia | Versão |
|-----------|-----------|---------|
| Linguagem | Python | 3.10+ |
| Interface | PyQt6 ou Tkinter | PyQt6 6.5+ / Tkinter (built-in) |
| Framework Web (Opcional) | Flask/FastAPI | FastAPI 0.100+ |
| Testes | pytest | 7.4+ |
| Gerenciador de Pacotes | pip | 23+ |
| Virtualenv | venv | built-in |
| Versionamento | Git | SemVer |
| SO Alvo | Windows/Linux/macOS | Multiplataforma |

## Restrições e Decisões Arquiteturais

### ADR-001: Separação de Camadas
**Decisão**: Manter lógica de cálculo (C++) completamente separada da interface (WPF/C#)
**Motivo**: Facilita testes, reutilização e manutenção
**Impacto**: Necessário criar wrapper de interop C++/C#

### ADR-002: Sem Dependências Externas (Fase 1)
**Decisão**: Inicialmente, usar apenas stdlib do C++ (sem Boost, etc)
**Motivo**: Simplificar setup e build
**Impacto**: Implementar funcionalidades com ferramentas padrão

### ADR-003: Estrutura em Camadas
**Decisão**: Organizar projeto em `src/core/`, `src/ui/`, `tests/`
**Motivo**: Clareza e escalabilidade
**Impacto**: Exige coordenação entre camadas via interop

## Roadmap de Implementação

### Fase 1: MVP (Semana 1)
- [x] Setup inicial do projeto (CMake, estrutura)
- [ ] Implementar classe `Calculator` em C++
- [ ] Operações básicas (+, -, *, /)
- [ ] Interface WPF básica
- [ ] Validação de divisão por zero

### Fase 2: Refinamento (Semana 2)
- [ ] Tratamento de erros melhorado
- [ ] Testes unitários para lógica
- [ ] Polish da interface
- [ ] Documentação de código

### Fase 3: Recursos Avançados (Opcional)
- [ ] Histórico de operações
- [ ] Modo científico (raiz quadrada, potência, etc)
- [ ] Temas de interface (dark mode)

## Ambiente de Desenvolvimento Recomendado

- **IDE**: Visual Studio Code, PyCharm Community, ou similar
- **Python**: 3.10+ (recomendado 3.11 ou 3.12)
- **Gerenciador de Pacotes**: pip ou Poetry
- **Virtualenv**: venv (built-in)
- **Git**: 2.20+
- **Interface**: PyQt6 OU Tkinter (recomendado Tkinter para simplicidade)

## Critérios de Conclusão

Uma funcionalidade é considerada pronta quando:
1. Código implementado e revisado
2. Testes escritos e passando (quando aplicável)
3. Interface integrada e testada
4. Documentação atualizada
5. Commit submetido com mensagem clara

---

**Status**: Em Planejamento  
**Última Atualização**: 09/09/2026  
**Responsável**: Desenvolvedor (Você)
