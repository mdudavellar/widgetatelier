# Galeria interna, calendários, componentes e menus móveis

Esta é a versão atual do Widget Atelier. Abra `dist/widget-atelier.html`. Para continuar um trabalho de outro arquivo/navegador, abra o JSON do projeto anterior.

## Menus que você pode mover

A barra flutuante, o painel de opções e o seletor de cores podem ser arrastados para qualquer área visível da janela.

- **Barra flutuante:** arraste pelo ícone de pontos à esquerda.
- **Opções detalhadas:** arraste pelo título do painel.
- **Seletor de cores:** arraste pelo cabeçalho.
- O botão com seta circular de cada menu restaura a **posição automática**.
- A posição escolhida é mantida durante alterações, seleção de outros objetos e reabertura do menu na sessão. Não é gravada no desenho nem na exportação. Recarregar o editor redefine essas posições.
- A barra também pode ser movida pelo teclado ao focar o ícone de arraste: setas movem 10 px; Shift + setas, 1 px.

Os painéis são limitados à janela para manter os controles acessíveis. Se o conteúdo ficar maior ou a janela for reduzida, a posição pode ser ajustada para que o menu continue visível. Os controles dentro do painel permanecem utilizáveis sem iniciar o arraste.

## Elementos disponíveis dentro do editor

A área de busca externa foi removida. **Elementos** agora tem:

- **Galeria:** 32 adesivos vetoriais originais e incorporados, com busca e categorias Natureza, Celestial, Objetos e Ornamentos.
- **Vetores:** os 64 elementos anteriores, organizados em oito categorias.
- **Minhas imagens:** importação e biblioteca dos seus PNGs/WebPs, preservadas.

São **96 desenhos disponíveis** sem acessar outro site. Clique em uma prévia para adicionar. Os novos desenhos incluem botânicos, flores, sol/lua/estrelas, arco-íris, nuvem, café, livro, envelope, fone, vela, lápis, câmera, cassete, laço, etiquetas, molduras e recortes editoriais. São desenhos próprios, não ativos extraídos do Pinterest ou do Canva. Aceitam posição, dimensões, cor, opacidade, rotação e espessura de traço quando pertinente ao desenho.

Projetos antigos continuam reconhecendo os IDs dos vetores e as imagens já importadas. Links de referência fornecidos pelo usuário são preservados com suas imagens; a galeria não faz buscas externas.

## Quatro cantos e rotação no canvas

Todo objeto selecionado e desbloqueado tem **quatro alças de canto**. Arraste para aumentar ou diminuir sua caixa. O canto oposto permanece ancorado, inclusive quando o objeto já está rotacionado.

- **Manter proporção** conserva a relação largura/altura; também é possível usar Shift durante o redimensionamento.
- Caixas de texto redimensionam sem alterar automaticamente o tamanho da fonte. O texto quebra conforme a nova largura.
- A **alça circular de rotação**, conectada à seleção, gira o objeto diretamente. Shift encaixa o ângulo em incrementos de 15°.
- Como alternativa, **Alt + arraste em qualquer canto** gira sem mudar as dimensões.
- As alças mantêm tamanho de interação estável quando o zoom muda. Objetos bloqueados não exibem essas alças.
- Cada gesto completo corresponde a uma operação de Desfazer; cancelar o ponteiro restaura o estado anterior.

Os contornos, alças e menus são ferramentas do editor e não aparecem no HTML exportado.

## Fundo transparente do widget

Em **Composição → Cores e fundo**, ative **Fundo do widget transparente**. A opção prevalece sobre o fundo sólido/degradê e preserva suas cores para uso posterior. O xadrez aparece apenas no editor para indicar transparência; a exportação usa um fundo transparente real.

Cartões de relógio, calendário e outros componentes mantêm seus próprios fundos. Para deixá-los transparentes também, selecione cada componente e escolha **Transparente** em seu tipo de fundo.

## Seis modelos de calendário

Em **Dinâmicos → Calendários**, escolha:

1. Mensal suave.
2. Mensal minimal.
3. Mensal editorial.
4. Semana horizontal.
5. Folha do dia.
6. Agenda semanal.

O modelo pode ser alterado pelo painel do componente existente. As opções incluem fonte, tamanho, cores, fundo próprio/transparente, raio e respiro do cartão, início da semana, dia atual, título, visibilidade do cabeçalho/dias da semana, tamanho relativo do cabeçalho e dos dias, espaço e arredondamento de células nos modelos aplicáveis, cor dos finais de semana e cores do destaque.

As setas permitem navegar pelos meses, semanas ou dias conforme o modelo. O deslocamento do período também é ajustável numericamente. Os cálculos usam o fuso e idioma do projeto e consideram anos bissextos.

A agenda aceita sete notas próprias, uma por linha, para as posições dos dias da semana. Não é uma integração com Google Calendar, Outlook ou calendário do Notion. Ao mudar de semana, as notas continuam nas mesmas posições; servem como um plano semanal recorrente/editável.

## Mais seis componentes para criar widgets

### Progresso

Acompanhe o dia, a semana, o mês ou o ano no fuso do projeto, ou configure o percentual de uma meta manual. Há barra, anel e pontos, título próprio, percentual opcional e cores de progresso/trilha. Os períodos temporais atualizam automaticamente.

### Contador

Rótulo, valor inicial/atual, passo, valores negativos opcionais e botões para diminuir, aumentar e recomeçar. O valor pode ser testado no editor e usado no HTML exportado.

### Checklist

Uma lista editável, com um item por linha. As caixas podem ser marcadas no canvas e no widget exportado. Alterar o texto da lista redefine as marcações para evitar associá-las aos itens errados.

### Hábitos

Uma linha de sete dias acompanha a semana atual, com nome próprio e início da semana configurável. Clique nos dias para marcar/desmarcar. As datas, não só as posições, identificam cada marcação.

### Frases

Cadastre uma frase por linha, com autoria opcional separada por ` | `. Escolha alternância diária ou uma escolha aleatória por carregamento. O conteúdo permanece estável durante os ticks do relógio; a opção aleatória pode repetir uma frase em aberturas consecutivas.

### Botão de link

Texto, endereço HTTP/HTTPS e estilos preenchido, contorno ou suave. No canvas, o clique seleciona o componente. Use **Testar link** no painel, a prévia ou o widget exportado para abrir o endereço em outra aba.

Todos esses componentes têm tipografia, tamanho, posição, opacidade, rotação e aparência editáveis. Os fundos dos componentes podem seguir o cartão da composição, usar cor própria ou ser transparentes.

## Marcação e persistência

No editor, alterações nos componentes entram no histórico e no projeto JSON. Na prévia Notion, as interações usam uma cópia: testar um contador ou checklist não modifica o projeto.

No HTML exportado, contador, checklist e hábitos tentam guardar as alterações no navegador e na origem de hospedagem daquele widget. Não há sincronização em nuvem, entre navegadores ou dispositivos. Se o navegador/iframe impedir o armazenamento, o componente continua funcionando na sessão e mostra que as alterações são temporárias. Os calendários navegam no período durante a sessão; reabrir o arquivo inicia no deslocamento configurado no projeto.

## Relógios

Os sete modelos anteriores e seus controles foram preservados. A ampliação de modelos de relógio não foi entregue nesta rodada: uma tentativa de alteração foi bloqueada por um filtro da ferramenta, sem um motivo específico disponível. Nenhum novo modelo foi apresentado como implementado. Os controles existentes de fontes, cores, data, transparência, tamanho e rotação continuam disponíveis.

## Validação

`tests/studio-v6.cjs` verifica galeria interna e pesquisa, arraste/reset dos três menus e estabilidade após edição, quatro cantos, rotação por alça/Alt e precisão em diferentes zooms, transparência real, seis calendários e personalização/navegação, ano bissexto e períodos, seis componentes, persistência, isolamento da prévia, links válidos, abertura de projetos, exportação sem ferramentas de edição e menus em mobile. Também força indisponibilidade do armazenamento para verificar o contador funcional e a mensagem de sessão temporária.

`tests/integration.cjs` e `tests/precision.cjs` verificam os recursos anteriores preservados. Arquivos de testes e guias de entregas antigas podem documentar interfaces que foram substituídas; o guia presente e o conjunto de testes acima descrevem a versão atual.
