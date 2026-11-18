> Atualização: a conexão compartilhada e a edição interna do quadro foram implementadas. Consulte [PERSONALIZACAO-E-COMPARTILHAMENTO.md](PERSONALIZACAO-E-COMPARTILHAMENTO.md). As limitações de sincronização descritas abaixo se referem à versão local anterior.

# Central de tarefas e projetos em abas

Abra `dist/widget-atelier.html` para usar o editor completo. Abra `dist/central-de-tarefas.html` para usar somente a central, inclusive no celular. `dist/central-de-tarefas-exemplo.html` contém tarefas fictícias identificadas como exemplo.

## Projetos em abas

As abas ficam acima do canvas. Use **+** para criar uma composição vazia, clique no nome para alternar, no lápis para renomear e no **×** para fechar. **Reabrir aba** recupera a última aba fechada durante esta sessão. É preciso manter uma aba aberta; até 12 projetos podem ficar abertos simultaneamente.

Cada projeto tem sua composição, tarefas e histórico de desfazer/refazer. As abas abertas são restauradas neste navegador; o histórico de desfazer é mantido durante a sessão. O comando **Abrir projeto** abre o arquivo em uma nova aba. **Baixar projeto** baixa a aba ativa; **Restaurar composição inicial** modifica somente a aba ativa e pode ser desfeito.

O armazenamento do navegador é limitado. Se o topo indicar **Não salvo**, baixe os projetos importantes antes de fechar. Limpar os dados do navegador apaga as cópias locais.

## Central de tarefas

No editor, vá em **Dinâmicos → Central de tarefas**. A central começa vazia. O canvas cresce, se necessário, para acomodar o componente. As tarefas são interativas no próprio canvas; use as bordas para selecionar/mover o componente, os quatro cantos para redimensionar e o controle circular para girar. Duplicar o componente cria outra visualização da mesma central dentro daquele projeto. Adicionar uma nova central cria uma lista independente.

- **Hoje:** prazos vencidos, plano do dia, concluídas hoje e caixa de entrada sem data.
- **Quadro:** A fazer, Em andamento, Aguardando retorno, Bloqueado e Concluído. Arraste cartões ou use o seletor de status, que também funciona no celular e por teclado.
- **Calendário:** mostra o dia planejado; na ausência dele, mostra o prazo. Arrastar entre dias muda o planejamento e preserva o prazo. Use a tabela ou o formulário para alterar as datas sem arrastar.
- **Tabela:** todas as tarefas, com responsáveis, status, planejamento, prazo e prioridade editáveis.

Todas as visualizações leem as mesmas tarefas. Buscar ou filtrar por responsável afeta apenas a visualização. O filtro **Você** e o filtro **Cliente** incluem tarefas compartilhadas; estas também têm um filtro próprio. A busca considera título, projeto e notas.

Cada tarefa tem título, responsável (Você/Cliente/Compartilhada/Sem responsável), status, dia planejado, prazo de entrega, prioridade, projeto/entrega, notas e até 30 etapas. Clique no título para editar. No formulário, use uma etapa por linha e `[x]` para etapas prontas; nos cartões, as etapas podem ser marcadas diretamente. As etapas não concluem automaticamente a tarefa principal.

O plano de hoje conta as tarefas planejadas para hoje ou com prazo hoje, uma vez cada. Prazos vencidos incluem apenas tarefas abertas com entrega anterior a hoje. “Concluídas hoje” considera o momento da conclusão, independentemente do prazo. O fuso da central é Brasília (`America/Sao_Paulo`); datas são dias de calendário, sem conversão inadvertida de UTC.

Excluir uma tarefa oferece **Recuperar exclusão** imediatamente. No editor, também há Desfazer. O botão **Exemplo** preenche apenas centrais vazias com tarefas fictícias.

## Exportação e dados

Selecione a central e use **Central de tarefas → Exportar central responsiva** no painel direito. Esse HTML funciona sozinho e adapta os controles à largura do celular. O **Exportar HTML** principal preserva a composição completa, com o comportamento proporcional/fixo do WA. Ambos usam o mesmo motor de tarefas, com fontes incorporadas e sem dependências externas.

**Backup** baixa um JSON das tarefas. **Importar** aceita esse formato em uma central vazia; não substitui silenciosamente uma lista existente. Limites: 500 tarefas por central, 20 centrais por projeto, 3 MB por backup de tarefas; o projeto completo mantém o limite de 15 MB. Backups de tarefas não incluem a composição; o JSON do projeto inclui ambos.

Na central exportada, mudanças são salvas localmente neste navegador e origem. Cópias com o mesmo identificador e mesma origem usam a mesma chave de armazenamento ao carregar; não há sincronização contínua entre abas ou dispositivos. Na prévia do Notion, os dados são uma cópia isolada.

**Não existe sincronização multiusuário, integração ativa com Notion nem controle de acesso nesta etapa.** Responsáveis são uma forma de organizar o trabalho, não permissões. Enviar o arquivo HTML para a cliente entrega uma cópia inicial; não conecta as edições dela às suas. A futura conexão requer uma base compartilhada e autenticação adequada. Nenhum token privado foi incorporado.

Para incorporar no Notion, hospede o HTML em HTTPS e use `/embed`. A simulação do editor é aproximada. Abra o editor por uma origem local/HTTPS estável para obter persistência previsível; o comportamento de armazenamento de arquivos abertos por duplo clique varia entre navegadores.

## Implementação e validação

O motor de composição continua independente. `src/taskhub.js` contém modelo, validação, quatro visualizações, interação e exportação da central. `src/taskhub.css` é compartilhado pelo editor e pelos HTMLs exportados. `engine.js` apenas monta o componente; `runtime.js` conecta a persistência do widget exportado. `app.js` integra o histórico, as abas, o salvamento e a importação de projetos. Relógios, calendários e componentes existentes foram preservados.

Gerar o editor: `python build.py`. Gerar a central vazia e a demonstração: `node compile-task-portals.cjs`.

Verificações: `tests/tasks-projects.cjs` cobre criação/etapas, quatro visualizações, responsáveis/busca, conclusão, desfazer/refazer, arraste, planejamento separado de prazo, prévia isolada, abas/renomeação/restauração, validação de datas, exportação independente, persistência e uso em largura de celular, backup/exclusão/importação. `tests/tasks-release.cjs` verifica os arquivos finais, armazenamento indisponível, uso mobile, fontes e exclusão de centrais não utilizadas da exportação. `tests/studio-v6.cjs` mantém 15 cenários de regressão das funcionalidades anteriores.
