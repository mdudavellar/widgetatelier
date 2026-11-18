# Análise do código original e refatoração

## Diagnóstico anterior à implementação

O HTML v2 contém uma interface, uma única folha de estilo e um script com estado global. O modelo fixa os IDs `title`, `greeting`, `motivation`, `clock` e `decor`. Posições são percentuais; o tamanho dos objetos não participa das restrições de arraste. Texto é atualizado com `textContent`, sem edição direta. A exportação clona o widget e copia toda a folha de estilo da aplicação, além de manter um segundo script de relógio/saudação separado do utilizado pela prévia.

São recursos existentes que precisam continuar: mensagens por quatro períodos com `{name}`, nome/etiqueta, simulação de horário, fuso e idioma da data, 12/24 horas, segundos/data opcionais, nove famílias de fontes, pesos/itálico/caixa alta/visibilidade, arraste, símbolos decorativos legados, cinco cores, degradê e ângulo, raio, quatro paletas, salvamento local, restauração e download de HTML.

Refatorações necessárias: um modelo de objetos extensível; dimensões e estilos por objeto; renderização compartilhada com exportação; histórico de alterações; separação entre dados de templates, arte e lógica temporal; interface que exponha camadas e coordenadas; migração do formato v2 em vez de apagar dados antigos.

## Implementação resultante

| Módulo | Responsabilidade |
| --- | --- |
| `src/templates.js` | Composição inicial e ponto de expansão do sistema de templates. |
| `src/engine.js` | Modelo normalizado, migração v2, dimensões, renderização, escala, limites rotacionados e histórico. |
| `src/library.js` | Catálogo de 16 vetores originais, categorias e SVGs editáveis. |
| `src/text.js` | Renderização segura de blocos de texto, sem interpretar HTML do conteúdo. |
| `src/dynamic.js` | Períodos, personalização e atualização de todos os componentes dinâmicos, sem depender do editor. |
| `src/runtime.js` | Montagem e redimensionamento do widget exportado, com o mesmo motor da prévia. |
| `src/exporter.js` | HTML independente, fontes utilizadas, licenças e configuração segura; exclui guias. |
| `src/app.js` | Interface, seleção, gestos, snap, guias, camadas, tipografia, projetos e prévia Notion. |
| `src/style.css` / `src/shell.html` | Interface do editor; não são copiados para o widget exportado. |
| `build.py` | Empacotamento local de módulos/fontes em um HTML único. |

O modelo passa a usar um array ordenado de objetos com IDs próprios. Tipos iniciais: texto livre, gráfico vetorial, texto dinâmico e relógio. Dimensões e coordenadas são pixels na composição de referência; a visualização aplica uma escala externa. As instâncias de componentes dinâmicos são independentes em posição, dimensões e estilo, compartilhando as configurações de horário e mensagens do projeto.

O histórico agrupa cada gesto de arraste/redimensionamento em uma operação. Cancelar um gesto restaura o estado anterior. Guias e edição são ferramentas do editor. O exportador reconstrói a composição a partir dos dados e inclui apenas a implementação necessária do motor e componentes, sem a interface do editor.

## Etapas executadas

1. Preservação do HTML recebido e análise de estado, funções, persistência e exportação.
2. Modelo extensível, migração, renderizador e biblioteca original.
3. Múltiplos textos, edição direta e controles por objeto.
4. Histórico, camadas, bloqueio, guias, margens, grade, snap e alinhamentos.
5. Prévia Notion com layouts e diagnósticos, exportação com fontes incorporadas.
6. Testes no navegador; correções nos gestos de edição, proteção da edição dinâmica durante ticks e cálculo imediato das larguras da prévia.

A formatação de trechos individuais foi deixada fora desta implementação para manter um modelo de texto simples e exportável. Não foi incluído conteúdo proprietário ou um importador de fontes sem verificação de licença. Os demais limites e próximos passos estão em `LEIA-ME.md`.

## Segunda entrega

`src/animations.js` gerencia animações de entrada sem interferir nos ticks de componentes dinâmicos. `src/automations.js` isola calendário e contagem regressiva. `src/fonts.js` valida/incorpora fontes próprias e registra as referências ainda sem arquivo confirmado. `src/icons.js` fornece os ícones vetoriais da interface; `src/more-art.js` amplia a biblioteca sem alterar os IDs antigos. O menu flutuante usa o mesmo modelo e eventos do inspetor. A exportação continua compartilhando o motor e inclui os novos componentes/animações, fontes usadas e suas licenças.

## Terceira entrega

`src/clocks.js` reúne modelos de relógio, formatação, renderização, data com estilo próprio e cálculo de ponteiros. `src/color-picker.js` isola roda HSV/RGB, alfa, HEX e paletas do editor. O estado dos relógios antigos é normalizado para herdar o cartão da composição e manter a data em 12 px/opacidade 0,72. Cores próprias e data passam a pertencer a cada instância. O exportador inclui as fontes da data, além das fontes dos objetos. Paletas e interface do seletor são excluídas da exportação. O registro de fontes é gerado pelo build a partir dos ativos efetivamente incluídos.

## Quarta entrega

`src/assets.js` renderiza arquivos raster incorporados e valida o registro de mídia. `src/image-import.js` separa leitura local/URL, assinatura de formato, limites de dimensões e inspeção de alfa. `src/scaling.js` isola proporção de caixas, escala global e formato de canvas. Objetos `image` referenciam arquivos por `assetId`; duplicar uma imagem não duplica os dados. O importador do projeto verifica novamente as imagens antes de trocar o estado atual. O exportador seleciona os arquivos usados e exclui links de referência para não depender de solicitações remotas.

## Estúdio e menus móveis

`src/stickers.js` adiciona uma galeria original incorporada. `src/calendars.js` separa modelos e cálculos de calendários. `src/widgets.js` reúne os novos componentes, ações e persistência opcional no navegador. `src/movable-menus.js` controla posições livres dos painéis, separadas do desenho. As alças são criadas por uma única função do motor e omitidas no runtime exportado. A prévia usa uma cópia profunda para suas interações. Os sete relógios existentes foram preservados; não houve ampliação dos modelos nesta rodada por bloqueio da ferramenta.
