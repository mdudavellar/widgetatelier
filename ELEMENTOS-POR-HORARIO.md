# Elementos que acompanham o horário

No Atelier online, abra **Dinâmicos → Elemento que muda com o horário**.

O elemento começa com quatro desenhos originais: sol retrô de manhã, sol editorial à tarde, lua e horizonte à noite, e constelação na madrugada. Selecione o elemento e, no painel **Elemento por horário**, escolha o desenho de cada período. As opções incluem os vetores e adesivos da biblioteca existente. Cor, opacidade, traço, tamanho, posição e rotação continuam editáveis pelas ferramentas do componente gráfico.

Também é possível selecionar qualquer texto, imagem ou componente e usar **Visibilidade por horário → Somente nos períodos escolhidos**. Marque um ou mais períodos. Isso permite, por exemplo, posicionar imagens próprias diferentes no mesmo lugar e atribuir um período a cada uma. O controle de visibilidade manual continua tendo prioridade. Não é permitido desmarcar todos os períodos; para ocultar completamente um objeto, use **Visível**.

O botão **◷** do menu flutuante abre a regra de visibilidade; **☀**, nos gráficos com variações, abre os desenhos por período. **Testar a composição** permite ver os quatro períodos sem alterar o relógio do dispositivo. A mesma seleção de teste é aplicada à saudação e à prévia contextualizada no Notion. O modo de teste não é gravado no widget publicado, que utiliza o horário real.

Os limites preservam os períodos já utilizados pela saudação do WA:

- Manhã: 05h00 a 11h59.
- Tarde: 12h00 a 17h59.
- Noite: 18h00 a 21h59.
- Madrugada/noite profunda: 22h00 a 04h59.

O fuso é o do projeto, em **Dinâmicos → Horário do projeto → Fuso horário**. A regra usa o relógio do dispositivo com esse fuso; não consulta clima ou a posição astronômica do sol. A atualização acontece automaticamente, sem precisar recarregar a página. Datas e fusos com horário de verão são tratados por `Intl.DateTimeFormat`.

No editor, elementos fora do período ficam esmaecidos e identificados como **Oculto neste período**, para continuarem selecionáveis. Na prévia e no widget exportado/publicado, ficam realmente ocultos. As indicações de edição não são exportadas. A visibilidade é uma regra de apresentação, não uma permissão de acesso aos dados.

Após configurar, clique em **Publicar e copiar link** para atualizar a composição no mesmo endereço incorporado no Notion. Os widgets antigos não mudam de configuração sozinhos: é preciso publicar a composição atualizada.

Implementação: `src/time-rules.js` mantém o calendário de períodos, as regras visuais e sua validação. `dynamic.js` e o renderer utilizam esse mesmo módulo no editor, na prévia e na exportação. O tipo gráfico existente foi ampliado com desenhos por período, preservando projetos e bibliotecas anteriores.

Verificações: quatro desenhos e troca personalizada, visibilidade e edição esmaecida, proteção contra períodos vazios, prévia sem indicações de edição, persistência, limites exatos, fuso com horário de verão, validação de projeto, troca de desenho e aparecimento automático em HTML exportado com relógio controlado. Os 15 cenários de regressão do estúdio também passaram. A interface foi testada na cópia local; a disponibilidade da atualização online é verificada pela publicação e por HTTP, sem alegar teste visual no Notion real.
