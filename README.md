# eps_-Onboarding_SecOps

[![DevSecOps Pipeline](https://github.com/Beatrizvn/eps_-Onboarding_SecOps/actions/workflows/devsecops.yml/badge.svg)](https://github.com/Beatrizvn/eps_-Onboarding_SecOps/actions/workflows/devsecops.yml)

**Disciplina:** Engenharia de Produto de Software (FGA0316) - 2026.1  
**Aluno:** Beatriz Vieira Nascimento | **Matrícula:** 211031628

---

## Sobre o Projeto

Projeto de Onboarding SecOps — implementação de um pipeline DevSecOps com análise estática de segurança (SAST), verificação de dependências (SCA) e lint de qualidade de código.

## Stack

- **Python 3.12** — runtime
- **Poetry** — gerenciamento de dependências e ambiente virtual isolado (`.venv` dentro do projeto)
- **Bandit** — análise estática de segurança (SAST)
- **Ruff** — linter e formatter
- **Safety** — verificação de CVEs em dependências (SCA)
- **GitHub Actions** — pipeline de CI/CD

---

## 1. Configuração do Ambiente

```
$ poetry env info

Virtualenv
Python:         3.12.13
Implementation: CPython
Path:           /Users/beatriznascimento/Documents/unb/eps_-Onboarding_SecOps/.venv
Executable:     /Users/beatriznascimento/Documents/unb/eps_-Onboarding_SecOps/.venv/bin/python
Valid:          True

Base
Platform:   darwin
OS:         posix
Python:     3.12.13
Path:       /Users/beatriznascimento/.pyenv/versions/3.12.13
Executable: /Users/beatriznascimento/.pyenv/versions/3.12.13/bin/python3.12
```

> **Evidência:** `.venv` criado dentro do projeto (`virtualenvs.in-project = true`).

---

## 2. Logs de Segurança e Qualidade

### 2.1. Bandit — Análise Estática (SAST)

```
$ poetry run bandit -r . --exclude ./.venv,./tests -ll

[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.12.13
Run started: 2026-04-01 22:25:54.947530+00:00

Test results:
        No issues identified.

Code scanned:
        Total lines of code: 32
        Total lines skipped (#nosec): 0
        Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0
                Low: 0
                Medium: 0
                High: 0
        Total issues (by confidence):
                Undefined: 0
                Low: 0
                Medium: 0
                High: 0
Files skipped (0):
```

> Vulnerabilidades encontradas: **ZERO**

### 2.2. Safety — Verificação de CVEs (SCA)

```
$ poetry run safety scan

Safety v3.7.0 scanning for Vulnerabilities...
Scanning dependencies in your environment:
-> .venv/lib/python3.12/site-packages

Using open-source vulnerability database
Found and scanned 46 packages
Timestamp 2026-04-01 19:26:11
0 vulnerabilities reported
0 vulnerabilities ignored

No known security vulnerabilities reported.
```

### 2.3. Ruff — Linter e Formatter

```
$ poetry run ruff check .

All checks passed!
```

---

## 3. Pipeline CI/CD — GitHub Actions

- **Link da Action de Sucesso:** [Ver no GitHub Actions](https://github.com/Beatrizvn/eps_-Onboarding_SecOps/actions)

---

## Como Executar Localmente

```bash
# Pré-requisitos: Python 3.12, Poetry

# 1. Configurar ambiente virtual dentro do projeto
poetry config virtualenvs.in-project true

# 2. Instalar dependências
poetry install --with dev

# 3. Executar a aplicação
poetry run python main.py

# 4. Rodar análise de segurança
poetry run bandit -r . --exclude .venv,tests
poetry run ruff check .
poetry run safety check
```
