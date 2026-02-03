"""
快速开始
--------
确保 Android Automation API 服务已启动，然后运行示例：

```bash
# 运行各个示例
python -m examples 01_basic_device
python -m examples 02_input_operations
python -m examples 03_element_location
...
```

示例列表
--------

| 模块 | 功能 | 说明 |
|------|------|------|
| basic_device | 基础设备操作 | 连接、断开、状态查询 |
| input_operations | 输入操作 | 点击、输入、滑动、屏幕控制 |
| element_location | 元素定位 | 查找、等待、获取元素信息 |
| human_simulation | 人类模拟 | 模拟真实人类行为的操作 |
| app_management | 应用管理 | 启动、停止、查询应用 |
| adb_commands | ADB 命令 | Shell、文件传输、设备信息 |
| script_execution | 脚本执行 | 执行 DSL 自动化脚本 |
| navigation | 导航控制 | Home、返回、菜单等 |
| comprehensive_workflow | 综合流程 | 完整的自动化流程示例 |
| context_manager | 上下文管理 | 上下文管理器和错误处理 |

运行所有示例
------------

```bash
# 运行所有示例
python -m examples
```

注意事项
--------

1. 确保 Android Automation API 服务已启动
2. 确保设备已通过 USB 或 WiFi 连接
3. 某些操作可能需要设备管理员权限
4. 人类模拟操作包含随机延迟，实际执行时间会有差异
"""

__all__ = [
    "basic_device",
    "input_operations",
    "element_location",
    "human_simulation",
    "app_management",
    "adb_commands",
    "script_execution",
    "navigation",
    "comprehensive_workflow",
    "context_manager",
]
