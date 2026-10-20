# Visão geral da arquitetura funcional

> **Situação:** Proposto. 

```text
Usuário (membro/líder/revisor)
   ↓
Interface GPADS-OS (a verificar na aplicação existente)
   ↓
Serviços e regras de negócio (modelagem proposta)
   ├── Organização: células, membros, vínculos e lideranças
   ├── Entregas: produtos, épicos, histórias, microentregas
   ├── Operação: solicitações, impedimentos e prioridades
   ├── Qualidade: testes, evidências, revisão, validação e DoD
   └── Conhecimento: documentos, manuais, relatórios
   ↓
Persistência e integrações (tecnologia real não confirmada)
```

**Princípios:** IDs estáveis, histórico de estados, vínculo entre requisitos e evidências, segregação adequada de permissões, referência a artefatos versionados e não duplicação de tarefas em relatórios. **PENDENTE:** inspeção dos componentes que efetivamente existem na Base44.
