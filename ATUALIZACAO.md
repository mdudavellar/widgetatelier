# Atualização: controles, fontes e componentes dinâmicos

Este documento registra a segunda entrega. A versão atual amplia a biblioteca para 56 fontes e adiciona relógios, edição da data e seletor RGB; veja `RELOGIOS-CORES-FONTES.md`.

Abra `dist/widget-atelier.html`. A composição anterior e os projetos v3 continuam compatíveis. A distribuição anterior também foi preservada em `dist/widget-atelier-anterior.html`.

## Controles solicitados

- Barras deslizantes com leitura do valor para ângulo do degradê, arredondamento, opacidade, rotação, entreletras e entrelinhas. Funcionam com mouse, toque e setas do teclado. As alterações são vistas durante o ajuste e entram no histórico ao concluir o movimento.
- Botões **− / +** em cada lado do tamanho da fonte, mantendo a entrada numérica.
- Menu flutuante acima do objeto selecionado, acompanhando movimento, escala e rolagem. Ícones dão acesso a edição, posição, fonte, negrito, itálico, sublinhado, cor/opacidade, alinhamentos, rotação, animação, duplicação, bloqueio e exclusão, conforme o tipo do objeto.
- O botão **+** abre todos os controles em um painel flutuante, incluindo camadas, distribuição e ajustes específicos de calendário/contagem. Os campos desse painel e do inspetor lateral editam o mesmo estado.
- O menu se adapta à seleção múltipla e ao bloqueio. Em telas estreitas, os ícones têm rolagem horizontal e o **+** permanece acessível. Esses controles não aparecem na exportação.

## Biblioteca de elementos

Agora são **64 vetores originais**, oito por categoria. Foram acrescentadas variações de line art, formas, estrelas, botânicos, ornamentos, retrô e texturas. Cada item aceita cor, traço, dimensões, rotação e opacidade. Os IDs dos 16 elementos da entrega anterior foram preservados para manter os projetos compatíveis.

## Calendário

Em **Dinâmicos → Calendário mensal**, adicione um componente independente. Ele acompanha mês e dia no fuso do projeto, com idioma compartilhado com o relógio, início da semana em segunda/domingo, destaque opcional do dia atual e deslocamento de mês. O calendário considera meses de durações diferentes e anos bissextos. O deslocamento é relativo ao mês atual; não é uma agenda de compromissos, nem uma sincronização com Google Calendar/Notion.

## Contagem regressiva

Em **Dinâmicos → Contagem regressiva**, adicione quantas instâncias precisar. Cada uma tem nome, prazo e mensagem de encerramento próprios.

Formatos: cartões de dias/horas/minutos/segundos, compacto, relógio de horas totais e dias restantes. O prazo é selecionado no calendário nativo do navegador, no fuso do dispositivo mostrado no painel, e salvo como um instante ISO absoluto. Assim, o mesmo prazo representa o mesmo momento em outros dispositivos. O fuso do calendário/relógio do projeto não altera esse instante. A contagem atualiza a cada segundo e, depois do prazo, exibe a mensagem escolhida, sem valores negativos.

## Animação de entrada de texto

Textos livres e textos dinâmicos aceitam escrita letra a letra, desfoque, fade e subida, além de duração de 0,2 a 10 segundos e atraso de 0 a 10 segundos. O botão **Testar animação** reproduz o efeito no editor. A prévia Notion também executa as animações.

O HTML exportado inicia a animação ao carregar; abrir ou recarregar o embed reproduz o efeito de novo. O relógio e as saudações continuam atualizando sem reiniciar o efeito a cada segundo. Quebras de linha são preservadas. A preferência de movimento reduzido do dispositivo mostra o texto completo sem animação. Se o Notion reutilizar um iframe sem recarregá-lo, o efeito não reinicia apenas por alternar entre páginas; ele depende do carregamento real do widget.

## Fontes das imagens

As imagens foram analisadas pelos nomes legíveis nas legendas; uma imagem não contém o arquivo da fonte e as amostras visuais nem sempre correspondem à família escrita na legenda.

**24 famílias incorporadas:** DM Sans, Playfair Display, Fraunces, Nunito, Libre Baskerville, Cormorant Garamond, Montserrat, Quicksand, DM Serif Display, Bodoni Moda, Space Grotesk, Syne, Caveat, Raleway, League Spartan, Poppins, Lato, Great Vibes, Anton, Josefin Sans, Lora, Averia Sans Libre, EB Garamond e GFS Didot.

As famílias identificáveis e abertas das imagens foram incorporadas com seus avisos SIL OFL. Foram adicionadas faces/intervalos que permitem Montserrat Light, Raleway Italic, Poppins Light/Extra Light e outros pesos disponíveis. EB Garamond é uma alternativa explicitamente nomeada para a referência genérica “Garamond”; GFS Didot é uma alternativa aberta para “Didot”. Bodoni Moda é uma alternativa, não a mesma família que Bodoni FLF.

**Referências que aguardam arquivo/licença ou identificação exata:** Lumière, Amalfi, Velora, Soleil, Aura, Bellevue, Radiant, Chérie, Lys, Fleur, Noir, Éclat, Vanity, Blush, Précieuse, Nova, Solara, Vélo, Orion, Atlas, Kairos, Talon, Zephyr, Everlane, ITC Avant Garde, Quiche Sans, Bodoni FLF, Didot, TAN Nimbus, Garamond, Rosie Brown Serif, Soligant e NewYork.

Esses nomes estão catalogados em **Texto → Fontes das suas referências**, com o estado “Carregar arquivo”, e não como fontes instaladas. Para ativar uma delas, carregue seu arquivo WOFF2, WOFF, TTF ou OTF com permissão de incorporação. O editor valida o arquivo, permite informar nome, peso e estilo, e inclui os dados no projeto e no HTML exportado. Cada projeto aceita até 20 arquivos, até 1 MB por arquivo e 10 MB de dados de fontes. Projetos JSON têm limite de 15 MB. Falhas de armazenamento local continuam sendo sinalizadas; baixe o projeto para não depender da quota do navegador.

Fontes comerciais não foram baixadas de repositórios não autorizados nem renomeadas a partir de alternativas abertas. Algumas fontes têm homônimos; só os arquivos originais permitem confirmar o desenho exato. O nome da quarta imagem, inicialmente lido como “Rose Brown”, foi relacionado à família **Rosie Brown Serif**, de Letterhend, cuja distribuição demo não substitui uma licença comercial/web.

Fontes consultadas:

- [Rosie Brown, Letterhend Studio](https://www.letterhend.com/product/rosie-brown-font-duo/)
- [ITC Avant Garde Gothic, licenças MyFonts](https://www.myfonts.com/collections/itc-avant-garde-gothic-font-paratype?tab=licensing)
- [Catálogo Google Fonts](https://fonts.google.com/)
- [Arquivos e licenças oficiais Google Fonts](https://github.com/google/fonts/tree/main/ofl)

## Validação desta atualização

Os 17 cenários de integração existentes continuam aprovados, junto aos testes de precisão. Outros **13 cenários** verificam sliders, menu flutuante, sincronização, fonte +/−, 64 vetores, calendário/fuso/ano bissexto, quatro formatos e atualização da contagem, animações e replay, fontes abertas/arquivos próprios, persistência e exportação, movimento reduzido e mobile. Veja `tests/updates-results.json` e `tests/updates.cjs`.
