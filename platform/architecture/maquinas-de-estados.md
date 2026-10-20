# Máquina de estados de trabalho — proposta

> **Situação:** Proposto. 

```text
Backlog → Planejado → Em execução → Em revisão → Em validação → Concluído
                    ↑           │                │
                    └───────────┴────────────────┘
                           devolução motivada
```

**Invariantes sugeridas:** entrada em revisão requer artefato identificável; entrada em validação requer parecer favorável ou exceção registrada; conclusão requer DoD e validação; toda devolução guarda motivo e autor. Estados alternativos como bloqueado/cancelado podem ser atributos ou ramos, mas não foram decididos. Não assumir que os nomes reproduzem exatamente os estados da Base44.
