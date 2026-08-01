![](asserts/logo1.png)

# Awesome MCP Servers ![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

一个优秀 Model Context Protocol (MCP) 服务器、工具、框架、客户端和实用程序清单。MCP 是一个开放协议，使 AI 模型能够通过标准化的服务器实现，与本地和远程资源安全地交互。

---

另外，我们提供了一份完整的[MCP服务列表](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/Full-List-of-MCP-Servers.xlsx), 该列表由爬虫整理而来，包含大约6000条目。

---

## 所有语言的文档
> 文档翻译招募中! [We're looking for translators](https://github.com/YuzeHao2023/Awesome-MCP-Servers/issues/1) to help translate this spec for everyone!

**可以阅读如下语言的文档:**

| 语言     | 链接                                                                 |
|----------|---------------------------------------------------------------------|
| English  | [English](https://github.com/YuzeHao2023/Awesome-MCP-Servers?tab=readme-ov-file) |
| 简体中文  | [简体中文](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_zh_CN.md) |
| 繁體中文  | [繁體中文](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_zh_TW.md) |
| 日本語    | [日本語](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_ja.md) |
| 한국어    | [한국어](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_ko.md) |

---

## ⚠️ 安全警告

在没有适当沙箱隔离的情况下运行 MCP 服务器，可能会以宿主进程的权限执行任意代码，这会带来重大安全风险。

简要说明：
- 系统访问：可访问文件、网络和系统资源
- 代码执行：可能在机器上执行命令
- 提示注入：恶意提示可触发服务器执行非预期操作
- 数据泄露：敏感数据可能被访问或泄漏

安全最佳实践：
- 优先使用官方实现（标注为 ⭐）用于生产环境
- 在虚拟机或隔离容器中运行不受信任的服务器
- 在安装前审查代码和配置
- 将权限限制到最低必要范围
- 监控服务器活动和日志

---

## 支持的客户端示例

许多 MCP 客户端和 UI 可以连接此处列出的服务器。例如（但不限于）：
- Claude Desktop / Claude 客户端
- Zed
- Sourcegraph Cody
- Cursor
- Visual Studio Code
- LibreChat
- 各类 CLI 与浏览器客户端

（具体客户端的图标和链接通常展示在各服务器或项目页面上。）

---

## 服务器实现分类（目录）

- 📂 文件系统（File Systems）
- 📦 沙箱与虚拟化（Sandbox & Virtualization）
- 🔄 版本控制（Version Control）
- ☁️ 云存储（Cloud Storage）
- 🗄️ 数据库（Databases）
- 💬 通信（Communication）
- 📈 监控（Monitoring）
- 🔍 搜索与网络（Search & Web）
- 🗺️ 位置服务（Location Services）
- 🎯 营销（Marketing）
- 📝 笔记（Note Taking）
- ⚡ 云平台（Cloud Platforms）
- ⚙️ 工作流自动化（Workflow Automation）
- 🤖 系统自动化（System Automation）
- 📱 社交媒体（Social Media）
- 🎮 游戏（Gaming）
- 💹 金融（Finance）
- 🧬 研究与数据（Research & Data）
- 🤝 AI 服务（AI Services）
- 💻 开发工具（Development Tools）
- 📊 数据可视化（Data Visualization）
- 🆔 身份（Identity）
- 🔗 聚合器（Aggregators）
- 💬 语言与翻译（Language & Translation）
- 🔒 安全（Security）
- 🔌 物联网（IoT）
- 🧑‍🎨 艺术与文学（Art & Literature）
- 🛒 电子商务（E-Commerce）
- 📦 数据平台（Data Platforms）
- 🤖 机器人与物理 AI（Robotics & Physical AI）

图例：
- ⭐ 官方协议实现
- 数字 1、2、3...：当存在多个实现时的排序标注

---

# 参考服务器（Reference Servers）

这些是示例/参考服务器以及核心 SDK 示例，用于演示 MCP 功能。

- Everything（参考/测试服务器，包含 prompts、资源与工具）  
  https://github.com/modelcontextprotocol/servers/blob/main/src/everything
- Fetch  
  https://github.com/modelcontextprotocol/servers/tree/main/src/fetch
- Filesystem  
  https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
- Git  
  https://github.com/modelcontextprotocol/servers/tree/main/src/git
- Memory  
  https://github.com/modelcontextprotocol/servers/tree/main/src/memory
- Sequential Thinking  
  https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking
- Time  
  https://github.com/modelcontextprotocol/servers/blob/main/src/time

---

# 官方服务器（Official Servers）

由公司维护的、面向生产环境的官方集成（有时标注为 ⭐）：

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
- GitHub — https://github.com/github/github-mcp-server（官方）
- Notion — https://github.com/makenotion/notion-mcp（官方）
- Stripe — https://github.com/stripe/agent-toolkit/tree/main（⭐）
- PayPal — https://github.com/paypal/agent-toolkit/tree/main（⭐）
- Tinybird — https://github.com/tinybirdco/mcp-tinybird（⭐）
- 以及 AWS、Google 等厂商在 awslabs 与 modelcontextprotocol 仓库下的多个实现。

（完整官方服务器和厂商维护实现请参阅上方“官方服务器”和“参考服务器”链接中的详细列表。）

---

# 工具与实用程序（Tools & Utilities）

帮助发现、安装、管理与使用 MCP 服务器的实用工具。

服务器管理器：
- mcp-get — 安装与管理 MCP 服务器的 CLI（针对 Claude Desktop）  
  https://github.com/michaellatman/mcp-get
- mxcp — 构建安全、可测试的企业级 MCP 工具框架  
  http://github.com/raw-labs/mxcp
- Remote MCP — 远程 MCP 通信解决方案  
  https://github.com/ssut/Remote-MCP
- yamcp — MCP 工作区管理器（组织 MCP 服务器、扫描、监控等）  
  https://github.com/hamidra/yamcp
- ToolHive — 简化部署和管理的轻量工具  
  https://github.com/StacklokLabs/toolhive
- MCP Installer — https://github.com/anaisbetts/mcp-installer

其他实用工具：
- Secure Fetch（安全的 fetch 实现，防止访问本地资源）  
  https://github.com/appsec-innovation-labs/secure-mcp-fetch
- mcp-cli（MCP 服务器检查工具）  
  https://github.com/wong2/mcp-cli
- 及其他用于安装、发现与管理的工具

---

## 分类：文件系统（📂）

为本地或远程文件系统提供访问，支持可配置权限。

- Backup — https://github.com/hexitex/MCP-Backup-Server
- FileStash — https://github.com/mickael-kerjean/filestash/tree/master/server/plugin/plg_handler_mcp
- FileSystem（modelcontextprotocol 参考实现） — https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem (1)
- FileSystem（mark3labs） — https://github.com/mark3labs/mcp-filesystem-server (2)
- Everything Search — https://github.com/mamertofabian/mcp-everything-search
- fast-filesystem-mcp — https://github.com/efforthye/fast-filesystem-mcp
- llm-context — https://github.com/cyberchitta/llm-context.py

---

## 分类：沙箱与虚拟化（📦）

安全执行代码的隔离环境。

- Microsandbox（⭐） — https://github.com/microsandbox/microsandbox
- E2B（⭐） — https://github.com/e2b-dev/mcp-server
- Docker（QuantGeekDev） — https://github.com/QuantGeekDev/docker-mcp

---

## 分类：版本控制（🔄）

与 Git 及版本控制平台交互的服务器。

- GitHub（1，官方） — https://github.com/github/github-mcp-server
- GitHub Repos Manager — https://github.com/kurdin/github-repos-manager-mcp
- GitLab — https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab
- Git（直连） — https://github.com/modelcontextprotocol/servers/tree/main/src/git
- Phabricator — https://github.com/baba786/phabricator-mcp-server
- Gitingest-MCP — https://github.com/puravparab/Gitingest-MCP

---

## 分类：云存储（☁️）

访问云存储平台的服务器。

- Google Drive — https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive
- Box（⭐） — https://developer.box.com/guides/box-mcp/
- VideoDB（agent-toolkit，⭐） — https://github.com/video-db/agent-toolkit/tree/main/modelcontextprotocol
- Microsoft 365 — https://github.com/softeria/ms-365-mcp-server

---

## 分类：数据库（🗄️）

提供模式检查与查询能力的数据库接入。

- PostgreSQL — https://github.com/modelcontextprotocol/servers/tree/main/src/postgres
- SQLite — https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite
- DuckDB — https://github.com/ktanaka101/mcp-server-duckdb
- Excel — https://github.com/haris-musa/excel-mcp-server
- BigQuery — https://github.com/LucasHild/mcp-server-bigquery 与 https://github.com/ergut/mcp-bigquery-server
- Neon（⭐） — https://github.com/neondatabase/mcp-server-neon
- Qdrant（⭐） — https://github.com/qdrant/mcp-server-qdrant/
- MongoDB — https://github.com/kiliczsh/mcp-mongo-server
- MongoDB Lens — https://github.com/furey/mongodb-lens
- MySQL — https://github.com/designcomputer/mysql_mcp_server
- Airtable — https://github.com/domdomegg/airtable-mcp-server
- Snowflake — https://github.com/isaacwasserman/mcp-snowflake-server
- DBUtils — https://github.com/donghao1393/mcp-dbutils
- TiDB — https://github.com/c4pt0r/mcp-server-tidb
- NocoDB — https://github.com/edwinbernadus/nocodb-mcp-server
- Couchbase（⭐） — https://github.com/Couchbase-Ecosystem/mcp-server-couchbase
- Redis（⭐） — https://github.com/redis/mcp-redis

---

## 分类：通信（💬）

与聊天与消息平台集成。

- Slack — https://github.com/korotovsky/slack-mcp-server
- LINE Official Account（⭐） — https://github.com/line/line-bot-mcp-server
- Linear — https://github.com/jerhadf/linear-mcp-server
- Atlassian — https://github.com/sooperset/mcp-atlassian
- Carbon Voice（⭐） — https://github.com/PhononX/cv-mcp-server
- ntfy — https://github.com/gitmotion/ntfy-me-mcp

---

## 分类：监控（📈）

访问观测与监控系统的数据。

- Metoro — https://github.com/metoro-io/metoro-mcp-server
- Raygun — https://github.com/MindscapeHQ/mcp-server-raygun
- Sentry — https://github.com/modelcontextprotocol/servers/tree/main/src/sentry
- sslmon — https://github.com/firesh/sslmon-mcp
- Signoz — https://github.com/DrDroidLab/signoz-mcp-server
- VictoriaMetrics — https://github.com/VictoriaMetrics-Community/mcp-victoriametrics

---

## 分类：搜索与网络（🔍）

网页抓取、搜索与处理。

- Haunt — https://github.com/Darko893/mcp-server — AI-powered web scraping with Cloudflare bypass, JavaScript rendering, and structured data extraction. Pay-per-use API with free tier.
- Puppeteer — https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer
- Brave Search — https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search
- Bright Data — https://github.com/luminati-io/brightdata-mcp
- Dumpling AI — https://github.com/Dumpling-AI/mcp-server-dumplingai
- Fetch — https://github.com/modelcontextprotocol/servers/tree/main/src/fetch
- Kagi Search — https://github.com/ac3xx/mcp-servers-kagi
- Exa Search（⭐） — https://github.com/exa-labs/exa-mcp-server
- NYTimes — https://github.com/angheljf/nyt
- Google News — https://github.com/ChanMeng666/server-google-news
- Scrapeless — https://github.com/scrapeless-ai/scrapeless-mcp-server
- Search1API — https://github.com/fatwang2/search1api-mcp
- RivalSearchMCP — https://github.com/damionrashford/RivalSearchMCP
- Tavily — https://github.com/Tomatio13/mcp-server-tavily
- ArXiv — https://github.com/blazickjp/arxiv-mcp-server
- PapersWithCode — https://github.com/hbg/mcp-paperswithcode
- Playwright — https://github.com/executeautomation/mcp-playwright
- Websearch/SearXNG — https://github.com/mnhlt/WebSearch-MCP 与 https://github.com/ihor-sokoliuk/mcp-searxng
- Apify Actors 与 RAG Web Browser — https://github.com/apify/actors-mcp-server 与 https://github.com/apify/mcp-server-rag-web-browser

---

## 分类：位置服务（🗺️）

地图与地理信息服务。

- Campertunity — https://github.com/campertunity/mcp-server
- Google Maps — https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps
- IPLocate — https://github.com/iplocate/mcp-server-iplocate
- IP2Location.io — https://github.com/ip2location/mcp-ip2location-io
- QGIS — https://github.com/jjsantos01/qgis_mcp

---

## 分类：营销（🎯）

营销与分析工具。

- Agent Mindshare — https://agentmindshare.com
- Open Strategy Partners Marketing Tools — https://github.com/open-strategy-partners/osp_mark
- Fathom Analytics — https://github.com/mackenly/mcp-fathom-analytics
- Facebook Ads — https://github.com/gomarble-ai/facebook-ads-mcp-server
- Google Ads — https://github.com/gomarble-ai/google-ads-mcp-server

---

## 分类：笔记（📝）

笔记与知识管理集成。

- eBook-mcp — https://github.com/onebirdrocks/ebook-mcp
- Obsidian（1/2） — https://github.com/MarkusPfundstein/mcp-obsidian 与 https://github.com/calclavia/mcp-obsidian
- Notion（1/2） — https://github.com/danhilse/notion_mcp 与 https://github.com/suekou/mcp-notion-server
- Apple Notes — https://github.com/sirmews/apple-notes-mcp（仅 macOS）
- Slite — https://github.com/fajarmf/slite-mcp
- Todoist — https://github.com/abhiz123/todoist-mcp-server
- Google Keep — https://github.com/feuerdev/keep-mcp
- GoodMemory — https://github.com/hjqcan/GoodMemory（面向 Codex、Claude Code 与任意 MCP 客户端的本地优先、可审计记忆层。默认使用持久化 SQLite 与无嵌入召回；记忆可检查、纠正、导出和删除，写回需显式启用。安装：`npm install -g goodmemory@0.7.1`。）

---

## 分类：云平台（⚡）

云厂商与基础设施管理。

- Cloudflare（⭐） — https://github.com/cloudflare/mcp-server-cloudflare
- Kubernetes（多实现） — https://github.com/strowk/mcp-k8s-go、https://github.com/weibaohui/k8m、https://github.com/StacklokLabs/mkp
- Tinybird（⭐） — https://github.com/tinybirdco/mcp-tinybird
- Google Cloud Run — https://github.com/GoogleCloudPlatform/cloud-run-mcp
- Render（官方） — https://render.com/docs/mcp-server

---

## 分类：工作流自动化（⚙️）

自动化平台与工具集成。

- Make（⭐） — https://github.com/integromat/make-mcp-server
- Taskade（⭐） — https://github.com/taskade/mcp
- Zapier — https://zapier.com/mcp
- Pipedream — https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol
- 聚合器类工具（Rube、MCPJungle 等）见“聚合器”章节

---

## 分类：系统自动化（🤖）

Shell、操作系统与任务自动化相关。

- Shell（wcgw） — https://github.com/rusiaaman/wcgw
- Windows CLI — https://github.com/SimonB97/win-cli-mcp
- Windows Control — https://github.com/Cheffromspace/nutjs-windows-control
- Command Line — https://github.com/phialsbasement/cmd-mcp-server
- Apple Shortcuts — https://github.com/recursechat/mcp-server-apple-shortcuts

---

## 分类：社交媒体（📱）

社交平台集成。

- BlueSky — https://github.com/keturiosakys/bluesky-context-server
- YouTube — https://github.com/anaisbetts/mcp-youtube 与 https://github.com/kimtaeyoon83/mcp-server-youtube-transcript
- Spotify — https://github.com/varunneal/spotify-mcp
- TikTok — https://github.com/Seym0n/tiktok-mcp
- Instagram DMs — https://github.com/trypeggy/instagram_dm_mcp
- X/Twitter — https://github.com/mbelinky/x-mcp-server

---

## 分类：游戏（🎮）

游戏引擎与开发工具。

- Unity 引擎（多个实现） — https://github.com/IvanMurzak/Unity-MCP、https://github.com/CoderGamester/mcp-unity、https://github.com/codemaestroai/advanced-unity-mcp

---

## 分类：金融（💹）

支付、市场数据与金融服务。

- Octagon（⭐） — https://github.com/OctagonAI/octagon-mcp-server
- CoinMarket — https://github.com/anjor/coinmarket-mcp-server
- Chargebee（⭐） — https://github.com/chargebee/agentkit/tree/main/modelcontextprotocol
- DexPaprika（⭐） — https://github.com/donbagger/dexpaprika-mcp-server
- Mercado Pago — https://mcp.mercadopago.com/
- PayPal（⭐） — https://github.com/paypal/agent-toolkit
- Stripe（⭐） — https://github.com/stripe/agent-toolkit
- LongPort OpenAPI（⭐） — https://github.com/longportapp/openapi/tree/main/mcp

---

## 分类：研究与数据（🧬）

论文、数据集与专业数据服务。

- ArXiv — https://github.com/blazickjp/arxiv-mcp-server
- Ancestry — https://github.com/reeeeemo/ancestry-mcp
- Probe.dev — https://mcp.probe.dev
- OpenNutrition — https://github.com/deadletterq/mcp-opennutrition
- Congress（立法数据） — https://github.com/amurshak/congressMCP

---

## 分类：AI 服务（🤝）

与 AI 与机器学习服务的集成。

- Agentset AI — https://github.com/agentset-ai/mcp-server
- OpenAI — https://github.com/pierrebrunelle/mcp-server-openai
- NeuroLink — https://github.com/juspay/neurolink
- OpenAI 兼容 Chat — https://github.com/pyroprompts/any-chat-completions-mcp
- Perplexity — https://github.com/tanigami/mcp-server-perplexity
- LlamaCloud — https://github.com/run-llama/mcp-server-llamacloud
- HuggingFace Spaces — https://github.com/evalstate/mcp-hfspace
- PiAPI — https://github.com/apinetwork/piapi-mcp-server
- Chronulus AI — https://github.com/ChronulusAI/chronulus-mcp
- Creatify — https://github.com/TSavo/creatify-mcp
- ZenML（⭐） — https://github.com/zenml-io/mcp-zenml

---

## 分类：开发工具（💻）

面向开发者的 MCP 服务器与工具。

- CentralMind/Gateway — https://github.com/centralmind/gateway
- Currents（⭐） — https://github.com/currents-dev/currents-mcp
- Octocode — https://github.com/bgauryy/octocode-mcp
- OpenAPI Schema Explorer — https://github.com/kadykov/mcp-openapi-schema-explorer
- OpenRPC — https://github.com/shanejonas/openrpc
- Postman — https://github.com/delano/postman-mcp-server
- QA Sphere（⭐） — https://github.com/Hypersequent/qasphere-mcp
- marimo（⭐） — https://github.com/marimo-team/codemirror-mcp
- Figma — https://github.com/GLips/Figma-Context-MCP
- Comet Opik（⭐） — https://github.com/comet-ml/opik-mcp
- VSCode Devtools — https://github.com/biegehydra/BifrostMCP
- Mastra/mcp（⭐） — https://github.com/mastra-ai/mastra/tree/main/packages/mcp
- Bucket — https://github.com/bucketco/bucket-javascript-sdk/tree/main/packages/cli#model-context-protocol
- DefangLabs/defang — https://github.com/DefangLabs/defang

---

## 分类：数据可视化（📊）

图表与图形展示工具。

- VegaLite — https://github.com/isaacwasserman/mcp-vegalite-server
- Chart（AntV） — https://github.com/antvis/mcp-server-chart
- ECharts — https://github.com/hustcc/mcp-echarts
- Mermaid — https://github.com/hustcc/mcp-mermaid
- unified-diff-mcp — https://github.com/gorosun/unified-diff-mcp

---

## 分类：身份（🆔）

身份与访问管理相关。

- Keycloak — https://github.com/ChristophEnglisch/keycloak-model-context-protocol

---

## 分类：聚合器（🔗）

通过单一 MCP 端点访问多个应用和工具。

- MCPJungle — https://github.com/mcpjungle/MCPJungle
- Rube — https://rube.composio.dev
- Pipedream — https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol
- Zapier — https://zapier.com/mcp
- Plugged.in — https://github.com/VeriTeknik/pluggedin-mcp-proxy
- MCP Aggregator / Combine — https://github.com/nazar256/combine-mcp
- Magg — https://github.com/sitbon/magg

---

## 分类：语言与翻译（💬）

翻译与语言服务。

- Lara（⭐） — https://github.com/translated/lara-mcp

---

## 分类：安全（🔒）

安全与检测相关的服务器。

- Semgrep — https://github.com/semgrep/mcp
- Microsoft Entra ID — 与 Microsoft 相关的身份类 MCP 实现
- Netwrix（⭐） — https://github.com/netwrix/mcp-server-naa
- OSV — https://github.com/StacklokLabs/osv-mcp
- Vulert — https://vulert.com
- Thales / CDSP 类服务器 — 针对密钥与机密管理的 MCP 集成

---

## 分类：物联网（🔌）

设备与物联网集成。

- Coreflux MQTT — https://github.com/CorefluxCommunity/CorefluxMCPServer

---

## 分类：艺术与文学（🧑‍🎨）

书籍、图书馆与创意工具。

- MCP Open Library — https://github.com/8enSmith/mcp-open-library
- Pollinations — https://github.com/pollinations/model-context-protocol

---

## 分类：电子商务（🛒）

电商与市场平台集成。

- Mercado Libre — https://mcp.mercadolibre.com/
- Gunsnation — https://github.com/DynamicDeals/mcp-server-gunsnation
- ShopSavvy（⭐） — https://github.com/shopsavvy/shopsavvy-mcp-server

---

## 分类：数据平台（📦）

用于编排、转换和管理数据流水线的平台。

- Keboola（⭐） — https://github.com/keboola/keboola-mcp-server

---

## 分类：机器人与物理 AI（🤖）

机器人、无人机与物理 AI。

- Bagel — https://github.com/Extelligence-ai/bagel

---

# 社区服务器（Community Servers）

由社区维护的一系列服务器示例（节选，生态中还有大量项目）：

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
- BigQuery（社区实现） — https://github.com/LucasHild/mcp-server-bigquery 与 https://github.com/ergut/mcp-bigquery-server
- Binary Ninja 集成 — https://github.com/fosdickio/binary_ninja_mcp
- Bing Webmaster Tools — https://github.com/isiahw1/mcp-server-bing-webmaster
- Bluesky — https://github.com/keturiosakys/bluesky-context-server
- BloodHound-MCP — https://github.com/MorDavid/BloodHound-MCP-AI
- Box 社区实现 — https://github.com/hmk/box-mcp-server
- Browser MCPs — 多个实现（本地与云端浏览器自动化）
- bytebase/dbhub — https://github.com/bytebase/dbhub
- Calculator — https://github.com/githejie/mcp-server-calculator
- CalDAV MCP — https://github.com/dominik1001/caldav-mcp
- context-awesome、ref 等上下文与发现类服务器
- Currents — https://github.com/currents-dev/currents-mcp
- DINO-X、Digma、Driflyte、DreamFactory、Dash0、各类数据库与工具服务器等
  
---

# 客户端（Clients）

消费 MCP 服务器的客户端与 UI：

- MBro — https://github.com/sitbon/magg/blob/main/docs/mbro.md
- mcp-cli — https://github.com/wong2/mcp-cli
- mcp-client — https://github.com/rakesh-eltropy/mcp-client
- MCP-Bridge — https://github.com/SecretiveShell/MCP-Bridge
- MCP-Chatbot（CLI，⭐） — https://github.com/3choff/mcp-chatbot
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

# 框架（Frameworks）

用于构建 MCP 服务器的框架与脚手架：

- create-mcp-ts — https://github.com/stephencme/create-mcp-ts
- LiteMCP — https://github.com/wong2/litemcp
- mcp-framework — https://github.com/QuantGeekDev/mcp-framework
- MCP Plexus — https://github.com/super-i-tech/mcp_plexus
- oatpp-mcp — https://github.com/oatpp/oatpp-mcp
- centralmind/gateway — https://github.com/centralmind/gateway
- ToolHive — https://github.com/Stacklok/toolhive

---

# 如何贡献 / 提交服务器

多数 MCP 列表通过网站或特定贡献流程接受提交。集中提交入口示例：
- https://mcpservers.org/submit
- 各项目仓库中的 CONTRIBUTING.md 文档

提交时的建议：
- 遵循安全最佳实践
- 提供清晰的 README 与使用说明
- 列出支持的传输方式（stdio、SSE、HTTP）
- 提供安全与权限配置指引

---

# 备注与建议

- 在隔离环境（容器或虚拟机）中运行不受信任或社区服务器，并限制其访问敏感资源。
- 在生产环境中优先使用官方厂商维护的服务器（标注为 ⭐）。
- 查阅每个服务器仓库，了解其支持的传输方式（stdio、SSE、HTTP）、鉴权方式与示例客户端。
- 该生态系统发展迅速，新的服务器、客户端和框架不断加入。维护者请确保仓库包含清晰的安装与安全说明。

