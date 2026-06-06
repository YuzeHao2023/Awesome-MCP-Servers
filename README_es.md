![](asserts/logo1.png)

# Awesome Servidores MCP ![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

Una lista curada y mantenida por la comunidad de servidores, herramientas, frameworks, clientes y utilidades increíbles para Model Context Protocol (MCP). MCP es un protocolo abierto que permite a los modelos de IA interactuar de forma segura con recursos locales y remotos a través de implementaciones de servidores estandarizadas.

---

Nota: Proporcionamos una [lista completa de servidores MCP](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/Full-List-of-MCP-Servers.xlsx), compilada por un rastreador web y que contiene aproximadamente 6000 entradas.

---

## Todos los documentos
> ¡Se buscan traductores! Ayúdanos en el [issue de traductores](https://github.com/YuzeHao2023/Awesome-MCP-Servers/issues/1).

**Lee nuestra documentación en los siguientes idiomas:**

| Idioma | Enlace                                                               |
|--------|----------------------------------------------------------------------|
| English  | [English](https://github.com/YuzeHao2023/Awesome-MCP-Servers?tab=readme-ov-file) |
| 简体中文  | [简体中文](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_zh_CN.md) |
| 繁體中文  | [繁體中文](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_zh_TW.md) |
| 日本語    | [日本語](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_ja.md) |
| 한국어    | [한국어](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_ko.md) |
| Español   | [Español](https://github.com/YuzeHao2023/Awesome-MCP-Servers/blob/main/README_es.md) |

---

## ¿Qué es MCP?

[MCP](https://modelcontextprotocol.io/) (Model Context Protocol) es un protocolo abierto que permite a los modelos de IA interactuar de forma segura con recursos locales y remotos a través de implementaciones de servidores estandarizadas. Esta lista se centra en servidores MCP listos para producción y experimentales que amplían las capacidades de IA mediante acceso a archivos, conexiones a bases de datos, integraciones de API y otros servicios contextuales.

---

## Tutoriales

* [Model Context Protocol (MCP) Quickstart](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [Configurar la aplicación Claude Desktop con una base de datos SQLite](https://youtu.be/wxCCzo9dGj0)

## Comunidad

* [r/mcp Reddit](https://www.reddit.com/r/mcp)
* [Servidor Discord](https://glama.ai/mcp/discord)

---

## ⚠️ Advertencia de seguridad

Ejecutar servidores MCP sin un sandbox adecuado puede ejecutar código arbitrario en tu sistema con los mismos permisos que el proceso anfitrión, creando riesgos de seguridad significativos.

Riesgos de seguridad:
- Acceso al sistema: Acceso completo a archivos, red y recursos del sistema
- Ejecución de código: Puede ejecutar cualquier comando en tu máquina
- Inyección de prompts: Los prompts maliciosos podrían desencadenar acciones no deseadas del servidor
- Exposición de datos: Los datos sensibles pueden ser accedidos o filtrados

Mejores prácticas recomendadas:
- Usar implementaciones oficiales (⭐) cuando estén disponibles
- Ejecutar servidores en VMs o contenedores aislados
- Revisar el código y la configuración antes de la instalación
- Aplicar el principio de mínimo privilegio
- Monitorear la actividad y los registros del servidor

---

## Clientes compatibles (ejemplos)

Muchos clientes e interfaces MCP pueden conectarse a los servidores de esta lista. Ejemplos (no exhaustivos):
- Claude Desktop / clientes Claude
- Zed
- Sourcegraph Cody
- Cursor
- Visual Studio Code
- LibreChat
- Varios clientes CLI y basados en navegador

---

## Implementaciones de servidores (categorías)

- 📂 Sistemas de archivos
- 📦 Sandbox y virtualización
- 🔄 Control de versiones
- ☁️ Almacenamiento en la nube
- 🗄️ Bases de datos
- 💬 Comunicación
- 📈 Monitoreo
- 🔍 Búsqueda y web
- 🗺️ Servicios de ubicación
- 🎯 Marketing
- 📝 Toma de notas
- ⚡ Plataformas cloud
- ⚙️ Automatización de flujos de trabajo
- 🤖 Automatización del sistema
- 📱 Redes sociales
- 🎮 Juegos
- 💹 Finanzas
- 🧬 Investigación y datos
- 🤝 Servicios de IA
- 💻 Herramientas de desarrollo
- 📊 Visualización de datos
- 🆔 Identidad
- 🔗 Agregadores
- 💬 Idioma y traducción
- 🔒 Seguridad
- 🔌 IoT
- 🧑‍🎨 Arte y literatura
- 🛒 Comercio electrónico
- 📦 Plataformas de datos
- 🤖 Robótica e IA física

Leyenda:
- ⭐ Implementación oficial del protocolo

---

# Servidores de referencia

Los siguientes servidores y ejemplos de SDK demuestran las funcionalidades de MCP:

- Everything (servidor de referencia/prueba con prompts, recursos y herramientas)
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

# Servidores oficiales

Las integraciones oficiales son mantenidas por empresas que construyen servidores MCP listos para producción para sus plataformas. (⭐ si está indicado)

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
- GitHub — https://github.com/github/github-mcp-server (oficial)
- Notion — https://github.com/makenotion/notion-mcp (oficial)
- Stripe — https://github.com/stripe/agent-toolkit/tree/main (⭐)
- PayPal — https://github.com/paypal/agent-toolkit/tree/main (⭐)
- Tinybird — https://github.com/tinybirdco/mcp-tinybird (⭐)

---

# Herramientas y utilidades

Utilidades para buscar, instalar, gestionar y trabajar con servidores MCP:

- mcp-get — CLI para instalar/gestionar servidores MCP para Claude Desktop — https://github.com/michaellatman/mcp-get
- Remote MCP — Solución de comunicación MCP remota — https://github.com/ssut/Remote-MCP
- yamcp — Model Context Workspace Manager — https://github.com/hamidra/yamcp
- ToolHive — Utilidad ligera que simplifica el despliegue — https://github.com/StacklokLabs/toolhive
- MCP Installer — https://github.com/anaisbetts/mcp-installer

---

## Categoría: Sistemas de archivos (📂)

- Backup — https://github.com/hexitex/MCP-Backup-Server
- FileStash — https://github.com/mickael-kerjean/filestash/tree/master/server/plugin/plg_handler_mcp
- FileSystem (referencia modelcontextprotocol) — https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
- FileSystem (mark3labs) — https://github.com/mark3labs/mcp-filesystem-server
- Everything Search — https://github.com/mamertofabian/mcp-everything-search
- llm-context — https://github.com/cyberchitta/llm-context.py

---

## Categoría: Sandbox y virtualización (📦)

- Microsandbox (⭐) — https://github.com/microsandbox/microsandbox
- E2B (⭐) — https://github.com/e2b-dev/mcp-server
- Docker (QuantGeekDev) — https://github.com/QuantGeekDev/docker-mcp

---

## Categoría: Control de versiones (🔄)

- GitHub (oficial) — https://github.com/github/github-mcp-server
- GitHub Repos Manager — https://github.com/kurdin/github-repos-manager-mcp
- GitLab — https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab
- Git (directo) — https://github.com/modelcontextprotocol/servers/tree/main/src/git
- Phabricator — https://github.com/baba786/phabricator-mcp-server
- Gitingest-MCP — https://github.com/puravparab/Gitingest-MCP

---

## Categoría: Almacenamiento en la nube (☁️)

- Google Drive — https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive
- Box (⭐) — https://developer.box.com/guides/box-mcp/
- VideoDB (agent-toolkit, ⭐) — https://github.com/video-db/agent-toolkit/tree/main/modelcontextprotocol
- Microsoft 365 — https://github.com/softeria/ms-365-mcp-server

---

## Categoría: Bases de datos (🗄️)

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

## Categoría: Comunicación (💬)

- Slack — https://github.com/korotovsky/slack-mcp-server
- LINE Official Account (⭐) — https://github.com/line/line-bot-mcp-server
- Linear — https://github.com/jerhadf/linear-mcp-server
- Atlassian — https://github.com/sooperset/mcp-atlassian
- Carbon Voice (⭐) — https://github.com/PhononX/cv-mcp-server

---

## Categoría: Monitoreo (📈)

- Metoro — https://github.com/metoro-io/metoro-mcp-server
- Raygun — https://github.com/MindscapeHQ/mcp-server-raygun
- Sentry — https://github.com/modelcontextprotocol/servers/tree/main/src/sentry

---

## Categoría: Búsqueda y web (🔍)

- Puppeteer — https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer
- Brave Search — https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search
- Bright Data — https://github.com/luminati-io/brightdata-mcp
- Scrapeless — https://github.com/scrapeless-ai/scrapeless-mcp-server

---

## Categoría: Servicios de ubicación (🗺️)

- Google Maps — https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps

---

## Categoría: Marketing (🎯)

- Agent Mindshare — https://agentmindshare.com

---

## Categoría: Toma de notas (📝)

- Notion — https://github.com/danhilse/notion_mcp

---

## Categoría: Plataformas cloud (⚡)

- Cloudflare (⭐) — https://github.com/cloudflare/mcp-server-cloudflare

---

## Categoría: Automatización de flujos de trabajo (⚙️)

- Make (⭐) — https://github.com/integromat/make-mcp-server
- Zapier — https://zapier.com/mcp

---

## Categoría: Automatización del sistema (🤖)

- Shell (wcgw) — https://github.com/rusiaaman/wcgw

---

## Categoría: Redes sociales (📱)

- YouTube — https://github.com/anaisbetts/mcp-youtube

---

## Categoría: Juegos (🎮)

- Implementaciones de Unity

---

## Categoría: Finanzas (💹)

Pagos, datos de mercado y herramientas financieras.

- PayPal (⭐) — https://github.com/paypal/agent-toolkit
- Stripe (⭐) — https://github.com/stripe/agent-toolkit
- LongPort OpenAPI (⭐) — https://github.com/longportapp/openapi/tree/main/mcp
- x402engine-mcp (50+ APIs de pago para agentes IA via micropagos HTTP 402) — https://github.com/agentc22/x402engine-mcp
- TWZRD Agent Intel (MCP x402 nativo de Solana para puntuación de confianza de agentes IA — puntuación de confianza y verificación de micropagos x402 para agentes IA en Solana) — https://intel.twzrd.xyz

---

## Categoría: Investigación y datos (🧬)

- ArXiv — https://github.com/blazickjp/arxiv-mcp-server

---

## Categoría: Servicios de IA (🤝)

- OpenAI — https://github.com/pierrebrunelle/mcp-server-openai

---

## Categoría: Herramientas de desarrollo (💻)

- Currents (⭐) — https://github.com/currents-dev/currents-mcp

---

## Categoría: Visualización de datos (📊)

- VegaLite — https://github.com/isaacwasserman/mcp-vegalite-server

---

## Categoría: Identidad (🆔)

- Keycloak — https://github.com/ChristophEnglisch/keycloak-model-context-protocol

---

## Categoría: Agregadores (🔗)

- MCPJungle — https://github.com/mcpjungle/MCPJungle

---

## Categoría: Idioma y traducción (💬)

- Lara (⭐) — https://github.com/translated/lara-mcp

---

## Categoría: Seguridad (🔒)

- Semgrep — https://github.com/semgrep/mcp

---

## Categoría: IoT (🔌)

- Coreflux MQTT — https://github.com/CorefluxCommunity/CorefluxMCPServer

---

## Servidores de la comunidad

Una lista extensa de servidores mantenidos por la comunidad está incluida en el documento principal. Consulta la documentación para la lista completa.

---

# Notas

- Ejecuta los servidores de comunidad no confiables en un entorno aislado como un contenedor o una VM.
- En producción, prioriza las implementaciones oficiales (⭐).
- Verifica el método de transporte (stdio, SSE, HTTP), la autenticación y los clientes de ejemplo en el repositorio de cada servidor.
