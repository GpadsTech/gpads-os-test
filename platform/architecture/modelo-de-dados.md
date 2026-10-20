# Modelo conceitual de dados — proposta

> **Situação:** Proposto. 

| Entidade | Campos essenciais | Relações sugeridas |
|---|---|---|
| Pessoa | id, nome, identificador estável | N:M célula via Vínculo |
| Célula | id, nome, situação | N:M Pessoa, 1:N iniciativas |
| Vínculo | id, pessoa_id, celula_id, função, início/fim | histórico de participação |
| Produto | id, título, objetivo, responsável, situação | 1:N épicos |
| Épico | id, produto_id, resultado | 1:N histórias |
| História | id, epico_id, critérios | 1:N microentregas |
| Microentrega | id, historia_id, responsável, estado | N evidências/revisões |
| Solicitação | id, origem, destino, tipo, situação | dependências/encaminhamentos |
| Evidência | id, tipo, localização, revisão, item_id | testes, artefatos e links |
| Revisão/Validação | id, item_id, revisor, parecer, data | gate para conclusão |
| Relatório | id, vínculo_id, período, status, links | síntese de atividades |

**Atenção:** nem todos os campos ou relações foram validados contra a aplicação existente; cardinalidades precisam de análise de uso.
