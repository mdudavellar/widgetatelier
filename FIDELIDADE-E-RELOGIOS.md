# Texto fiel à composição e relógios com layouts diferentes

Esta atualização mantém o editor em `/atelier` e os links de widgets já publicados em `/w/<id>`.

## Texto no editor e no Notion

As caixas de texto agora usam o mesmo contêiner de recorte no editor, na prévia e na publicação. Selecionar um objeto pode mostrar suas alças, mas não libera texto para transbordar de uma caixa que será recortada no widget. A ampliação automática de texto do navegador móvel é desativada para a composição, mantendo a escala proporcional do projeto. A publicação aguarda as fontes utilizadas antes de revelar o conteúdo.

Textos dinâmicos reduzem a fonte somente quando a mensagem não cabe na caixa; o tamanho escolhido continua sendo o máximo. Em **Texto na caixa**, escolha entre **Reduzir a fonte para caber** e **Manter tamanho fixo**. Textos comuns permanecem no modo fixo por padrão. Essa regra não move elementos nem altera as coordenadas, dimensões e tipografia salvas.

No caso reportado, a fonte Raleway a 49 px permite as quatro saudações em duas linhas dentro da caixa original, sem reduzir o tamanho escolhido. A medição com a fonte incorporada mostrou que uma ampliação de 20% produz a terceira linha observada na captura. O ajuste de escala de texto e o carregamento da fonte são padronizados nos dois ambientes; a captura, isoladamente, não identifica todas as configurações do navegador do dispositivo.

Os widgets antigos recebem a atualização de renderização ao serem servidos. O HTML armazenado e os dados do projeto não são regravados: o serviço aplica uma camada de compatibilidade à resposta. Assim, o link e a revisão de publicação existentes permanecem válidos. Recarregue a página/bloco do Notion para buscar a resposta corrigida. Novas publicações usam diretamente o renderer atualizado.

O modo responsivo aplica uma única escala uniforme considerando tanto a largura quanto a altura disponíveis. A arte inteira cabe no bloco sem alterar a relação entre seus elementos. O modo fixo preserva o tamanho original e pode exigir um bloco maior. A página ao redor e os controles externos do Notion continuam pertencendo ao Notion.

## Nove composições de relógio

- **Digital suave:** horário em linha e segundos em um contador separado.
- **Minimal:** horas e minutos separados por uma barra diagonal, com uma linha que acompanha o percurso do dia.
- **Editorial:** selo de dia/mês, divisor e hierarquia de horário local.
- **Flip retrô:** placas, divisórias e rótulos de unidade; animação dos números quando mudam, respeitando movimento reduzido.
- **Vertical:** horas e minutos empilhados, divisória e rótulos verticais.
- **Analógico leve:** mostrador circular limpo, marcações e números nos quartos.
- **Romano:** caixa quadrada arredondada, algarismos romanos e submostrador de segundos.
- **Órbita:** horário dentro de um anel que acompanha o percurso do dia.
- **Barras:** valores e barras reais de horas, minutos e segundos.

As miniaturas são geradas pelo mesmo renderer dos modelos, com horário de amostra, em vez de trocar a fonte de um desenho genérico. Os modelos continuam usando o fuso, idioma, formato 12/24 horas e opção de segundos do projeto. A legenda de data mantém seus controles de fonte, tamanho, cor, opacidade, alinhamento, posição, dimensões e rotação. Trocar o modelo preserva esses ajustes e as cores de fundo. O tamanho do horário se adapta ao espaço disponível, sem alterar a fonte máxima salva. Diagramas, placas e divisórias são originais do WA.

Para mudar um relógio no seu widget: atualize o Atelier, selecione o relógio e escolha o modelo. Depois clique em **Publicar e copiar link** para atualizar o mesmo endereço incorporado no Notion.

## Verificações e limites

Foram verificados: nove estruturas DOM distintas, valores reais do relógio, ponteiros e submostrador, barras e anel, virada de data por fuso, 12 horas, segundos, visibilidade da data, preservação de preferências ao trocar modelos e miniaturas. Também foram verificados ajuste de texto e cache, objetos ocultos e ainda não montados, espera de fontes, sintaxe e idempotência da compatibilidade e preservação dos dados do widget reportado. O HTML real reportado foi executado em um DOM de teste para verificar a estrutura atualizada. A fonte incorporada foi usada na medição das quatro saudações. API de publicação e API de tarefas passaram pelos testes de regressão.

O DOM de teste e as medições não são uma verificação visual de pixels. O navegador gerenciado não estava disponível nesta execução; não foi realizado teste visual dentro do Notion real nem no dispositivo da usuária. A publicação e a resposta HTTP do link reportado são verificadas separadamente.
