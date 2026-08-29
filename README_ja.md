![](asserts/logo1.png)

# Awesome MCP Servers ![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

モデルコンテキストプロトコル（MCP）のサーバー、ツール、フレームワーク、クライアント、およびユーティリティの、キュレーションされたコミュニティ主導の一覧です。MCPはAIモデルが標準化されたサーバー実装を通じてローカルおよびリモートのリソースと安全にやり取りすることを可能にするオープンプロトコルです。本リストは…（原文省略部分の意図を保ちつつ、以下に続きます）[...]

---

また、[MCPサーバー完全リスト](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/Full-List-of-MCP-Servers.xlsx)を提供しており、このリストはクローラーによって整理されており、約6000件のエントリーが含まれています。

---

## すべてのドキュメント
> 翻訳者募集中！[この仕様の翻訳を手伝ってくれる翻訳者を探しています](https://github.com/YuzeHao2023/Awesome-MCP-Servers/issues/1)！

**以下の言語でドキュメントをお読みいただけます：**

| 言語 | リンク |
|------|--------|
| English | [English](https://github.com/YuzeHao2023/Awesome-MCP-Servers?tab=readme-ov-file) |
| 简体中文 | [简体中文](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_zh_CN.md) |
| 繁体中文 | [繁体中文](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_zh_TW.md) |
| 日本語   | [日本語](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_ja.md) |
| 한국어   | [한국어](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_ko.md) |

---

## MCPとは？

[MCP](https://modelcontextprotocol.io/)（Model Context Protocol）は、AIモデルが標準化されたサーバー実装を通じてローカルおよびリモートのリソースと安全にやり取りすることを可能にするオープンプロトコルです。本リストは主に…（原文の続きに沿って説明されます）[...]

---

## チュートリアル

* [Model Context Protocol (MCP) クイックスタート](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [Claude Desktop アプリを SQLite データベースで使用する設定](https://youtu.be/wxCCzo9dGj0)

## コミュニティ

* [r/mcp Reddit](https://www.reddit.com/r/mcp)
* [Discord サーバー](https://glama.ai/mcp/discord)

---

## ⚠️ セキュリティ警告

適切なサンドボックス化を行わずに MCP サーバーを実行すると、ホストプロセスと同じ権限で任意のコードを実行できる可能性があり、重大なセキュリティリスクを引き起こします。

警告の要点：
- システムアクセス: ファイル、ネットワーク、システムリソースへのフルアクセス
- コード実行: マシン上でコマンドを実行する可能性
- プロンプトインジェクション: 悪意のあるプロンプトが意図しないサーバー動作を引き起こす可能性
- データ漏洩: 機密データがアクセスまたは漏洩されるリスク

ベストプラクティス：
- 可能な場合は公式実装（⭐でマーク）を使用する
- サーバーはVMや隔離されたコンテナで実行する
- インストール前にコードと設定を確認する
- 必要最小限の権限に制限する
- サーバーのアクティビティとログを監視する

---

## 対応クライアントの例

多くの MCP クライアントや UI がここにリストされたサーバーに接続できます。例（これらに限定されません）：
- Claude Desktop / Claude クライアント
- Zed
- Sourcegraph Cody
- Cursor
- Visual Studio Code
- LibreChat
- 各種 CLI およびブラウザベースのクライアント

（アイコンや特定クライアントへのリンクは各サーバー／プロジェクトページに表示されることが一般的です。）

---

## サーバー実装（カテゴリ）

- 📂 ファイルシステム
- 📦 サンドボックス & 仮想化
- 🔄 バージョン管理
- ☁️ クラウドストレージ
- 🗄️ データベース
- 💬 コミュニケーション
- 📈 モニタリング
- 🔍 検索 & Web
- 🗺️ 位置情報サービス
- 🎯 マーケティング
- 📝 ノート取り
- ⚡ クラウドプラットフォーム
- ⚙️ ワークフロー自動化
- 🤖 システム自動化
- 📱 ソーシャルメディア
- 🎮 ゲーミング
- 💹 ファイナンス
- 🧬 研究 & データ
- 🤝 AI サービス
- 💻 開発ツール
- 📊 データ可視化
- 🆔 アイデンティティ
- 🔗 集約サービス
- 💬 言語 & 翻訳
- 🔒 セキュリティ
- 🔌 IoT
- 🧑‍🎨 アート & 文学
- 🛒 Eコマース
- 📦 データプラットフォーム
- 🤖 ロボティクス & 物理的AI

凡例：
- ⭐ 公式プロトコル実装
- 1,2,3,... 複数の実装がある場合の順序

---

# 参照サーバー（Reference Servers）

これらは MCP の機能を示すサンプル／参照サーバーおよびコア SDK の例です。

- Everything（参照／テスト用サーバー、プロンプト、リソース、ツールを含む）
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

# 公式サーバー（Official Servers）

公式の統合は、プラットフォーム向けに本番環境対応の MCP サーバーを構築している企業によって維持されています。（存在する場合は ⭐ でマーク）

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
- GitHub — https://github.com/github/github-mcp-server (公式)
- Notion — https://github.com/makenotion/notion-mcp (公式)
- Stripe — https://github.com/stripe/agent-toolkit/tree/main (⭐)
- PayPal — https://github.com/paypal/agent-toolkit/tree/main (⭐)
- Tinybird — https://github.com/tinybirdco/mcp-tinybird (⭐)
- Cloud-run、AWS、Azure、Google の提供物 — modelcontextprotocol の awslabs や Google のリポジトリにある各種公式 MCP サーバー

（公式サーバーやベンダー管理の実装の完全な一覧は、このドキュメント内の「Official Servers」および「Reference Servers」、並びにリンク先のリポジトリを参照してください。）

---

# ツール & ユーティリティ（Tools & Utilities）

MCP サーバーの発見、インストール、管理、および操作に役立つユーティリティ。

サーバーマネージャー：
- mcp-get — MCP サーバーをインストール・管理する CLI ツール（Claude Desktop 向け） — https://github.com/michaellatman/mcp-get
- mxcp — エンタープライズ向けのセキュアな MCP ツールを構築するオープンソースフレームワーク — http://github.com/raw-labs/mxcp
- Remote MCP — リモート MCP 通信のソリューション — https://github.com/ssut/Remote-MCP
- yamcp — Model Context Workspace Manager — https://github.com/hamidra/yamcp
- ToolHive — デプロイと管理を簡素化する軽量ユーティリティ — https://github.com/StacklokLabs/toolhive
- MCP Installer — https://github.com/anaisbetts/mcp-installer

その他のユーティリティ：
- Secure Fetch — ローカルリソースへのアクセスを防ぐ安全な fetch — https://github.com/appsec-innovation-labs/secure-mcp-fetch
- mcp-cli — MCP サーバーのための CLI インスペクタ — https://github.com/wong2/mcp-cli
- mcp-get、mcp-installer、および同様のユーティリティはインストールや発見を簡単にします。

---

## カテゴリ：ファイルシステム（📂）

設定可能な権限でローカルまたはリモートのファイルシステムにアクセスを提供します。

- Backup — https://github.com/hexitex/MCP-Backup-Server
- FileStash — https://github.com/mickael-kerjean/filestash/tree/master/server/plugin/plg_handler_mcp
- FileSystem (modelcontextprotocol reference) — https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem (1)
- FileSystem (mark3labs) — https://github.com/mark3labs/mcp-filesystem-server (2)
- Everything Search — https://github.com/mamertofabian/mcp-everything-search
- fast-filesystem-mcp — https://github.com/efforthye/fast-filesystem-mcp
- llm-context — https://github.com/cyberchitta/llm-context.py

---

## カテゴリ：サンドボックス & 仮想化（📦）

コード実行のための安全なサンドボックス環境。

- Microsandbox (⭐) — https://github.com/microsandbox/microsandbox
- E2B (⭐) — https://github.com/e2b-dev/mcp-server
- Docker (QuantGeekDev) — https://github.com/QuantGeekDev/docker-mcp

---

## カテゴリ：バージョン管理（🔄）

Git およびバージョン管理関連の MCP サーバー。

- GitHub (1) — https://github.com/github/github-mcp-server (公式)
- GitHub Repos Manager — https://github.com/kurdin/github-repos-manager-mcp
- GitLab — https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab
- Git (direct) — https://github.com/modelcontextprotocol/servers/tree/main/src/git
- Phabricator — https://github.com/baba786/phabricator-mcp-server
- Gitingest-MCP — https://github.com/puravparab/Gitingest-MCP

---

## カテゴリ：クラウドストレージ（☁️）

クラウドストレージプラットフォームへのアクセス。

- Google Drive — https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive
- Box (⭐) — https://developer.box.com/guides/box-mcp/
- VideoDB (agent-toolkit) — https://github.com/video-db/agent-toolkit/tree/main/modelcontextprotocol (⭐)
- Microsoft 365 — https://github.com/softeria/ms-365-mcp-server

---

## カテゴリ：データベース（🗄️）

スキーマの検査やクエリ機能を備えたデータベースアクセス。

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
- コミュニティサーバーには他にも多数のDB専用サーバーがリストされています。

---

## カテゴリ：コミュニケーション（💬）

チャットおよびメッセージングプラットフォームとの統合。

- Slack — https://github.com/korotovsky/slack-mcp-server
- LINE Official Account (⭐) — https://github.com/line/line-bot-mcp-server
- Linear — https://github.com/jerhadf/linear-mcp-server
- Atlassian — https://github.com/sooperset/mcp-atlassian
- Carbon Voice (⭐) — https://github.com/PhononX/cv-mcp-server
- ntfy — https://github.com/gitmotion/ntfy-me-mcp

---

## カテゴリ：モニタリング（📈）

可観測性および監視システムへのアクセス。

- Metoro — https://github.com/metoro-io/metoro-mcp-server
- Raygun — https://github.com/MindscapeHQ/mcp-server-raygun
- Sentry — https://github.com/modelcontextprotocol/servers/tree/main/src/sentry
- sslmon — https://github.com/firesh/sslmon-mcp
- Signoz — https://github.com/DrDroidLab/signoz-mcp-server
- VictoriaMetrics — https://github.com/VictoriaMetrics-Community/mcp-victoriametrics

---

## カテゴリ：検索 & Web（🔍）

Web フェッチ、スクレイピング、検索。

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
- Scrapeless やその他の Web スクレイピングに特化した MCP サーバーはコミュニティサーバーに多数リストされています。

---

## カテゴリ：位置情報サービス（🗺️）

マッピングおよびジオロケーション。

- Campertunity — https://github.com/campertunity/mcp-server
- Google Maps — https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps
- IPLocate — https://github.com/iplocate/mcp-server-iplocate
- IP2Location.io — https://github.com/ip2location/mcp-ip2location-io
- QGIS — https://github.com/jjsantos01/qgis_mcp

---

## カテゴリ：マーケティング（🎯）

マーケティングおよびアナリティクスツール。

- Agent Mindshare — https://agentmindshare.com
- Open Strategy Partners Marketing Tools — https://github.com/open-strategy-partners/osp_mark
- Fathom Analytics — https://github.com/mackenly/mcp-fathom-analytics
- Facebook Ads — https://github.com/gomarble-ai/facebook-ads-mcp-server
- Google Ads — https://github.com/gomarble-ai/google-ads-mcp-server

---

## カテゴリ：ノート取り（📝）

個人知識管理やノートとの統合。

- eBook-mcp — https://github.com/onebirdrocks/ebook-mcp
- Obsidian (1/2) — https://github.com/MarkusPfundstein/mcp-obsidian and https://github.com/calclavia/mcp-obsidian
- Notion (1/2) — https://github.com/danhilse/notion_mcp and https://github.com/suekou/mcp-notion-server
- Apple Notes — https://github.com/sirmews/apple-notes-mcp (macOS)
- Slite — https://github.com/fajarmf/slite-mcp
- Todoist — https://github.com/abhiz123/todoist-mcp-server
- Google Keep — https://github.com/feuerdev/keep-mcp

---

## カテゴリ：クラウドプラットフォーム（⚡）

クラウドベンダーおよびオーケストレーション。

- Cloudflare (⭐) — https://github.com/cloudflare/mcp-server-cloudflare
- Kubernetes（複数の実装） — https://github.com/strowk/mcp-k8s-go (1), https://github.com/weibaohui/k8m (2), https://github.com/StacklokLabs/mkp (3)
- Tinybird (⭐) — https://github.com/tinybirdco/mcp-tinybird
- Google Cloud Run — https://github.com/GoogleCloudPlatform/cloud-run-mcp
- Render — https://render.com/docs/mcp-server

---

## カテゴリ：ワークフロー自動化（⚙️）

自動化プラットフォームおよびワークフローツール。

- Make (⭐) — https://github.com/integromat/make-mcp-server
- Taskade (⭐) — https://github.com/taskade/mcp
- Zapier — https://zapier.com/mcp
- Pipedream — https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol
- ツール集約サービス（Rube、Rube/Composio、MCPJungle など）は Aggregators にリストされています。

---

## カテゴリ：システム自動化（🤖）

シェル、OS、タスク自動化。

- Shell (wcgw) — https://github.com/rusiaaman/wcgw
- Windows CLI — https://github.com/SimonB97/win-cli-mcp
- Windows Control — https://github.com/Cheffromspace/nutjs-windows-control
- Command Line — https://github.com/phialsbasement/cmd-mcp-server
- Apple Shortcuts — https://github.com/recursechat/mcp-server-apple-shortcuts

---

## カテゴリ：ソーシャルメディア（📱）

ソーシャルプラットフォームとの統合。

- BlueSky — https://github.com/keturiosakys/bluesky-context-server
- YouTube — https://github.com/anaisbetts/mcp-youtube and https://github.com/kimtaeyoon83/mcp-server-youtube-transcript
- Spotify — https://github.com/varunneal/spotify-mcp
- TikTok — https://github.com/Seym0n/tiktok-mcp
- Instagram DMs — https://github.com/trypeggy/instagram_dm_mcp
- X/Twitter — https://github.com/mbelinky/x-mcp-server

---

## カテゴリ：ゲーミング（🎮）

ゲームエンジンおよび関連ツール。

- Unity Engine（各種） — https://github.com/IvanMurzak/Unity-MCP, https://github.com/CoderGamester/mcp-unity, https://github.com/codemaestroai/advanced-unity-mcp

---

## カテゴリ：ファイナンス（💹）

決済、マーケットデータ、ファイナンスツール。

- Octagon (⭐) — https://github.com/OctagonAI/octagon-mcp-server
- CoinMarket — https://github.com/anjor/coinmarket-mcp-server
- Chargebee (⭐) — https://github.com/chargebee/agentkit/tree/main/modelcontextprotocol
- DexPaprika (⭐) — https://github.com/donbagger/dexpaprika-mcp-server
- Mercado Pago — https://mcp.mercadopago.com/
- PayPal (⭐) — https://github.com/paypal/agent-toolkit
- Stripe (⭐) — https://github.com/stripe/agent-toolkit
- LongPort OpenAPI (⭐) — https://github.com/longportapp/openapi/tree/main/mcp

---

## カテゴリ：研究 & データ（🧬）

論文、データセット、ドメインデータ。

- ArXiv — https://github.com/blazickjp/arxiv-mcp-server
- Ancestry — https://github.com/reeeeemo/ancestry-mcp
- Probe.dev — https://mcp.probe.dev
- OpenNutrition — https://github.com/deadletterq/mcp-opennutrition
- Congress（立法データ） — https://github.com/amurshak/congressMCP

---

## カテゴリ：AI サービス（🤝）

AI モデルおよび ML サービスとの統合。

- Agentset AI — https://github.com/agentset-ai/mcp-server
- OpenAI — https://github.com/pierrebrunelle/mcp-server-openai
- OpenAI 互換のチャット — https://github.com/pyroprompts/any-chat-completions-mcp
- OpenAgent — https://github.com/the-open-agent/openagent — オープンソースのパーソナル AI アシスタント。LLM、RAG、エージェントループ、ブラウザ自動化、シェル実行、MCP ツール統合をサポート
- Perplexity — https://github.com/tanigami/mcp-server-perplexity
- LlamaCloud — https://github.com/run-llama/mcp-server-llamacloud
- HuggingFace Spaces — https://github.com/evalstate/mcp-hfspace
- PiAPI — https://github.com/apinetwork/piapi-mcp-server
- Chronulus AI — https://github.com/ChronulusAI/chronulus-mcp
- Creatify — https://github.com/TSavo/creatify-mcp
- ZenML (⭐) — https://github.com/zenml-io/mcp-zenml

---

## カテゴリ：開発ツール（💻）

開発者向けの MCP サーバーとツール。

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
- コミュニティサーバーや公式サーバーにさらに多くのツールがリストされています

---

## カテゴリ：データ可視化（📊）

チャートや図表ツール。

- VegaLite — https://github.com/isaacwasserman/mcp-vegalite-server
- Chart (AntV) — https://github.com/antvis/mcp-server-chart
- ECharts — https://github.com/hustcc/mcp-echarts
- Mermaid — https://github.com/hustcc/mcp-mermaid
- unified-diff-mcp — https://github.com/gorosun/unified-diff-mcp

---

## カテゴリ：アイデンティティ（🆔）

アイデンティティとアクセス管理。

- Keycloak — https://github.com/ChristophEnglisch/keycloak-model-context-protocol

---

## カテゴリ：集約サービス（🔗）

多くの統合を一つの MCP エンドポイントで公開するもの。

- MCPJungle — https://github.com/mcpjungle/MCPJungle
- Rube — https://rube.composio.dev
- Pipedream — https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol
- Zapier — https://zapier.com/mcp
- Plugged.in — https://github.com/VeriTeknik/pluggedin-mcp-proxy
- MCP Aggregator / Combine — https://github.com/nazar256/combine-mcp
- Magg — https://github.com/sitbon/magg

---

## カテゴリ：言語 & 翻訳（💬）

翻訳および言語サービス。

- Lara (⭐) — https://github.com/translated/lara-mcp

---

## カテゴリ：セキュリティ（🔒）

セキュリティに特化したサーバーやスキャンツール。

- Semgrep — https://github.com/semgrep/mcp
- Microsoft Entra ID — Microsoft 関連の MCP（アイデンティティ用）
- Netwrix (⭐) — https://github.com/netwrix/mcp-server-naa
- OSV — https://github.com/StacklokLabs/osv-mcp
- Vulert — https://vulert.com
- Thales / CDSP サーバー — シークレットや鍵管理のための各種 MCP 統合

---

## カテゴリ：IoT（🔌）

デバイスおよび IoT 統合の MCP サーバー。

- Coreflux MQTT — https://github.com/CorefluxCommunity/CorefluxMCPServer

---

## カテゴリ：アート & 文学（🧑‍🎨）

書籍、ライブラリ、クリエイティブツール。

- MCP Open Library — https://github.com/8enSmith/mcp-open-library
- Pollinations — https://github.com/pollinations/model-context-protocol

---

## カテゴリ：Eコマース（🛒）

商取引およびマーケットプレイス統合。

- Mercado Libre — https://mcp.mercadolibre.com/
- Gunsnation — https://github.com/DynamicDeals/mcp-server-gunsnation
- ShopSavvy (⭐) — https://github.com/shopsavvy/shopsavvy-mcp-server

---

## カテゴリ：データプラットフォーム（📦）

オーケストレーションおよびデータパイプラインプラットフォーム。

- Keboola (⭐) — https://github.com/keboola/keboola-mcp-server

---

## カテゴリ：ロボティクス & 物理的AI（🤖）

ロボットやデバイス制御。

- Bagel — https://github.com/Extelligence-ai/bagel

---

# コミュニティサーバー（Community Servers）

コミュニティによって維持されている幅広い MCP サーバーのコレクション（ハイライトを選出 — エコシステムにはさらに多く存在します）：

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
- BigQuery サーバー — https://github.com/LucasHild/mcp-server-bigquery and https://github.com/ergut/mcp-bigquery-server
- Binary Ninja 統合 — https://github.com/fosdickio/binary_ninja_mcp
- Bing Webmaster Tools — https://github.com/isiahw1/mcp-server-bing-webmaster
- Bluesky — https://github.com/keturiosakys/bluesky-context-server
- BloodHound-MCP — https://github.com/MorDavid/BloodHound-MCP-AI
- Box community server — https://github.com/hmk/box-mcp-server
- ブラウザ MCP（複数） — ローカルおよびリモートのブラウザ自動化用の実装多数
- bytebase/dbhub — https://github.com/bytebase/dbhub
- Calculator — https://github.com/githejie/mcp-server-calculator
- CalDAV MCP — https://github.com/dominik1001/caldav-mcp
- コンテキスト対応 & 発見サーバー（context-awesome、ref など）
- Currents — https://github.com/currents-dev/currents-mcp
- DINO-X、Digma、Driflyte、DreamFactory、Dash0、DB 専用サーバーなど多数

（コミュニティサーバーや他の長大なリストについては、MCP エコシステム内の集約リストを参照してください。本 README は主要な…（続き））

---

# クライアント（Clients）

MCP サーバーを消費するクライアントおよび UI ツール：

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

# フレームワーク（Frameworks）

MCP サーバー構築のためのフレームワークと雛形：

- create-mcp-ts — https://github.com/stephencme/create-mcp-ts
- LiteMCP — https://github.com/wong2/litemcp
- mcp-framework — https://github.com/QuantGeekDev/mcp-framework
- MCP Plexus — https://github.com/super-i-tech/mcp_plexus
- oatpp-mcp — https://github.com/oatpp/oatpp-mcp
- centralmind/gateway — https://github.com/centralmind/gateway
- ToolHive — https://github.com/Stacklok/toolhive
- サーバー作成、型安全性、セキュリティのベストプラクティスを簡素化するその他多数のフレームワーク

---

# 注意 & 推奨事項（Notes & Recommendations）

- 信頼できない、またはコミュニティ提供の MCP サーバーを実行する際は、必ず隔離環境（コンテナまたはVM）で実行し、機密リソースへのアクセスを制限してください。
- 本番環境では公式のベンダー管理のサーバー（⭐でマーク）を優先してください。
- 各サーバーのリポジトリで、トランスポート（stdio、SSE、HTTP）、認証、サンプルクライアントに関するドキュメントを確認してください。
- このエコシステムは急速に進化しています — 多くの新しいサーバー、クライアント、フレームワークが頻繁に追加されます。サーバーを維持している場合は、インストールとセキュリティに関する明確なドキュメントを用意してください。
