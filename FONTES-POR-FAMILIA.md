# Biblioteca de fontes por família

Removidos os limites de quantidade de fontes importadas e de tamanho por arquivo de fonte. TTF, OTF, WOFF e WOFF2 são identificados pelos metadados internos: família, estilo, peso e faixa variável. Regular, Light, Bold e Itálico ficam na mesma família, com escolhas em **Variação** no painel e nas amostras da biblioteca. Formatos diferentes do mesmo estilo não repetem a opção. Variações de largura e subfamílias adicionais permanecem disponíveis.

A biblioteca fica no IndexedDB deste navegador, separada dos projetos. Cada projeto leva apenas as fontes usadas em seu conteúdo. O botão de backup da biblioteca permite transferir todas as fontes para outro navegador ou computador; o JSON do projeto continua incluindo as fontes utilizadas. O armazenamento disponível depende do navegador; falhas são informadas e o backup permite guardar os arquivos da sessão.

Fontes antigas mantêm os identificadores e declarações originais de renderização. Quando necessário, uma declaração adicional oferece os pesos reais para novos usos, sem alterar o desenho salvo. A opção **Renomear ou unir família** corrige metadados imprecisos. Importar uma fonte exige um arquivo que você possa utilizar e incorporar; a ferramenta não fornece fontes proprietárias do Canva.

Verificados metadados reais nos quatro formatos, mais de 20 importações, fontes variáveis e itálicas, arquivos duplicados, preservação de projetos antigos, armazenamento, backup portável e falhas de quota. O leitor de metadados funciona localmente; suas licenças estão em `licenses/`.
