# Analise de Test Smells

## Smell 1 — Eager Test
- Local: "deve criar e buscar um usuário corretamente"
- Problema: um teste cobre criar e buscar.
- Risco: diagnostico confuso e falha de responsabilidade unica.

## Smell 2 — Conditional Logic in Test
- Local: "deve desativar usuários se eles não forem administradores"
- Problema: for + if/else com expect condicional.
- Regra ESLint: jest/no-conditional-expect.
- Risco: asserts podem nao executar em certos caminhos.

## Smell 3 — Error Handling Anti-Pattern
- Local: "deve falhar ao criar usuário menor de idade"
- Problema: try/catch permite teste passar sem assert.
- Risco: bug de validacao fica invisivel.

## Smell 4 — Fragile Test
- Local: "deve gerar um relatório de usuários formatado"
- Problema: verifica string exata do relatorio.
- Risco: falhas cosmeticas sem quebra real de comportamento.

## Smell 5 — Skipped Test
- Local: "deve retornar uma lista vazia quando não há usuários"
- Problema: test.skip com TODO.
- Regra ESLint: jest/no-disabled-tests (warn).
- Risco: comportamento sem especificacao.
