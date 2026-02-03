# 快速开始

## 安装

```bash
# 使用 uv 安装（推荐）
uv pip install android-automation-sdk

# 或使用 pip
pip install android-automation-sdk
```

## 基本使用

### 创建客户端

```python
from android_automation import AndroidAutomation

# 创建客户端
client = AndroidAutomation(base_url="http://localhost:8000")
```

### 连接设备

```python
# 连接设备（自动选择第一个可用设备）
device_info = client.device.connect()
print(f"已连接设备: {device_info.serial}")

# 通过序列号连接
device_info = client.device.connect(device_serial="emulator-5554")

# WiFi 连接
device_info = client.device.connect(device_serial="192.168.1.100:5555")
```

### 基础操作

```python
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

## 完整示例

```python
from android_automation import AndroidAutomation

def main():
    # 创建客户端
    client = AndroidAutomation(base_url="http://localhost:8000")

    try:
        # 连接设备
        device_info = client.device.connect()
        print(f"已连接设备: {device_info.serial}")

        # 启动应用
        client.app.start("com.example.app")

        # 等待应用启动
        import time
        time.sleep(2)

        # 点击按钮
        client.input.click(resource_id="com.example:id/button")

        # 输入文本
        client.input.set_text(resource_id="com.example:id/input", text="Hello")

        # 获取设备状态
        status = client.device.get_status()
        print(f"设备状态: {status}")

    except Exception as e:
        print(f"错误: {e}")
    finally:
        # 断开设备
        client.device.disconnect()

if __name__ == "__main__":
    main()
```

## 使用上下文管理器

```python
from android_automation import AndroidAutomation

with AndroidAutomation(base_url="http://localhost:8000") as client:
    client.device.connect()
    client.app.start("com.example.app")
    client.input.click(resource_id="com.example:id/button")
# 自动断开连接
```

## 下一步

- 查看 [API 参考](api-reference.md) 了解更多功能
- 查看 [示例代码](examples.md) 获取更多使用场景
- 查看 [配置指南](configuration.md) 了解高级配置
