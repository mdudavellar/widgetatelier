# Verificação da exportação

A conferência usa SHA-256 individual para os 158 arquivos originais do commit v32. O ZIP também recebe checksum externo e teste de integridade. EXPORT-REPORT.json registra os resultados da execução nesta sessão.

## Testes portáteis

`npm test` monta o editor e roda o teste SQLite/API original mais 18 testes selecionados de controles numéricos, barra contextual, navegação, tags do calendário, legendas/texto, edição no canvas, formas, carregamento/cache de ícones, catálogos e partes editáveis.

A ferramenta copia os testes para .local-tests e substitui caminhos absolutos da sessão antiga por caminhos deste checkout; também resolve linkedom via npm. Os testes originais em source/ ficam intactos. As asserções originais não são removidas.

Os demais testes históricos também foram preservados, mas alguns dependem de arquivos /tmp de sessões anteriores ou de Playwright e fixtures de navegador. Não são uma suíte portátil completa sem revisão adicional. A seleção executada não comprova fidelidade visual nem compatibilidade total com todos os dispositivos.

`npm run test:local` sobe um servidor HTTP em porta temporária, testa o editor e catálogo, autenticação e alteração de tarefas, publicação e atualização de widget, oEmbed, e persistência após reiniciar. Usa pasta temporária própria e a apaga; não faz chamadas à produção.

Nesta transferência não foi feita uma validação visual em navegador nem um teste dentro do Notion. Não foram consultados ou exportados os dados privados de produção.


A seleção da v32 acrescenta publicação compacta com link estável, falha/tentativa posterior e versão/cache do Worker compilado.

## Resultado desta cópia v32

- 158/158 arquivos originais e 22/22 complementos conferidos.
- HTML reconstruído idêntico ao snapshot publicado: SHA-256 `deefe9f5d1fcda9fc2c650822dc58e258e0be54f5a4521d88836f3db14f29e22`.
- Seleção portátil: **18/19 testes passaram**, incluindo os dois novos testes da v32. A falha histórica em catalogs-editor.cjs procura o seletor #contextBar .quick-font-size; foi preservada e não foi corrigida nesta transferência.
- Servidor local: editor, catálogo, autenticação, tarefas, publicação, atualização, oEmbed e persistência após reinício passaram.
- A configuração npm/lockfile da v31 foi preservada, com a identificação do pacote atualizada para 32.0.0. As dependências não mudaram; a instalação havia sido validada na transferência anterior.
