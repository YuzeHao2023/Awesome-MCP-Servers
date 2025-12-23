# GitHub 真实贡献图生成器

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/shaozheng0503/github-realistic-contributions.svg)](https://github.com/shaozheng0503/github-realistic-contributions)
[![GitHub forks](https://img.shields.io/github/forks/shaozheng0503/github-realistic-contributions.svg)](https://github.com/shaozheng0503/github-realistic-contributions)
[![GitHub issues](https://img.shields.io/github/issues/shaozheng0503/github-realistic-contributions.svg)](https://github.com/shaozheng0503/github-realistic-contributions/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/shaozheng0503/github-realistic-contributions.svg)](https://github.com/shaozheng0503/github-realistic-contributions/pulls)

> 🎯 **基于 [@Shpota/github-activity-generator](https://github.com/Shpota/github-activity-generator) 灵感开发**  
> 🚀 **完全中文化 + 真实贡献模式 + 智能中断算法**

## ⚠️ 重要声明

**本项目仅用于教育目的，旨在：**
- 学习 Git 和 GitHub 的使用
- 理解版本控制的工作机制  
- 演示开源项目的开发流程

**请勿用于虚假展示专业贡献或任何欺诈行为。**

---

## 📖 项目简介

一个智能的 GitHub 贡献图生成器，能够创建**高度真实**的开发者活动模式，模拟真实的编程工作习惯。该脚本可以在过去一年内为您的 GitHub 账户生成大量提交记录，以丰富您的贡献图表。

### 🎯 效果展示

**使用前：**
```
GitHub 贡献图表空白或稀疏
```

**使用后：**
```
GitHub 贡献图表丰富多彩，展示活跃的开发者形象
```

## ✨ 主要特性

### 🎯 真实贡献模式
- **智能中断算法**: 每隔 4-8 天自动中断 1-3 天，模拟休息和项目暂停
- **人性化时间分布**: 9:00-23:00 的工作时间，符合真实开发习惯
- **多样化提交**: 20 种不同的中文提交消息模板
- **自然频率**: 每天 1-5 次提交，避免机械化的规律模式

### 🌟 核心改进
- **完全中文化**: 用户界面、错误提示、文档全部中文化
- **面向对象设计**: 模块化架构，易于维护和扩展
- **智能配置**: 灵活的配置选项和参数验证
- **详细日志**: 完整的操作日志和错误追踪
- **测试覆盖**: 完整的单元测试和集成测试

### 🛠️ 开发工具
- **配置文件管理**: 集中化的配置管理
- **依赖管理**: requirements.txt 和 setup.py
- **CI/CD 支持**: GitHub Actions 自动化测试
- **开发工具**: Makefile 简化开发流程

## 📊 效果对比

### 传统生成器 vs 真实模式生成器

| 特性 | 传统生成器 | 真实模式生成器 |
|------|------------|----------------|
| 提交模式 | 机械规律 | 自然随机 |
| 时间分布 | 固定时间 | 真实工作时间 |
| 中断处理 | 无 | 智能中断算法 |
| 语言支持 | 英文 | 完全中文化 |
| 代码架构 | 过程式 | 面向对象 |
| 配置管理 | 硬编码 | 灵活配置 |
| 测试覆盖 | 基础 | 完整测试 |
| 开发工具 | 简单 | 丰富工具链 |

## 🚀 快速开始

### 1. 环境要求

```bash
# 确保已安装 Python 3.8+ 和 Git
python --version  # Python 3.8+
git --version     # Git 2.0+
```

### 2. 安装项目

```bash
# 克隆项目
git clone https://github.com/shaozheng0503/github-realistic-contributions.git
cd github-realistic-contributions

# 安装依赖（可选）
pip install -r requirements.txt
```

### 3. 基本使用

```bash
# 生成一年的真实贡献记录
python generate_realistic_contributions.py

# 或者使用原始脚本
python contribute.py --repository=git@github.com:用户名/仓库名.git
```

## 📖 详细使用指南

### 🎯 真实贡献模式生成器

#### 基本命令
```bash
python generate_realistic_contributions.py
```

#### 交互式配置
程序会引导您输入以下信息：
- **天数**: 要生成的天数（默认 365 天）
- **用户名称**: Git 用户名称（可选）
- **用户邮箱**: Git 用户邮箱（可选）
- **远程仓库**: GitHub 仓库链接（可选）

#### 生成模式说明
- **每天提交数**: 1-5 次随机分布
- **提交时间**: 9:00-23:00 随机分布
- **中断频率**: 每隔 4-8 天中断一次
- **中断时长**: 1-3 天随机
- **提交消息**: 20 种中文模板随机选择

### 🔧 原始脚本使用

#### 基本用法
```bash
# 生成一年的贡献记录
python contribute.py --repository=git@github.com:用户名/仓库名.git

# 工作日模式（跳过周末）
python contribute.py --max_commits=12 --frequency=60 --no_weekends

# 自定义时间范围
python contribute.py --days_before=30 --days_after=10

# 本地测试（不推送到远程）
python contribute.py --max_commits=5 --frequency=100 --days_before=7
```

#### 参数说明

| 参数 | 说明 | 默认值 | 示例 |
|------|------|--------|------|
| `--max_commits` | 每天最大提交次数 (1-20) | 10 | `--max_commits=12` |
| `--frequency` | 提交频率百分比 (0-100) | 80 | `--frequency=60` |
| `--no_weekends` | 不在周末提交 | False | `--no_weekends` |
| `--days_before` | 从当前日期往前多少天 | 365 | `--days_before=30` |
| `--days_after` | 从当前日期往后多少天 | 0 | `--days_after=10` |
| `--user_name` | 覆盖 Git 用户名称 | 全局配置 | `--user_name="张三"` |
| `--user_email` | 覆盖 Git 用户邮箱 | 全局配置 | `--user_email="zhangsan@example.com"` |
| `--repository` | 远程 Git 仓库链接 | 无 | `--repository=git@github.com:user/repo.git` |

## 📁 项目结构

```
github-realistic-contributions/
├── contribute.py                    # 原始贡献生成器（中文化 + 优化）
├── generate_realistic_contributions.py  # 真实贡献模式生成器
├── test_contribute.py              # 测试文件
├── config.py                       # 配置文件
├── setup.py                        # 安装脚本
├── requirements.txt                # 依赖管理
├── Makefile                        # 开发工具
├── .gitignore                      # Git 忽略文件
├── README.md                       # 项目文档
├── CHANGELOG.md                    # 更新日志
├── LICENSE                         # 许可证文件
└── .github/
    └── workflows/
        └── build.yml               # CI/CD 配置
```

## 🎯 使用场景

### 1. 学习目的
- 了解 Git 和 GitHub 的工作机制
- 学习版本控制和贡献图原理
- 演示开源项目的开发流程

### 2. 项目演示
- 展示开发者的活跃度
- 创建示例项目的历史记录
- 演示持续集成的效果

### 3. 个人品牌
- 展示编程技能和活跃度
- 创建专业的开发者形象
- 提升 GitHub 个人资料质量

## 🔧 开发指南

### 环境设置
```bash
# 克隆项目
git clone https://github.com/shaozheng0503/github-realistic-contributions.git
cd github-realistic-contributions

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
```

### 运行测试
```bash
# 运行所有测试
python -m pytest

# 运行特定测试
python -m pytest test_contribute.py

# 生成测试报告
python -m pytest --cov=contribute --cov-report=html
```

### 代码质量检查
```bash
# 代码格式化
black contribute.py

# 代码检查
flake8 contribute.py

# 类型检查
mypy contribute.py
```

### 使用 Makefile
```bash
# 查看所有可用命令
make help

# 运行测试
make test

# 代码检查
make lint

# 代码格式化
make format

# 安装项目
make install
```

## 📈 贡献指南

### 提交 Issue
1. 检查是否已有相关 Issue
2. 使用清晰的标题描述问题
3. 提供详细的复现步骤
4. 包含错误信息和环境信息

### 提交 Pull Request
1. Fork 项目到您的账户
2. 创建功能分支
3. 编写代码和测试
4. 确保所有测试通过
5. 提交 Pull Request

### 代码规范
- 遵循 PEP 8 代码风格
- 添加适当的注释和文档
- 编写单元测试
- 使用中文注释和文档

## 🛠️ 技术栈

- **Python**: 主要编程语言
- **Git**: 版本控制
- **GitHub Actions**: CI/CD 自动化
- **pytest**: 测试框架
- **black/flake8**: 代码质量工具

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- **灵感来源**: [@Shpota/github-activity-generator](https://github.com/Shpota/github-activity-generator)
- **开源社区**: 感谢所有贡献者和用户的支持
- **技术栈**: Python, Git, GitHub Actions

## 📞 联系我们

- **项目地址**: [https://github.com/shaozheng0503/github-realistic-contributions](https://github.com/shaozheng0503/github-realistic-contributions)
- **问题反馈**: [Issues](https://github.com/shaozheng0503/github-realistic-contributions/issues)
- **功能建议**: [Discussions](https://github.com/shaozheng0503/github-realistic-contributions/discussions)

## ⭐ 支持项目

如果这个项目对您有帮助，请给我们一个 ⭐ Star！

---

**免责声明**: 本项目仅用于教育目的，请勿用于任何虚假展示或欺诈行为。我们鼓励进行真实的开源贡献和编程实践。 
