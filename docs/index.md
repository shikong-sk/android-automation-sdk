# Android Automation SDK 文档

Python SDK for [Android Automation API](https://github.com/shikong-sk/android-automation-api) - 基于 uiautomator2 和 adbutils 的安卓设备自动化控制 REST API 服务的 Python SDK。

## 功能特性

- **设备管理**: 连接、断开、设备状态查询
- **输入操作**: 点击、输入文本、滑动、屏幕控制
- **元素定位**: 通过 resource-id、text、class、XPath 定位元素
- **人类模拟**: 模拟真实人类的点击、拖拽行为
- **导航控制**: Home、返回、菜单、最近应用
- **应用管理**: 启动、停止、清除应用数据
- **ADB 命令**: Shell 命令、文件传输、截图、设备信息
- **脚本执行**: 执行自动化脚本，支持 SSE 流式输出

## 快速链接

- [快速开始](getting-started.md)
- [API 参考](api-reference.md)
- [示例代码](examples.md)
- [配置指南](configuration.md)

## 安装

```bash
# 使用 uv 安装（推荐）
uv pip install android-automation-sdk

# 或使用 pip
pip install android-automation-sdk
```

## 版本要求

- Python 3.10+
- Android Automation API 服务 (需单独部署)

## 相关链接

- [GitHub 仓库](https://github.com/shikong-sk/android-automation-sdk)
- [API 服务仓库](https://github.com/shikong-sk/android-automation-api)
- [问题反馈](https://github.com/shikong-sk/android-automation-sdk/issues)
