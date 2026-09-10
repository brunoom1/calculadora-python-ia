# Design Visual — Calculadora Simples

**Versão**: 1.0  
**Data**: 09/09/2026  
**Status**: ✅ Aprovado

## Dimensões Gerais

- **Largura**: 280px
- **Altura**: 520px
- **Padding**: 12px
- **Gap entre elementos**: 8px

## Componentes

### 1. Título
- **Conteúdo**: "Calculadora v1.0"
- **Tamanho**: 14px
- **Peso**: Bold
- **Cor**: #ecf0f1 (cinza claro)
- **Alinhamento**: Centro

### 2. Display
- **Dimensões**: 256px × 70px
- **Background**: #000000 (preto)
- **Borda**: #444444, 1px
- **Padding**: 15px
- **Texto**:
  - **Tamanho**: 32px
  - **Cor**: #00ff00 (verde fluorescente)
  - **Família**: Monoespacial (Roboto Mono ou similar)
  - **Alinhamento**: Direita
  - **Conteúdo padrão**: "0"

### 3. Grade de Botões
- **Layout**: Vertical, 5 linhas
- **Gap**: 6px entre botões
- **Altura de cada linha**: 45px

#### Linha 1: Limpar + Divisão
- **C** (vermelho): 3 colunas, #e74c3c
- **÷** (azul): 1 coluna, #3498db

#### Linha 2: 7-9 + Multiplicação
- **7, 8, 9** (cinza): 1 coluna cada, #34495e
- **×** (azul): 1 coluna, #3498db

#### Linha 3: 4-6 + Subtração
- **4, 5, 6** (cinza): 1 coluna cada, #34495e
- **−** (azul): 1 coluna, #3498db

#### Linha 4: 1-3 + Adição
- **1, 2, 3** (cinza): 1 coluna cada, #34495e
- **+** (azul): 1 coluna, #3498db

#### Linha 5: 0, 0, Ponto + Igual
- **0** (cinza): 1 coluna, #34495e
- **0** (cinza): 1 coluna, #34495e
- **.** (cinza): 1 coluna, #34495e
- **=** (verde): 1 coluna, #27ae60

## Paleta de Cores

| Elemento | Cor | Código |
|----------|-----|--------|
| Fundo Principal | Cinza Escuro | #2c3e50 |
| Display (fundo) | Preto | #000000 |
| Display (texto) | Verde Fluorescente | #00ff00 |
| Botões Numéricos | Cinza Médio | #34495e |
| Botões Operação | Azul | #3498db |
| Botão Limpar (C) | Vermelho | #e74c3c |
| Botão Igual (=) | Verde | #27ae60 |
| Texto Geral | Cinza Claro | #ecf0f1 |
| Borda Padrão | Cinza Escuro | #2c3e50 |

## Tipografia

- **Fonte Padrão**: Segoe UI, Sans-serif
- **Fonte Display**: Monoespacial (Roboto Mono ou Courier New)
- **Tamanho Botões Numéricos**: 16px, Bold
- **Tamanho Botões Especiais**: 10px (para labels maiores como "÷", "×"), 16px (para símbolos simples), Bold

## Estados e Interações

### Estado Inativo (Repouso)
- Botões com sombra suave
- Cor padrão definida

### Estado Hover (Mouse Over)
- Botões com sombra mais escura
- Cor ligeiramente mais intensa (a implementar)

### Estado Ativo/Pressionado
- Botões com sombra mínima
- Elevação reduzida (a implementar)

### Estado de Erro
- Display mostra mensagem em vermelho (#ff6b6b)
- Texto: "Erro: Divisão por zero" (exemplo)

## Notas de Implementação

1. **Responsividade**: Design é fixo em 280x520px para aplicação desktop WPF
2. **Proporções**: Todos os elementos estão em proporção fixa
3. **Espaçamento**: Uso de gap constante garante consistência visual
4. **Acessibilidade**: Contraste suficiente entre texto e fundo
5. **Escalabilidade**: Design pode ser escalado proporcionalmente para diferentes resoluções

## Arquivo de Design

- **Ferramentas**: Pencil Project
- **Arquivo**: `/design/projeto.pen`
- **Último atualizado**: 09/09/2026

---

**Design aprovado e pronto para implementação! ✅**
