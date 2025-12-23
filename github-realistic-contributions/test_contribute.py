#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GitHub 贡献图生成器测试模块
测试贡献生成器的各项功能
"""

import unittest
import tempfile
import os
import shutil
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta

import contribute


class TestContribute(unittest.TestCase):
    """贡献生成器测试类"""

    def setUp(self):
        """测试前的准备工作"""
        self.temp_dir = tempfile.mkdtemp()
        self.original_cwd = os.getcwd()
        os.chdir(self.temp_dir)

    def tearDown(self):
        """测试后的清理工作"""
        os.chdir(self.original_cwd)
        shutil.rmtree(self.temp_dir)

    def test_arguments_parsing(self):
        """测试命令行参数解析"""
        # 测试基本参数
        args = contribute.parse_arguments(['-nw'])
        self.assertTrue(args.no_weekends)
        self.assertEqual(args.max_commits, 10)
        self.assertEqual(args.frequency, 80)
        
        # 测试自定义参数
        args = contribute.parse_arguments([
            '--max_commits=15',
            '--frequency=70',
            '--days_before=30',
            '--days_after=10'
        ])
        self.assertEqual(args.max_commits, 15)
        self.assertEqual(args.frequency, 70)
        self.assertEqual(args.days_before, 30)
        self.assertEqual(args.days_after, 10)

    def test_argument_validation(self):
        """测试参数验证"""
        # 测试正常参数
        args = contribute.parse_arguments(['--max_commits=10', '--frequency=80'])
        contribute.validate_arguments(args)
        
        # 测试无效参数
        with self.assertRaises(ValueError):
            args = contribute.parse_arguments(['--max_commits=25'])
            contribute.validate_arguments(args)
        
        with self.assertRaises(ValueError):
            args = contribute.parse_arguments(['--frequency=150'])
            contribute.validate_arguments(args)
        
        with self.assertRaises(ValueError):
            args = contribute.parse_arguments(['--days_before=-10'])
            contribute.validate_arguments(args)

    def test_git_repository_initialization(self):
        """测试 Git 仓库初始化"""
        repo = contribute.GitRepository('test-repo', 'test-user', 'test@example.com')
        
        with patch('contribute.Popen') as mock_popen:
            mock_process = MagicMock()
            mock_process.returncode = 0
            mock_process.wait.return_value = None
            mock_popen.return_value = mock_process
            
            repo.init_repository()
            
            # 验证 Git 命令被正确调用
            expected_calls = [
                (['git', 'init', '-b', 'main'],),
                (['git', 'config', 'user.name', 'test-user'],),
                (['git', 'config', 'user.email', 'test@example.com'],)
            ]
            self.assertEqual(mock_popen.call_count, 3)
            
            for i, call_args in enumerate(mock_popen.call_args_list):
                self.assertEqual(call_args[0], expected_calls[i])

    def test_contribution_generator(self):
        """测试贡献生成器"""
        repo = contribute.GitRepository('test-repo')
        generator = contribute.ContributionGenerator(
            repo, max_commits=5, frequency=100, no_weekends=False
        )
        
        # 测试提交次数计算
        commits = generator._get_commits_for_day()
        self.assertTrue(1 <= commits <= 5)
        
        # 测试日期判断 - 使用正确的日期创建方法
        from datetime import datetime, timedelta
        today = datetime.now()
        weekday = today - timedelta(days=today.weekday())  # 本周一
        weekend = today + timedelta(days=(5 - today.weekday()))  # 本周六
        
        self.assertTrue(generator._should_commit_on_day(weekday))
        
        # 测试周末跳过
        generator.no_weekends = True
        self.assertFalse(generator._should_commit_on_day(weekend))

    def test_commit_message_generation(self):
        """测试提交消息生成"""
        repo = contribute.GitRepository('test-repo')
        generator = contribute.ContributionGenerator(repo)
        
        test_date = datetime(2023, 12, 25, 14, 30)
        message = generator._generate_commit_message(test_date)
        
        # 验证消息格式
        self.assertIn('2023-12-25 14:30', message)
        self.assertTrue(any(template.split(':')[0] in message 
                           for template in contribute.COMMIT_MESSAGES))

    @patch('contribute.Popen')
    def test_integration_with_mocked_git(self, mock_popen):
        """测试与模拟 Git 的集成"""
        mock_process = MagicMock()
        mock_process.returncode = 0
        mock_process.wait.return_value = None
        mock_popen.return_value = mock_process
        
        # 创建临时参数
        args = contribute.parse_arguments([
            '--user_name=testuser',
            '--user_email=test@example.com',
            '--max_commits=3',
            '--frequency=100',
            '--days_before=2',
            '--days_after=0'
        ])
        
        # 模拟主函数执行
        with patch('contribute.parse_arguments', return_value=args):
            with patch('contribute.validate_arguments'):
                with patch('contribute.datetime') as mock_datetime:
                    mock_datetime.now.return_value = datetime(2023, 12, 25, 12, 0)
                    
                    # 执行主函数
                    contribute.main(['--user_name=testuser', '--days_before=1'])
                    
                    # 验证 Git 命令被调用
                    self.assertTrue(mock_popen.called)

    def test_error_handling(self):
        """测试错误处理"""
        # 测试无效参数
        with self.assertRaises(ValueError):
            contribute.main(['--max_commits=25'])
        
        with self.assertRaises(ValueError):
            contribute.main(['--frequency=150'])


class TestGitRepository(unittest.TestCase):
    """Git 仓库类测试"""

    def setUp(self):
        """测试前的准备工作"""
        self.temp_dir = tempfile.mkdtemp()
        self.original_cwd = os.getcwd()
        os.chdir(self.temp_dir)

    def tearDown(self):
        """测试后的清理工作"""
        os.chdir(self.original_cwd)
        shutil.rmtree(self.temp_dir)

    def test_repository_creation(self):
        """测试仓库创建"""
        repo = contribute.GitRepository('test-repo', 'test-user', 'test@example.com')
        self.assertEqual(repo.directory, 'test-repo')
        self.assertEqual(repo.user_name, 'test-user')
        self.assertEqual(repo.user_email, 'test@example.com')

    @patch('contribute.Popen')
    def test_command_execution(self, mock_popen):
        """测试命令执行"""
        repo = contribute.GitRepository('test-repo')
        
        # 模拟成功执行
        mock_process = MagicMock()
        mock_process.returncode = 0
        mock_process.wait.return_value = None
        mock_popen.return_value = mock_process
        
        repo._run_command(['git', 'init'])
        mock_popen.assert_called_once()
        
        # 模拟执行失败
        mock_process.returncode = 1
        with self.assertRaises(Exception):
            repo._run_command(['git', 'invalid-command'])


if __name__ == '__main__':
    # 运行测试
    unittest.main(verbosity=2)
