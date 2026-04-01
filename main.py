"""
SecOps PCDF - Fase 1
Módulo principal de demonstração de boas práticas de segurança.
Disciplina: EPS FGA0316 - 2026.1
Aluno: Beatriz Vieira Nascimento
"""

import hashlib
import logging
import os
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def hash_data(data: str) -> str:
    """Retorna o hash SHA-256 de uma string de entrada."""
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def get_environment() -> str:
    """Lê a variável de ambiente APP_ENV com valor padrão seguro."""
    return os.environ.get("APP_ENV", "development")


def main() -> int:
    """Ponto de entrada principal da aplicação."""
    env = get_environment()
    logger.info("Ambiente: %s", env)

    sample = "secops-pcdf-2026"
    digest = hash_data(sample)
    logger.info("Hash SHA-256 de '%s': %s", sample, digest)

    logger.info("Pipeline DevSecOps inicializado com sucesso.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
