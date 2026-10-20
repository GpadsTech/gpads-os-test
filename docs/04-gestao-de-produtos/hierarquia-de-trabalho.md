# Hierarquia de trabalho

> **Situação:** Confirmado (quatro níveis); Proposto (campos). 

**Estrutura definida:**

1. **Produto/entregável:** resultado identificável com finalidade, escopo, responsável e evidências de aceite.
2. **Épico:** bloco coerente de capacidades ou resultados, vinculado a um produto.
3. **História:** necessidade observável, com critérios de aceitação e rastreabilidade ao épico.
4. **Microentrega:** menor unidade planejável, executável e verificável de trabalho, vinculada à história.

**Relações:** produto 1:N épicos; épico 1:N histórias; história 1:N microentregas. A regra de cardinalidade é uma **proposta de modelagem**, não um esquema de banco confirmado.

Cada nível deve ter ID, título, estado, responsável, célula, links, dependências e evidências quando pertinentes. Não tratar a palavra “tarefa” como substituta automática dos quatro níveis.
