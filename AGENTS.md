# Continuidade do Ateliê

Este é o projeto existente, não um pedido para recriá-lo. Leia README.md e docs antes de editar.

- Fontes de desenvolvimento: source/ui/src; backend: source/worker; migrações: source/drizzle.
- A versão de referência é 32, commit registrado em SOURCE-PROVENANCE.json.
- tools/ é uma camada de portabilidade adicionada no handoff. A produção não foi modificada.
- Não publique, não envie commits à hospedagem Sites original e não reutilize a identidade source/.openai/hosting.json sem instrução explícita.
- Não exponha credenciais ou chaves de edição. .env, .local-data e backups pessoais nunca devem entrar no Git.
- Evite editar somente source/ui/editor.html: é um snapshot compilado. npm run dev/build monta os fontes atuais de ui/src por meio do builder original.
- Faça mudanças incrementais, preserve o editor, exportador, publicação, catálogos, templates, projetos, biblioteca e central de tarefas.
- npm test usa cópias portáteis dos testes originais; leia docs/VALIDACAO.md. npm run test:local cobre a infraestrutura local, não equivale a teste visual.
- Para outra hospedagem pública, configure DB e BUCKET e URLs próprias. Localhost não serve como embed público do Notion.
- O tamanho externo do iframe no Notion pertence ao Notion. Não prometa ajustá-lo automaticamente apenas com CSS dentro do widget.
