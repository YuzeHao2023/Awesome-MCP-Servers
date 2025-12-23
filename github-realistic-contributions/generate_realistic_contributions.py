#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
真实贡献模式生成器
生成更真实的 GitHub 贡献模式：
- 每天 1-5 次提交
- 每隔 4-8 天中断一次（模拟休息日或项目暂停）
"""

import os
import sys
import random
from datetime import datetime, timedelta
from subprocess import Popen, CalledProcessError
import subprocess
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('realistic_contributions.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

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
    "功能增强: {date}",
    "修复编译错误: {date}",
    "优化算法: {date}",
    "清理代码: {date}",
    "更新注释: {date}",
    "修复测试: {date}"
]


class RealisticContributionGenerator:
    """真实贡献模式生成器"""
    
    def __init__(self, user_name=None, user_email=None):
        self.user_name = user_name
        self.user_email = user_email
        self.commit_count = 0
        self.directory = None
        
    def generate_realistic_pattern(self, days=365, repository=None):
        """生成真实贡献模式"""
        # 创建目录
        self.directory = f'realistic-contributions-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}'
        if repository:
            start = repository.rfind('/') + 1
            end = repository.rfind('.')
            self.directory = repository[start:end]
        
        # 初始化仓库
        self._init_repository()
        
        # 生成贡献模式
        current_date = datetime.now()
        start_date = current_date - timedelta(days=days)
        
        logger.info(f"开始生成真实贡献模式，时间范围: {start_date.date()} 到 {current_date.date()}")
        
        current_day = start_date
        consecutive_days = 0
        
        while current_day <= current_date:
            # 决定是否中断（每隔4-8天）
            if consecutive_days >= random.randint(4, 8):
                # 中断期：1-3天
                break_days = random.randint(1, 3)
                logger.info(f"中断期: {current_day.date()} 到 {(current_day + timedelta(days=break_days-1)).date()} ({break_days} 天)")
                current_day += timedelta(days=break_days)
                consecutive_days = 0
                continue
            
            # 生成当天的提交
            commits_today = random.randint(1, 5)
            self._generate_daily_commits(current_day, commits_today)
            
            consecutive_days += 1
            current_day += timedelta(days=1)
        
        logger.info(f"真实贡献模式生成完成，总共 {self.commit_count} 次提交")
        
        # 推送到远程仓库
        if repository:
            self._push_to_remote(repository)
        
        return self.commit_count
    
    def _init_repository(self):
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
    
    def _generate_daily_commits(self, date, commit_count):
        """生成一天的提交"""
        logger.info(f"生成 {date.date()} 的 {commit_count} 次提交")
        
        for i in range(commit_count):
            # 随机选择提交时间（9:00-23:00）
            hour = random.randint(9, 23)
            minute = random.randint(0, 59)
            commit_time = date.replace(hour=hour, minute=minute)
            
            self._make_commit(commit_time)
    
    def _make_commit(self, commit_time):
        """执行一次提交"""
        try:
            # 创建或更新文件
            self._update_file(commit_time)
            
            # 添加文件到暂存区
            self._run_command(['git', 'add', '.'])
            
            # 提交更改
            commit_message = self._generate_commit_message(commit_time)
            self._run_command([
                'git', 'commit', '-m', f'"{commit_message}"',
                '--date', commit_time.strftime('"%Y-%m-%d %H:%M:%S"')
            ])
            
            self.commit_count += 1
            
        except Exception as e:
            logger.error(f"提交失败: {e}")
            raise
    
    def _update_file(self, date):
        """更新文件内容"""
        # 更新 README.md
        readme_path = os.path.join(os.getcwd(), 'README.md')
        with open(readme_path, 'a', encoding='utf-8') as file:
            file.write(f"贡献记录: {date.strftime('%Y-%m-%d %H:%M')}\n\n")
        
        # 随机更新其他文件
        if random.random() < 0.3:  # 30% 概率更新其他文件
            files = ['src/main.py', 'src/utils.py', 'tests/test_main.py', 'docs/README.md']
            for file_path in files:
                if random.random() < 0.2:  # 20% 概率更新每个文件
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    with open(file_path, 'a', encoding='utf-8') as f:
                        f.write(f"# 更新于 {date.strftime('%Y-%m-%d %H:%M')}\n")
    
    def _generate_commit_message(self, date):
        """生成提交消息"""
        import random
        template = random.choice(COMMIT_MESSAGES)
        return template.format(date=date.strftime('%Y-%m-%d %H:%M'))
    
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
    
    def _push_to_remote(self, repository):
        """推送到远程仓库"""
        try:
            self._run_command(['git', 'remote', 'add', 'origin', repository])
            self._run_command(['git', 'branch', '-M', 'main'])
            self._run_command(['git', 'push', '-u', 'origin', 'main'])
            logger.info("更改推送成功")
        except Exception as e:
            logger.error(f"推送失败: {e}")
            raise


def main():
    """主函数"""
    print("🎯 真实贡献模式生成器")
    print("=" * 50)
    
    # 获取用户输入
    days = input("请输入要生成的天数 (默认 365): ").strip()
    days = int(days) if days else 365
    
    user_name = input("请输入 Git 用户名称 (可选): ").strip()
    user_email = input("请输入 Git 用户邮箱 (可选): ").strip()
    
    repository = input("请输入远程仓库链接 (可选，留空仅生成本地): ").strip()
    repository = repository if repository else None
    
    print(f"\n📊 生成配置:")
    print(f"   天数: {days}")
    print(f"   用户: {user_name or '使用全局配置'}")
    print(f"   邮箱: {user_email or '使用全局配置'}")
    print(f"   仓库: {repository or '仅生成本地'}")
    print(f"   模式: 每天 1-5 次提交，每隔 4-8 天中断一次")
    
    confirm = input("\n确认开始生成? (y/N): ").strip().lower()
    if confirm != 'y':
        print("已取消生成")
        return
    
    try:
        # 创建生成器
        generator = RealisticContributionGenerator(user_name, user_email)
        
        # 生成贡献
        total_commits = generator.generate_realistic_pattern(days, repository)
        
        print(f"\n🎉 生成完成!")
        print(f"📁 本地目录: {generator.directory}")
        if repository:
            print(f"🌐 远程仓库: {repository}")
        print(f"📊 总提交数: {total_commits}")
        print(f"📈 平均每天: {total_commits/days:.1f} 次提交")
        
    except Exception as e:
        logger.error(f"生成失败: {e}")
        print(f"❌ 生成失败: {e}")


if __name__ == "__main__":
    main() 