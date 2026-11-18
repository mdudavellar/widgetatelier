# Estado de continuidade

A referência desta transferência é a versão publicada 32. O pedido atual é exportar o projeto; pedidos anteriores da conversa não foram executados novamente nem usados para alterar recursos durante esta entrega.

## Recursos presentes no código

Editor com modos rápido/livre, projetos, componentes dinâmicos, relógios e calendários, textos/fontes importáveis, catálogos, formas, seleção múltipla, partes editáveis, grupos pessoais, camadas, undo/redo, controles contextuais, navegação personalizável, calendário com tags/legendas, animações, condições por horário, prévias de dispositivos, exportação HTML/JSON, publicação e central de tarefas compartilhável. Esses sistemas foram copiados dos fontes existentes; sua presença não significa uma nova homologação completa de cada interação.

A alteração mais recente registrada é a edição numérica dos controles de barra: ângulo, arredondamento, opacidade, espaçamento e controles relacionados, mantendo as barras e undo/redo. O teste original numeric-sliders.cjs está incluído.

## Cuidados para o próximo agente

- Trabalhe nos módulos de ui/src, não apenas no snapshot editor.html.
- Mantenha as migrações existentes e acrescente novas quando necessário; não apague dados para resolver incompatibilidades.
- Preserve revisões, autenticação e conflitos da central/publicações.
- Diferencie histórico de solicitações do que foi verificado no código. Não declare todos os relatos anteriores resolvidos sem reproduzir.
- Faça validação visual de redimensionamento, texto multilinha, fontes, barra de navegação e embeds em dispositivos reais. Os testes DOM usam geometria determinística, não um navegador.
- Bibliotecas remotas podem não retornar prévias se o provedor ou a rede falhar; não são todas assets offline.
- O editor local começa sem os projetos privados do navegador de produção. Isso é separação de origem/armazenamento, não perda do código.
- Não publique automaticamente sobre o site antigo. A identidade antiga em .openai é referência histórica.

As notas originais em source/*.md detalham mudanças de versões anteriores e ajudam a entender decisões de implementação. SOURCE-PROVENANCE.json permite rastrear a origem exata sem incluir o histórico Git ou sua configuração remota.

## Fontes completas recuperadas

O repositório publicado armazena um fonts.json reduzido (duas famílias), mas ui/editor.html incorpora 56. O arquivo completo foi encontrado na cópia de trabalho /workspace/widget-atelier e preservado em authoring-supplement/fonts.json. O build de transferência monta os inputs em staging usando esse arquivo completo. Não simplifique essa etapa para ler somente source/ui/fonts.json: isso reduziria as fontes disponíveis e divergiria do publicado.

## Correção publicada v32

A publicação passou a usar o mesmo snapshot validado utilizado para exportar o HTML. A troca de modo normaliza imediatamente a altura de projetos compactos, evitando um caminho reproduzível de erro 400. Em caso de falha, o diálogo não apresenta o link anterior como atualização bem-sucedida. O editor exibe v32 e responde com no-store. A publicação desta correção foi autorizada e confirmada na integração Sites antes de preparar esta cópia.

Foram acrescentados os testes publishing-compact-navigation.cjs e editor-version.cjs. A descrição anterior dos controles numéricos refere-se à mudança v31, também preservada.
