#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GitHub 贡献图生成器配置文件
管理项目的各种设置和常量
"""

import os
from datetime import time

# 项目信息
PROJECT_NAME = "GitHub 贡献图生成器"
PROJECT_VERSION = "2.0.0"
PROJECT_AUTHOR = "Shpota"
PROJECT_LICENSE = "Apache License 2.0"

# 默认配置
DEFAULT_MAX_COMMITS = 10
DEFAULT_FREQUENCY = 80
DEFAULT_DAYS_BEFORE = 365
DEFAULT_DAYS_AFTER = 0
DEFAULT_COMMIT_TIME = time(20, 0)  # 晚上 8 点

# 限制值
MIN_COMMITS_PER_DAY = 1
MAX_COMMITS_PER_DAY = 20
MIN_FREQUENCY = 0
MAX_FREQUENCY = 100

# 提交消息模板
COMMIT_MESSAGES = [
    "更新文档: {date}",
    "修复小问题: {date}",
    "代码优化: {date}",
    "添加新功能: {date}",
    "重构代码: {date}",
    "更新配置: {date}",
    "修复bug: {date}",
    "改进性能: {date}",
    "添加测试: {date}",
    "更新依赖: {date}",
    "代码审查: {date}",
    "文档完善: {date}",
    "性能调优: {date}",
    "安全修复: {date}",
    "功能增强: {date}"
]

# 日志配置
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_FILE = "contribute.log"

# Git 配置
GIT_BRANCH = "main"
GIT_REMOTE_NAME = "origin"

# 文件配置
README_FILENAME = "README.md"
ENCODING = "utf-8"

# 错误消息
ERROR_MESSAGES = {
    "invalid_days_before": "days_before 不能为负数",
    "invalid_days_after": "days_after 不能为负数",
    "invalid_max_commits": "max_commits 必须在 1-20 之间",
    "invalid_frequency": "frequency 必须在 0-100 之间",
    "git_init_failed": "Git 仓库初始化失败",
    "git_config_failed": "Git 配置失败",
    "git_push_failed": "Git 推送失败",
    "file_write_failed": "文件写入失败",
    "invalid_repository": "无效的仓库链接"
}

# 成功消息
SUCCESS_MESSAGES = {
    "repository_created": "Git 仓库初始化成功: {directory}",
    "remote_added": "远程仓库添加成功: {repository}",
    "changes_pushed": "更改推送成功",
    "contributions_generated": "贡献记录生成完成，总共 {count} 次提交",
    "generation_completed": "🎉 仓库生成成功完成!"
}

# 工作日配置
WEEKEND_DAYS = [5, 6]  # 周六和周日

# 环境变量
ENV_VARS = {
    "GITHUB_TOKEN": "GitHub 访问令牌",
    "GIT_USER_NAME": "Git 用户名称",
    "GIT_USER_EMAIL": "Git 用户邮箱"
}

def get_env_config():
    """获取环境变量配置"""
    config = {}
    for var, description in ENV_VARS.items():
        value = os.getenv(var)
        if value:
            config[var] = value
    return config

def validate_config():
    """验证配置的有效性"""
    errors = []
    
    if not (MIN_COMMITS_PER_DAY <= DEFAULT_MAX_COMMITS <= MAX_COMMITS_PER_DAY):
        errors.append(f"默认最大提交次数必须在 {MIN_COMMITS_PER_DAY}-{MAX_COMMITS_PER_DAY} 之间")
    
    if not (MIN_FREQUENCY <= DEFAULT_FREQUENCY <= MAX_FREQUENCY):
        errors.append(f"默认频率必须在 {MIN_FREQUENCY}-{MAX_FREQUENCY} 之间")
    
    if DEFAULT_DAYS_BEFORE < 0:
        errors.append("默认天数不能为负数")
    
    if len(COMMIT_MESSAGES) == 0:
        errors.append("提交消息模板不能为空")
    
    return errors

# 验证配置
if __name__ == "__main__":
    errors = validate_config()
    if errors:
        print("配置错误:")
        for error in errors:
            print(f"  - {error}")
        exit(1)
    else:
        print("✅ 配置验证通过") 