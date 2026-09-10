# Especificação de Configuração de Locale

**Status**: Especificação para Desenvolvimento  
**Data**: 09/09/2026  
**Versão**: 1.0

---

## Objetivo

Definir uma arquitetura extensível para suporte a múltiplos idiomas/locales na calculadora, começando com **português Brasil (pt-BR)** como padrão, permitindo futuras expansões.

---

## Estrutura de Locale

Cada locale deve definir:

### 1. **Separador Decimal**
- Caractere usado para separar a parte inteira da parte fracionária
- **pt-BR**: `,` (vírgula)
- **en-US**: `.` (ponto)

### 2. **Separador de Milhar**
- Caractere usado para agrupar dígitos em intervalos de 3
- **pt-BR**: `.` (ponto)
- **en-US**: `,` (vírgula)

### 3. **Formato de Exibição**
- Padrão de como números são exibidos no display
- Exemplo: `1.234,56` (pt-BR) vs `1,234.56` (en-US)

---

## Perfis de Locale Suportados (MVP + Futuro)

### pt-BR (Português Brasil) — MVP
```
Locale ID:          pt-BR
Decimal Separator:  ,
Thousands Sep:      .
Example:            1.234,56
Max Decimals:       6 casas
Description:        Padrão brasileiro
```

### en-US (English - USA) — Futuro
```
Locale ID:          en-US
Decimal Separator:  .
Thousands Sep:      ,
Example:            1,234.56
Max Decimals:       6 casas
Description:        Padrão americano
```

### pt-PT (Português Portugal) — Futuro
```
Locale ID:          pt-PT
Decimal Separator:  ,
Thousands Sep:      .
Example:            1.234,56
Max Decimals:       6 casas
Description:        Padrão português
```

---

## Arquitetura de Implementação

### Classe: `LocaleProfile`

```cpp
// src/core/locale.h
class LocaleProfile {
public:
    // Getters
    char getDecimalSeparator() const;
    char getThousandsSeparator() const;
    int getMaxDecimals() const;
    std::string getLocaleId() const;
    
    // Formatação
    std::string formatNumber(double value) const;
    bool isValidDecimalSeparator(char c) const;
    
private:
    std::string localeId;
    char decimalSeparator;
    char thousandsSeparator;
    int maxDecimals;
};
```

### Classe: `LocaleManager` (Singleton)

```cpp
// src/core/locale_manager.h
class LocaleManager {
public:
    static LocaleManager& getInstance();
    
    // Gerenciar locales
    void registerLocale(const LocaleProfile& profile);
    LocaleProfile& getLocale(const std::string& localeId);
    LocaleProfile& getCurrentLocale();
    void setCurrentLocale(const std::string& localeId);
    
    // Parsing e formatação
    double parseNumber(const std::string& input);
    std::string formatNumber(double value);
    
private:
    static LocaleManager instance;
    std::map<std::string, LocaleProfile> locales;
    std::string currentLocaleId;  // Default: "pt-BR"
};
```

---

## Fluxo de Entrada/Saída

### Entrada (Input)
```
Usuário digita: "1.234,56"
    ↓
LocaleManager::parseNumber("1.234,56")
    ↓
Remover separador de milhar "." → "1234,56"
    ↓
Substituir separador decimal "," por "." para conversão → "1234.56"
    ↓
std::stod("1234.56") → 1234.56 (double)
    ↓
Armazenar como double internamente
```

### Saída (Output)
```
Valor interno: 1234.56 (double)
    ↓
LocaleManager::formatNumber(1234.56)
    ↓
Formatar com 6 casas decimais max
    ↓
Aplicar separador de milhar "."
    ↓
Aplicar separador decimal ","
    ↓
Resultado exibido: "1.234,56"
```

---

## Regras de Validação

### Durante Entrada
1. **Separador decimal único**: Apenas um "," (pt-BR) ou "." (en-US) permitido
2. **Múltiplos separadores ignorados**: Se usuário clica "," duas vezes, segunda é ignorada
3. **Números negativos**: Sinal "-" sempre permitido no início
4. **Precisão**: Máximo 6 casas decimais (configurable por locale)

### Durante Saída
1. **Arredondamento**: Usar `std::fixed` e `std::setprecision(6)`
2. **Remoção de zeros**: "5.00" → "5", "5.10" → "5,1"
3. **Separadores**: Aplicar sempre que houver milhar ou decimal

---

## Integração com Calculator

### Modificação na Classe `Calculator`

```cpp
class Calculator {
public:
    // ... métodos existentes ...
    
    // Novo
    std::string getFormattedResult() const;
    bool parseAndValidateInput(const std::string& input);
    
private:
    LocaleManager& localeManager;  // Referência ao singleton
};
```

### Fluxo de Operação

1. Usuário digita número → passa por `parseNumber()` → armazenado como double
2. Usuário clica operação → `Calculator::add/subtract/etc()` calcula
3. Usuário clica "=" → resultado é formatado via `formatNumber()` → exibido no display

---

## Testes Esperados para US10

### PT-BR — Entrada
```
Entrada: "3,5"      → Internamente: 3.5
Entrada: "1.234,56" → Internamente: 1234.56
Entrada: "0,1"      → Internamente: 0.1
```

### PT-BR — Saída
```
1234.56  → Exibir: "1.234,56"
3.5      → Exibir: "3,5"
5.0      → Exibir: "5"
0.3333333 → Exibir: "0,333333"
```

### Validação
```
Separador decimal único: "3,5,1" → aceita apenas "3,51"
Múltiplas vírgulas: clica "," duas vezes → segunda é ignorada
Números negativos: "-5,25" funciona corretamente
```

---

## Extensibilidade (US11)

Para adicionar novo locale (ex: en-US), o desenvolvedor deve:

1. **Criar novo LocaleProfile**
   ```cpp
   LocaleProfile en_us("en-US", '.', ',', 6);
   localeManager.registerLocale(en_us);
   ```

2. **Sem modificar** `Calculator`, `LocaleManager` ou parsing logic

3. **Apenas** registrar a configuração antes da execução

---

## Configuração Padrão (MVP)

- **Locale Padrão**: `pt-BR` (carregado na inicialização)
- **Arquivo de Configuração**: `.github/config/locale.json` (futuro)
- **Hardcoded para MVP**: Inicializar com pt-BR sem arquivo externo

---

## Roadmap

### Fase 1 (MVP) — US10
- [x] Definir `LocaleProfile`
- [x] Implementar `LocaleManager` singleton
- [x] Integrar com `Calculator`
- [x] Testar pt-BR entrada/saída
- [x] Validar separadores únicos

### Fase 2 — US11
- [ ] Adicionar arquivo de configuração (config.json)
- [ ] Carregar locale do sistema operacional
- [ ] Menu de seleção de idioma (GUI)
- [ ] Tradução de mensagens de erro

### Fase 3 (Futuro)
- [ ] Suporte en-US, pt-PT, otros
- [ ] Persistência de preferência de locale
- [ ] API REST para mudança de locale

---

**Fim da Especificação**
