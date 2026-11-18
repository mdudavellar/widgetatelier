# Edição interna de todos os componentes

Todos os elementos do canvas oferecem **Desagrupar para edição**. O modo permite selecionar partes no canvas, no seletor do painel ou na lista de Camadas; mover, escalar pelos quatro cantos, rotacionar, ocultar, alterar tipografia, cores, fundos e traços de vetores. Concluir edição limpa a seleção, mantendo as partes liberadas para o próximo clique. Use Testar interações para os controles nativos ou Agrupar novamente para mover o conjunto. Imagens rasterizadas continuam imagens únicas; o editor não reconstrói objetos dentro dos pixels de uma fotografia.

A estrutura lógica do componente permanece vinculada: não é uma conversão em textos estáticos nem uma separação definitiva em objetos de primeiro nível. Posições e estilos internos são registrados em `partEdits`, por modelo e caminho de parte, e reaplicados após os dados atualizarem. Tarefas recebem âncoras por ID para que uma personalização não passe a outra tarefa quando a ordem muda. Fundos viram camadas visuais próprias. Ponteiros mantêm as rotações calculadas pelo relógio. Cores das partes usam o seletor RGB/HEX, cores salvas e recentes existente.

Editar um conteúdo automático oferece uma substituição explícita de texto; limpar essa substituição restaura o conteúdo automático. Os dados de calendário, contagem e central continuam sendo configurados nos controles do componente. Formulários temporários da central não entram no inventário da composição.

## Correção das legendas do relógio vertical

A conversão anterior criava os blocos com `textFit: shrink`, mesmo para caixas extremamente estreitas. Os textos livres convertidos usam tamanho fixo e não quebram cada caractere numa nova linha. Ao alterar sua tipografia no editor, a caixa cresce para comportar o texto. A normalização reconhece as unidades de relógio e as legendas HORAS/MINUTOS antigas, retirando a redução automática sem substituir textos e posições. A fonte e o peso de cada parte podem ser alterados independentemente.

## Persistência e exportação

As edições integram o estado do projeto, salvamento local, desfazer/refazer, JSON editável e HTML publicado. Fontes importadas usadas somente numa parte interna também são incluídas no projeto e na publicação. Não são incluídos os controles de edição no HTML exportado.

## Verificação

Testes com uma implementação real de DOM (LinkeDOM) e geometria determinística: inicialização do editor completo, eventos reais dos controles, legado de legenda 8→36 px e peso 900, ampliação da caixa, persistência e execução do HTML exportado; 31 variantes de modelos/tipos; transformações sem acumulação; continuidade dos ponteiros; preservação da identidade das tarefas; fundos após redesenho; validação de dados; checklist, navegação do calendário e conclusão de tarefas após edições. As regressões de fontes, relógios, publicação e central compartilhada também passaram.

Esses testes não medem pixels nem são testes dentro do Notion real. O ambiente não oferece `cua_repl.js`; a instrução do Sites impede iniciar um navegador alternativo nesse caso. O comportamento visual final no dispositivo da usuária continua sem essa verificação.
