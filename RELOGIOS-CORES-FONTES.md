# Relógios, cores e fontes · atualização

Abra `dist/widget-atelier.html` ou o arquivo individual `widget-atelier-relogios-cores.html`. A versão anterior permanece preservada no workspace. Projetos anteriores são migrados automaticamente ao abrir.

## Fundo do relógio

Selecione um relógio e use o ícone **Fundo do relógio** no menu flutuante ou a seção **Fundo do relógio** no painel direito.

- **Usar cartão da composição:** mantém a vinculação à cor global do cartão, preservando o comportamento dos projetos antigos.
- **Cor própria:** cada relógio passa a ter seu fundo independente. Clicar na amostra de cor abre o seletor. Escolher uma cor ativa esse modo automaticamente.
- **Transparente:** remove somente o fundo do relógio e preserva texto/data. O que aparece atrás é o fundo da composição. Para revelar a página do Notion através de toda a composição, também deixe o fundo da composição com alfa zero e desative o degradê ou torne as duas cores transparentes.

Arredondamento e respiro interno são ajustáveis. No modelo Flip, as placas dos números têm sua própria cor; podem permanecer visíveis quando o fundo geral do relógio é transparente.

## Seletor de cores

As amostras de cor do editor abrem um painel com roda de matiz/saturação, luminosidade, alfa, canais RGB e HEX. O HEX aceita seis dígitos (`#RRGGBB`) ou oito, incluindo alfa (`#RRGGBBAA`). Há também o botão **Transparente**.

A roda funciona por arraste e pelo teclado: esquerda/direita alteram o matiz, cima/baixo a saturação. Os campos RGB aceitam valores de 0 a 255. As alterações são exibidas enquanto você ajusta a cor. Um gesto da roda é uma operação no histórico; Desfazer recupera a cor anterior.

**Recentes** mantém até 12 cores e **Salvas**, até 24. Use **Salvar cor** para adicionar uma favorita e o pequeno × para removê-la. Clique na amostra para reutilizar. As paletas são guardadas com o projeto, incluindo transparência, e acompanham o JSON de backup. O HTML exportado contém as cores usadas no design e exclui a interface/paletas do editor.

## Texto da data

A data deixou de ter tamanho, peso e opacidade fixos no código. Clique diretamente na data no canvas ou escolha **Data** nas abas do relógio para editar sua tipografia. **Horário** retorna aos ajustes dos números.

A data possui fonte própria ou herda a fonte do horário; tamanho com −/+, peso, itálico, sublinhado, cor, opacidade, entreletras, entrelinhas, alinhamentos, caixa, rotação, deslocamentos X/Y e dimensões de caixa. Largura/altura zero usam medidas automáticas. Os deslocamentos são relativos à posição da data dentro do relógio. Conteúdo fora da caixa do relógio pode ser cortado na exportação; os avisos ajudam a identificar esse caso. Aumente a caixa do relógio quando necessário.

A data tem cinco formatos e pode seguir a visibilidade global, ser mostrada ou ocultada apenas naquele relógio. O idioma e o fuso continuam sendo os do projeto. Editar a data não altera a fonte/tamanho dos números. Fontes usadas só na data também são incorporadas na exportação.

## Sete modelos de relógio

Em **Dinâmicos → Modelos de relógio**, clique em uma amostra para adicionar. Para mudar um relógio existente, selecione-o e escolha seu modelo no painel direito.

| Modelo | Característica |
| --- | --- |
| Digital suave | Cartão digital compatível com a composição anterior. |
| Minimal | Números amplos e desenho limpo. |
| Editorial | Serifada de contraste e espaçamento mais fechado. |
| Flip retrô | Placas separadas, linha central e transição na troca dos números. |
| Vertical | Horas e minutos empilhados. |
| Analógico leve | Mostrador, marcas e ponteiros calculados a partir do horário/fuso. |
| Analógico romano | Mostrador com algarismos romanos e fonte editorial. |

Escolher um modelo ajusta dimensões, fonte e parâmetros tipográficos do horário. Cores e configurações da data são preservadas. Nos analógicos, largura/altura controlam o diâmetro; o tamanho da fonte controla os numerais do mostrador. Os ponteiros continuam atualizando no HTML exportado. Todos mantêm as opções existentes de fuso, 12/24 horas, segundos e data, conforme o que faz sentido para o desenho. As transições de Flip respeitam movimento reduzido.

Referência funcional consultada: [Indify · Clock Widget](https://helpcenter.indify.co/widget-guides/clock-widget), que documenta opções digitais, analógicas e Flip, cores, transparência e tipografia. Os modelos do WA são implementações próprias; não copiam código ou ativos do Indify nem prometem reproduzir todas as suas opções.

## Fontes no painel esquerdo

Em **Texto**, as amostras são botões reais, renderizados nas respectivas fontes. Clique para aplicar ao texto selecionado, ao horário ou à data, conforme a parte ativa do relógio. Use a busca para filtrar. Sem seleção, escolher uma fonte cria um bloco de texto nessa família. Objetos bloqueados precisam ser desbloqueados antes da alteração.

O botão **Carregar minhas fontes**, perto da biblioteca, permite escolher vários arquivos WOFF2, WOFF, TTF ou OTF. Os arquivos válidos são mantidos mesmo quando outro arquivo do lote falha. Cada arquivo aparece como uma opção clicável. O nome do arquivo identifica cada entrada em um lote; em importações individuais, você também pode informar um nome. Peso/estilo podem ser configurados nos campos de importação. Não há agrupamento automático de arquivos de uma família ou importação de ZIP.

Limites atuais: até 1 MB por arquivo, 20 arquivos e 10 MB de dados de fontes por projeto; JSON até 15 MB. Falhas de salvamento local são sinalizadas, pois a quota depende do navegador. Baixe o JSON para guardar o trabalho.

## Sobre o catálogo do Canva

O catálogo completo do Canva não foi copiado. Estar disponível no Canva não significa que o arquivo possa ser extraído e redistribuído em outro aplicativo ou HTML. A biblioteca inclui famílias abertas e permite carregar seus arquivos quando a licença autoriza a incorporação pretendida. Fontes comerciais e referências não confirmadas continuam identificadas como pendentes de arquivo/licença.

A biblioteca incorporada foi ampliada de 24 para **56 famílias abertas**, com arquivos e avisos de licença obtidos dos repositórios oficiais. As faces embarcadas variam por família; quando uma face/peso não está incluída, o navegador pode sintetizar o estilo, de forma consistente com a exportação.

As 32 novas famílias: Inter, Roboto, Open Sans, Oswald, Rubik, Manrope, Outfit, Urbanist, Work Sans, DM Mono, Archivo, Barlow, Righteous, Bebas Neue, Pacifico, Dancing Script, Sacramento, Allura, Parisienne, Satisfy, Cinzel, Prata, Italiana, Marcellus, Forum, Abril Fatface, Alfa Slab One, Comfortaa, Amatic SC, Shadows Into Light, Patrick Hand e Indie Flower.

As 24 anteriores continuam disponíveis. Fontes e licenças: [Google Fonts](https://fonts.google.com/) e [repositório oficial](https://github.com/google/fonts). Veja também a orientação do [Canva sobre arquivos próprios e incorporação](https://www.canva.com/en_in/help/upload-fonts/).

## Testes

`tests/clocks-colors.cjs` valida 13 cenários desta entrega, incluindo fundos independentes e transparência real; RGB/HEX/alfa/cores salvas/recentes; arraste da roda e histórico; clique e controles independentes da data; sete modelos e posições matemáticas dos ponteiros; visibilidade; importação múltipla com arquivo inválido no lote; persistência, validação de JSON e exportação com a fonte própria da data; seleção de fontes à esquerda; popup em mobile e Escape.

Os testes das entregas anteriores também foram mantidos. Foram executados em Chromium/Playwright, sem alegar validação no aplicativo real do Notion ou em Safari/Firefox. A prévia Notion continua sendo uma aproximação visual.
