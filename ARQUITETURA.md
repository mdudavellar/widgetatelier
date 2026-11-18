# Mapa do código existente

O editor é uma aplicação de HTML/CSS/JavaScript sem framework. `source/ui/build.py` concatena os módulos e recursos em um HTML independente. A ordem de montagem está nesse script; os módulos compartilham o mesmo escopo, portanto não devem ser convertidos isoladamente em imports sem avaliar suas dependências.

## Editor: source/ui/src

| Área | Arquivos principais |
| --- | --- |
| Estrutura visual e estado | shell.html, style.css, app.js, runtime.js, engine.js |
| Texto e fontes | text.js, text-layout.js, fonts.js, font-metadata.js, catalog-fonts.js |
| Biblioteca e ícones | assets.js, library.js, catalog-ui.js, icon-elements.js, icons.js, image-import.js |
| Seleção e geometria | canvas-selection.js, selection-geometry.js, scaling.js, composition-fit.js |
| Partes editáveis e grupos | component-parts.js, part-editor.js, component-builder.js, composition-groups.js, group-library.js, element-clipboard.js |
| Controles | context-toolbar.js, element-context.js, movable-menus.js, color-picker.js, numeric-sliders.js, studio-tools.js |
| Dinâmicos | dynamic.js, widgets.js, clocks.js, clock-parts.js, calendars.js, calendar-events.js, legend.js, legend-editor.js |
| Navegação | navigation.js, navigation-editor.js |
| Animação e horário | animations.js, automations.js, time-rules.js |
| Templates e formas | templates.js, shapes.js, stickers.js, more-art.js |
| Notion e exportação | device-preview.js, embed-layout.js, exporter.js, publishing.js |
| Central de tarefas | taskhub.js, taskhub.css, task-layout.js, task-sharing.js |

## Servidor

`source/build.cjs` monta `source/dist/server/index.js`, incluindo o editor, assets e módulos do backend. O exportador local utiliza a saída atualizada de `ui/build.py`, sem editar o script original.

- `worker/api.js`: central de tarefas, autenticação por chave, revisões e resolução de conflitos.
- `worker/widgets.js`: criar/atualizar publicação, servir `/w/:id`, `/w/:id/content`, descoberta oEmbed e dimensões declaradas.
- `worker/catalog.js`: catálogo de fontes, provedores externos de fontes/ícones e caches.
- `worker/boot.js`: inicialização/roteamento compartilhado.
- `worker/rendering-compat.js`: compatibilidade de widgets publicados em versões anteriores do renderizador.

## Persistência

O navegador mantém projetos e preferências em localStorage; fontes e grupos pessoais usam IndexedDB, com os fallbacks implementados nos módulos correspondentes. A origem do navegador delimita esses dados: localhost não enxerga automaticamente os dados do domínio publicado.

D1 armazena `task_boards`, `creation_limits` e `published_widgets`; as migrações originais estão em `source/drizzle`. R2 guarda o HTML publicado e seus metadados. Para o ambiente local, `tools/local-bindings.cjs` implementa somente as operações desses contratos efetivamente usadas pelos fontes atuais. Não é um emulador completo do Cloudflare.

## Ciclo local

1. Copia os inputs para .local-build/editor-input, acrescenta o fonts.json completo da cópia de trabalho e executa o builder Python original.
2. O builder original monta o Worker usando esse editor, com adaptação em memória do caminho do HTML.
3. A origem pública fixa é substituída apenas na saída gerada; o resultado fica em .local-build/worker.mjs.
4. O servidor Node adapta HTTP para Request/Response e injeta DB/BUCKET locais.

As pastas source/dist, source/ui/dist, .local-build, .local-data e .local-tests são geradas e não precisam entrar no controle de versão.
