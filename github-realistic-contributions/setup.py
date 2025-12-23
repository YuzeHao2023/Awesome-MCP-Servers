#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GitHub 贡献图生成器安装脚本
"""

from setuptools import setup, find_packages
import os

# 读取 README 文件
def read_readme():
    """读取 README.md 文件内容"""
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "GitHub 贡献图生成器"

# 读取 requirements.txt
def read_requirements():
    """读取 requirements.txt 文件内容"""
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(requirements_path):
        with open(requirements_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name="github-activity-generator",
    version="2.0.0",
    author="Shpota",
    author_email="shpota@users.noreply.github.com",
    description="一个帮助您瞬间生成美观 GitHub 贡献图的 Python 脚本",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Shpota/github-activity-generator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    install_requires=[
        # 本项目主要使用 Python 标准库，无需额外依赖
    ],
    extras_require={
        "dev": read_requirements(),
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "pytest-mock>=3.8.0",
        ],
        "lint": [
            "flake8>=4.0.0",
            "pylint>=2.15.0",
            "black>=22.0.0",
            "isort>=5.10.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "github-activity-generator=contribute:main",
            "contribute=contribute:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="github, contribution, graph, git, automation",
    project_urls={
        "Bug Reports": "https://github.com/Shpota/github-activity-generator/issues",
        "Source": "https://github.com/Shpota/github-activity-generator",
        "Documentation": "https://github.com/Shpota/github-activity-generator#readme",
    },
) 