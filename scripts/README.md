# Scripts de manutenção

> **Situação:** Implementado. 

O script `validate_repository.py` verifica a presença das sete células, os 37 vínculos, arquivos essenciais, modelo de relatórios e a consistência básica de Markdown. Execute a partir da raiz:

```bash
python scripts/validate_repository.py
```

O teste automatizado está em `tests/test_repository_structure.py` e usa apenas a biblioteca padrão do Python. Não há alteração de dados externos nem integração com serviços.
