# Pinterest, imagens transparentes e proporção da arte

## O que foi adicionado

Em **Elementos**, há três abas: **Vetores**, **Pinterest / PNG** e **Minhas imagens**. A biblioteca vetorial anterior continua disponível.

### Buscar no Pinterest

Digite o assunto e clique em **Buscar no Pinterest**. O WA abre uma busca no Pinterest em uma nova aba, acrescentando “png transparente” ao termo. Há sugestões rápidas de botânicos, sparkles e vintage.

**Essa busca é externa. Não há uma galeria de resultados do Pinterest dentro do WA nem uma conexão com a conta do Pinterest.** A busca não garante que um resultado seja um PNG com alfa real ou que sua licença permita o uso. A miniatura pode ter branco/xadrez desenhado no próprio arquivo.

Para utilizar uma imagem, baixe o PNG/WebP disponibilizado pelo autor ou na fonte original e volte ao editor. O Pinterest pode exigir login e pode disponibilizar um arquivo opaco/JPG mesmo quando o pin menciona “PNG”. O WA não transforma uma captura de tela em transparência nem remove o fundo automaticamente.

Uma integração com resultados autenticados dentro do aplicativo exigiria uma aplicação autorizada e um fluxo próprio de autenticação/servidor, além das permissões e dos limites da API. Não foram colocados tokens privados no HTML nem criado um extrator de páginas de pins.

Referências consultadas: [Pinterest · baixar uma imagem](https://help.pinterest.com/en/article/download-an-image), [autenticação e autorização](https://developers.pinterest.com/docs/getting-started/set-up-authentication-and-authorization/) e [cliente oficial: busca dos pins do usuário](https://github.com/pinterest/pinterest-python-generated-api-client/blob/main/docs/SearchApi.md).

### Importar imagens

- Clique em **Carregar imagens** ou arraste arquivos PNG/WebP para a área indicada. É possível escolher vários arquivos.
- **Somente com transparência real** vem ativado. O editor decodifica o arquivo e verifica os valores alfa dos pixels. Um arquivo totalmente opaco é rejeitado com uma explicação; desmarque a opção para aceitá-lo conscientemente.
- O campo **Link do pin ou fonte** é opcional e guarda a referência junto ao arquivo no projeto. Ele não inicia um download da página.
- Em **Importar por link direto de imagem**, cole uma URL HTTPS que entregue o arquivo PNG/WebP. Links de páginas de pins são identificados e orientam a usar o original/arquivo. Alguns servidores bloqueiam o acesso direto pelo navegador; o editor avisa para usar o arquivo baixado.
- JPG, HTML e SVG não são aceitos nesta importação. Mudar a extensão para `.png` não transforma o conteúdo em PNG.

A verificação considera a imagem decodificada; se o WebP for animado, ela se refere ao quadro decodificado, não a uma análise de todos os quadros. O arquivo original é incorporado sem achatamento em um fundo branco. Uma imagem inteiramente invisível é rejeitada para evitar adicionar um elemento sem conteúdo.

Os limites são 2 MB por arquivo, 4096 × 4096 px, 30 arquivos e 8 milhões de caracteres de dados de imagem na biblioteca. O conjunto de imagens/fontes também respeita o limite do JSON do projeto, de 15 MB. O salvamento local depende da quota do navegador; baixe um backup quando o cabeçalho indicar que não foi possível salvar.

### Minhas imagens e exportação

A biblioteca mostra uma prévia sobre xadrez, informa **Transparência real** ou **Fundo opaco** e permite clicar para adicionar outras instâncias. Instâncias do mesmo arquivo reutilizam os dados. Para remover um arquivo da biblioteca, remova antes as suas instâncias do canvas; a ação de exclusão fica desativada enquanto ele está em uso.

As imagens aceitam posição, dimensões, rotação, opacidade, bloqueio, camadas e três ajustes na caixa: conter, preencher/cortar e esticar. Cor/traço de vetor não são oferecidos para uma imagem raster.

Os dados das imagens acompanham o JSON e o HTML exportado. A exportação inclui somente os arquivos usados na composição e não depende de URLs remotas. A referência ao pin/fonte fica no projeto, sem provocar solicitações ao Pinterest na execução do widget. Não é necessário manter o site da imagem disponível para o widget funcionar.

## Escala de elementos

Selecione um vetor ou uma imagem e use **Escala do elemento** no painel direito ou o ícone **Escala e proporção** no menu flutuante. A barra e os botões −/+ alteram largura e altura juntas. **Manter proporção ao redimensionar** também controla os cantos de arraste e as entradas numéricas de largura/altura.

Desative o bloqueio de proporção para editar largura e altura independentemente. Na imagem, o ajuste **Conter** continua preservando o conteúdo; escolha **Esticar** apenas se quiser deformá-lo para preencher a caixa.

A escala é relativa ao tamanho de referência do elemento. Alterar dimensões numericamente ou pelos cantos redefine a referência como 100%. Em textos, o redimensionamento da caixa permanece independente do tamanho da fonte. Objetos bloqueados não são modificados pela escala individual.

## Formato e tamanho de toda a composição

Em **Composição → Tamanho e proporção da arte**:

- **Formato do canvas** oferece quadrado 1:1, horizontal 4:3, fotografia 3:2, horizontal 16:9, vertical 9:16 e faixa 3:1. Mudar o formato altera a área disponível e mantém os elementos nas posições atuais. Os avisos indicam conteúdo que passe a ficar fora da área.
- **Manter proporção do canvas** vincula as entradas de largura e altura.
- **Escala de toda a arte** altera as dimensões da composição e, proporcionalmente, as posições/caixas, fontes, imagens, detalhes da data, preenchimentos internos de componentes e guias. Objetos bloqueados também acompanham essa mudança global. É uma operação reversível no histórico.

Os valores aplicados respeitam os limites de tela, fontes e caixas do editor; por isso a escala mínima/máxima pode ficar mais restrita em algumas composições. Alterar manualmente as medidas/formato do canvas redefine sua escala como 100%.

**Escala não é zoom:** zoom muda apenas a visualização do editor. Escala muda medidas salvas/exportadas. Com o zoom em “Ajustar”, a arte pode continuar ocupando uma largura visual semelhante no editor. No modo responsivo, a composição também se adapta à largura disponível do embed; para alterar o tamanho de um desenho em relação à composição, use a escala do elemento.

## Validação

`tests/images-scaling.cjs` testa busca externa e codificação de termos; alfa real versus fundo opaco/xadrez; importação PNG/WebP e rejeição de dimensões excessivas; sucesso parcial de lote; escala e bloqueio de proporção; arraste pelos cantos; opacidade/rotação/ajuste na caixa; reutilização da biblioteca; link direto e fallback de acesso bloqueado; escala global e histórico; formatos de canvas; persistência e JSON inválido; exportação offline com canal alfa; e controles em mobile. Veja `tests/images-scaling-results.json`.

A imagem da captura de apresentação é um desenho original usado para demonstrar a importação; não é um resultado ou ativo extraído do Pinterest.
