"""
app_management.py
==================
应用管理示例 - 启动、停止、查询应用
"""

import time
from android_automation import AndroidAutomation


def main():
    print("=" * 50)
    print("应用管理示例")
    print("=" * 50)

    client = AndroidAutomation(base_url="http://localhost:8000")

    try:
        print("\n连接设备...")
        client.device.connect()
        print("✓ 设备已连接")

        print("\n1. 启动应用...")
        client.app.start("com.android.settings")
        print("   ✓ 已启动设置应用")

        time.sleep(2)

        print("\n2. 停止应用...")
        client.app.stop("com.android.settings")
        print("   ✓ 已停止设置应用")

        print("\n3. 清除应用数据...")
        client.app.clear("com.example.app")
        print("   ✓ 已清除应用数据")

        print("\n4. 获取应用版本...")
        app_info = client.app.get_version("com.android.settings")
        print(f"   - 包名: {app_info.package}")
        print(f"   - 版本: {app_info.version}")

        print("\n5. 检查应用运行状态...")
        client.app.start("com.android.settings")
        time.sleep(1)

        status = client.app.get_status("com.android.settings")
        print(f"   - 包名: {status.package}")
        print(f"   - 运行中: {status.running}")

        print("\n6. 获取当前前台应用...")
        current = client.app.get_current()
        print(f"   - 包名: {current.package}")
        print(f"   - Activity: {current.activity}")

    except Exception as e:
        print(f"\n错误: {e}")
    finally:
        client.device.disconnect()
        client.close_sync()


if __name__ == "__main__":
    main()
