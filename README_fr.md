![](asserts/logo1.png)

# Awesome Serveurs MCP ![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

Une liste organisée et pilotée par la communauté de serveurs, outils, frameworks, clients et utilitaires Model Context Protocol (MCP) remarquables. MCP est un protocole ouvert qui permet aux modèles d'IA d'interagir en toute sécurité avec des ressources locales et distantes via des implémentations de serveurs standardisées.

---

Remarque : Nous fournissons une [liste complète des serveurs MCP](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/Full-List-of-MCP-Servers.xlsx), compilée par un robot d'exploration web et contenant environ 6000 entrées.

---

## Tous les documents
> Traducteurs recherchés ! Aidez-nous via l'[issue traducteurs](https://github.com/YuzeHao2023/Awesome-MCP-Servers/issues/1).

**Lisez notre documentation dans les langues suivantes :**

| Langue | Lien                                                                 |
|--------|----------------------------------------------------------------------|
| English  | [English](https://github.com/YuzeHao2023/Awesome-MCP-Servers?tab=readme-ov-file) |
| 简体中文  | [简体中文](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_zh_CN.md) |
| 繁體中文  | [繁體中文](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_zh_TW.md) |
| 日本語    | [日本語](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_ja.md) |
| 한국어    | [한국어](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_ko.md) |
| Français  | [Français](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_fr.md) |

---

## Qu'est-ce que MCP ?

[MCP](https://modelcontextprotocol.io/) (Model Context Protocol) est un protocole ouvert qui permet aux modèles d'IA d'interagir en toute sécurité avec des ressources locales et distantes via des implémentations de serveurs standardisées. Cette liste se concentre sur les serveurs MCP prêts pour la production et expérimentaux qui étendent les capacités de l'IA grâce à l'accès aux fichiers, aux connexions aux bases de données, aux intégrations d'API et à d'autres services contextuels.

---

## Tutoriels

* [Model Context Protocol (MCP) Quickstart](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [Configurer l'application Claude Desktop avec une base de données SQLite](https://youtu.be/wxCCzo9dGj0)

## Communauté

* [r/mcp Reddit](https://www.reddit.com/r/mcp)
* [Serveur Discord](https://glama.ai/mcp/discord)

---

## ⚠️ Avertissement de sécurité

L'exécution de serveurs MCP sans sandbox approprié peut exécuter du code arbitraire sur votre système avec les mêmes autorisations que le processus hôte, créant des risques de sécurité importants.

Risques de sécurité :
- Accès système : Accès complet aux fichiers, au réseau et aux ressources système
- Exécution de code : Peut exécuter n'importe quelle commande sur votre machine
- Injection de prompts : Des prompts malveillants pourraient déclencher des actions serveur non intentionnelles
- Exposition des données : Des données sensibles peuvent être consultées ou divulguées

Bonnes pratiques recommandées :
- Utiliser les implémentations officielles (⭐) en priorité
- Exécuter les serveurs dans des VMs ou des conteneurs isolés
- Examiner le code et la configuration avant l'installation
- Appliquer le principe du moindre privilège
- Surveiller l'activité et les journaux du serveur

---

## Clients pris en charge (exemples)

De nombreux clients et interfaces MCP peuvent se connecter aux serveurs de cette liste. Exemples (non exhaustifs) :
- Claude Desktop / clients Claude
- Zed
- Sourcegraph Cody
- Cursor
- Visual Studio Code
- LibreChat
- Divers clients CLI et basés sur navigateur

---

## Implémentations de serveurs (catégories)

- 📂 Systèmes de fichiers
- 📦 Sandbox & Virtualisation
- 🔄 Contrôle de version
- ☁️ Stockage cloud
- 🗄️ Bases de données
- 💬 Communication
- 📈 Monitoring
- 🔍 Recherche & Web
- 🗺️ Services de localisation
- 🎯 Marketing
- 📝 Prise de notes
- ⚡ Plateformes cloud
- ⚙️ Automatisation des workflows
- 🤖 Automatisation système
- 📱 Réseaux sociaux
- 🎮 Jeux
- 💹 Finance
- 🧬 Recherche & Données
- 🤝 Services IA
- 💻 Outils de développement
- 📊 Visualisation de données
- 🆔 Identité
- 🔗 Agrégateurs
- 💬 Langue & Traduction
- 🔒 Sécurité
- 🔌 IoT
- 🧑‍🎨 Art & Littérature
- 🛒 E-commerce
- 📦 Plateformes de données
- 🤖 Robotique & IA physique

Légende :
- ⭐ Implémentation officielle du protocole

---

# Serveurs de référence

Les serveurs et exemples SDK suivants démontrent les fonctionnalités MCP :

- Everything (serveur de référence/test avec prompts, ressources et outils)
  - https://github.com/modelcontextprotocol/servers/blob/main/src/everything
- Fetch
  - https://github.com/modelcontextprotocol/servers/tree/main/src/fetch
- Filesystem
  - https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
- Git
  - https://github.com/modelcontextprotocol/servers/tree/main/src/git
- Memory
  - https://github.com/modelcontextprotocol/servers/tree/main/src/memory
- Sequential Thinking
  - https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking
- Time
  - https://github.com/modelcontextprotocol/servers/blob/main/src/time

---

# Serveurs officiels

Les intégrations officielles sont maintenues par des entreprises construisant des serveurs MCP prêts pour la production pour leurs plateformes. (⭐ si indiqué)

- 1mcpserver — https://github.com/particlefuture/1mcpserver
- 21st.dev Magic — https://github.com/21st-dev/magic-mcp
- 4everland/4everland-hosting-mcp — https://github.com/4everland/4everland-hosting-mcp
- Adfin — https://github.com/Adfin-Engineering/mcp-server-adfin
- AgentQL — https://github.com/tinyfish-io/agentql-mcp
- AgentRPC — https://github.com/agentrpc/agentrpc
- Aiven — https://github.com/Aiven-Open/mcp-aiven
- AlibabaCloud DevOps MCP — https://github.com/aliyun/alibabacloud-devops-mcp-server
- Apify Actors — https://github.com/apify/actors-mcp-server
- Box — https://github.com/box-community/mcp-server-box (⭐)
- Cloudflare — https://github.com/cloudflare/mcp-server-cloudflare (⭐)
- GitHub — https://github.com/github/github-mcp-server (officiel)
- Notion — https://github.com/makenotion/notion-mcp (officiel)
- Stripe — https://github.com/stripe/agent-toolkit/tree/main (⭐)
- PayPal — https://github.com/paypal/agent-toolkit/tree/main (⭐)
- Tinybird — https://github.com/tinybirdco/mcp-tinybird (⭐)

---

# Outils & Utilitaires

Utilitaires pour rechercher, installer, gérer et travailler avec les serveurs MCP :

- mcp-get — CLI pour installer/gérer les serveurs MCP pour Claude Desktop — https://github.com/michaellatman/mcp-get
- Remote MCP — Solution de communication MCP distante — https://github.com/ssut/Remote-MCP
- yamcp — Model Context Workspace Manager — https://github.com/hamidra/yamcp
- ToolHive — Utilitaire léger simplifiant le déploiement — https://github.com/StacklokLabs/toolhive
- MCP Installer — https://github.com/anaisbetts/mcp-installer

---

## Catégorie : Systèmes de fichiers (📂)

- Backup — https://github.com/hexitex/MCP-Backup-Server
- FileStash — https://github.com/mickael-kerjean/filestash/tree/master/server/plugin/plg_handler_mcp
- FileSystem (référence modelcontextprotocol) — https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
- FileSystem (mark3labs) — https://github.com/mark3labs/mcp-filesystem-server
- Everything Search — https://github.com/mamertofabian/mcp-everything-search
- llm-context — https://github.com/cyberchitta/llm-context.py

---

## Catégorie : Sandbox & Virtualisation (📦)

- Microsandbox (⭐) — https://github.com/microsandbox/microsandbox
- E2B (⭐) — https://github.com/e2b-dev/mcp-server
- Docker (QuantGeekDev) — https://github.com/QuantGeekDev/docker-mcp

---

## Catégorie : Contrôle de version (🔄)

- GitHub (officiel) — https://github.com/github/github-mcp-server
- GitHub Repos Manager — https://github.com/kurdin/github-repos-manager-mcp
- GitLab — https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab
- Git (direct) — https://github.com/modelcontextprotocol/servers/tree/main/src/git
- Phabricator — https://github.com/baba786/phabricator-mcp-server
- Gitingest-MCP — https://github.com/puravparab/Gitingest-MCP

---

## Catégorie : Stockage cloud (☁️)

- Google Drive — https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive
- Box (⭐) — https://developer.box.com/guides/box-mcp/
- VideoDB (agent-toolkit, ⭐) — https://github.com/video-db/agent-toolkit/tree/main/modelcontextprotocol
- Microsoft 365 — https://github.com/softeria/ms-365-mcp-server

---

## Catégorie : Bases de données (🗄️)

- PostgreSQL — https://github.com/modelcontextprotocol/servers/tree/main/src/postgres
- SQLite — https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite
- DuckDB — https://github.com/ktanaka101/mcp-server-duckdb
- Excel — https://github.com/haris-musa/excel-mcp-server
- BigQuery — https://github.com/LucasHild/mcp-server-bigquery
- Neon (⭐) — https://github.com/neondatabase/mcp-server-neon
- Qdrant (⭐) — https://github.com/qdrant/mcp-server-qdrant/
- MongoDB — https://github.com/kiliczsh/mcp-mongo-server
- MySQL — https://github.com/designcomputer/mysql_mcp_server
- Airtable — https://github.com/domdomegg/airtable-mcp-server
- Snowflake — https://github.com/isaacwasserman/mcp-snowflake-server

---

## Catégorie : Communication (💬)

- Slack — https://github.com/korotovsky/slack-mcp-server
- LINE Official Account (⭐) — https://github.com/line/line-bot-mcp-server
- Linear — https://github.com/jerhadf/linear-mcp-server
- Atlassian — https://github.com/sooperset/mcp-atlassian
- Carbon Voice (⭐) — https://github.com/PhononX/cv-mcp-server

---

## Catégorie : Monitoring (📈)

- Metoro — https://github.com/metoro-io/metoro-mcp-server
- Raygun — https://github.com/MindscapeHQ/mcp-server-raygun
- Sentry — https://github.com/modelcontextprotocol/servers/tree/main/src/sentry

---

## Catégorie : Recherche & Web (🔍)

- Puppeteer — https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer
- Brave Search — https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search
- Bright Data — https://github.com/luminati-io/brightdata-mcp
- Scrapeless — https://github.com/scrapeless-ai/scrapeless-mcp-server

---

## Catégorie : Services de localisation (🗺️)

- Google Maps — https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps

---

## Catégorie : Marketing (🎯)

- Agent Mindshare — https://agentmindshare.com

---

## Catégorie : Prise de notes (📝)

- Notion — https://github.com/danhilse/notion_mcp

---

## Catégorie : Plateformes cloud (⚡)

- Cloudflare (⭐) — https://github.com/cloudflare/mcp-server-cloudflare

---

## Catégorie : Automatisation des workflows (⚙️)

- Make (⭐) — https://github.com/integromat/make-mcp-server
- Zapier — https://zapier.com/mcp

---

## Catégorie : Automatisation système (🤖)

- Shell (wcgw) — https://github.com/rusiaaman/wcgw

---

## Catégorie : Réseaux sociaux (📱)

- YouTube — https://github.com/anaisbetts/mcp-youtube

---

## Catégorie : Jeux (🎮)

- Implémentations Unity

---

## Catégorie : Finance (💹)

Paiements, données de marché et outils financiers.

- PayPal (⭐) — https://github.com/paypal/agent-toolkit
- Stripe (⭐) — https://github.com/stripe/agent-toolkit
- LongPort OpenAPI (⭐) — https://github.com/longportapp/openapi/tree/main/mcp
- x402engine-mcp (50+ APIs payantes pour agents IA via micropaiements HTTP 402) — https://github.com/agentc22/x402engine-mcp
- TWZRD Agent Intel (MCP x402 natif Solana pour la notation de confiance des agents IA — notation de confiance et vérification de micropaiements x402 pour agents IA sur Solana) — https://intel.twzrd.xyz

---

## Catégorie : Recherche & Données (🧬)

- ArXiv — https://github.com/blazickjp/arxiv-mcp-server

---

## Catégorie : Services IA (🤝)

- OpenAI — https://github.com/pierrebrunelle/mcp-server-openai

---

## Catégorie : Outils de développement (💻)

- Currents (⭐) — https://github.com/currents-dev/currents-mcp

---

## Catégorie : Visualisation de données (📊)

- VegaLite — https://github.com/isaacwasserman/mcp-vegalite-server

---

## Catégorie : Identité (🆔)

- Keycloak — https://github.com/ChristophEnglisch/keycloak-model-context-protocol

---

## Catégorie : Agrégateurs (🔗)

- MCPJungle — https://github.com/mcpjungle/MCPJungle

---

## Catégorie : Langue & Traduction (💬)

- Lara (⭐) — https://github.com/translated/lara-mcp

---

## Catégorie : Sécurité (🔒)

- Semgrep — https://github.com/semgrep/mcp

---

## Catégorie : IoT (🔌)

- Coreflux MQTT — https://github.com/CorefluxCommunity/CorefluxMCPServer

---

## Serveurs communautaires

Une liste étendue de serveurs maintenus par la communauté est incluse dans le document principal. Consultez la documentation pour la liste complète.

---

# Notes

- Exécutez les serveurs communautaires non fiables dans un environnement isolé tel qu'un conteneur ou une VM.
- En production, privilégiez les implémentations officielles (⭐).
- Vérifiez la méthode de transport (stdio, SSE, HTTP), l'authentification et les exemples de clients dans le dépôt de chaque serveur.
