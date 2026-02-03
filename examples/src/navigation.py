"""
navigation.py
==============
导航控制示例 - Home、返回、菜单等
"""

import time
from android_automation import AndroidAutomation


def main():
    print("=" * 50)
    print("导航控制示例")
    print("=" * 50)

    client = AndroidAutomation(base_url="http://localhost:8000")

    try:
        print("\n连接设备...")
        client.device.connect()
        print("✓ 设备已连接")

        print("\n启动设置应用...")
        client.app.start("com.android.settings")
        time.sleep(2)

        print("\n1. 返回主屏幕...")
        client.navigation.home()
        print("   ✓ 已返回主屏幕")

        print("\n2. 重新打开设置...")
        client.app.start("com.android.settings")
        time.sleep(2)

        print("\n3. 返回上一页...")
        client.navigation.back()
        print("   ✓ 已返回")

        print("\n4. 打开菜单...")
        client.navigation.menu()
        print("   ✓ 菜单已打开")

        print("\n5. 确保返回主页...")
        client.navigation.go_home()
        print("   ✓ 已返回主页")

        print("\n6. 打开最近应用...")
        client.navigation.recent_apps()
        print("   ✓ 最近应用已打开")

        print("\n7. 综合示例...")
        client.app.start("com.android.settings")
        time.sleep(2)

        if client.input.exists(resource_id="android:id/title"):
            client.input.click_by_text(text="WLAN")
            time.sleep(1)
            print("   - 点击 WLAN")

        client.input.swipe(direction="up", percent=0.3)
        time.sleep(0.5)
        print("   - 向上滑动")

        client.navigation.go_home()
        print("   - 返回主页")

        print("\n✓ 导航流程完成")

    except Exception as e:
        print(f"\n错误: {e}")
    finally:
        client.device.disconnect()
        client.close_sync()


if __name__ == "__main__":
    main()
