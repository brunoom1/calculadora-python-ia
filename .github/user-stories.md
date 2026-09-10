# Histórias de Usuários — Calculadora Simples

**Escopo MVP**: Operações básicas (+, -, *, /) com suporte a números decimais  
**Data de Criação**: 09/09/2026

---

## US01: Realizar Adição de Dois Números

**Como um** usuário da calculadora  
**Eu quero** somar dois números  
**Para que** eu possa obter o resultado de uma adição  

### Critérios de Aceitação

```gherkin
Dado que a calculadora está aberta e limpa
E o display mostra "0"
Quando eu digito "5"
E clico em "+"
E digito "3"
E clico em "="
Então o display mostra "8"
E o estado da calculadora está pronto para nova operação
```

**Testes Específicos**:
```
1. 5 + 3 = 8
2. 0 + 0 = 0
3. -5 + 10 = 5
4. 12.5 + 7.5 = 20
5. 100 + 0.01 = 100.01
```

**Componentes a Entregar**:
- ✅ **Lógica**: Método `Calculator::add(double a, double b)` retorna soma correta
- ✅ **Frontend**: Botões numéricos (0-9), botão "+", display atualizado
- ✅ **Integração**: Cliques em botões disparam cálculo no backend
- ❌ **API**: N/A
- ❌ **SDK**: N/A

**Prioridade**: 🔴 **Crítica** (primeira operação)  
**Estimativa**: 2-3 horas (setup + lógica + UI + testes)  
**Dependências**: T1.1, T1.2, T1.3, T1.4, T1.5 (Setup completo)

---

## US02: Realizar Subtração de Dois Números

**Como um** usuário da calculadora  
**Eu quero** subtrair dois números  
**Para que** eu possa obter o resultado de uma subtração  

### Critérios de Aceitação

```gherkin
Dado que a calculadora está aberta e limpa
E o display mostra "0"
Quando eu digito "10"
E clico em "-"
E digito "3"
E clico em "="
Então o display mostra "7"
E o estado da calculadora está pronto para nova operação
```

**Testes Específicos**:
```
1. 10 - 3 = 7
2. 0 - 5 = -5
3. -5 - (-3) = -2
4. 10.5 - 2.5 = 8
5. 0.1 - 0.2 = -0.1
```

**Componentes a Entregar**:
- ✅ **Lógica**: Método `Calculator::subtract(double a, double b)` retorna subtração correta
- ✅ **Frontend**: Botão "-" adicionado (reutiliza interface anterior)
- ✅ **Integração**: Cliques em "-" disparam subtração no backend
- ❌ **API**: N/A
- ❌ **SDK**: N/A

**Prioridade**: 🔴 **Crítica** (segunda operação)  
**Estimativa**: 1 hora (reutiliza framework de US01)  
**Dependências**: US01

---

## US03: Realizar Multiplicação de Dois Números

**Como um** usuário da calculadora  
**Eu quero** multiplicar dois números  
**Para que** eu possa obter o resultado de uma multiplicação  

### Critérios de Aceitação

```gherkin
Dado que a calculadora está aberta e limpa
E o display mostra "0"
Quando eu digito "6"
E clico em "*"
E digito "7"
E clico em "="
Então o display mostra "42"
E o estado da calculadora está pronto para nova operação
```

**Testes Específicos**:
```
1. 6 * 7 = 42
2. 0 * 100 = 0
3. -5 * 3 = -15
4. 2.5 * 4 = 10
5. 0.1 * 0.1 = 0.01
```

**Componentes a Entregar**:
- ✅ **Lógica**: Método `Calculator::multiply(double a, double b)` retorna multiplicação correta
- ✅ **Frontend**: Botão "*" adicionado
- ✅ **Integração**: Cliques em "*" disparam multiplicação no backend
- ❌ **API**: N/A
- ❌ **SDK**: N/A

**Prioridade**: 🔴 **Crítica** (terceira operação)  
**Estimativa**: 1 hora  
**Dependências**: US02

---

## US04: Realizar Divisão de Dois Números

**Como um** usuário da calculadora  
**Eu quero** dividir dois números  
**Para que** eu possa obter o resultado de uma divisão  

### Critérios de Aceitação

```gherkin
Dado que a calculadora está aberta e limpa
E o display mostra "0"
Quando eu digito "20"
E clico em "/"
E digito "4"
E clico em "="
Então o display mostra "5"
E o estado da calculadora está pronto para nova operação
```

**Testes Específicos**:
```
1. 20 / 4 = 5
2. 10 / 3 = 3.33333... (precisão até 6 casas)
3. -20 / 4 = -5
4. 7.5 / 2.5 = 3
5. 1 / 3 = 0.333333
```

**Componentes a Entregar**:
- ✅ **Lógica**: Método `Calculator::divide(double a, double b)` retorna divisão correta
- ✅ **Frontend**: Botão "/" adicionado
- ✅ **Integração**: Cliques em "/" disparam divisão no backend
- ❌ **API**: N/A
- ❌ **SDK**: N/A

**Prioridade**: 🔴 **Crítica** (quarta operação)  
**Estimativa**: 1 hora  
**Dependências**: US03

---

## US05: Validar Divisão por Zero

**Como um** usuário da calculadora  
**Eu quero** receber um aviso quando tento dividir por zero  
**Para que** não tenha resultados indefinidos ou crashes  

### Critérios de Aceitação

```gherkin
Dado que a calculadora está aberta
Quando eu digito "10"
E clico em "/"
E digito "0"
E clico em "="
Então o display mostra mensagem de erro "Erro: Divisão por zero"
E a calculadora volta ao estado inicial (pronta para novo cálculo)
```

**Testes Específicos**:
```
1. 5 / 0 → "Erro: Divisão por zero"
2. 0 / 0 → "Erro: Divisão por zero"
3. -10 / 0 → "Erro: Divisão por zero"
4. 0.5 / 0 → "Erro: Divisão por zero"
```

**Componentes a Entregar**:
- ✅ **Lógica**: `Calculator::divide()` valida divisor ≠ 0, retorna erro ou flag
- ✅ **Frontend**: Display pode exibir mensagem de erro
- ✅ **Integração**: Erro é capturado e exibido na UI
- ❌ **API**: N/A
- ❌ **SDK**: N/A

**Prioridade**: 🔴 **Crítica** (validação obrigatória)  
**Estimativa**: 30 minutos  
**Dependências**: US04

---

## US06: Limpar Calculadora (Botão C)

**Como um** usuário da calculadora  
**Eu quero** poder limpar o display e resetar o estado  
**Para que** eu possa começar um novo cálculo do zero  

### Critérios de Aceitação

```gherkin
Dado que a calculadora tem um número ou resultado no display
Quando eu clico no botão "C"
Então o display volta a mostrar "0"
E o estado interno da calculadora é resetado
E estou pronto para digitar uma nova operação
```

**Testes Específicos**:
```
1. Após "5 + 3 =" → clico "C" → display mostra "0"
2. Após "10 / 0" (erro) → clico "C" → display mostra "0"
3. Após um número isolado (ex: "123") → clico "C" → display mostra "0"
4. Múltiplos cliques em "C" consecutivos → apenas "0" no display
```

**Componentes a Entregar**:
- ✅ **Lógica**: Método `Calculator::reset()` limpa estado interno
- ✅ **Frontend**: Botão "C" disponível
- ✅ **Integração**: Clique em "C" chama `reset()` e atualiza display
- ❌ **API**: N/A
- ❌ **SDK**: N/A

**Prioridade**: 🔴 **Crítica** (funcionalidade essencial)  
**Estimativa**: 30 minutos  
**Dependências**: US01

---

## US07: Suporte a Separador Decimal (Vírgula para PT-BR)

**Como um** usuário português falante  
**Eu quero** usar a vírgula "," como separador decimal  
**Para que** a calculadora siga a convenção de números decimais do Brasil  

### Critérios de Aceitação

```gherkin
Dado que a calculadora está configurada para português (Brasil)
E o display mostra "0"
Quando eu digito "3,5"
E clico em "+"
E digito "2,3"
E clico em "="
Então o display mostra "5,8"

Dado que estou digitando um número
Quando eu já usei uma vírgula como separador decimal
E clico em "," novamente
Então a calculadora ignora o segundo clique (apenas uma vírgula por número)
```

**Testes Específicos**:
```
1. 3,5 + 2,3 = 5,8
2. 10,1 - 5,05 = 5,05
3. 2,5 * 2,4 = 6
4. 7,5 / 2,5 = 3
5. 0,1 + 0,2 = 0,3
6. Display permite apenas uma vírgula como separador decimal por número
7. Múltiplas vírgulas são ignoradas: "3,5,1" → registra como "3,51"
```

**Componentes a Entregar**:
- ✅ **Lógica**: Calculadora aceita "," como separador decimal internamente converte para `double`
- ✅ **Frontend**: Botão "," adicionado no layout
- ✅ **Integração**: Entrada de "," funciona corretamente e valida duplicatas
- ✅ **Configuração**: Sistema de locale reconhece pt-BR como padrão
- ❌ **API**: N/A
- ❌ **SDK**: N/A

**Prioridade**: 🔴 **Crítica** (requisito do MVP)  
**Estimativa**: 1 hora  
**Dependências**: US01

---

## US07B: Suporte a Separador de Milhar (Ponto para PT-BR)

**Como um** usuário português falante  
**Eu quero** que números grandes tenham separador de milhar com ponto  
**Para que** seja mais fácil ler números com muitos dígitos  

### Critérios de Aceitação

```gherkin
Dado que a calculadora está configurada para português (Brasil)
E eu realizo uma operação que resulta em número ≥ 1.000
Quando o resultado é exibido no display
Então os algarismos são separados por ponto a cada 3 dígitos
E o separador decimal continua sendo vírgula

Exemplos:
  - 1000 é exibido como "1.000"
  - 1000000 é exibido como "1.000.000"
  - 1234,56 é exibido como "1.234,56"
```

**Testes Específicos**:
```
1. 500 * 2 = 1000 → exibe "1.000"
2. 100 * 100 = 10000 → exibe "10.000"
3. 1000000 * 1 = 1000000 → exibe "1.000.000"
4. 1234,56 + 0 = 1234,56 → exibe "1.234,56"
5. Display permite entrada de números grandes sem formatter automático na entrada
6. Formatação ocorre apenas na exibição do resultado
```

**Componentes a Entregar**:
- ✅ **Lógica**: Função de formatação de display respeitando locale pt-BR
- ✅ **Frontend**: Display respeita formatação da lógica
- ✅ **Integração**: Resultado formatado com separador de milhar é exibido corretamente
- ✅ **Configuração**: Formatação usa perfil de locale do sistema
- ❌ **API**: N/A
- ❌ **SDK**: N/A

**Prioridade**: 🟡 **Alta** (melhora legibilidade)  
**Estimativa**: 45 minutos  
**Dependências**: US07

---

## US08: Exibir Resultado com Precisão Adequada

**Como um** usuário da calculadora  
**Eu quero** ver resultados com número apropriado de casas decimais  
**Para que** os resultados sejam legíveis e não mostrem ruído numérico  

### Critérios de Aceitação

```gherkin
Dado que a calculadora mostra um resultado decimal
Quando o resultado tem mais de 6 casas decimais
Então o display mostra apenas 6 casas decimais (ex: 0,333333)

Dado que o resultado é um número inteiro
Quando eu faço uma divisão que resulta em inteiro
Então o display não mostra ",00" (ex: "5" em vez de "5,00")
```

**Testes Específicos**:
```
1. 1 / 3 = 0,333333 (não 0,33333333333...)
2. 10 / 2 = 5 (não 5,00)
3. 7,5 / 2,5 = 3 (não 3,00)
4. 2 / 3 = 0,666667 (arredonda na 6ª casa)
5. 0,1 + 0,2 = 0,3 (não 0,30000000000001)
```

**Componentes a Entregar**:
- ✅ **Lógica**: Formatação de output em `Calculator` ou wrapper
- ✅ **Frontend**: Display respeita formatação da lógica
- ✅ **Integração**: Resultado formatado é exibido corretamente
- ✅ **Configuração**: Formatação respeita perfil de locale (separador decimal)
- ❌ **API**: N/A
- ❌ **SDK**: N/A

**Prioridade**: 🟡 **Alta** (qualidade visual)  
**Estimativa**: 30 minutos  
**Dependências**: US01, US02, US03, US04, US07

---

## US09: Realizar Operação Encadeada

**Como um** usuário da calculadora  
**Eu quero** poder continuar operando sem clicar em "C"  
**Para que** eu possa fazer cálculos sequenciais (ex: 5 + 3 - 2 * 4)  

### Critérios de Aceitação

```gherkin
Dado que a calculadora exibe resultado de uma operação
Quando eu digito um novo número
Então o display limpa e começa nova entrada
E posso continuar com outra operação

Exemplo: 5 + 3 = 8, depois clico "+", digito "2", clico "=" → 10
```

**Testes Específicos**:
```
1. 5 + 3 = 8, clico "+", digito "2", clico "=" → 10
2. 10 - 2 = 8, clico "*", digito "2", clico "=" → 16
3. Operação incompleta + número novo = substitui operação anterior
```

**Componentes a Entregar**:
- ✅ **Lógica**: `Calculator` gerencia estado de operação vs. entrada nova
- ✅ **Frontend**: Display e lógica de botões refletem estado
- ✅ **Integração**: Transição de estados funciona corretamente
- ❌ **API**: N/A
- ❌ **SDK**: N/A

**Prioridade**: 🟡 **Alta** (UX)  
**Estimativa**: 1 hora  
**Dependências**: US01, US02, US03, US04

---

## US10: Configurar Locale Padrão (Português Brasil)

**Como um** usuário da calculadora  
**Eu quero** que a aplicação use automaticamente as convenções de número do Brasil  
**Para que** não precise fazer configurações manuais  

### Critérios de Aceitação

```gherkin
Dado que a calculadora é iniciada
Quando nenhuma configuração de idioma é explicitamente definida
Então o sistema assume automaticamente locale "pt-BR"

Dado que a calculadora está usando locale "pt-BR"
E eu entro com números
Então:
  - Separador decimal aceito é "," (vírgula)
  - Separador de milhar exibido é "." (ponto)
  - Exemplo: entrada "1234,56" é exibida como "1.234,56"
```

**Testes Específicos**:
```
1. Inicializar aplicação → locale padrão é "pt-BR"
2. Arquivo de config/sistema retorna "pt-BR" como padrão
3. Entrada com "," funciona como separador decimal
4. Saída com "." funciona como separador de milhar
5. Sistema está preparado para futuros locales (en-US, pt-PT, etc.)
```

**Componentes a Entregar**:
- ✅ **Lógica**: Classe `LocaleConfig` ou similar com suporte a pt-BR
- ✅ **Lógica**: Função de parsing de entrada que respeita locale
- ✅ **Lógica**: Função de formatação de saída que respeita locale
- ✅ **Configuração**: Sistema inicializa com pt-BR como padrão
- ✅ **Integração**: Calculator usa locale para entrada/saída
- ❌ **UI**: Menu de seleção de idioma (versão futura)
- ❌ **API**: N/A
- ❌ **SDK**: N/A

**Prioridade**: 🔴 **Crítica** (infraestrutura de locale)  
**Estimativa**: 1.5 horas  
**Dependências**: T1.1, T1.2 (Setup básico), antes de US07

---

## US11: Extensibilidade de Novos Locales (Futuro)

**Como um** desenvolvedor  
**Eu quero** que o sistema de locale seja extensível  
**Para que** seja fácil adicionar suporte a novos idiomas no futuro  

### Critérios de Aceitação

```gherkin
Dado que existe uma classe LocaleConfig ou perfil de configuração
Quando um novo locale (ex: en-US) precisa ser adicionado
Então devo poder:
  - Definir separador decimal (ponto vs vírgula)
  - Definir separador de milhar (vírgula vs ponto)
  - Definir formato de exibição de números
  - Sem modificar código de business logic
```

**Testes Específicos**:
```
1. LocaleConfig permite registrar novo locale sem alterar Calculator
2. En-US usa "." como decimal e "," como milhar
3. Pt-PT usa "," como decimal e "." como milhar (como pt-BR)
4. Sistema seleciona locale correto baseado em configuração
```

**Componentes a Entregar**:
- ✅ **Lógica**: Interface/padrão para LocaleProfile
- ✅ **Lógica**: Factory ou registry para gerenciar locales
- ✅ **Documentação**: Instruções para adicionar novo locale
- ❌ **UI**: N/A para MVP
- ❌ **API**: N/A
- ❌ **SDK**: N/A

**Prioridade**: 🟢 **Baixa** (planejamento para futuro)  
**Estimativa**: 1 hora (opcional para MVP)  
**Dependências**: US10 (Não bloqueia MVP se não implementado)

---

## Mapa de Dependências

```
Setup Completo (T1.1-T1.5)
    ↓
US10 (Configurar Locale pt-BR)
    ↓
US01 (Adição)
    ↓
US02 (Subtração)
    ↓
US03 (Multiplicação)
    ↓
US04 (Divisão)
    ├→ US05 (Validação Div Zero) ← ocorre em paralelo com US04
    └→ US06 (Limpar - Botão C) ← pode começar em paralelo com US01
        ↓
US07 (Separador Decimal ",")
    ↓
US07B (Separador de Milhar ".")
    ↓
US08 (Precisão Display)
    ↓
US09 (Operação Encadeada)
    ↓
US11 (Extensibilidade de Locales) ← opcional para MVP
```

---

## Resumo para Desenvolvimento

| # | Título | Prioridade | Estimativa | Dependência |
|---|--------|-----------|-----------|-----------|
| US10 | Configurar Locale pt-BR | 🔴 Crítica | 1.5h | Setup Completo |
| US01 | Adição | 🔴 Crítica | 2-3h | US10 |
| US02 | Subtração | 🔴 Crítica | 1h | US01 |
| US03 | Multiplicação | 🔴 Crítica | 1h | US02 |
| US04 | Divisão | 🔴 Crítica | 1h | US03 |
| US05 | Validar Div/0 | 🔴 Crítica | 30m | US04 |
| US06 | Limpar (C) | 🔴 Crítica | 30m | US01 |
| US07 | Separador Decimal (,) | 🔴 Crítica | 1h | US10 |
| US07B | Separador Milhar (.) | 🟡 Alta | 45m | US07 |
| US08 | Precisão | 🟡 Alta | 30m | US01-04 |
| US09 | Encadeada | 🟡 Alta | 1h | US01-05 |
| US11 | Extensibilidade Locales | 🟢 Baixa | 1h | US10 (opcional) |

**Total Estimado**: ~12-13 horas (MVP completo com suporte a pt-BR)

---

**Versão**: 1.1  
**Última Atualização**: 09/09/2026  
**Status**: Pronto para Revisão
