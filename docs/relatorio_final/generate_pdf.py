#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

doc = SimpleDocTemplate("docs/relatorio_final/relatorio_final.pdf", pagesize=letter,
                        leftMargin=0.75*inch, rightMargin=0.75*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)
styles = getSampleStyleSheet()
story = []

title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=18, spaceAfter=20)
heading1_style = ParagraphStyle('Heading1', parent=styles['Heading1'], fontSize=14, spaceBefore=20, spaceAfter=10)
heading2_style = ParagraphStyle('Heading2', parent=styles['Heading2'], fontSize=12, spaceBefore=15, spaceAfter=8)
normal_style = styles['Normal']
normal_style.fontSize = 10
normal_style.leading = 14

story.append(Paragraph("Análise de Test Smells e Refatoração", title_style))
story.append(Paragraph("Disciplina: Teste de Software", normal_style))
story.append(Paragraph("Gustavo Pimentel Carvalho Costa - Matrícula: 833151", normal_style))
story.append(Paragraph("Projeto: test-smelly", normal_style))
story.append(Spacer(1, 20))

story.append(Paragraph("1. Resumo dos Resultados", heading1_style))
story.append(Paragraph("Após a refatoração, a suite de testes apresenta:", normal_style))

data = [
    ['Métrica', 'Antes', 'Depois'],
    ['Total de testes', '4 (+ 1 skipped)', '14 (+ 1 skipped)'],
    ['ESLint errors (smelly)', '4 errors, 2 warnings', '0 errors, 0 warnings'],
    ['ESLint warnings (clean)', '-', '0 warnings'],
    ['Testes passando', '4 passed', '14 passed'],
    ['Smells identificados', '5', '0 (refatorados)'],
]
t = Table(data, colWidths=[2.5*inch, 1.5*inch, 1.5*inch])
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 9),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))
story.append(t)
story.append(Spacer(1, 15))

story.append(Paragraph("2. Análise de Smells Identificados", heading1_style))

smells_data = [
    ['#', 'Smell', 'Localização', 'Regra ESLint'],
    ['1', 'Eager Test', 'deve criar e buscar usuário', 'N/A (manual)'],
    ['2', 'Conditional Logic', 'deve desativar usuários', 'jest/no-conditional-expect'],
    ['3', 'Error Handling', 'deve falhar menor idade', 'N/A (manual)'],
    ['4', 'Fragile Test', 'deve gerar relatório', 'N/A (manual)'],
    ['5', 'Skipped Test', 'lista vazia', 'jest/no-disabled-tests'],
]
t2 = Table(smells_data, colWidths=[0.4*inch, 1.8*inch, 2*inch, 1.8*inch])
t2.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
    ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 8),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
]))
story.append(t2)
story.append(Spacer(1, 15))

story.append(PageBreak())

story.append(Paragraph("3. Detecção por Ferramenta", heading1_style))
story.append(Paragraph("Resultado do ESLint no arquivo smelly:", normal_style))
story.append(Spacer(1, 5))

code_style = ParagraphStyle('Code', fontName='Courier', fontSize=8, leading=10,
                             backgroundColor=colors.lightgrey, spaceAfter=10)
story.append(Paragraph("test/userService.smelly.test.js", code_style))
story.append(Paragraph("44:9  error    Avoid calling expect conditionally  jest/no-conditional-expect", code_style))
story.append(Paragraph("46:9  error    Avoid calling expect conditionally  jest/no-conditional-expect", code_style))
story.append(Paragraph("49:9  error    Avoid calling expect conditionally  jest/no-conditional-expect", code_style))
story.append(Paragraph("73:7  error    Avoid calling expect conditionally  jest/no-conditional-expect", code_style))
story.append(Paragraph("77:3  warning  Tests should not be skipped        jest/no-disabled-tests", code_style))
story.append(Paragraph("77:3  warning  Test has no assertions             jest/expect-expect", code_style))
story.append(Spacer(1, 10))
story.append(Paragraph("Total: 4 errors, 2 warnings", normal_style))
story.append(Spacer(1, 10))
story.append(Paragraph("Após refatoração:", normal_style))
story.append(Paragraph("test/userService.clean.test.js - 0 errors, 0 warnings", normal_style))
story.append(Spacer(1, 20))

story.append(Paragraph("4. Processo de Refatoração", heading1_style))

story.append(Paragraph("4.1 Error Handling Anti-Pattern (Smell 3)", heading2_style))
story.append(Paragraph("ANTES (try/catch silencioso):", normal_style))
story.append(Paragraph("""
test('deve falhar ao criar usuário menor de idade', () => {
  try {
    userService.createUser('Menor', 'menor@email.com', 17);
  } catch (e) {
    expect(e.message).toBe('O usuário deve ser maior de idade.');
  }
});
""", code_style))

story.append(Paragraph("PROBLEMA: Se a validação for removida, o teste passa silenciosamente sem nenhuma asserção executada.", normal_style))
story.append(Spacer(1, 8))

story.append(Paragraph("DEPOIS (expect().toThrow()):", normal_style))
story.append(Paragraph("""
test('deve lançar erro ao criar usuário menor de idade', () => {
  expect(() => {
    userService.createUser('Menor', 'menor@email.com', 17);
  }).toThrow('O usuário deve ser maior de idade.');
});
""", code_style))

story.append(Paragraph("SOLUÇÃO: O expect().toThrow() guarantees que a exceção será lançada. Se a validação for removida, o teste falha imediatamente.", normal_style))
story.append(Spacer(1, 15))

story.append(Paragraph("4.2 Conditional Logic in Test (Smell 2)", heading2_style))
story.append(Paragraph("ANTES (loop + if com expect condicional):", normal_style))
story.append(Paragraph("""
for (const user of todosOsUsuarios) {
  const resultado = userService.deactivateUser(user.id);
  if (!user.isAdmin) {
    expect(resultado).toBe(true);
  } else {
    expect(resultado).toBe(false);
  }
}
""", code_style))

story.append(Paragraph("PROBLEMA: expect dentro de if pode não executar para todos os casos. Um mutante que inverta a lógica pode sobreviver.", normal_style))
story.append(Spacer(1, 8))

story.append(Paragraph("DEPOIS (testes explícitos separados):", normal_style))
story.append(Paragraph("""
test('deve desativar usuário comum e retornar true', () => {
  const usuario = userService.createUser('Comum', 'comum@email.com', 30);
  const resultado = userService.deactivateUser(usuario.id);
  expect(resultado).toBe(true);
});

test('deve recusar desativação de admin e retornar false', () => {
  const admin = userService.createUser('Admin', 'admin@email.com', 40, true);
  const resultado = userService.deactivateUser(admin.id);
  expect(resultado).toBe(false);
});
""", code_style))

story.append(Paragraph("SOLUÇÃO: Cada teste verifica um caminho específico. Sem lógica condicional, todo comportamento é explícito.", normal_style))
story.append(PageBreak())

story.append(Paragraph("5. Estrutura AAA nos Testes Refatorados", heading1_style))
story.append(Paragraph("Todos os testes seguem o padrão Arrange-Act-Assert:", normal_style))
story.append(Spacer(1, 5))

story.append(Paragraph("""
test('deve retornar o usuário correto pelo id', () => {
  // Arrange
  const criado = userService.createUser('Bob', 'bob@email.com', 30);
  
  // Act
  const encontrado = userService.getUserById(criado.id);
  
  // Assert
  expect(encontrado.nome).toBe('Bob');
});
""", code_style))

story.append(Spacer(1, 15))

story.append(Paragraph("6. Conclusão", heading1_style))
story.append(Paragraph("""
A refatoração seguindo o padrão AAA (Arrange-Act-Assert) eliminou os 5 smells identificados:
1. Eager Test → separados em testes unitários
2. Conditional Logic → testes explícitos sem loop/if
3. Error Handling → expect().toThrow() em vez de try/catch
4. Fragile Test → verificação de comportamento em vez de string exata
5. Skipped Test → implementado

O ESLint como ferramenta de análise estática complementa o teste manual, detectando 2 dos 5 smells automaticamente (conditional-expect e disabled-tests). Os outros 3 requerem revisão de código.

A qualidade da suite de testes melhorou significativamente: 14 testes passando, zero warnings ESLint, e código legível que especifica comportamento ao invés de apenas executar.
""", normal_style))

doc.build(story)
print("PDF gerado: docs/relatorio_final/relatorio_final.pdf")