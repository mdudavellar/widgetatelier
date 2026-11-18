# Seleção e arraste no canvas

Depois de usar **Desagrupar para edição**, a propriedade `partsUnlocked` mantém as partes acessíveis ao clique no canvas, mesmo após concluir a edição. **Agrupar novamente** restaura a seleção do conjunto sem apagar suas personalizações. **Testar interações** permite usar os controles do componente no editor.

O mouse esquerdo sobre um item seleciona e arrasta. Arrastar no espaço vazio desenha uma área de seleção em qualquer direção. A área pode incluir partes de diferentes componentes e elementos comuns. Shift (ou Ctrl/Cmd) + clique adiciona ou retira itens. Arrastar um dos itens selecionados move todos pelo mesmo deslocamento, preservando distâncias; os controles do painel permitem editar propriedades em conjunto. As partes consideram a rotação do componente original. Fundos muito grandes só entram na área quando ficam inteiramente contidos, e objetos bloqueados são respeitados.

O desenho da seleção usa as coordenadas do canvas, com conversão explícita do zoom e da posição da área de trabalho. Gestos inteiros produzem uma transação no histórico; cancelar o ponteiro restaura todas as posições. Campos de texto em edição e formulários temporários são protegidos da seleção por arraste.

A identificação das partes desconsidera alças e outros controles de edição. Identificadores de fundos antigos são migrados para o caminho estável quando necessário. Isso evita que selecionar ou retirar a seleção mude a parte apontada por uma personalização.

Verificação: geometria da seleção em ambas as direções; seleção mista; arraste direto após concluir; pai permanece no lugar ao mover uma parte; Shift adiciona e remove; movimento e fonte em conjunto; zoom; objetos comuns e bloqueados; desfazer e pointercancel. O editor completo e o HTML exportado foram executados em testes com implementação de DOM e geometria controlada. Os testes não constituem verificação visual de pixels em navegador real.
