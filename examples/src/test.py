import sys
import io

from android_automation import AndroidAutomation

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

client = AndroidAutomation(base_url="http://localhost:8000")

try:
    print("\n1. 连接设备（自动选择）...")
    device_info = client.device.connect(sync=True)
    print(f"   [OK] 已连接设备: {device_info.serial}")
    print(f"   - 产品名称: {device_info.product_name}")
    print(f"   - API 级别: {device_info.api_level}")
    print(f"   - 电池电量: {device_info.battery_level}%")

    print("\n获取设备状态...")
    status = client.device.get_status(sync=True)
    if status.connected:
        print(f"   [OK] 设备已连接")
        print(f"   - 序列号: {status.device_info.serial}")
    else:
        print("   [X] 设备未连接")

    print("\n6. 获取当前前台应用...")
    current = client.app.get_current()

    print(f"   - 包名: {current.package}")
    print(f"   - Activity: {current.activity}")
except Exception as e:
    print(f"\n错误: {e}")
finally:
    client.close_sync()
