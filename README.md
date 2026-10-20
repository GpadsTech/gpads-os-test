# GPADS-OS — Sistema Operacional do GPADS

> **Versão da estrutura:** 0.3 (20/10/2026). **Natureza:** consolidação documental para avaliação. **Importante:** os documentos distinguem **Confirmado**, **Proposto** e **Pendente**; uma proposta escrita não equivale a uma decisão do grupo.

Este repositório é a referência central para a organização de trabalho do GPADS: células, membros, governança, produtos/entregáveis, fluxos, padrões, manuais, relatórios quinzenais e especificações da aplicação de gestão GPADS-OS. Seu propósito é permitir que as atividades sejam **rastreáveis, verificáveis, documentadas e reproduzíveis**.

## Por onde começar

| Necessidade | Local |
|---|---|
| Entender o GPADS-OS | [`docs/00-visao-geral`](docs/00-visao-geral/README.md) |
| Conhecer as sete células e membros | [`cells/`](cells/README.md) |
| Consultar papéis e decisões | [`docs/02-arquitetura-organizacional`](docs/02-arquitetura-organizacional/README.md), [`docs/03-governanca`](docs/03-governanca/README.md) |
| Organizar um produto | [`products/`](products/README.md) e [`templates/`](templates/README.md) |
| Ver fluxo e estados das entregas | [`docs/04-gestao-de-produtos`](docs/04-gestao-de-produtos/README.md) e [`workflows/`](workflows/README.md) |
| Enviar relatório quinzenal | [`docs/05-processos-operacionais/relatorios-quinzenais.md`](docs/05-processos-operacionais/relatorios-quinzenais.md) |
| Consultar DoD | [`standards/definition-of-done`](standards/definition-of-done/README.md) |
| Entrar no grupo | [`docs/07-onboarding`](docs/07-onboarding/README.md) |
| Conhecer a plataforma | [`platform/`](platform/README.md) |
| Ver limites das evidências disponíveis | [`docs/08-decisoes/fontes-e-rastreabilidade.md`](docs/08-decisoes/fontes-e-rastreabilidade.md) |

## Organização

- `docs/`: contexto, estratégia, organização, governança e decisões.
- `cells/`: **sete células** e seus **37 vínculos de participação**, incluindo líderes; a mesma pessoa pode aparecer em mais de uma célula.
- `products/`: catálogo e modelo para gerenciar produtos por **produto/entregável → épico → história → microentrega**.
- `platform/`: especificação arquitetural e integração com Base44/GitHub (não representa um dump do código em produção).
- `workflows/`: procedimentos de execução, solicitações, revisão e validação.
- `standards/`: critérios de qualidade e Definition of Done.
- `templates/`: modelos para produtos, trabalhos, decisões e relatórios.
- `knowledge-base/`: manuais, tutoriais, referências e glossário.
- `operations/`: planejamento, reuniões, indicadores e consolidados do grupo.
- `infrastructure/`, `scripts/`, `tests/`: orientação técnica e validação do pacote.

## Princípios de operação

1. Cada entrega deve ter dono, critérios de aceitação, vínculos hierárquicos e evidências.
2. **Revisão e validação antecedem a conclusão**, com DoD apropriada ao tipo de trabalho.
3. Solicitações entre células devem ser registradas, com responsável e encaminhamento.
4. Relatórios quinzenais pertencem à **célula em que o trabalho ocorreu**; mudanças de célula não apagam o histórico.
5. Manuais devem permitir que um novo integrante reproduza atividades e localize os artefatos versionados.
6. Informações não confirmadas ficam marcadas como pendentes, não são inventadas.

## Como contribuir

Leia [`CONTRIBUTING.md`](CONTRIBUTING.md). Execute `python scripts/validate_repository.py` para conferir diretórios, arquivos e vínculos. Não inclua segredos, dados pessoais desnecessários nem relatórios de atividades fictícias.

## Limitações e próximos passos

Esta versão foi construída a partir do contexto disponível de conversas do projeto gpadsLab e das definições explícitas do usuário. Não foi obtida uma cópia independente do repositório Git nem inspecionada a aplicação Base44 em execução. Cronogramas, produtos efetivos, decisões não registradas e atividades individuais devem ser confirmados antes de divulgação institucional. A licença de uso ainda precisa ser escolhida.
