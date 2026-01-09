![](asserts/logo1.png)

# Awesome MCP Servers ![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

A curated, community-driven list of awesome Model Context Protocol (MCP) servers, tools, frameworks, clients, and utilities. MCP is an open protocol that enables AI models to securely interact with local and remote resources through standardized server implementations.

---

BTW, we provide a [full list of MCP (Master Control Program) Servers](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/Full-List-of-MCP-Servers.xlsx), which is compiled by a web crawler and contains approximately 6000 entries.

---

## All Documents
> Call for translators! [We're looking for translators](https://github.com/YuzeHao2023/Awesome-MCP-Servers/issues/1) to help translate this spec for everyone!

**Read our documentation in the following languages:**

| Language | Link                                                                 |
|----------|---------------------------------------------------------------------|
| English  | [English](https://github.com/YuzeHao2023/Awesome-MCP-Servers?tab=readme-ov-file) |
| 简体中文  | [简体中文](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_zh_CN.md) |
| 繁體中文  | [繁體中文](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_zh_TW.md) |
| 日本語    | [日本語](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_ja.md) |
| 한국어    | [한국어](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_ko.md) |

---

## What is MCP?

[MCP](https://modelcontextprotocol.io/) is an open protocol that enables AI models to securely interact with local and remote resources through standardized server implementations. This list focuses on production-ready and experimental MCP servers that extend AI capabilities through file access,  database connections, API integrations, and other contextual services.

---

# Contents

## Tutorials

* [Model Context Protocol (MCP) Quickstart](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [Setup Claude Desktop App to Use a SQLite Database](https://youtu.be/wxCCzo9dGj0)

## Community

* [r/mcp Reddit](https://www.reddit.com/r/mcp)
* [Discord Server](https://glama.ai/mcp/discord)

---

## ⚠️ Security Warning

When running MCP servers without proper sandboxing, they can execute arbitrary code on your system with the same permissions as the host process. This creates significant security risks.

Warning summary:
- System Access: Full access to files, network, and system resources
- Code Execution: Can run commands on your machine
- Prompt Injection: Malicious prompts could trigger unintended server actions
- Data Exposure: Sensitive data may be accessed or leaked

Best practices:
- Use official implementations (marked with ⭐) when available
- Run servers in VMs or isolated containers
- Review code and configuration before installation
- Limit permissions to the minimum required
- Monitor server activity and logs

---

## Examples of Supported Clients

Many MCP clients and UIs can connect to servers listed here. Examples include (but are not limited to):
- Claude Desktop / Claude clients
- Zed
- Sourcegraph Cody
- Cursor
- Visual Studio Code
- LibreChat
- Various CLI and browser-based clients

(Icons and links for specific clients are commonly shown on the individual server/project pages.)

---

## Server Implementations (Categories)

- 📂 File Systems
- 📦 Sandbox & Virtualization
- 🔄 Version Control
- ☁️ Cloud Storage
- 🗄️ Databases
- 💬 Communication
- 📈 Monitoring
- 🔍 Search & Web
- 🗺️ Location Services
- 🎯 Marketing
- 📝 Note Taking
- ⚡ Cloud Platforms
- ⚙️ Workflow Automation
- 🤖 System Automation
- 📱 Social Media
- 🎮 Gaming
- 💹 Finance
- 🧬 Research & Data
- 🤝 AI Services
- 💻 Development Tools
- 📊 Data Visualization
- 🆔 Identity
- 🔗 Aggregators
- 💬 Language & Translation
- 🔒 Security
- 🔌 IoT
- 🧑‍🎨 Art & Literature
- 🛒 E-Commerce
- 📦 Data Platforms
- 🤖 Robotics & Physical AI

Legend:
- ⭐ Official protocol implementation
- 1,2,3,... Implementation ordering when multiple exist

---

# Reference Servers

These are example/reference servers and core SDK examples demonstrating MCP features.

- Everything (Reference / test server with prompts, resources, and tools)
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

# Official Servers

Official integrations are maintained by companies building production-ready MCP servers for their platforms. (Marked with ⭐ when present)

- 1mcpserver — https://github.com/particlefuture/1mcpserver
- 21st.dev Magic — https://github.com/21st-dev/magic-mcp
- 4everland/4everland-hosting-mcp — https://github.com/4everland/4everland-hosting-mcp
- Adfin — https://github.com/Adfin-Engineering/mcp-server-adfin
- Agent Mindshare — https://agentmindshare.com
- AgentQL — https://github.com/tinyfish-io/agentql-mcp
- AgentRPC — https://github.com/agentrpc/agentrpc
- Aiven — https://github.com/Aiven-Open/mcp-aiven
- AlibabaCloud DevOps MCP — https://github.com/aliyun/alibabacloud-devops-mcp-server
- Apify Actors — https://github.com/apify/actors-mcp-server
- Box — https://github.com/box-community/mcp-server-box (⭐)
- Cloudflare — https://github.com/cloudflare/mcp-server-cloudflare (⭐)
- GitHub — https://github.com/github/github-mcp-server (official)
- Notion — https://github.com/makenotion/notion-mcp (official)
- Stripe — https://github.com/stripe/agent-toolkit/tree/main (⭐)
- PayPal — https://github.com/paypal/agent-toolkit/tree/main (⭐)
- Tinybird — https://github.com/tinybirdco/mcp-tinybird (⭐)
- Cloud-run, AWS, Azure, Google offerings — various official MCP servers in the awslabs and Google repos under modelcontextprotocol.

(For a full list of official servers and vendor-maintained implementations, see the "Official Servers" and "Reference Servers" in this document and the linked repos.)

---

# Tools & Utilities

Helpful utilities to discover, install, manage, and work with MCP servers.

Server Managers:
- mcp-get — CLI tool to install and manage MCP servers (Claude Desktop oriented) — https://github.com/michaellatman/mcp-get
- mxcp — An open-source framework for building secure enterprise MCP tools — http://github.com/raw-labs/mxcp
- Remote MCP — Solution for remote MCP communication — https://github.com/ssut/Remote-MCP
- yamcp — Model Context Workspace Manager — https://github.com/hamidra/yamcp
- ToolHive — Lightweight utility to simplify deployment & management — https://github.com/StacklokLabs/toolhive
- MCP Installer — https://github.com/anaisbetts/mcp-installer

Other utilities:
- Secure Fetch — secure fetch to prevent access to local resources — https://github.com/appsec-innovation-labs/secure-mcp-fetch
- mcp-cli — CLI inspector for MCP servers — https://github.com/wong2/mcp-cli
- mcp-get, mcp-installer, and similar utilities to simplify installation and discovery.

---

## Category: File Systems (📂)

Provides access to local or remote file systems with configurable permissions.

- Backup — https://github.com/hexitex/MCP-Backup-Server
- FileStash — https://github.com/mickael-kerjean/filestash/tree/master/server/plugin/plg_handler_mcp
- FileSystem (modelcontextprotocol reference) — https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem (1)
- FileSystem (mark3labs) — https://github.com/mark3labs/mcp-filesystem-server (2)
- Everything Search — https://github.com/mamertofabian/mcp-everything-search
- fast-filesystem-mcp — https://github.com/efforthye/fast-filesystem-mcp
- llm-context — https://github.com/cyberchitta/llm-context.py

---

## Category: Sandbox & Virtualization (📦)

Secure sandbox environments for code execution.

- Microsandbox (⭐) — https://github.com/microsandbox/microsandbox
- E2B (⭐) — https://github.com/e2b-dev/mcp-server
- Docker (QuantGeekDev) — https://github.com/QuantGeekDev/docker-mcp

---

## Category: Version Control (🔄)

Git and version control related MCP servers.

- GitHub (1) — https://github.com/github/github-mcp-server (official)
- GitHub Repos Manager — https://github.com/kurdin/github-repos-manager-mcp
- GitLab — https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab
- Git (direct) — https://github.com/modelcontextprotocol/servers/tree/main/src/git
- Phabricator — https://github.com/baba786/phabricator-mcp-server
- Gitingest-MCP — https://github.com/puravparab/Gitingest-MCP

---

## Category: Cloud Storage (☁️)

Access to cloud storage platforms.

- Google Drive — https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive
- Box (⭐) — https://developer.box.com/guides/box-mcp/
- VideoDB (agent-toolkit) — https://github.com/video-db/agent-toolkit/tree/main/modelcontextprotocol (⭐)
- Microsoft 365 — https://github.com/softeria/ms-365-mcp-server

---

## Category: Databases (🗄️)

Database access with schema inspection and query capabilities.

- PostgreSQL — https://github.com/modelcontextprotocol/servers/tree/main/src/postgres
- SQLite — https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite
- DuckDB — https://github.com/ktanaka101/mcp-server-duckdb
- Excel — https://github.com/haris-musa/excel-mcp-server
- BigQuery — https://github.com/LucasHild/mcp-server-bigquery (1) & https://github.com/ergut/mcp-bigquery-server (2)
- Neon (⭐) — https://github.com/neondatabase/mcp-server-neon
- Qdrant (⭐) — https://github.com/qdrant/mcp-server-qdrant/
- MongoDB — https://github.com/kiliczsh/mcp-mongo-server
- MongoDB Lens — https://github.com/furey/mongodb-lens
- MySQL — https://github.com/designcomputer/mysql_mcp_server
- Airtable — https://github.com/domdomegg/airtable-mcp-server
- Snowflake — https://github.com/isaacwasserman/mcp-snowflake-server
- DBUtils — https://github.com/donghao1393/mcp-dbutils
- TiDB — https://github.com/c4pt0r/mcp-server-tidb
- NocoDB — https://github.com/edwinbernadus/nocodb-mcp-server
- Couchbase (⭐) — https://github.com/Couchbase-Ecosystem/mcp-server-couchbase
- Redis (⭐) — https://github.com/redis/mcp-redis
- Many other DB-specific servers are listed in Community Servers.

---

## Category: Communication (💬)

Integration with chat and messaging platforms.

- Slack — https://github.com/korotovsky/slack-mcp-server
- LINE Official Account (⭐) — https://github.com/line/line-bot-mcp-server
- Linear — https://github.com/jerhadf/linear-mcp-server
- Atlassian — https://github.com/sooperset/mcp-atlassian
- Carbon Voice (⭐) — https://github.com/PhononX/cv-mcp-server
- ntfy — https://github.com/gitmotion/ntfy-me-mcp

---

## Category: Monitoring (📈)

Access observability and monitoring systems.

- Metoro — https://github.com/metoro-io/metoro-mcp-server
- Raygun — https://github.com/MindscapeHQ/mcp-server-raygun
- Sentry — https://github.com/modelcontextprotocol/servers/tree/main/src/sentry
- sslmon — https://github.com/firesh/sslmon-mcp
- Signoz — https://github.com/DrDroidLab/signoz-mcp-server
- VictoriaMetrics — https://github.com/VictoriaMetrics-Community/mcp-victoriametrics

---

## Category: Search & Web (🔍)

Web fetching, scraping, and search.

- Puppeteer — https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer
- Brave Search — https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search
- Bright Data — https://github.com/luminati-io/brightdata-mcp
- Dumpling AI — https://github.com/Dumpling-AI/mcp-server-dumplingai
- Fetch — https://github.com/modelcontextprotocol/servers/tree/main/src/fetch
- Kagi Search — https://github.com/ac3xx/mcp-servers-kagi
- Exa Search (⭐) — https://github.com/exa-labs/exa-mcp-server
- NYTimes — https://github.com/angheljf/nyt
- Google News — https://github.com/ChanMeng666/server-google-news
- Scrapeless — https://github.com/scrapeless-ai/scrapeless-mcp-server
- Search1API — https://github.com/fatwang2/search1api-mcp
- RivalSearchMCP — https://github.com/damionrashford/RivalSearchMCP
- Tavily — https://github.com/Tomatio13/mcp-server-tavily
- ArXiv — https://github.com/blazickjp/arxiv-mcp-server
- PapersWithCode — https://github.com/hbg/mcp-paperswithcode
- Playwright — https://github.com/executeautomation/mcp-playwright
- Websearch (SearXNG) — https://github.com/mnhlt/WebSearch-MCP and https://github.com/ihor-sokoliuk/mcp-searxng
- Apify Actors & RAG Web Browser — https://github.com/apify/actors-mcp-server and https://github.com/apify/mcp-server-rag-web-browser
- Scrapeless and many web-scraping-focused MCP servers are listed in Community Servers.

---

## Category: Location Services (🗺️)

Mapping and geolocation.

- Campertunity — https://github.com/campertunity/mcp-server
- Google Maps — https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps
- IPLocate — https://github.com/iplocate/mcp-server-iplocate
- IP2Location.io — https://github.com/ip2location/mcp-ip2location-io
- QGIS — https://github.com/jjsantos01/qgis_mcp

---

## Category: Marketing (🎯)

Marketing and analytics tools.

- Agent Mindshare — https://agentmindshare.com
- Open Strategy Partners Marketing Tools — https://github.com/open-strategy-partners/osp_mark
- Fathom Analytics — https://github.com/mackenly/mcp-fathom-analytics
- Facebook Ads — https://github.com/gomarble-ai/facebook-ads-mcp-server
- Google Ads — https://github.com/gomarble-ai/google-ads-mcp-server

---

## Category: Note Taking (📝)

Personal knowledge and notes integrations.

- eBook-mcp — https://github.com/onebirdrocks/ebook-mcp
- Obsidian (1/2) — https://github.com/MarkusPfundstein/mcp-obsidian and https://github.com/calclavia/mcp-obsidian
- Notion (1/2) — https://github.com/danhilse/notion_mcp and https://github.com/suekou/mcp-notion-server
- Apple Notes — https://github.com/sirmews/apple-notes-mcp (macOS)
- Slite — https://github.com/fajarmf/slite-mcp
- Todoist — https://github.com/abhiz123/todoist-mcp-server
- Google Keep — https://github.com/feuerdev/keep-mcp

---

## Category: Cloud Platforms (⚡)

Cloud vendors and orchestration.

- Cloudflare (⭐) — https://github.com/cloudflare/mcp-server-cloudflare
- Kubernetes (multiple implementations) — https://github.com/strowk/mcp-k8s-go (1), https://github.com/weibaohui/k8m (2), https://github.com/StacklokLabs/mkp (3)
- Tinybird (⭐) — https://github.com/tinybirdco/mcp-tinybird
- Google Cloud Run — https://github.com/GoogleCloudPlatform/cloud-run-mcp
- Render — https://render.com/docs/mcp-server

---

## Category: Workflow Automation (⚙️)

Automation platforms and workflow tools.

- Make (⭐) — https://github.com/integromat/make-mcp-server
- Taskade (⭐) — https://github.com/taskade/mcp
- Zapier — https://zapier.com/mcp
- Pipedream — https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol
- Tool aggregators like Rube, Rube/Composio and MCPJungle are listed in Aggregators.

---

## Category: System Automation (🤖)

Shell, OS, and task automation.

- Shell (wcgw) — https://github.com/rusiaaman/wcgw
- Windows CLI — https://github.com/SimonB97/win-cli-mcp
- Windows Control — https://github.com/Cheffromspace/nutjs-windows-control
- Command Line — https://github.com/phialsbasement/cmd-mcp-server
- Apple Shortcuts — https://github.com/recursechat/mcp-server-apple-shortcuts

---

## Category: Social Media (📱)

Social platforms integration.

- BlueSky — https://github.com/keturiosakys/bluesky-context-server
- YouTube — https://github.com/anaisbetts/mcp-youtube and https://github.com/kimtaeyoon83/mcp-server-youtube-transcript
- Spotify — https://github.com/varunneal/spotify-mcp
- TikTok — https://github.com/Seym0n/tiktok-mcp
- Instagram DMs — https://github.com/trypeggy/instagram_dm_mcp
- X/Twitter — https://github.com/mbelinky/x-mcp-server

---

## Category: Gaming (🎮)

Game engines and tooling.

- Unity Engine (various) — https://github.com/IvanMurzak/Unity-MCP, https://github.com/CoderGamester/mcp-unity, https://github.com/codemaestroai/advanced-unity-mcp

---

## Category: Finance (💹)

Payments, market data, and finance tools.

- Octagon (⭐) — https://github.com/OctagonAI/octagon-mcp-server
- CoinMarket — https://github.com/anjor/coinmarket-mcp-server
- Chargebee (⭐) — https://github.com/chargebee/agentkit/tree/main/modelcontextprotocol
- DexPaprika (⭐) — https://github.com/donbagger/dexpaprika-mcp-server
- Mercado Pago — https://mcp.mercadopago.com/
- PayPal (⭐) — https://github.com/paypal/agent-toolkit
- Stripe (⭐) — https://github.com/stripe/agent-toolkit
- LongPort OpenAPI (⭐) — https://github.com/longportapp/openapi/tree/main/mcp

---

## Category: Research & Data (🧬)

Papers, datasets, and domain data.

- ArXiv — https://github.com/blazickjp/arxiv-mcp-server
- Ancestry — https://github.com/reeeeemo/ancestry-mcp
- Probe.dev — https://mcp.probe.dev
- OpenNutrition — https://github.com/deadletterq/mcp-opennutrition
- Congress (legislative data) — https://github.com/amurshak/congressMCP

---

## Category: AI Services (🤝)

AI model & ML service integrations.

- Agentset AI — https://github.com/agentset-ai/mcp-server
- OpenAI — https://github.com/pierrebrunelle/mcp-server-openai
- OpenAI Compatible Chat — https://github.com/pyroprompts/any-chat-completions-mcp
- Perplexity — https://github.com/tanigami/mcp-server-perplexity
- LlamaCloud — https://github.com/run-llama/mcp-server-llamacloud
- HuggingFace Spaces — https://github.com/evalstate/mcp-hfspace
- PiAPI — https://github.com/apinetwork/piapi-mcp-server
- Chronulus AI — https://github.com/ChronulusAI/chronulus-mcp
- Creatify — https://github.com/TSavo/creatify-mcp
- ZenML (⭐) — https://github.com/zenml-io/mcp-zenml

---

## Category: Development Tools (💻)

Developer-focused MCP servers and tools.

- CentralMind/Gateway — https://github.com/centralmind/gateway
- Currents (⭐) — https://github.com/currents-dev/currents-mcp
- Octocode — https://github.com/bgauryy/octocode-mcp
- OpenAPI Schema Explorer — https://github.com/kadykov/mcp-openapi-schema-explorer
- OpenRPC — https://github.com/shanejonas/openrpc
- Postman — https://github.com/delano/postman-mcp-server
- QA Sphere (⭐) — https://github.com/Hypersequent/qasphere-mcp
- marimo (⭐) — https://github.com/marimo-team/codemirror-mcp
- Figma — https://github.com/GLips/Figma-Context-MCP
- Comet Opik (⭐) — https://github.com/comet-ml/opik-mcp
- VSCode Devtools — https://github.com/biegehydra/BifrostMCP
- Mastra/mcp (⭐) — https://github.com/mastra-ai/mastra/tree/main/packages/mcp
- Bucket — https://github.com/bucketco/bucket-javascript-sdk/tree/main/packages/cli#model-context-protocol
- DefangLabs/defang — https://github.com/DefangLabs/defang
- many others in Community Servers and Official Servers

---

## Category: Data Visualization (📊)

Charting and diagram tools.

- VegaLite — https://github.com/isaacwasserman/mcp-vegalite-server
- Chart (AntV) — https://github.com/antvis/mcp-server-chart
- ECharts — https://github.com/hustcc/mcp-echarts
- Mermaid — https://github.com/hustcc/mcp-mermaid
- unified-diff-mcp — https://github.com/gorosun/unified-diff-mcp

---

## Category: Identity (🆔)

Identity and access management.

- Keycloak — https://github.com/ChristophEnglisch/keycloak-model-context-protocol

---

## Category: Aggregators (🔗)

Single MCP endpoints that expose many integrations.

- MCPJungle — https://github.com/mcpjungle/MCPJungle
- Rube — https://rube.composio.dev
- Pipedream — https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol
- Zapier — https://zapier.com/mcp
- Plugged.in — https://github.com/VeriTeknik/pluggedin-mcp-proxy
- MCP Aggregator / Combine — https://github.com/nazar256/combine-mcp
- Magg — https://github.com/sitbon/magg

---

## Category: Language & Translation (💬)

Translation and language services.

- Lara (⭐) — https://github.com/translated/lara-mcp

---

## Category: Security (🔒)

Security-focused servers and scanning tools.

- Semgrep — https://github.com/semgrep/mcp
- Microsoft Entra ID — Microsoft-related MCPs for identity
- Netwrix (⭐) — https://github.com/netwrix/mcp-server-naa
- OSV — https://github.com/StacklokLabs/osv-mcp
- Vulert — https://vulert.com
- Thales / CDSP servers — various MCP integrations for secrets & keys

---

## Category: IoT (🔌)

MCP servers for device and IoT integration.

- Coreflux MQTT — https://github.com/CorefluxCommunity/CorefluxMCPServer

---

## Category: Art & Literature (🧑‍🎨)

Books, libraries, and creative tools.

- MCP Open Library — https://github.com/8enSmith/mcp-open-library
- Pollinations — https://github.com/pollinations/model-context-protocol

---

## Category: E-Commerce (🛒)

Commerce and marketplace integrations.

- Mercado Libre — https://mcp.mercadolibre.com/
- ShopSavvy (⭐) — https://github.com/shopsavvy/shopsavvy-mcp-server

---

## Category: Data Platforms (📦)

Orchestration and data pipeline platforms.

- Keboola (⭐) — https://github.com/keboola/keboola-mcp-server

---

## Category: Robotics & Physical AI (🤖)

Robotics and device control.

- Bagel — https://github.com/Extelligence-ai/bagel

---

# Community Servers

A broad collection of community-maintained MCP servers (selected highlights — many more are available in the ecosystem):

- AllInOneMCP / MCP Discovery / MCP of MCPs — https://github.com/particlefuture/MCPDiscovery
- Airtable — https://github.com/domdomegg/airtable-mcp-server
- Agentset — https://github.com/agentset-ai/mcp-server
- Alertmanager — https://github.com/ntk148v/alertmanager-mcp-server
- Algorand — https://github.com/GoPlausible/algorand-mcp
- Android MCP — https://github.com/minhalvp/android-mcp-server
- AniList — https://github.com/yuna0x0/anilist-mcp
- AnkiConnect — https://github.com/spacholski1225/anki-connect-mcp
- APISIX-MCP — https://github.com/api7/apisix-mcp
- Apple Notes — https://github.com/RafalWilinski/mcp-apple-notes
- Apple Shortcuts — https://github.com/recursechat/mcp-server-apple-shortcuts
- AWS EC2 Pricing — https://github.com/trilogy-group/aws-pricing-mcp
- Backup — https://github.com/hexitex/MCP-Backup-Server
- Basecamp — https://github.com/georgeantonopoulos/Basecamp-MCP-Server
- BigQuery servers — https://github.com/LucasHild/mcp-server-bigquery and https://github.com/ergut/mcp-bigquery-server
- Binary Ninja integration — https://github.com/fosdickio/binary_ninja_mcp
- Bing Webmaster Tools — https://github.com/isiahw1/mcp-server-bing-webmaster
- Bluesky — https://github.com/keturiosakys/bluesky-context-server
- BloodHound-MCP — https://github.com/MorDavid/BloodHound-MCP-AI
- Box community server — https://github.com/hmk/box-mcp-server
- Browser MCPs — multiple implementations for local and remote browser automation
- bytebase/dbhub — https://github.com/bytebase/dbhub
- Calculator — https://github.com/githejie/mcp-server-calculator
- CalDAV MCP — https://github.com/dominik1001/caldav-mcp
- Context-aware & discovery servers (context-awesome, ref, etc.)
- Currents — https://github.com/currents-dev/currents-mcp
- DINO-X, Digma, Driflyte, DreamFactory, Dash0, DB-specific servers, and many more.

(For the exhaustive long list of community servers and links, refer to the aggregated listings in community and official sections across the MCP ecosystem. This README collects and organizes the major categories and many example projects; the community maintains a rapidly growing set of servers — check the linked repos for the latest.)

---

# Clients

Clients and UI tools that consume MCP servers:

- MBro — https://github.com/sitbon/magg/blob/main/docs/mbro.md
- mcp-cli — https://github.com/wong2/mcp-cli
- mcp-client — https://github.com/rakesh-eltropy/mcp-client
- MCP-Bridge — https://github.com/SecretiveShell/MCP-Bridge
- MCP-Chatbot (⭐ CLI) — https://github.com/3choff/mcp-chatbot
- Zed — https://github.com/zed-industries/zed
- genkit — https://github.com/firebase/genkit
- Continue — https://github.com/continuedev/continue
- gpt-computer-assistant — https://github.com/Upsonic/gpt-computer-assistant
- MCP-Connect — https://github.com/EvalsOne/mcp-connect
- codemirror-mcp — https://github.com/marimo-team/codemirror-mcp
- LibreChat — https://www.librechat.ai/
- mcphub.nvim — https://github.com/ravitemer/mcphub.nvim
- Nerve — https://github.com/evilsocket/nerve
- Shinkai — http://github.com/dcSpark/shinkai-apps/
- mcps-playground — https://mcpsplayground.com/chat

---

# Frameworks

Frameworks and scaffolding for building MCP servers:

- create-mcp-ts — https://github.com/stephencme/create-mcp-ts
- LiteMCP — https://github.com/wong2/litemcp
- mcp-framework — https://github.com/QuantGeekDev/mcp-framework
- MCP Plexus — https://github.com/super-i-tech/mcp_plexus
- oatpp-mcp — https://github.com/oatpp/oatpp-mcp
- centralmind/gateway — https://github.com/centralmind/gateway
- ToolHive — https://github.com/Stacklok/toolhive
- many others to simplify server creation, type-safety, and security best practices

---

# Notes & Recommendations

- Always run untrusted or community MCP servers in an isolated environment (container or VM) and restrict access to sensitive resources.
- Prefer official vendor-maintained servers (marked with ⭐) for production use.
- Check each server repo for documentation about transports (stdio, SSE, HTTP), authentication, and example clients.
- This ecosystem evolves rapidly — many new servers, clients, and frameworks are added frequently. If you maintain a server, ensure the repo has clear installation and security instructions.

<div align="right">
    <b><a href="#Contents">↥ back to top</a></b>
</div>
