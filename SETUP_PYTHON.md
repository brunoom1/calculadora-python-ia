# 🚀 Guia de Setup — Python para Calculadora

**Data**: 09/09/2026  
**Status**: Python não está instalado no sistema

## ⚠️ Pré-requisito: Instalar Python 3.10+

### Opção 1: Instalador Oficial (Recomendado)

1. Visite **https://www.python.org/downloads/**
2. Baixe **Python 3.12** (ou 3.11, 3.10+)
3. **Execute o installer**
4. ✅ **IMPORTANTE**: Marque `Add Python to PATH` durante a instalação
5. Clique em `Install Now`
6. Aguarde conclusão

### Opção 2: Microsoft Store

```powershell
# Abrir Microsoft Store e procurar por "Python"
# Instalar versão 3.12 (ou mais recente)
```

### Opção 3: Gestor de Pacotes (Linux/macOS)

```bash
# Linux (Debian/Ubuntu)
sudo apt install python3.12 python3.12-venv

# macOS (Homebrew)
brew install python@3.12
```

---

## ✅ Verificar Instalação

Após instalar, abra um **novo** PowerShell/Terminal e execute:

```powershell
python --version
# Deve mostrar: Python 3.12.x ou similar
```

Se não funcionar:
1. Feche e reabra PowerShell/Terminal
2. Reinicie o computador
3. Verifique se `Add Python to PATH` foi marcado durante instalação

---

## 🔧 Setup Completo (Primeira Vez)

Após instalar Python com sucesso:

```powershell
# 1. Navegar até o projeto
cd "C:\Users\[seu-usuário]\Projetos\gerais\estudo\calculadora"

# 2. Criar virtual environment (isola dependências)
python -m venv venv

# 3. Ativar virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
# Deve mostrar: (venv) no prompt

# 4. Atualizar pip (gerenciador de pacotes)
python -m pip install --upgrade pip

# 5. Instalar dependências do projeto
pip install -r app/requirements.txt

# 6. Verificar instalação
pip list
# Deve mostrar: pytest, pytest-cov, pytest-watch
```

---

## 🧪 Verificar Setup com Testes

```powershell
# Ativar venv (se não estiver)
venv\Scripts\activate

# Executar testes
pytest app/tests/ -v

# Resultado esperado:
# ===== test session starts =====
# app/tests/test_calculator.py::test_init PASSED
# app/tests/test_calculator.py::test_add_positive_numbers PASSED
# ... (mais 70+ testes)
# ===== 70+ passed in X.XXs =====
```

Se todos os testes passam ✅, o setup foi bem-sucedido!

---

## 🎮 Executar a Aplicação

```powershell
# Ativar venv (se não estiver)
venv\Scripts\activate

# Executar
python app/src/main.py

# Deve abrir uma janela com a calculadora!
# Teste as operações básicas
```

---

## 📝 Desenvolvimento — Cada Vez Que Abrir

```powershell
# 1. Abrir PowerShell/Terminal na pasta do projeto
cd "C:\Users\[seu-usuário]\Projetos\gerais\estudo\calculadora"

# 2. Ativar venv
venv\Scripts\activate
# Deve mostrar: (venv) no prompt

# 3. Fazer seu trabalho
# - Editar arquivos em app/src/
# - Executar testes: pytest app/tests/ -v
# - Executar app: python app/src/main.py

# 4. Ao terminar, é opcional desativar venv
deactivate
```

---

## 🐛 Troubleshooting

### Erro: `python: command not found`

```powershell
# Python não está no PATH
# Solução 1: Reinstalar Python com "Add Python to PATH"
# Solução 2: Adicionar manualmente ao PATH (avançado)

# Verificar se Python está em local alternativo:
Get-Command python 2>$null  # Se não encontrar, Python não está instalado

# Procurar instalações
ls C:\Python*  # Verificar se há Python instalado em C:\
```

### Erro: `No module named 'pytest'`

```powershell
# Dependências não instaladas
# Solução:
pip install -r app/requirements.txt

# Ou instalar manualmente:
pip install pytest pytest-cov pytest-watch
```

### Erro: `No module named 'tkinter'`

```powershell
# Tkinter não veio com Python
# Solução: Reinstalar Python incluindo "tcl/tk and IDLE"
# Ou instalar via apt (Linux):
sudo apt install python3.12-tk
```

### Erro: `ModuleNotFoundError: No module named 'src'`

```powershell
# Estar em diretório errado ao rodar testes
# Solução: Executar sempre a partir da raiz do projeto
cd calculadora
pytest app/tests/ -v  # Correto

# Evitar:
cd app
pytest tests/ -v  # Pode causar erro de imports
```

---

## 📦 Instalar Dependências Opcionais

Se precisar adicionar funcionalidades:

```powershell
# Formatação de código (opcional)
pip install black flake8

# Linter (opcional)
pip install pylint

# PyQt6 (se quiser interface melhor que Tkinter)
pip install PyQt6

# Visualizar dependencies
pip freeze
```

**Após adicionar**, atualizar `app/requirements.txt`:

```powershell
pip freeze > app/requirements.txt
```

---

## 🔄 Atualizar Dependências

```powershell
# Atualizar todas
pip install -r app/requirements.txt --upgrade

# Ou individual
pip install pytest --upgrade
```

---

## 💾 Desfazer — Remover Tudo e Começar de Novo

```powershell
# Remover virtual environment (vai perder instalações)
rmdir /s /q venv

# Remover cache Python
rmdir /s /q __pycache__
rmdir /s /q .pytest_cache
rmdir /s /q app\__pycache__
rmdir /s /q app\tests\__pycache__
rmdir /s /q app\src\__pycache__

# Começar do zero
python -m venv venv
venv\Scripts\activate
pip install -r app/requirements.txt
```

---

## ✨ Próximas Etapas Após Setup

1. **Ler documentação**:
   - `README.md` — Início rápido
   - `.github/copilot-instructions.md` — Como desenvolver
   - `.github/tasks.md` — Tarefas disponíveis

2. **Executar testes** para confirmar que tudo funciona:
   ```powershell
   pytest app/tests/ -v
   ```

3. **Iniciar desenvolvimento** seguindo `.github/tasks.md`

---

## 📞 Suporte

Se encontrar problemas:

1. Consultar `.github/copilot-instructions.md`
2. Ler `.github/requirements.md`
3. Verificar logs de erro
4. Recriar venv do zero (ver "Desfazer" acima)

---

**Após completar este setup, o projeto está 100% pronto para desenvolvimento! 🚀**
