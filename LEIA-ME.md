# Elementos por horário

No editor online, use **Dinâmicos → Elemento que muda com o horário**. Para outros objetos, selecione-os e use **Visibilidade por horário**. Guia: [ELEMENTOS-POR-HORARIO.md](ELEMENTOS-POR-HORARIO.md).

# Atelier publicado e links prontos para o Notion

Editor: https://wa-central-compartilhada.snappykookaburra.chatgpt.site/atelier

Use **Publicar e copiar link** para incorporar a composição no Notion. Clique nas medidas acima do canvas para redimensionar o projeto. Detalhes: [ATELIER-ONLINE-E-NOTION.md](ATELIER-ONLINE-E-NOTION.md).

# Atualização: quadro personalizável e compartilhado

Abra `dist/widget-atelier-compartilhado.html`. Guia: [PERSONALIZACAO-E-COMPARTILHAMENTO.md](PERSONALIZACAO-E-COMPARTILHAMENTO.md). A central online está em https://wa-central-compartilhada.snappykookaburra.chatgpt.site. Use Compartilhar para gerar o link da sua central.

# Atualização: central de tarefas e projetos em abas

Abra `dist/widget-atelier.html` para a versão atual. Para usar só a central adaptável ao celular, abra `dist/central-de-tarefas.html`. Guia e limites: [CENTRAL-E-PROJETOS.md](CENTRAL-E-PROJETOS.md).

# Widget Atelier · Editor de composição visual

**Versão atual:** veja `ESTUDIO-GALERIA-MENUS.md` para menus móveis, galeria interna com 96 elementos, seis calendários, seis novos componentes, fundo transparente e alças de tamanho/rotação. A busca externa foi removida; os guias anteriores registram versões históricas.

Abra `dist/widget-atelier.html` em um navegador moderno. O editor é um único arquivo, sem instalação e sem conexão obrigatória. As fontes estão incorporadas. O arquivo `original-v2.html` preserva a versão recebida, sem alterações.

## Uso

1. Em **Elementos**, escolha uma categoria ou busque um vetor. Clique para adicionar.
2. Em **Texto**, adicione título, texto ou nota manuscrita. Dois cliques no canvas iniciam a edição. Enter quebra a linha; Ctrl/⌘ + Enter conclui; Escape cancela a edição atual. Clique fora para concluir.
3. Selecione um objeto e ajuste posição, dimensões, rotação, cor, opacidade e tipografia no painel direito. Redimensionar a caixa não altera o tamanho da fonte.
4. Shift + clique seleciona vários objetos. As ferramentas de alinhamento usam o canvas para uma seleção única ou os limites da seleção para múltiplos objetos. A distribuição, com três ou mais objetos, iguala os espaços entre eles.
5. Em **Precisão**, ative réguas, guias, margens, grade, snap e limites. Arraste da régua superior para uma guia horizontal; da lateral para uma vertical. Arraste uma guia para fora do canvas para removê-la.
6. **Camadas** permite selecionar, ocultar, bloquear e alterar a ordem. Um objeto bloqueado pode ser selecionado para desbloquear, mas não pode ser movido ou ter seu estilo alterado no painel.
7. **Dinâmicos** mantém nome, quatro períodos de saudação/frase, simulação de período, fuso horário, idioma, formato de 12/24 horas, segundos e data. Componentes podem ser adicionados independentemente, inclusive várias instâncias. O nome na edição direta das mensagens é reconvertido em `{name}` para manter a personalização.
8. **Composição** controla medidas, paletas, cores, degradê, raio e comportamento de exportação.
9. **Prévia no Notion** simula páginas padrão/total, de uma a cinco colunas, proporções diferentes, coluna do widget, altura do embed e desktop/mobile. Proporções são números positivos separados por vírgulas, um por coluna. No mobile, as colunas são empilhadas. Os avisos identificam objetos fora da área, fontes abaixo de 11 px após escala e texto cortado na caixa. São verificações geométricas, não uma avaliação completa de legibilidade.
10. **Projeto** baixa/abre um JSON editável. Trocar ou restaurar um projeto é reversível por Desfazer. **Exportar HTML** gera somente o widget com relógio e saudações ativos.

Atalhos: Ctrl/⌘ Z desfaz; Ctrl/⌘ Shift Z ou Ctrl/⌘ Y refaz; Ctrl/⌘ D duplica; Delete exclui objetos desbloqueados; setas movem 1 px, ou 10 px com Shift. Ao editar texto, valem os atalhos nativos do campo.

## Responsividade e Notion

- **Responsivo**: reduz a composição inteira proporcionalmente para caber na largura disponível, até a escala de 100%. Mantém relações visuais, sem reorganizar elementos individualmente. O HTML ajusta sua altura de conteúdo à escala. A altura do bloco no Notion precisa ser ajustada na própria página.
- **Fixo**: preserva medidas em pixels e posições. Um embed mais estreito pode cortar o conteúdo; a prévia mostra avisos.
- A simulação é uma aproximação. Não garante equivalência com cada versão, espaçamento ou dispositivo do Notion.
- Para usar `/embed`, hospede o HTML exportado em um endereço HTTPS acessível e compatível com iframes. Um arquivo local não é uma URL incorporável. Publicação e hospedagem automáticas não foram implementadas.

## Tipografia e arte

Inclui 56 famílias abertas com fontes incorporadas; detalhes da biblioteca e da nova interface estão em `RELOGIOS-CORES-FONTES.md`; as referências anteriores e fontes pendentes estão em `ATUALIZACAO.md`. Os avisos SIL OFL estão em `licenses/` e acompanham as fontes usadas no HTML exportado. Arquivos próprios WOFF2/WOFF/TTF/OTF podem ser carregados e são incluídos no projeto e na exportação; use arquivos com permissão de incorporação.

A biblioteca tem 96 elementos originais: 64 vetores e 32 adesivos prontos. As cinco imagens enviadas nesta atualização foram consideradas como referências tipográficas e estéticas; nenhum ativo proprietário do Canva foi redistribuído.

## Salvamento e compatibilidade

O estado é salvo em `widget-atelier-v3`. Quando não existe um projeto v3, o editor tenta migrar `millena-v2`: textos, posições percentuais convertidas em pixels, fontes, visibilidade, símbolos antigos, cores e relógio. A migração exige que os dados antigos estejam disponíveis **no mesmo navegador e na mesma origem**. Navegadores podem isolar armazenamento por arquivo local. Baixe o projeto JSON para transferir ou guardar seu trabalho. Falhas de armazenamento aparecem no cabeçalho.

Verificado no Chromium instalado no ambiente. Firefox e Safari não foram executados. Navegadores antigos podem não suportar todos os recursos usados, como `dialog`, `ResizeObserver` e edição `plaintext-only`. Não há sincronização em nuvem.

## Limites desta entrega

- A formatação é por bloco; não há estilos diferentes em trechos do mesmo bloco.
- A aba Vetores contém oito desenhos por categoria; a Galeria adiciona 32 adesivos originais.
- Importar SVGs próprios, edição de caminhos, outros tipos de widgets além de calendário/contagem, sincronização e publicação automática ficam para etapas posteriores. Animações de entrada de texto já estão disponíveis. Não há botões que simulem esses recursos.
- Há uma composição inicial no sistema de templates; a biblioteca extensa de templates não foi implementada.
- O histórico guarda até 100 operações e vale para a sessão atual. As ferramentas visuais de precisão não são exportadas.

## Desenvolvimento

O editor não requer build para uso. Para alterar o código e reconstruir o arquivo único:

```sh
python build.py
```

Os módulos estão em `src/`. O build usa `fonts.json`, já fornecido; não acessa a rede. `fetch_fonts.py` é apenas uma ferramenta de manutenção que busca as fontes abertas e suas licenças nas origens oficiais.

Para executar os testes de integração, com Node, Playwright e Chromium instalados:

```sh
python -m http.server 8766 --bind 127.0.0.1 --directory .
# Em outro terminal:
node tests/integration.cjs
node tests/precision.cjs
node tests/studio-v6.cjs
```

Os testes usam o executável `/usr/bin/chromium` e a porta 8766. Verifique `tests/results.json` e `VALIDACAO.md` para os resultados da execução desta entrega.
