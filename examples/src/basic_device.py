"""
basic_device.py
===============
基础设备连接和状态查询示例
"""
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from android_automation import AndroidAutomation


def main():
    print("=" * 50)
    print("基础设备连接示例")
    print("=" * 50)

    client = AndroidAutomation(base_url="http://localhost:8000")

    try:
        print("\n1. 连接设备（自动选择）...")
        device_info = client.device.connect()
        print(f"   [OK] 已连接设备: {device_info.serial}")
        print(f"   - 产品名称: {device_info.product_name}")
        print(f"   - API 级别: {device_info.api_level}")
        print(f"   - 电池电量: {device_info.battery_level}%")

        print("\n2. 通过序列号连接...")
        device_info = client.device.connect(device_serial="emulator-5554")
        print(f"   [OK] 已连接设备: {device_info.serial}")

        print("\n3. 通过 WiFi IP 连接...")
        device_info = client.device.connect(device_serial="192.168.1.100:5555")
        print(f"   [OK] 已连接设备: {device_info.serial}")

        print("\n4. 获取设备状态...")
        status = client.device.get_status()
        if status.connected:
            print(f"   [OK] 设备已连接")
            print(f"   - 序列号: {status.device_info.serial}")
        else:
            print("   [X] 设备未连接")

        print("\n5. 断开设备连接...")
        client.device.disconnect()
        print("   [OK] 已断开连接")

    except Exception as e:
        print(f"\n错误: {e}")
    finally:
        client.close_sync()


if __name__ == "__main__":
    main()
