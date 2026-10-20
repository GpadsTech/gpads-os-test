# Esquema lógico — proposta inicial

> **Situação:** Proposto. 

```text
Pessoa 1---N Vinculo N---1 Celula
Produto 1---N Epico 1---N Historia 1---N Microentrega
Microentrega 1---N Evidencia
Microentrega 1---N RevisaoValidacao
Vinculo 1---N RelatorioQuinzenal
Celula 1---N Solicitacao (origem/destino)
```

Chaves e atributos sugeridos: `id` imutável; `created_at`, `updated_at` e `status`; datas e revisão por registro; permissões por relação de perfil. Conflitos de integridade: duplicidade de nomes (Carlos vs Carlos Touca), múltiplas lideranças e mudanças históricas de célula. **Não implementar migrations sem comparação com o esquema real.**
