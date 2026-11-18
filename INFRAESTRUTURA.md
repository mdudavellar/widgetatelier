# Infraestrutura, dependências e futura hospedagem

## Dependências declaradas nesta transferência

- Node 24: HTTP, filesystem, Web APIs e `node:sqlite` nativo.
- Python 3: build.py, somente biblioteca padrão.
- linkedom 0.18.15: testes DOM, sem renderização visual.
- Playwright 1.62.1: preservado como dependência de desenvolvimento para testes históricos de navegador. Os binários dos navegadores não integram o ZIP; não são necessários para o servidor nem para a seleção de npm test.
- `source/ui/vendor/fontkit.min.js`: parser de fontes já incorporado no projeto, com avisos originais.

O package-lock da raiz pertence às ferramentas adicionadas para portabilidade; não havia um lockfile original a recuperar. Npm ci instala apenas ferramentas de teste. Nenhuma dependência instalada foi copiada.

## Serviços externos preservados

O catálogo de fontes e ícones pode buscar conteúdo de provedores externos (incluindo Google Fonts e Iconify). O código, índices e recursos já incorporados estão no ZIP; **não** foi feito um download integral de todos os arquivos desses provedores. Busca/importação de itens remotos exige conexão e disponibilidade dos respectivos serviços. O acesso pode depender de limites, CORS e licenças. Imagens carregadas por URL externa continuam dependendo dessa URL.

Os arquivos de licença suplementares em docs/font-licenses foram recuperados da cópia de trabalho local, sem substituir as licenças originais em source. Não há promessa de acesso ao catálogo proprietário do Canva.

## Variáveis e segredos

As únicas variáveis do runner local estão em .env.example e README. Nenhuma é uma credencial. O código original exige os bindings `DB` e `BUCKET`, injetados pela plataforma de execução. Chaves individuais de edição de quadros/widgets são geradas pelo aplicativo, não devem virar variáveis fixas do build.

O manifesto original source/.openai/hosting.json contém identificadores da infraestrutura antiga, não segredos. Foi preservado para referência e integridade histórica. Não é uma configuração portátil de deploy nem autorização para gravar no projeto antigo.

## Caminho para publicar em outra infraestrutura

O site antigo e seus links continuam separados desta exportação. Para a nova instância pública, o próximo agente deverá:

1. Escolher um domínio HTTPS e uma infraestrutura compatível com Worker fetch, D1 e R2, ou adaptar esses contratos para outros serviços com revisão e testes.
2. Provisionar banco e armazenamento **novos**, aplicar as migrações SQL e configurar os bindings DB e BUCKET.
3. Usar uma origem pública nova no build. O build de tools/ gera um Worker ESM e ajusta a origem somente no resultado. O servidor Node local também pode ser um ponto de partida para uma hospedagem própria, mas precisa de revisão operacional, TLS, backups e persistência adequada antes de exposição pública.
4. Configurar manualmente a infraestrutura e credenciais do provedor escolhido, fora do código e do ZIP. Nenhuma credencial antiga foi exportada ou solicitada.
5. Validar publicação, atualização, links da navegação dentro do iframe, políticas de sandbox, dados compartilhados e acesso por link. Quem possui uma chave de quadro pode editá-lo, conforme o modelo atual.
6. Se necessário, migrar dados de produção por um processo separado e autorizado; manter consistência entre linhas D1, HTMLs R2 e metadados. Não é suficiente copiar só um desses serviços.

Não existe configuração Wrangler original no repositório. Esta entrega não cria contas, não migra registros, não muda DNS e não oferece um novo endpoint público. `npm run build` não faz deploy.

## Limite do embed no Notion

O widget controla seu conteúdo, layout e dimensões anunciadas em oEmbed. O Notion controla o bloco/iframe que o envolve e pode manter dimensões anteriores. Um widget não tem acesso de mesma origem ao documento do Notion para redimensionar esse bloco. Preservar o código existente não resolve automaticamente esse limite; continue os testes em dispositivos reais antes de prometer ajuste sem intervenção.
