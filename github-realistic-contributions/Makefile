# GitHub 贡献图生成器 Makefile
# 简化开发、测试和部署流程

.PHONY: help install test lint clean build dist publish docs

# 默认目标
help:
	@echo "GitHub 贡献图生成器 - 可用命令:"
	@echo ""
	@echo "  安装和设置:"
	@echo "    install     - 安装开发依赖"
	@echo "    install-dev - 安装开发环境"
	@echo ""
	@echo "  测试和质量检查:"
	@echo "    test        - 运行所有测试"
	@echo "    test-cov    - 运行测试并生成覆盖率报告"
	@echo "    lint        - 运行代码风格检查"
	@echo "    type-check  - 运行类型检查"
	@echo ""
	@echo "  构建和分发:"
	@echo "    build       - 构建项目"
	@echo "    dist        - 创建分发包"
	@echo "    clean       - 清理构建文件"
	@echo ""
	@echo "  文档:"
	@echo "    docs        - 生成文档"
	@echo ""
	@echo "  开发工具:"
	@echo "    format      - 格式化代码"
	@echo "    check       - 运行所有检查"

# 安装依赖
install:
	pip install -r requirements.txt

install-dev:
	pip install -e ".[dev]"

# 测试
test:
	python -m pytest test_contribute.py -v

test-cov:
	python -m pytest test_contribute.py -v --cov=contribute --cov-report=html --cov-report=term-missing

# 代码质量检查
lint:
	flake8 contribute.py test_contribute.py config.py setup.py --max-line-length=120 --ignore=E501,W503
	pylint contribute.py test_contribute.py config.py setup.py

type-check:
	mypy contribute.py test_contribute.py config.py setup.py

# 格式化代码
format:
	black contribute.py test_contribute.py config.py setup.py
	isort contribute.py test_contribute.py config.py setup.py

# 运行所有检查
check: lint type-check test

# 构建
build:
	python setup.py build

# 创建分发包
dist: clean
	python setup.py sdist bdist_wheel

# 清理
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

# 文档
docs:
	sphinx-build -b html docs/ docs/_build/html

# 验证配置
validate-config:
	python config.py

# 运行示例
example:
	python contribute.py --max_commits=5 --frequency=100 --days_before=7

# 安装到系统
install-system:
	python setup.py install

# 卸载
uninstall:
	pip uninstall github-activity-generator -y

# 检查依赖
check-deps:
	pip check

# 更新依赖
update-deps:
	pip install --upgrade -r requirements.txt

# 安全检查
security-check:
	safety check

# 性能测试
benchmark:
	python -m timeit -n 100 -r 3 "import contribute; contribute.parse_arguments(['--help'])"

# 创建发布版本
release: clean test lint type-check dist
	@echo "✅ 发布版本准备完成"
	@echo "📦 分发包已创建在 dist/ 目录中"

# 开发环境设置
dev-setup: install-dev
	pre-commit install
	@echo "✅ 开发环境设置完成"

# 运行预提交检查
pre-commit:
	pre-commit run --all-files

# 显示项目信息
info:
	@echo "项目信息:"
	@echo "  名称: GitHub 贡献图生成器"
	@echo "  版本: 2.0.0"
	@echo "  Python 版本: $(shell python --version)"
	@echo "  当前目录: $(PWD)"
	@echo "  Git 状态: $(shell git status --porcelain 2>/dev/null || echo '未初始化')" 