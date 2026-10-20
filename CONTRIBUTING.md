# Como contribuir para o GPADS-OS

> **Situação:** Proposto, sujeito à ratificação de governança.

## Antes de editar

1. Localize o documento proprietário do assunto: `docs/` (regras), `cells/` (operação de célula), `products/` (produto), `standards/` (critérios) ou `knowledge-base/` (procedimento técnico).
2. Confirme se está alterando uma **decisão aprovada**, um **modelo proposto** ou uma **informação pendente**. Não transforme propostas em normas sem registro de decisão.
3. Abra uma alteração com motivação, arquivos afetados, impacto e evidências; escolha revisor conforme regras de governança aplicáveis.
4. Verifique referências, links relativos, nomes de arquivo e ortografia. Prefira nomes de diretório ASCII minúsculos separados por hífen; preserve os nomes reais no conteúdo.
5. Execute `python scripts/validate_repository.py` e `python -m unittest discover -s tests -v` antes da integração.

## Relatórios individuais

Crie `cells/<celula>/membros/<slug>/relatorios-quinzenais/<ano>/AAAA-MM-Q1.md` ou `AAAA-MM-Q2.md` a partir de `templates/relatorio-quinzenal.md`. Inclua identificadores das tarefas e evidências, sem copiar informação sigilosa. A pasta registra vínculo com a célula no período.

## Alterações relevantes

Registre decisões de arquitetura, governo de dados, mudanças de hierarquia ou fluxos em `docs/08-decisoes/adrs/`; sintetize a mudança em `CHANGELOG.md`. Não crie credenciais no Git. Campos que dependam de validação devem estar marcados `PENDENTE` e conter o responsável pela confirmação, quando conhecido.

## Ética e privacidade

Evite matrículas, CPF, e-mail pessoal, telefones, dados acadêmicos sensíveis, logins e resultados de avaliação individual. Quando necessário, utilize armazenamento com permissão adequada e apenas referencie seu identificador, sem publicar conteúdo privado.
