# Quadro personalizável e compartilhado

A central online está em https://wa-central-compartilhada.snappykookaburra.chatgpt.site. O arquivo atualizado do editor é `dist/widget-atelier-compartilhado.html`.

## Compartilhar com a cliente e incorporar no Notion

No WA, adicione uma central em **Dinâmicos → Central de tarefas**. Dentro dela, clique em **Compartilhar**. Esse comando envia as tarefas e a personalização interna para a base compartilhada e gera o link de edição daquela central. Copie o link completo, incluindo a parte depois de `#`.

Você e a cliente devem abrir o **mesmo link**. No Notion, digite `/embed` e cole esse link. A central é um widget incorporado; as tarefas não são linhas de uma database nativa do Notion. Não é preciso hospedar o arquivo por conta própria para usar a central online.

Quem tiver o link poderá ver, criar, editar e excluir tarefas, além de mudar a aparência da central, conforme a opção solicitada. Não há restrição por responsável: “Você”, “Cliente” e “Compartilhada” organizam as tarefas. A chave de acesso vai no fragmento do link e é enviada à API pelo cabeçalho de autorização; a base guarda apenas seu hash. Não há listagem pública de centrais.

A atualização automática consulta a base a cada cinco segundos, aproximadamente. Durante a edição de um formulário ou de um controle de aparência com foco, a atualização visual é adiada para preservar o conteúdo em edição. Ao salvar, as alterações são enviadas imediatamente. A central não oferece garantia de operação offline: se houver falha, o status informa que não foi sincronizado e oferece recuperação/backup quando há conflito.

Alterações independentes são combinadas pelo servidor. Se duas pessoas alterarem de formas diferentes o mesmo campo, a versão local fica preservada, o conflito é sinalizado e é possível baixar essa versão antes de carregar a compartilhada. Exclusões concorrentes com edições também geram conflito.

Use o estado de conexão acima da central como referência de sincronização. Uma confirmação de salvamento local no topo do WA não substitui a confirmação da base compartilhada. Guardar ou enviar um backup de um projeto conectado também pode incluir o link de edição; compartilhe-o somente com quem deve ter acesso.

## Mover e personalizar o conteúdo interno

Clique em **Personalizar quadro** dentro da central ou em **Personalizar conteúdos** no painel direito do WA. **Ampliar** abre a central em tela cheia, quando permitido pelo navegador. Esc retorna ao editor. Se o Notion não permitir tela cheia, abra o link da central em uma aba.

- Arraste pelas alças **⋮⋮** para reorganizar cabeçalho, resumos, navegação, filtros, tarefas e rodapé.
- Reorganize também os cartões de resumo, as seções do dia e as colunas do Kanban. As setas permitem fazer isso sem arrastar, inclusive por teclado.
- Em **Aparência e conteúdo**, ajuste destaque, fundo, cores dos cartões, texto, resumos e colunas; fundo transparente; cantos; espaçamento; tamanhos do título e dos cartões; número de resumos/seções por linha; largura das colunas e densidade.
- Mostre ou oculte responsável/prazo/prioridade, projeto, etapas e data do cabeçalho.
- Em **Ordem, nomes e visibilidade**, renomeie as seções e os status e escolha o que aparece. Ocultar uma parte não apaga suas tarefas. Navegação e área de tarefas permanecem disponíveis pelos controles visuais.
- Clique em **Concluir personalização** para sair do modo de organização. Os contornos e alças desaparecem; a configuração permanece. Restaurar aparência e ordem preserva as tarefas.

A organização interna usa blocos e grades que se adaptam à largura disponível. Não é posicionamento absoluto de cada palavra. As caixas e os elementos do canvas do WA continuam com os controles de posição, tamanho e rotação. No quadro, também é possível arrastar tarefas para mudar seu status e sua ordem.

A personalização interna acompanha a central compartilhada. A composição externa do WA — outros objetos, posições no canvas e tipografia atribuída ao componente pelo editor — pertence ao projeto/HTML exportado. O link da central online não publica a composição inteira do WA. A central online inclui as fontes DM Sans e Cormorant Garamond; fontes próprias do projeto permanecem incorporadas na exportação correspondente.

## Arquivos locais e exportação

`dist/central-de-tarefas.html` funciona como central independente. Sem clicar em Compartilhar, continua local; o botão gera uma central online e o respectivo link. A exportação de uma central que já está conectada mantém a conexão, desde que haja internet. A exportação de uma central local preserva o comportamento local.

Na prévia contextualizada do Notion, as tarefas e o design são uma cópia: editar essa prévia não publica alterações. Para compartilhar, use o componente real no canvas ou a central online.

## Implementação e testes

`src/task-layout.js` mantém o modelo de personalização, a validação e os controles de organização. `src/task-sharing.js` mantém o cliente de sincronização, status, link e recuperação de conflitos. O renderer e o modelo de tarefas continuam em `src/taskhub.js`. A interação por ponteiro permite mover as seções sem depender do arraste nativo de HTML; as setas oferecem alternativa acessível.

A fonte do serviço está em `/workspace/sites/wa-central-compartilhada`, com API Worker, migrações D1 e cópia versionada do motor da central. O serviço foi publicado com o plugin Sites. O helper local do plugin não estava instalado; o código foi enviado ao repositório do Site por Git autenticado em memória, e o artefato foi validado e publicado pelos comandos nativos do Sites. O acesso público foi configurado conforme a escolha de abrir por link sem login. O navegador gerenciado do Sites não estava disponível: a verificação do serviço publicado foi feita por HTTP e pela API, sem alegar verificação visual no Site hospedado.

Verificações adicionais: organização interna, exportação e responsividade em navegador no editor local; dois contextos de navegador isolados usando a API real com SQLite de teste; teste da API publicada com dois clientes, combinação de alterações e conflito; 15 cenários de regressão do editor anterior.
