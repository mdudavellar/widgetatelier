# Ateliê de Widgets — transferência para Antigravity / Gemini

Esta pasta contém o **código original da versão publicada 32**, commit `45c7529b131e7dad468a806f6dbe20c69f1e371b`, e ferramentas adicionais para executá-lo fora da hospedagem Sites. A preparação desta cópia não modifica o site publicado. Nenhum recurso foi reimplementado ou removido nesta transferência.

## Abrir e executar

1. Extraia o ZIP e abra **esta pasta inteira** no Google Antigravity; não abra apenas `source/ui`.
2. Instale **Node.js 24 LTS** (inclui npm) e **Python 3**. No Windows, habilite a inclusão do Python no PATH. Confira com `node --version` e `python3 --version` (ou `python --version`).
3. No terminal desta pasta:

```sh
npm run doctor
npm run verify
npm run dev
```

4. Abra **http://localhost:8787/atelier**. Mantenha o terminal aberto. Para encerrar, pressione Ctrl+C. Após editar os fontes, encerre e execute `npm run dev` novamente; não há atualização automática.

O servidor de desenvolvimento usa somente bibliotecas nativas do Node e Python. **Não exige tokens, conta de hospedagem ou instalação de pacotes npm para iniciar.** Para os testes DOM, execute `npm ci` (ou `npm install` se você alterar as dependências). O `package-lock.json` fixa as dependências das ferramentas de teste.

Não use `file://` ou apenas um servidor de arquivos estáticos: publicação, catálogos e tarefas compartilhadas precisam das rotas do backend.

## O que está incluído

```text
source/                  158 arquivos originais, preservados byte a byte
  ui/src/                editor: componentes JavaScript, HTML e CSS
  ui/build.py            montagem original do editor
  ui/editor.html         snapshot compilado da versão publicada
  ui/tests/              testes originais e fixtures
  ui/vendor/             parser de fontes e imagens dos templates
  ui/*.json              fontes, catálogos e mídia declarados
  worker/                APIs, publicação, catálogos e compatibilidade
  drizzle/               migrações SQL originais
  build.cjs              montagem original do Worker
  .openai/hosting.json    referência não secreta à hospedagem original
  *.md                   notas técnicas originais
authoring-supplement/     fontes completas e notas/scripts da cópia de trabalho
 tools/                   execução e testes portáteis, separados dos fontes
 docs/                    arquitetura, dependências e continuidade
 docs/font-licenses/       textos de licença suplementares disponíveis
 SOURCE-PROVENANCE.json    origem, commit e SHA-256 de cada arquivo original
 EXPORT-REPORT.json       verificações realizadas nesta transferência
 .env.example             variáveis locais; nenhum segredo real
 package*.json            comandos e dependências das ferramentas adicionais
```

O projeto original usa JavaScript sem framework e um Worker com contratos Cloudflare D1/R2. Não existia `package.json`, lockfile ou configuração de deploy portátil no repositório original. Os arquivos npm da raiz foram adicionados para esta transferência, sem inventar dependências de produção.

## Configuração local e dados

Os padrões funcionam sem `.env`. Se necessário, copie `.env.example` para `.env` usando seu gerenciador de arquivos e altere:

| Variável | Padrão | Uso |
| --- | --- | --- |
| `HOST` | `127.0.0.1` | Interface do servidor local |
| `PORT` | `8787` | Porta HTTP |
| `PUBLIC_BASE_URL` | `http://localhost:8787` | Origem dos links e chamadas gerados; mantenha igual ao endereço usado no navegador |
| `WA_DATA_DIR` | `.local-data` | Pasta local de banco e objetos publicados |
| `PYTHON` | detecção de `python3` / `python` | Caminho do executável Python, se necessário |

Se mudar a porta, atualize também `PUBLIC_BASE_URL`. Para acessar de outro dispositivo, configure um host acessível e a origem correspondente. HTTP em IP de rede pode restringir APIs do navegador; use HTTPS para esse fluxo.

O arquivo `source/ui/fonts.json` contém apenas duas famílias, embora o snapshot publicado tenha 56. A cópia de trabalho original preservava o arquivo completo: ele foi incluído, sem alterações, em `authoring-supplement/fonts.json`. O build local usa esse complemento em uma pasta de montagem isolada para reproduzir as fontes publicadas, sem substituir o arquivo original do repositório. As notas e scripts auxiliares da cópia de trabalho também foram preservados nessa pasta; esses scripts históricos não são necessários para iniciar o editor.

A camada local implementa os contratos usados pelo código original:

- `DB`: SQLite persistente em `.local-data/d1.sqlite`; aplica as migrações originais automaticamente.
- `BUCKET`: arquivos HTML e metadados em `.local-data/objects` e `.local-data/metadata`.

O build lê os fontes originais, monta o editor e o Worker e troca a origem fixa de produção **somente no resultado gerado localmente**. As APIs do build local apontam para a instância local. O código original em `source/` continua intacto.

O editor pode criar projetos, salvar no navegador, montar widgets e publicar no servidor local. Os links locais `/w/...` funcionam enquanto esse servidor estiver disponível. Eles **não são URLs HTTPS públicas para incorporar no Notion**. A publicação pública original foi preservada; a migração para outra hospedagem é uma etapa separada, descrita em `docs/INFRAESTRUTURA.md`.

## Executar verificações

```sh
npm run verify       # compara os 158 arquivos com a origem
npm run build        # gera o editor e o Worker para esta instância
npm ci               # instala dependências de teste
npm test             # seleção de testes originais portabilizados em cópias temporárias
npm run test:local   # APIs reais via HTTP local + persistência, com dados temporários
```

Os testes não acessam nem atualizam a produção. `npm run verify` é uma conferência da transferência: depois de você começar a desenvolver em `source/`, ele apontará as diferenças esperadas. Não atualize os hashes para esconder alterações; use Git para acompanhar o desenvolvimento.

Os testes históricos continuam todos incluídos. Alguns exigem navegador ou fixtures temporárias de sessões anteriores e não fazem parte da seleção portátil. Veja `docs/VALIDACAO.md`. Testes DOM não substituem validação visual em navegador e no Notion.

## O que precisa ser migrado separadamente

**Código-fonte completo não é uma cópia dos dados de produção nem do armazenamento do seu navegador.** Não foram exportados registros de clientes, artes privadas, chaves de edição, tokens de publicação, bancos ou buckets da hospedagem.

Antes de trocar de ambiente/domínio, abra o Ateliê no navegador/dispositivo em que seus projetos estão salvos:

1. Exporte cada projeto em JSON pelo recurso de exportação do editor e guarde também uma versão HTML quando útil. Reimporte os JSONs na instância nova.
2. Em Minha biblioteca, exporte a biblioteca de grupos (`atelier-minha-biblioteca.json`) e importe no novo ambiente.
3. Guarde os arquivos das suas fontes. O projeto pode incorporar as fontes utilizadas; fontes importadas que não aparecem nos projetos continuam pertencendo ao armazenamento do navegador e precisam ser reimportadas.
4. Salve os arquivos originais de imagens/mídias pessoais; recursos externos por URL precisam continuar acessíveis.
5. Para levar tarefas compartilhadas e publicações existentes mantendo IDs e links, será necessária uma exportação autorizada do D1 e do R2, além de configuração de domínio/rotas. Esta transferência não acessou esses dados. Subir o código em outro domínio não redireciona os links já colados no Notion.

**JSONs de projetos e backups de dados podem conter chaves de edição/publicação.** Guarde-os de forma privada; não acrescente esses arquivos a um repositório público ou a esta distribuição de código.

## Continuar com Gemini

Abra esta pasta no Antigravity e peça ao agente:

> Leia README.md, AGENTS.md, docs/ARQUITETURA.md, docs/CONTINUIDADE.md e EXPORT-REPORT.json. Continue o desenvolvimento do Ateliê existente a partir de source/ui/src e source/worker. Preserve os recursos atuais. Use npm run dev para executar localmente. Não recrie o aplicativo e não publique na hospedagem original. Antes de mudar infraestrutura ou dados, proponha a migração correspondente.

## Licenças e limites

Preserve os avisos em `source/ui/licenses`, metadados das fontes e `docs/font-licenses`. Fontes de catálogos e fontes próprias mantêm suas licenças; a disponibilidade em um catálogo não significa domínio público. Esta cópia não concede direitos adicionais sobre fontes, imagens ou ícones.

Não foram incluídos `.git`, dependências instaladas, caches, bancos, `.env` reais ou pastas temporárias. Para iniciar seu próprio histórico, você pode executar `git init` nesta raiz, revisar os arquivos e fazer seu primeiro commit.

## Atualização da transferência — versão 32

Este pacote substitui a transferência v31 para continuar o desenvolvimento. Inclui exatamente os fontes da correção publicada: dimensões da prévia e publicação consistentes, tratamento explícito de falha na publicação, identificação v32 e headers para evitar cache do editor. Os controles de aplicar aos demais botões, hover/ativo alternáveis e entradas numéricas dos sliders continuam incluídos.

Não é necessário reaplicar atelier-v32-correcao.patch neste projeto: as mudanças já fazem parte dos fontes. Os dados privados do navegador/produção continuam exigindo migração separada, conforme as instruções acima.
