# Relatório de Prontidão Técnica: Onboarding SecOps

**Disciplina:** Engenharia de Produto de Software (FGA0316) - 2026.1  
**Aluno:** Beatriz Vieira Nascimento | **Matrícula:** 211031628

---

## 1. Configuração do Ambiente (Zero Trust & Isolamento)

Conforme as diretrizes de Soberania Técnica, as seguintes configurações foram aplicadas:

- [x] **Python 3.12:** Instalado e verificado (3.12.13 via pyenv).
- [x] **Poetry:** Configurado para criar `.venv` dentro do projeto (`virtualenvs.in-project true`).
- [x] **Determinismo:** Arquivos `pyproject.toml` e `poetry.lock` gerados com sucesso.

### Evidência de Ambiente

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

---

## 2. Logs de Auditoria e Qualidade (Security Gate)

### 2.1. Auditoria Estática (Bandit)

> **Resultado: ZERO vulnerabilidades identificadas no código do projeto.**

*Comando: `poetry run bandit -r . --exclude ./.venv,./tests -ll`*

```
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

---

### 2.2. Verificação de Dependências (Safety)

> **Resultado: 0 vulnerabilidades (CVEs) encontradas nas 46 dependências escaneadas.**

*Comando: `poetry run safety check`*

```
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

---

### 2.3. Qualidade e Conformidade (Ruff)

> **Resultado: Todas as verificações passaram sem erros.**

*Comando: `poetry run ruff check .`*

```
$ poetry run ruff check .

All checks passed!
```

---

## 3. Evidência de Integração Contínua (CI)

O pipeline automatizado foi configurado no GitHub Actions com os seguintes stages:

1. **[SAST] Bandit** — Análise estática de segurança
2. **[Lint] Ruff** — Qualidade e conformidade de código
3. **[SCA] Safety** — Verificação de CVEs em dependências

- **Repositório:** [https://github.com/Beatrizvn/eps_-Onboarding_SecOps](https://github.com/Beatrizvn/eps_-Onboarding_SecOps)
- **Link da Action de Sucesso:** [https://github.com/Beatrizvn/eps_-Onboarding_SecOps/actions/runs/23874250092/job/69613467150](https://github.com/Beatrizvn/eps_-Onboarding_SecOps/actions/runs/23874250092/job/69613467150)

---

## 4. Declaração de Soberania Técnica (CISSP Domain 8)

Eu, **Beatriz Vieira Nascimento**, declaro que auditei manualmente as ferramentas e dependências deste projeto. Confirmo que o código gerado via IA (GitHub Copilot) passou pela minha revisão humana (*Human-in-the-loop*), garantindo que não há vazamento de segredos ou falhas lógicas críticas antes da migração para o ecossistema da PCDF.

---

*Relatório gerado em: 2026-04-01*
