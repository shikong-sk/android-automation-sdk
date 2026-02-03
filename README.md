# Android Automation SDK

Python SDK for [Android Automation API](https://github.com/anomalyco/android-automation-api) - 基于 uiautomator2 和 adbutils 的安卓设备自动化控制 REST API 服务的 Python SDK。

## 功能特性

- **设备管理**: 连接、断开、设备状态查询
- **输入操作**: 点击、输入文本、滑动、屏幕控制
- **元素定位**: 通过 resource-id、text、class、XPath 定位元素
- **人类模拟**: 模拟真实人类的点击、拖拽行为
- **导航控制**: Home、返回、菜单、最近应用
- **应用管理**: 启动、停止、清除应用数据
- **ADB 命令**: Shell 命令、文件传输、截图、设备信息
- **脚本执行**: 执行自动化脚本，支持 SSE 流式输出

## 安装

```bash
# 使用 uv 安装（推荐）
uv pip install android-automation-sdk

# 或使用 pip
pip install android-automation-sdk
```

## 快速开始

```python
from android_automation import AndroidAutomation

# 创建客户端
client = AndroidAutomation(base_url="http://localhost:8000")

# 连接设备（自动选择第一个可用设备）
device_info = client.device.connect()
print(f"已连接设备: {device_info.serial}")

# 点击元素
client.input.click(resource_id="com.example:id/button")

# 输入文本
client.input.set_text(resource_id="com.example:id/input", text="Hello World")

# 启动应用
client.app.start("com.example.app")

# 执行滑动
client.input.swipe(direction="up", percent=0.5)

# 获取设备状态
status = client.device.get_status()
print(f"连接状态: {status.connected}")

# 断开设备
client.device.disconnect()
```

## API 文档

### 设备管理

```python
# 连接设备
device_info = client.device.connect(device_serial=None)  # 自动选择设备
device_info = client.device.connect(device_serial="emulator-5554")  # 通过序列号连接
device_info = client.device.connect(device_serial="192.168.1.100:5555")  # WiFi 连接

# 获取设备状态
status = client.device.get_status()
print(status.connected)
print(status.device_info.serial if status.connected else "未连接")

# 断开设备
client.device.disconnect()
```

### 输入操作

```python
# 点击元素
client.input.click(resource_id="com.example:id/button")
client.input.click_by_text(text="确定")
client.input.click_by_class(class_name="android.widget.Button")
client.input.click_by_xpath(xpath="//Button[@text='确定']")

# 输入文本
client.input.set_text(resource_id="com.example:id/input", text="Hello")

# 清除文本
client.input.clear_text(resource_id="com.example:id/input")

# 滑动屏幕
client.input.swipe(direction="up", percent=0.5)  # 向上滑动 50%
client.input.swipe(direction="down", percent=0.3)  # 向下滑动 30%
client.input.swipe(direction="left")  # 向左滑动
client.input.swipe(direction="right")  # 向右滑动

# 屏幕控制
client.input.screen_on()   # 亮屏
client.input.screen_off()  # 锁屏
client.input.unlock()      # 解锁
```

### 元素定位

```python
# 查找元素
element = client.input.find_by_id(resource_id="com.example:id/button")
element = client.input.find_by_text(text="确定")
element = client.input.find_by_class(class_name="android.widget.Button")
element = client.input.find_by_xpath(xpath="//Button[@text='确定']")

# 查找所有匹配元素
elements = client.input.find_elements_by_class(class_name="android.widget.TextView")
print(f"找到 {elements.count} 个元素")

# 检查元素是否存在
exists = client.input.exists(resource_id="com.example:id/button")
exists = client.input.exists_by_text(text="确定")

# 获取元素信息
text = client.input.get_text(resource_id="com.example:id/title")
bounds = client.input.get_bounds(resource_id="com.example:id/button")

# 等待元素
client.input.wait_appear(resource_id="com.example:id/dialog", timeout=10.0)
client.input.wait_gone(resource_id="com.example:id/loading", timeout=10.0)

# 获取界面结构
hierarchy = client.input.get_hierarchy()
```

### 人类模拟操作

模拟真实人类的点击和拖拽行为，包含随机偏移、延迟和自然的运动轨迹：

```python
# 人类模拟点击
client.input.human_click(x=500, y=800)
client.input.human_click(
    selector_type="id",
    selector_value="com.example:id/button",
    offset_min=5,
    offset_max=15,
    delay_min=0.1,
    delay_max=0.5,
)

# 人类模拟双击
client.input.human_double_click(
    selector_type="text",
    selector_value="确定",
    interval_min=0.1,
    interval_max=0.3,
)

# 人类模拟长按
client.input.human_long_press(
    x=500,
    y=800,
    duration_min=1.0,
    duration_max=2.0,
)

# 人类模拟拖拽
client.input.human_drag(
    start_x=100,
    start_y=1500,
    end_x=100,
    end_y=500,
    trajectory_type="bezier",  # 或 "linear_jitter"
    speed_mode="ease_in_out",  # ease_in, ease_out, linear, random
    duration=1.0,
)

# 元素到元素拖拽
client.input.human_drag(
    start_selector_type="id",
    start_selector_value="com.example:id/source",
    end_selector_type="id",
    end_selector_value="com.example:id/target",
)
```

### 导航控制

```python
client.navigation.home()         # 返回主屏幕
client.navigation.back()         # 返回上一页
client.navigation.menu()         # 打开菜单
client.navigation.go_home()      # 确保返回主页
client.navigation.recent_apps()  # 打开最近应用
```

### 应用管理

```python
# 启动应用
client.app.start("com.example.app")

# 停止应用
client.app.stop("com.example.app")

# 清除应用数据
client.app.clear("com.example.app")

# 获取应用版本
version = client.app.get_version("com.example.app")
print(f"版本: {version.version}")

# 检查应用运行状态
status = client.app.get_status("com.example.app")
print(f"运行中: {status.running}")

# 获取当前前台应用
current = client.app.get_current()
print(f"当前应用: {current.package}")
```

### ADB 命令

```python
# 获取已安装应用列表
packages = client.adb.list_packages(filter_type="third_party")  # third_party, system, None

# 获取应用详细信息
info = client.adb.get_package_info("com.example.app")

# 安装 APK
client.adb.install_apk("/path/to/app.apk", reinstall=False, grant_permissions=True)

# 卸载应用
client.adb.uninstall_package("com.example.app", keep_data=False)

# 获取设备信息
info = client.adb.get_device_info()

# 获取电池信息
battery = client.adb.get_battery_info()

# 获取屏幕分辨率
resolution = client.adb.get_screen_resolution()

# 获取屏幕密度
density = client.adb.get_screen_density()

# 获取设备属性
model = client.adb.get_prop("ro.product.model")

# 执行 Shell 命令
output = client.adb.shell("ls /sdcard")

# 推送文件到设备
client.adb.push_file("/local/path/file.txt", "/sdcard/file.txt")

# 从设备拉取文件
client.adb.pull_file("/sdcard/file.txt", "/local/path/file.txt")

# 截取屏幕截图
client.adb.take_screenshot("/local/path/screenshot.png")

# 重启设备
client.adb.reboot()  # 正常重启
client.adb.reboot(mode="recovery")  # 重启到 recovery
client.adb.reboot(mode="bootloader")  # 重启到 bootloader
```

### 脚本执行

```python
# 执行脚本内容
result = client.script.execute(
    content="""
    home
    wait 1
    start_app "com.example.app"
    wait 2
    click id:"com.example:id/button"
    """
)
print(f"执行成功: {result.success}")
print(f"日志: {result.logs}")

# 执行脚本文件
result = client.script.execute_file("my_script.script")

# 验证脚本语法
validation = client.script.validate(
    content="""
    click id:"button"
    wait 1
    """
)
print(f"语法正确: {validation.valid}")

# 流式执行脚本（SSE）
for event in client.script.execute_stream(content="home\nwait 1\nlog '完成'"):
    print(event)  # {'type': 'log', 'data': '...'}
    if event["type"] == "end":
        break

# 停止正在执行的脚本
client.script.stop(session_id)

# 脚本管理
scripts = client.script.list()  # 获取脚本列表
script = client.script.get("my_script.script")  # 获取脚本内容
client.script.save("my_script.script", content="...")  # 保存脚本
client.script.delete("my_script.script")  # 删除脚本
```

## 通用选择器

所有输入操作都支持多种选择器类型：

```python
from android_automation import SelectorType

# 通过 ID 定位
client.input.click_by_selector(
    selector_type=SelectorType.ID,
    selector_value="com.example:id/button"
)

# 通过文本定位
client.input.click_by_selector(
    selector_type=SelectorType.TEXT,
    selector_value="确定"
)

# 通过类名定位
client.input.click_by_selector(
    selector_type=SelectorType.CLASS,
    selector_value="android.widget.Button"
)

# 通过 XPath 定位
client.input.click_by_selector(
    selector_type=SelectorType.XPATH,
    selector_value="//Button[@text='确定']"
)
```

## 错误处理

```python
from android_automation import AndroidAutomation
from android_automation.exceptions import (
    APIError,
    DeviceNotConnectedError,
    ElementNotFoundError,
    TimeoutError,
)

try:
    client.device.connect()
    client.input.click(resource_id="com.example:id/button")
except DeviceNotConnectedError:
    print("设备未连接")
except ElementNotFoundError:
    print("元素未找到")
except TimeoutError:
    print("操作超时")
except APIError as e:
    print(f"API 错误: {e.status_code} - {e.message}")
```

## 配置

```python
from android_automation import AndroidAutomation

# 自定义配置
client = AndroidAutomation(
    base_url="http://localhost:8000",
    timeout=30.0,  # 请求超时时间（秒）
    verify=True,   # SSL 验证
)

# 使用上下文管理器
with AndroidAutomation(base_url="http://localhost:8000") as client:
    client.device.connect()
    # ...
# 自动断开连接
```

## 开发

```bash
# 克隆仓库
git clone https://github.com/anomalyco/android-automation-sdk.git
cd android-automation-sdk

# 创建虚拟环境
uv venv
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate  # Windows

# 安装依赖
uv pip install -e ".[dev]"

# 运行测试
pytest

# 代码格式化
black src tests
ruff check src tests
mypy src
```

## 许可证

MIT License
