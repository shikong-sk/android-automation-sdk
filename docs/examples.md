# 示例代码

## 基础示例

### 连接设备并执行基本操作

```python
from android_automation import AndroidAutomation

client = AndroidAutomation(base_url="http://localhost:8000")

# 连接设备
device_info = client.device.connect()
print(f"已连接设备: {device_info.serial}")

# 点击按钮
client.input.click(resource_id="com.example:id/button")

# 输入文本
client.input.set_text(resource_id="com.example:id/input", text="Hello World")

# 断开连接
client.device.disconnect()
```

### 使用上下文管理器

```python
from android_automation import AndroidAutomation

with AndroidAutomation(base_url="http://localhost:8000") as client:
    client.device.connect()
    client.app.start("com.example.app")
    client.input.click(resource_id="com.example:id/submit")
```

---

## 应用操作

### 启动和管理应用

```python
from android_automation import AndroidAutomation

client = AndroidAutomation(base_url="http://localhost:8000")
client.device.connect()

# 启动应用
client.app.start("com.example.app")

# 等待应用启动
import time
time.sleep(2)

# 检查应用状态
status = client.app.get_status("com.example.app")
print(f"应用运行中: {status.running}")

# 获取应用版本
version = client.app.get_version("com.example.app")
print(f"版本: {version.version}")

# 获取当前前台应用
current = client.app.get_current()
print(f"当前应用: {current.package}")

# 停止应用
client.app.stop("com.example.app")

client.device.disconnect()
```

### 安装和卸载应用

```python
client.adb.install_apk("/path/to/app.apk", reinstall=True, grant_permissions=True)
client.adb.uninstall_package("com.example.app", keep_data=False)
```

---

## 元素操作

### 查找和交互元素

```python
client.device.connect()

# 等待元素出现
client.input.wait_appear(resource_id="com.example:id/login_button", timeout=10.0)

# 点击元素
client.input.click(resource_id="com.example:id/login_button")

# 检查元素是否存在
if client.input.exists(resource_id="com.example:id/error_message"):
    error = client.input.get_text(resource_id="com.example:id/error_message")
    print(f"错误: {error}")

# 等待元素消失
client.input.wait_gone(resource_id="com.example:id/loading", timeout=10.0)

client.device.disconnect()
```

### 获取界面结构

```python
hierarchy = client.input.get_hierarchy()
print(hierarchy)
```

---

## 人类模拟操作

### 自然点击和拖拽

```python
client.device.connect()

# 人类模拟点击（带随机偏移和延迟）
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
    trajectory_type="bezier",
    speed_mode="ease_in_out",
    duration=1.0,
)

# 元素到元素拖拽
client.input.human_drag(
    start_selector_type="id",
    start_selector_value="com.example:id/source",
    end_selector_type="id",
    end_selector_value="com.example:id/target",
)

client.device.disconnect()
```

---

## ADB 操作

### 文件传输

```python
client.device.connect()

# 推送文件到设备
client.adb.push_file("/local/path/file.txt", "/sdcard/file.txt")

# 从设备拉取文件
client.adb.pull_file("/sdcard/screenshot.png", "/local/path/screenshot.png")

# 截图
client.adb.take_screenshot("/local/path/screenshot.png")

client.device.disconnect()
```

### 获取设备信息

```python
client.device.connect()

# 获取设备信息
info = client.adb.get_device_info()
print(f"设备: {info.model}")
print(f"制造商: {info.manufacturer}")
print(f"Android 版本: {info.android_version}")

# 获取电池信息
battery = client.adb.get_battery_info()
print(f"电量: {battery.level}%")
print(f"状态: {battery.status}")

# 获取屏幕信息
resolution = client.adb.get_screen_resolution()
print(f"分辨率: {resolution.width}x{resolution.height}")

density = client.adb.get_screen_density()
print(f"密度: {density.density}")

# 获取设备属性
model = client.adb.get_prop("ro.product.model")
print(f"型号: {model}")

client.device.disconnect()
```

### 执行 Shell 命令

```python
client.device.connect()

# 执行 Shell 命令
output = client.adb.shell("ls /sdcard")
print(output)

# 获取已安装应用列表
packages = client.adb.list_packages(filter_type="third_party")
for pkg in packages:
    print(pkg.package_name)

client.device.disconnect()
```

---

## 脚本执行

### 执行自动化脚本

```python
client.device.connect()

# 执行脚本内容
result = client.script.execute(
    content="""
    home
    wait 1
    start_app "com.example.app"
    wait 2
    click id:"com.example:id/button"
    input text:"Hello World"
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

client.device.disconnect()
```

### 流式执行脚本

```python
client.device.connect()

# SSE 流式执行
for event in client.script.execute_stream(content="home\nwait 1\nlog '完成'"):
    if event["type"] == "log":
        print(f"日志: {event['data']}")
    elif event["type"] == "error":
        print(f"错误: {event['data']}")
    elif event["type"] == "end":
        print("执行完成")
        break

client.device.disconnect()
```

---

## 错误处理

### 完整错误处理示例

```python
from android_automation import AndroidAutomation
from android_automation.exceptions import (
    APIError,
    DeviceNotConnectedError,
    ElementNotFoundError,
    TimeoutError,
)

client = AndroidAutomation(base_url="http://localhost:8000", timeout=30.0)

try:
    # 连接设备
    device_info = client.device.connect()
    print(f"已连接设备: {device_info.serial}")

    # 启动应用
    client.app.start("com.example.app")

    # 点击元素（可能抛出 ElementNotFoundError）
    client.input.click(resource_id="com.example:id/button")

except DeviceNotConnectedError:
    print("设备未连接，请检查设备连接状态")
except ElementNotFoundError:
    print("元素未找到，请检查元素定位信息")
except TimeoutError:
    print("操作超时，请增加超时时间")
except APIError as e:
    print(f"API 错误: {e.status_code} - {e.message}")
except Exception as e:
    print(f"未知错误: {e}")
finally:
    try:
        client.device.disconnect()
    except:
        pass
```

---

## 完整场景示例

### 登录流程自动化

```python
from android_automation import AndroidAutomation
import time

def login_flow():
    client = AndroidAutomation(base_url="http://localhost:8000")

    try:
        # 连接设备
        device_info = client.device.connect()
        print(f"已连接设备: {device_info.serial}")

        # 启动应用
        client.app.start("com.example.app")
        time.sleep(2)

        # 输入用户名
        client.input.set_text(
            resource_id="com.example:id/username_input",
            text_content="test_user"
        )

        # 输入密码
        client.input.set_text(
            resource_id="com.example:id/password_input",
            text_content="password123"
        )

        # 点击登录按钮
        client.input.click(resource_id="com.example:id/login_button")

        # 等待登录结果
        time.sleep(3)

        # 检查是否登录成功
        if client.input.exists(resource_id="com.example:id/user_profile"):
            print("登录成功")
        else:
            # 获取错误信息
            if client.input.exists(resource_id="com.example:id/error_message"):
                error = client.input.get_text(resource_id="com.example:id/error_message")
                print(f"登录失败: {error}")

    except Exception as e:
        print(f"错误: {e}")
    finally:
        client.device.disconnect()

if __name__ == "__main__":
    login_flow()
```

### 数据抓取流程

```python
from android_automation import AndroidAutomation
import json

def scrape_data():
    client = AndroidAutomation(base_url="http://localhost:8000")

    try:
        client.device.connect()
        client.app.start("com.example.app")

        # 获取所有列表项
        items = []
        while True:
            elements = client.input.find_elements_by_class("android.widget.ListItem")

            for element in elements:
                item = {
                    "title": element.text,
                    "bounds": element.bounds
                }
                items.append(item)

            # 滑动到下一页
            if len(items) >= 20:
                break
            client.input.swipe(direction="up", percent=0.8)

        # 保存数据
        with open("scraped_data.json", "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=2)

        print(f"已抓取 {len(items)} 条数据")

    finally:
        client.device.disconnect()

if __name__ == "__main__":
    scrape_data()
```
