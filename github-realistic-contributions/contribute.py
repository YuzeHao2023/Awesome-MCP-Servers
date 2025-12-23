#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GitHub 贡献图生成器
用于生成美观的 GitHub 贡献图，展示过去一年的活动记录

作者: Shpota
许可证: Apache License 2.0
"""

import argparse
import os
import sys
from datetime import datetime, timedelta
from random import randint, choice
import subprocess
from subprocess import Popen, CalledProcessError
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('contribute.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

# 默认提交消息模板
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
    "更新依赖: {date}"
]


class GitRepository:
    """Git 仓库管理类"""
    
    def __init__(self, directory, user_name=None, user_email=None):
        self.directory = directory
        self.user_name = user_name
        self.user_email = user_email
        
    def init_repository(self):
        """初始化 Git 仓库"""
        try:
            os.makedirs(self.directory, exist_ok=True)
            os.chdir(self.directory)
            
            # 初始化 Git 仓库
            self._run_command(['git', 'init', '-b', 'main'])
            
            # 配置用户信息
            if self.user_name:
                self._run_command(['git', 'config', 'user.name', self.user_name])
            if self.user_email:
                self._run_command(['git', 'config', 'user.email', self.user_email])
                
            logger.info(f"Git 仓库初始化成功: {self.directory}")
            
        except Exception as e:
            logger.error(f"初始化仓库失败: {e}")
            raise
    
    def add_remote(self, repository_url):
        """添加远程仓库"""
        try:
            self._run_command(['git', 'remote', 'add', 'origin', repository_url])
            self._run_command(['git', 'branch', '-M', 'main'])
            logger.info(f"远程仓库添加成功: {repository_url}")
        except Exception as e:
            logger.error(f"添加远程仓库失败: {e}")
            raise
    
    def push_changes(self):
        """推送更改到远程仓库"""
        try:
            self._run_command(['git', 'push', '-u', 'origin', 'main'])
            logger.info("更改推送成功")
        except Exception as e:
            logger.error(f"推送更改失败: {e}")
            raise
    
    def _run_command(self, commands):
        """执行 Git 命令"""
        try:
            process = Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            process.wait()
            if process.returncode != 0:
                raise CalledProcessError(process.returncode, commands)
        except CalledProcessError as e:
            logger.error(f"命令执行失败: {' '.join(commands)}")
            raise


class ContributionGenerator:
    """贡献生成器类"""
    
    def __init__(self, git_repo, max_commits=10, frequency=80, no_weekends=False):
        self.git_repo = git_repo
        self.max_commits = max_commits
        self.frequency = frequency
        self.no_weekends = no_weekends
        self.commit_count = 0
        
    def generate_contributions(self, start_date, days_before, days_after):
        """生成贡献记录"""
        logger.info(f"开始生成贡献记录，时间范围: {start_date} 前后 {days_before}/{days_after} 天")
        
        for day in (start_date + timedelta(n) for n in range(days_before + days_after)):
            if self._should_commit_on_day(day):
                commits_today = self._get_commits_for_day()
                for commit_time in (day + timedelta(minutes=m) for m in range(commits_today)):
                    self._make_contribution(commit_time)
        
        logger.info(f"贡献记录生成完成，总共 {self.commit_count} 次提交")
    
    def _should_commit_on_day(self, day):
        """判断是否应该在指定日期提交"""
        # 检查是否跳过周末
        if self.no_weekends and day.weekday() >= 5:
            return False
        
        # 根据频率决定是否提交
        return randint(0, 100) < self.frequency
    
    def _get_commits_for_day(self):
        """获取当天的提交次数"""
        max_c = max(1, min(20, self.max_commits))
        return randint(1, max_c)
    
    def _make_contribution(self, commit_time):
        """执行一次提交"""
        try:
            # 创建或更新 README.md 文件
            readme_path = os.path.join(os.getcwd(), 'README.md')
            with open(readme_path, 'a', encoding='utf-8') as file:
                file.write(self._generate_commit_message(commit_time) + '\n\n')
            
            # 添加文件到暂存区
            self.git_repo._run_command(['git', 'add', '.'])
            
            # 提交更改
            commit_message = self._generate_commit_message(commit_time)
            self.git_repo._run_command([
                'git', 'commit', '-m', f'"{commit_message}"',
                '--date', commit_time.strftime('"%Y-%m-%d %H:%M:%S"')
            ])
            
            self.commit_count += 1
            
        except Exception as e:
            logger.error(f"提交失败: {e}")
            raise
    
    def _generate_commit_message(self, date):
        """生成提交消息"""
        template = choice(COMMIT_MESSAGES)
        return template.format(date=date.strftime('%Y-%m-%d %H:%M'))


def validate_arguments(args):
    """验证命令行参数"""
    if args.days_before < 0:
        raise ValueError("days_before 不能为负数")
    if args.days_after < 0:
        raise ValueError("days_after 不能为负数")
    if not (1 <= args.max_commits <= 20):
        raise ValueError("max_commits 必须在 1-20 之间")
    if not (0 <= args.frequency <= 100):
        raise ValueError("frequency 必须在 0-100 之间")


def main(def_args=sys.argv[1:]):
    """主函数"""
    try:
        # 解析命令行参数
        args = parse_arguments(def_args)
        validate_arguments(args)
        
        # 获取当前时间
        curr_date = datetime.now()
        
        # 确定目录名称
        if args.repository:
            start = args.repository.rfind('/') + 1
            end = args.repository.rfind('.')
            directory = args.repository[start:end]
        else:
            directory = 'repository-' + curr_date.strftime('%Y-%m-%d-%H-%M-%S')
        
        # 创建 Git 仓库
        git_repo = GitRepository(directory, args.user_name, args.user_email)
        git_repo.init_repository()
        
        # 创建贡献生成器
        generator = ContributionGenerator(
            git_repo, 
            args.max_commits, 
            args.frequency, 
            args.no_weekends
        )
        
        # 计算开始日期
        start_date = curr_date.replace(hour=20, minute=0) - timedelta(days=args.days_before)
        
        # 生成贡献记录
        generator.generate_contributions(start_date, args.days_before, args.days_after)
        
        # 推送到远程仓库
        if args.repository:
            git_repo.add_remote(args.repository)
            git_repo.push_changes()
        
        print('\n🎉 仓库生成 \033[6;30;42m成功完成\033[0m!')
        print(f'📁 本地目录: {directory}')
        if args.repository:
            print(f'🌐 远程仓库: {args.repository}')
        print(f'📊 总提交数: {generator.commit_count}')
        
    except Exception as e:
        logger.error(f"程序执行失败: {e}")
        sys.exit(1)


def parse_arguments(argsval):
    """解析命令行参数"""
    parser = argparse.ArgumentParser(
        description='GitHub 贡献图生成器 - 生成美观的 GitHub 贡献图',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  python contribute.py --repository=git@github.com:user/repo.git
  python contribute.py --max_commits=12 --frequency=60 --no_weekends
  python contribute.py --days_before=30 --days_after=10
        """
    )
    
    parser.add_argument('-nw', '--no_weekends',
                        action='store_true', default=False,
                        help="不在周末提交代码")
    
    parser.add_argument('-mc', '--max_commits', type=int, default=10,
                        help="每天最大提交次数 (1-20，默认: 10)")
    
    parser.add_argument('-fr', '--frequency', type=int, default=80,
                        help="提交频率百分比 (0-100，默认: 80)")
    
    parser.add_argument('-r', '--repository', type=str,
                        help="远程 Git 仓库链接 (SSH 或 HTTPS 格式)")
    
    parser.add_argument('-un', '--user_name', type=str,
                        help="覆盖 Git 用户名称配置")
    
    parser.add_argument('-ue', '--user_email', type=str,
                        help="覆盖 Git 用户邮箱配置")
    
    parser.add_argument('-db', '--days_before', type=int, default=365,
                        help="从当前日期往前多少天开始提交 (默认: 365)")
    
    parser.add_argument('-da', '--days_after', type=int, default=0,
                        help="从当前日期往后多少天继续提交 (默认: 0)")
    
    parser.add_argument('--version', action='version', version='1.0.0')
    
    return parser.parse_args(argsval)


if __name__ == "__main__":
    main()
