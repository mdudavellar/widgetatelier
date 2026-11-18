# Atelier online, links prontos e tamanho do projeto

O editor completo está em:

https://wa-central-compartilhada.snappykookaburra.chatgpt.site/atelier

A central compartilhada existente e seus links continuam funcionando no mesmo serviço.

## Colocar qualquer composição no Notion

1. Abra um projeto no Atelier online.
2. Clique em **Publicar e copiar link**, no topo.
3. No Notion, use `/embed`, cole o link e escolha **Incorporar**.

Não é preciso baixar o HTML nem contratar/configurar outra hospedagem. O diálogo mantém o link visível e oferece **Copiar link** e **Abrir widget** caso o navegador não permita copiar automaticamente.

Publicar novamente na mesma aba atualiza o widget no mesmo endereço. O Notion pode precisar recarregar o bloco para mostrar a versão mais recente. O link mostra a composição publicada; edições locais do design só aparecem depois de publicar novamente.

Uma central de tarefas visível na composição é conectada à base compartilhada antes da publicação. As tarefas continuam sincronizando independentemente da publicação do design. Se houver conflito ou falha de sincronização, a publicação é interrompida e o projeto é preservado.

Quem tiver o link poderá visualizar o widget. As tarefas compartilhadas mantêm a permissão de edição por link escolhida anteriormente. A permissão de substituir a composição publicada fica guardada no projeto do editor; não é incluída no HTML público do widget.

Baixe o JSON editável em **Projeto → Baixar projeto** para guardar a composição e sua permissão de atualização. Guarde esse arquivo como um projeto editável: ele pode incluir credenciais de edição daquela publicação e das centrais compartilhadas. Ao abrir esse JSON em outro navegador, a publicação pode continuar no mesmo link. Se duas cópias publicarem versões divergentes, o serviço impede a substituição silenciosa por uma versão desatualizada.

O editor salva projetos no navegador, por origem. Para migrar do arquivo antigo para o editor online, baixe o JSON no antigo e use **Projeto → Abrir projeto** no online. Não há migração automática entre origens diferentes do navegador.

## Alterar o tamanho do projeto

Clique no botão com as medidas, acima do canvas. No diálogo **Redimensionar projeto**, defina largura e altura e clique em **Aplicar tamanho**.

- **Alterar somente a área do projeto:** mantém os objetos nas posições e dimensões atuais. Uma área menor pode cortar elementos; os avisos de limites continuam disponíveis.
- **Redimensionar toda a arte proporcionalmente:** muda a área e os objetos juntos, mantendo a proporção. Os limites dos elementos podem reduzir o tamanho efetivamente aplicado; o resultado é informado.
- **Manter proporção:** vincula largura e altura. Pode ser desativado ao alterar somente a área.

Também é possível arrastar as alças externas da borda direita, inferior e do canto inferior direito do projeto. Shift mantém a proporção durante o arraste. Esses controles ficam fora dos elementos e não são exportados. As medidas da barra superior mostram o tamanho real em pixels; **Ajustar** é apenas o enquadramento do zoom. Durante o arraste, o zoom fica estável para a borda acompanhar o ponteiro.

Os campos de largura e altura do painel de composição aplicam o valor ao terminar a edição, sem redimensionar a cada dígito digitado. Desfazer e refazer preservam as mudanças de tamanho. Limites atuais: 200–2400 px de largura e 150–2000 px de altura.

## Implementação e verificações

A API publica o HTML em R2 e mantém metadados e controle de revisão no D1. O endereço de visualização `/w/<id>` permanece estável. Atualizar exige a chave de edição, e revisões divergentes são rejeitadas. O conteúdo do widget é servido em um iframe com origem isolada, inclusive quando a rota de conteúdo é aberta diretamente. Isso separa o HTML publicado do armazenamento do editor. O HTML público inclui fontes e imagens utilizadas e não inclui a chave que permite substituir a publicação.

A migração `0002_published_widgets.sql` adiciona a tabela de publicações sem modificar as migrações já aplicadas das tarefas. A conexão de armazenamento é declarada no manifesto do Site. O editor permanece em `/atelier`; a central anterior permanece em `/`.

Testes específicos: API de publicação com SQLite/R2 de teste; criação, atualização estável, autenticação, conflito de revisão, retenção limitada de versões e isolamento do conteúdo; fluxo do editor com redimensionamento atômico, escala de toda a arte, arraste da borda, desfazer, digitação numérica, clipboard, recarregamento, backup com edição e conexão automática de tarefas. Os 15 cenários atuais de regressão do estúdio passaram. A suíte histórica `images-scaling.cjs` não pôde ser executada integralmente porque ainda referencia a aba Pinterest removida anteriormente a pedido da usuária; os testes atuais de galeria e os específicos de redimensionamento cobrem esses fluxos presentes.

O navegador gerenciado do Sites não estava disponível. A publicação e as rotas públicas são verificadas pelo serviço e por HTTP; a interação do editor foi testada na cópia local com API de teste, sem alegar teste visual dentro da página real do Notion.
