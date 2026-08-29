![](asserts/logo1.png)

# Awesome MCP Servers ![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

一份經過整理的、社群驅動的優秀 Model Context Protocol (MCP) 伺服器、工具、框架、用戶端與實用工具清單。MCP 是一個開放協議，讓 AI 模型能透過標準化的伺服器實作，與本地與遠端資源安全互動。本專案聚焦於整理各式 MCP 伺服器與相關生態資源，並提供連結與分類以便探索。

---

另外，我們提供了一份完整的[MCP服務列表](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/Full-List-of-MCP-Servers.xlsx)，該列表由爬蟲整理而來，包含大約6000筆條目。

---

## 所有文件語言
> 招募翻譯志工！[我們正在招募翻譯者](https://github.com/YuzeHao2023/Awesome-MCP-Servers/issues/1)，協助將文件翻譯給更多使用者！

**可閱讀的語言版本：**

| 語言     | 連結                                                                 |
|----------|---------------------------------------------------------------------|
| English  | [English](https://github.com/YuzeHao2023/Awesome-MCP-Servers?tab=readme-ov-file) |
| 简体中文  | [简体中文](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_zh_CN.md) |
| 繁体中文  | [繁体中文](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_zh_TW.md) |
| 日本語    | [日本語](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_ja.md) |
| 한국어    | [한국어](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_ko.md) |

---

## 什麼是 MCP？

[MCP](https://modelcontextprotocol.io/)（Model Context Protocol）是一個開放協議，允許 AI 模型透過標準化的伺服器實作，安全地與本地與遠端資源互動。此清單專注於蒐集範例伺服器、社群實作、官方整合，以及能擴展 AI 助手功能的相關工具。

---

## 教學資源

- [Model Context Protocol (MCP) Quickstart](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
- [設定 Claude Desktop 使用 SQLite 資料庫（教學影片）](https://youtu.be/wxCCzo9dGj0)

## 社群

- [r/mcp Reddit](https://www.reddit.com/r/mcp)
- [Discord Server](https://glama.ai/mcp/discord)

---

## ⚠️ 安全警告

在沒有適當沙箱（sandbox）隔離的情況下執行 MCP 伺服器，可能會以宿主程序的權限執行任意程式碼，這會構成重大的安全風險。

風險概要：
- 系統存取：可存取檔案、網路與系統資源
- 程式碼執行：可能在機器上執行指令
- 提示（prompt）注入：惡意提示可能觸發伺服器執行非預期行為
- 資料外洩：敏感資料可能被存取或洩漏

安全最佳實務：
- 優先使用官方實作（標註為 ⭐）於正式環境
- 在虛擬機或隔離容器中執行不受信任的伺服器
- 安裝前審查程式碼與設定
- 將權限限制為最低必要範圍
- 監控伺服器活動與日誌

---

## 支援的用戶端範例

許多 MCP 用戶端與介面可連接此處列出的伺服器，範例包括（但不限於）：
- Claude Desktop / Claude 用戶端
- Zed
- Sourcegraph Cody
- Cursor
- Visual Studio Code
- LibreChat
- 各式 CLI 與瀏覽器用戶端

（各伺服器或專案頁面通常會顯示客戶端圖示與連結。）

---

## 伺服器實作分類（目錄）

- 📂 檔案系統（File Systems）
- 📦 沙箱與虛擬化（Sandbox & Virtualization）
- 🔄 版本控制（Version Control）
- ☁️ 雲端儲存（Cloud Storage）
- 🗄️ 資料庫（Databases）
- 💬 通訊（Communication）
- 📈 監控（Monitoring）
- 🔍 搜尋與網路（Search & Web）
- 🗺️ 位置服務（Location Services）
- 🎯 行銷（Marketing）
- 📝 筆記（Note Taking）
- ⚡ 雲端平台（Cloud Platforms）
- ⚙️ 工作流程自動化（Workflow Automation）
- 🤖 系統自動化（System Automation）
- 📱 社群媒體（Social Media）
- 🎮 遊戲（Gaming）
- 💹 金融（Finance）
- 🧬 研究與數據（Research & Data）
- 🤝 AI 服務（AI Services）
- 💻 開發工具（Development Tools）
- 📊 資料視覺化（Data Visualization）
- 🆔 身分識別（Identity）
- 🔗 聚合器（Aggregators）
- 💬 語言與翻譯（Language & Translation）
- 🔒 安全（Security）
- 🔌 物聯網（IoT）
- 🧑‍🎨 藝術與文學（Art & Literature）
- 🛒 電子商務（E-Commerce）
- 📦 數據平台（Data Platforms）
- 🤖 機器人與實體 AI（Robotics & Physical AI）

圖例：
- ⭐ 官方協議實作
- 1、2、3…：當存在多個實作時的排序標注

---

# 參考伺服器（Reference Servers）

以下為示例/參考伺服器與核心 SDK 範例，用以示範 MCP 功能：

- Everything（參考 / 測試伺服器，包含 prompts、資源與工具）  
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

# 官方伺服器（Official Servers）

由各公司維護、針對正式使用的 MCP 官方整合（有標註 ⭐ 的為官方/推薦實作）：

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
- 以及 AWS、Google 等廠商於 awslabs 與 modelcontextprotocol 倉庫下的多項實作

（如需完整官方伺服器與廠商維護之實作，請參考本文件中「官方伺服器」與「參考伺服器」的連結。）

---

# 工具與實用程式（Tools & Utilities）

有助於發現、安裝、管理與使用 MCP 伺服器的工具：

伺服器管理器：
- mcp-get — 用於安裝與管理 MCP 伺服器的 CLI（針對 Claude Desktop）  
  https://github.com/michaellatman/mcp-get
- mxcp — 建立安全、可測試企業級 MCP 工具的框架  
  http://github.com/raw-labs/mxcp
- Remote MCP — 遠端 MCP 通訊解決方案  
  https://github.com/ssut/Remote-MCP
- yamcp — MCP 工作區管理器（組織、掃描、監控 MCP 伺服器）  
  https://github.com/hamidra/yamcp
- ToolHive — 簡化部署與管理的輕量工具  
  https://github.com/StacklokLabs/toolhive
- MCP Installer — https://github.com/anaisbetts/mcp-installer

其他實用工具：
- Secure Fetch（安全的 fetch 實作，避免存取本地資源）  
  https://github.com/appsec-innovation-labs/secure-mcp-fetch
- mcp-cli（MCP 伺服器檢查 CLI）  
  https://github.com/wong2/mcp-cli

---

## 分類：檔案系統（📂）

提供對本地或遠端檔案系統的存取，支援可配置的權限：

- Backup — https://github.com/hexitex/MCP-Backup-Server
- FileStash — https://github.com/mickael-kerjean/filestash/tree/master/server/plugin/plg_handler_mcp
- FileSystem（modelcontextprotocol 參考實作） — https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem (1)
- FileSystem（mark3labs） — https://github.com/mark3labs/mcp-filesystem-server (2)
- Everything Search — https://github.com/mamertofabian/mcp-everything-search
- fast-filesystem-mcp — https://github.com/efforthye/fast-filesystem-mcp
- llm-context — https://github.com/cyberchitta/llm-context.py

---

## 分類：沙箱與虛擬化（📦）

提供安全的程式碼執行隔離環境：

- Microsandbox（⭐） — https://github.com/microsandbox/microsandbox
- E2B（⭐） — https://github.com/e2b-dev/mcp-server
- Docker（QuantGeekDev） — https://github.com/QuantGeekDev/docker-mcp

---

## 分類：版本控制（🔄）

與 Git 及版本控制平台互動的 MCP 伺服器：

- GitHub（1，官方） — https://github.com/github/github-mcp-server
- GitHub Repos Manager — https://github.com/kurdin/github-repos-manager-mcp
- GitLab — https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab
- Git（直接操作） — https://github.com/modelcontextprotocol/servers/tree/main/src/git
- Phabricator — https://github.com/baba786/phabricator-mcp-server
- Gitingest-MCP — https://github.com/puravparab/Gitingest-MCP

---

## 分類：雲端儲存（☁️）

存取雲端儲存平台的伺服器：

- Google Drive — https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive
- Box（⭐） — https://developer.box.com/guides/box-mcp/
- VideoDB（agent-toolkit，⭐） — https://github.com/video-db/agent-toolkit/tree/main/modelcontextprotocol
- Microsoft 365 — https://github.com/softeria/ms-365-mcp-server

---

## 分類：資料庫（🗄️）

具備 schema 檢視與查詢能力的資料庫接入：

- PostgreSQL — https://github.com/modelcontextprotocol/servers/tree/main/src/postgres
- SQLite — https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite
- DuckDB — https://github.com/ktanaka101/mcp-server-duckdb
- Excel — https://github.com/haris-musa/excel-mcp-server
- BigQuery — https://github.com/LucasHild/mcp-server-bigquery 與 https://github.com/ergut/mcp-bigquery-server
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

## 分類：通訊（💬）

整合聊天與訊息平台的伺服器：

- Slack — https://github.com/korotovsky/slack-mcp-server
- LINE Official Account（⭐） — https://github.com/line/line-bot-mcp-server
- Linear — https://github.com/jerhadf/linear-mcp-server
- Atlassian — https://github.com/sooperset/mcp-atlassian
- Carbon Voice（⭐） — https://github.com/PhononX/cv-mcp-server
- ntfy — https://github.com/gitmotion/ntfy-me-mcp

---

## 分類：監控（📈）

存取觀測與監控系統資料：

- Metoro — https://github.com/metoro-io/metoro-mcp-server
- Raygun — https://github.com/MindscapeHQ/mcp-server-raygun
- Sentry — https://github.com/modelcontextprotocol/servers/tree/main/src/sentry
- sslmon — https://github.com/firesh/sslmon-mcp
- Signoz — https://github.com/DrDroidLab/signoz-mcp-server
- VictoriaMetrics — https://github.com/VictoriaMetrics-Community/mcp-victoriametrics

---

## 分類：搜尋與網路（🔍）

網頁擷取、抓取與搜尋：

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
- Websearch / SearXNG — https://github.com/mnhlt/WebSearch-MCP 與 https://github.com/ihor-sokoliuk/mcp-searxng
- Apify Actors 與 RAG Web Browser — https://github.com/apify/actors-mcp-server 與 https://github.com/apify/mcp-server-rag-web-browser

---

## 分類：位置服務（🗺️）

地圖與地理資訊服務：

- Campertunity — https://github.com/campertunity/mcp-server
- Google Maps — https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps
- IPLocate — https://github.com/iplocate/mcp-server-iplocate
- IP2Location.io — https://github.com/ip2location/mcp-ip2location-io
- QGIS — https://github.com/jjsantos01/qgis_mcp

---

## 分類：行銷（🎯）

行銷與分析工具：

- Agent Mindshare — https://agentmindshare.com
- Open Strategy Partners Marketing Tools — https://github.com/open-strategy-partners/osp_mark
- Fathom Analytics — https://github.com/mackenly/mcp-fathom-analytics
- Facebook Ads — https://github.com/gomarble-ai/facebook-ads-mcp-server
- Google Ads — https://github.com/gomarble-ai/google-ads-mcp-server

---

## 分類：筆記（📝）

筆記與個人知識管理整合：

- eBook-mcp — https://github.com/onebirdrocks/ebook-mcp
- Obsidian（1/2） — https://github.com/MarkusPfundstein/mcp-obsidian 與 https://github.com/calclavia/mcp-obsidian
- Notion（1/2） — https://github.com/danhilse/notion_mcp 與 https://github.com/suekou/mcp-notion-server
- Apple Notes — https://github.com/sirmews/apple-notes-mcp（macOS 專用）
- Slite — https://github.com/fajarmf/slite-mcp
- Todoist — https://github.com/abhiz123/todoist-mcp-server
- Google Keep — https://github.com/feuerdev/keep-mcp

---

## 分類：雲端平台（⚡）

雲端供應商與編排工具：

- Cloudflare（⭐） — https://github.com/cloudflare/mcp-server-cloudflare
- Kubernetes（多種實作） — https://github.com/strowk/mcp-k8s-go、https://github.com/weibaohui/k8m、https://github.com/StacklokLabs/mkp
- Tinybird（⭐） — https://github.com/tinybirdco/mcp-tinybird
- Google Cloud Run — https://github.com/GoogleCloudPlatform/cloud-run-mcp
- Render — https://render.com/docs/mcp-server

---

## 分類：工作流程自動化（⚙️）

自動化平台與工作流程工具：

- Make（⭐） — https://github.com/integromat/make-mcp-server
- Taskade（⭐） — https://github.com/taskade/mcp
- Zapier — https://zapier.com/mcp
- Pipedream — https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol

---

## 分類：系統自動化（🤖）

Shell、作業系統與任務自動化相關工具：

- Shell（wcgw） — https://github.com/rusiaaman/wcgw
- Windows CLI — https://github.com/SimonB97/win-cli-mcp
- Windows Control — https://github.com/Cheffromspace/nutjs-windows-control
- Command Line — https://github.com/phialsbasement/cmd-mcp-server
- Apple Shortcuts — https://github.com/recursechat/mcp-server-apple-shortcuts

---

## 分類：社群媒體（📱）

社群平台整合：

- BlueSky — https://github.com/keturiosakys/bluesky-context-server
- YouTube — https://github.com/anaisbetts/mcp-youtube 與 https://github.com/kimtaeyoon83/mcp-server-youtube-transcript
- Spotify — https://github.com/varunneal/spotify-mcp
- TikTok — https://github.com/Seym0n/tiktok-mcp
- Instagram DMs — https://github.com/trypeggy/instagram_dm_mcp
- X/Twitter — https://github.com/mbelinky/x-mcp-server

---

## 分類：遊戲（🎮）

遊戲引擎與開發工具：

- Unity 引擎（數個實作） — https://github.com/IvanMurzak/Unity-MCP、https://github.com/CoderGamester/mcp-unity、https://github.com/codemaestroai/advanced-unity-mcp

---

## 分類：金融（💹）

支付、行情資料與金融服務：

- Octagon（⭐） — https://github.com/OctagonAI/octagon-mcp-server
- CoinMarket — https://github.com/anjor/coinmarket-mcp-server
- Chargebee（⭐） — https://github.com/chargebee/agentkit/tree/main/modelcontextprotocol
- DexPaprika（⭐） — https://github.com/donbagger/dexpaprika-mcp-server
- Mercado Pago — https://mcp.mercadolpago.com/
- PayPal（⭐） — https://github.com/paypal/agent-toolkit
- Stripe（⭐） — https://github.com/stripe/agent-toolkit
- LongPort OpenAPI（⭐） — https://github.com/longportapp/openapi/tree/main/mcp

---

## 分類：研究與數據（🧬）

論文、資料集與專業資料來源：

- ArXiv — https://github.com/blazickjp/arxiv-mcp-server
- Ancestry — https://github.com/reeeeemo/ancestry-mcp
- Probe.dev — https://mcp.probe.dev
- OpenNutrition — https://github.com/deadletterq/mcp-opennutrition
- Congress（立法資料） — https://github.com/amurshak/congressMCP

---

## 分類：AI 服務（🤝）

AI 與機器學習服務整合：

- Agentset AI — https://github.com/agentset-ai/mcp-server
- OpenAI — https://github.com/pierrebrunelle/mcp-server-openai
- OpenAI 相容 Chat — https://github.com/pyroprompts/any-chat-completions-mcp
- OpenAgent — https://github.com/the-open-agent/openagent — 開源個人 AI 助理，支援 LLM、RAG、Agent 迴圈、瀏覽器自動化、命令列執行與 MCP 工具整合
- Perplexity — https://github.com/tanigami/mcp-server-perplexity
- LlamaCloud — https://github.com/run-llama/mcp-server-llamacloud
- HuggingFace Spaces — https://github.com/evalstate/mcp-hfspace
- PiAPI — https://github.com/apinetwork/piapi-mcp-server
- Chronulus AI — https://github.com/ChronulusAI/chronulus-mcp
- Creatify — https://github.com/TSavo/creatify-mcp
- ZenML（⭐） — https://github.com/zenml-io/mcp-zenml

---

## 分類：開發工具（💻）

針對開發者的 MCP 伺服器與工具：

- CentralMind / Gateway — https://github.com/centralmind/gateway
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
- Mastra / mcp（⭐） — https://github.com/mastra-ai/mastra/tree/main/packages/mcp
- Bucket — https://github.com/bucketco/bucket-javascript-sdk/tree/main/packages/cli#model-context-protocol
- DefangLabs / defang — https://github.com/DefangLabs/defang

---

## 分類：資料視覺化（📊）

圖表與圖形生成工具：

- VegaLite — https://github.com/isaacwasserman/mcp-vegalite-server
- Chart（AntV） — https://github.com/antvis/mcp-server-chart
- ECharts — https://github.com/hustcc/mcp-echarts
- Mermaid — https://github.com/hustcc/mcp-mermaid
- unified-diff-mcp — https://github.com/gorosun/unified-diff-mcp

---

## 分類：身分識別（🆔）

身分與存取管理：

- Keycloak — https://github.com/ChristophEnglisch/keycloak-model-context-protocol

---

## 分類：聚合器（🔗）

透過單一 MCP 端點存取多種整合：

- MCPJungle — https://github.com/mcpjungle/MCPJungle
- Rube — https://rube.composio.dev
- Pipedream — https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol
- Zapier — https://zapier.com/mcp
- Plugged.in — https://github.com/VeriTeknik/pluggedin-mcp-proxy
- MCP Aggregator / Combine — https://github.com/nazar256/combine-mcp
- Magg — https://github.com/sitbon/magg

---

## 分類：語言與翻譯（💬）

翻譯與語言服務：

- Lara（⭐） — https://github.com/translated/lara-mcp

---

## 分類：安全（🔒）

安全掃描與檢測相關伺服器：

- Semgrep — https://github.com/semgrep/mcp
- Microsoft Entra ID — 與 Microsoft 有關的身分類 MCP 實作
- Netwrix（⭐） — https://github.com/netwrix/mcp-server-naa
- OSV — https://github.com/StacklokLabs/osv-mcp
- Vulert — https://vulert.com
- Thales / CDSP 類伺服器 — 用於金鑰與機密管理的 MCP 整合

---

## 分類：物聯網（🔌）

裝置與物聯網整合：

- Coreflux MQTT — https://github.com/CorefluxCommunity/CorefluxMCPServer

---

## 分類：藝術與文學（🧑‍🎨）

圖書館與創作相關工具：

- MCP Open Library — https://github.com/8enSmith/mcp-open-library
- Pollinations — https://github.com/pollinations/model-context-protocol

---

## 分類：電子商務（🛒）

商城與市場平台整合：

- Mercado Libre — https://mcp.mercadolibre.com/
- Gunsnation — https://github.com/DynamicDeals/mcp-server-gunsnation
- ShopSavvy（⭐） — https://github.com/shopsavvy/shopsavvy-mcp-server

---

## 分類：數據平台（📦）

編排、轉換與管理資料流水線的平台：

- Keboola（⭐） — https://github.com/keboola/keboola-mcp-server

---

## 分類：機器人與實體 AI（🤖）

機器人、無人機與實體 AI：

- Bagel — https://github.com/Extelligence-ai/bagel

---

# 社群伺服器（Community Servers）

由社群維護的各式伺服器（節錄，生態系中尚有大量專案）：

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
- BigQuery（社群實作） — https://github.com/LucasHild/mcp-server-bigquery 與 https://github.com/ergut/mcp-bigquery-server
- Binary Ninja 整合 — https://github.com/fosdickio/binary_ninja_mcp
- Bing Webmaster Tools — https://github.com/isiahw1/mcp-server-bing-webmaster
- Bluesky — https://github.com/keturiosakys/bluesky-context-server
- BloodHound-MCP — https://github.com/MorDavid/BloodHound-MCP-AI
- Box 社群實作 — https://github.com/hmk/box-mcp-server
- Browser MCPs — 多個本地與雲端瀏覽器自動化實作
- bytebase / dbhub — https://github.com/bytebase/dbhub
- Calculator — https://github.com/githejie/mcp-server-calculator
- CalDAV MCP — https://github.com/dominik1001/caldav-mcp
- context-awesome、ref 等上下文與資源發現伺服器
- Currents — https://github.com/currents-dev/currents-mcp
- DINO-X、Digma、Driflyte、DreamFactory、Dash0、以及各類資料庫或工具伺服器等

（社群伺服器清單龐大且持續成長；請參閱各倉庫以取得最新資訊與安裝說明。）

---

# 用戶端（Clients）

可消費 MCP 伺服器的用戶端與介面：

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

用於構建 MCP 伺服器的框架與腳手架：

- create-mcp-ts — https://github.com/stephencme/create-mcp-ts
- LiteMCP — https://github.com/wong2/litemcp
- mcp-framework — https://github.com/QuantGeekDev/mcp-framework
- MCP Plexus — https://github.com/super-i-tech/mcp_plexus
- oatpp-mcp — https://github.com/oatpp/oatpp-mcp
- centralmind / gateway — https://github.com/centralmind/gateway
- ToolHive — https://github.com/Stacklok/toolhive

---

# 如何貢獻 / 提交伺服器

多數 MCP 清單接受透過網站或專屬流程提交。集中提交入口範例：
- https://mcpservers.org/submit
- 各專案倉庫中的 CONTRIBUTING.md

提交建議：
- 遵循安全最佳實務
- 提供清晰的 README 與使用說明
- 列出支援的傳輸方式（stdio、SSE、HTTP）
- 提供安全與權限設定指南

---

# 備註與建議

- 執行不受信任或社群伺服器時，務必在隔離環境（容器或虛擬機）中執行，並限制其存取敏感資源。
- 正式環境建議優先使用官方廠商維護的伺服器（標註為 ⭐）。
- 檢視各伺服器倉庫以了解支援之傳輸方式（stdio、SSE、HTTP）、認證方式與範例用戶端。
- 此生態系迅速演進，新伺服器、用戶端與框架經常加入；維護者請確保倉庫附有清楚的安裝與安全說明。


