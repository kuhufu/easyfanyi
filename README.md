# EasyFanyi - 简易翻译工具

一个基于命令行的高效翻译工具，支持有道和百度翻译 API。

## 功能特性

- 🚀 快速命令行翻译
- 🔍 支持有道和百度两个翻译引擎
- 📖 显示音标和详细解释
- ⚡ 轻量级，无额外依赖
- 💻 Linux/macOS 友好

## 系统要求

- Python 3.6+
- Linux/macOS 操作系统
- 网络连接（用于访问翻译 API）

## 安装步骤

### 1. 克隆仓库（可选）

```bash
git clone <repository-url>
cd easyfanyi
```

### 2. 运行安装脚本

```bash
sudo python3 setup.py $USER
```

或者指定用户名：

```bash
sudo python3 setup.py your_username
```

### 3. 激活配置

安装完成后，重启终端或执行：

```bash
source ~/.bashrc
```

## 使用方法

### 有道翻译（默认）

```bash
# 基本翻译
dic hello

# 显示美式发音
dic hello -p
```

### 百度翻译

```bash
python3 /opt/easyfanyi/dic-baidu.py hello
```

或者创建别名：

```bash
alias dic-baidu='python3 /opt/easyfanyi/dic-baidu.py'
dic-baidu hello
```

## 目录结构

```
easyfanyi/
├── README.md           # 项目文档
├── setup.py            # 安装脚本
├── dic/
│   ├── dic-youdao.py   # 有道翻译工具
│   └── dic-baidu.py    # 百度翻译工具
└── .gitignore          # Git 忽略文件
```

## 代码重构说明

本项目已完成代码重构，主要改进包括：

### 架构优化
- ✅ 模块化设计：分离 API 调用、数据处理和展示逻辑
- ✅ 配置集中管理：API 密钥和端点统一配置
- ✅ 函数职责单一：每个函数只负责一个明确的任务

### 代码质量
- ✅ 类型注解：添加完整的类型提示
- ✅ 文档字符串：所有函数都有详细的 docstring
- ✅ 错误处理：完善的异常处理和错误信息
- ✅ 资源管理：使用 try-finally 确保 HTTP 连接正确关闭

### 用户体验
- ✅ 友好的命令行提示
- ✅ 清晰的错误信息
- ✅ 支持多种使用方式
- ✅ 安装脚本提供详细反馈

### 可维护性
- ✅ 遵循 PEP 8 代码规范
- ✅ 常量集中定义
- ✅ 消除魔法数字
- ✅ 代码注释清晰

## API 配置

### 有道 API
- 当前使用测试密钥，生产环境请替换为自己的密钥
- 文档：https://ai.youdao.com/DOCSIRMA/html/trans/api/wbfy/index.html

### 百度 API
- 当前使用测试密钥，生产环境请替换为自己的密钥
- 文档：https://fanyi-api.baidu.com/

## 故障排除

### 常见问题

**1. 权限错误**
```
Error: Permission denied. Please run with sudo.
```
解决方案：使用 `sudo` 运行安装脚本

**2. 命令未找到**
```
bash: dic: command not found
```
解决方案：确保已运行 `source ~/.bashrc`

**3. 翻译失败**
检查网络连接，确认 API 服务可用

## 贡献指南

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License

## 联系方式

如有问题，请提交 Issue 或联系维护者。
