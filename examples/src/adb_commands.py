"""
adb_commands.py
================
ADB 命令示例 - Shell 命令、文件传输、设备信息
"""

from android_automation import AndroidAutomation


def main():
    print("=" * 50)
    print("ADB 命令示例")
    print("=" * 50)

    client = AndroidAutomation(base_url="http://localhost:8000")

    try:
        print("\n连接设备...")
        client.device.connect()
        print("✓ 设备已连接")

        print("\n1. 获取已安装应用列表...")
        packages = client.adb.list_packages(filter_type="third_party")
        print(f"   - 第三方应用数量: {len(packages)}")
        print(f"   - 前 5 个: {packages[:5]}")

        print("\n2. 获取应用详细信息...")
        info = client.adb.get_package_info("com.android.settings")
        print(f"   - 包名: {info.get('package_name')}")
        print(f"   - 版本: {info.get('version_name')}")

        print("\n3. 获取设备详细信息...")
        info = client.adb.get_device_info()
        print(f"   - 型号: {info.model}")
        print(f"   - Android 版本: {info.android_version}")

        print("\n4. 获取电池信息...")
        battery = client.adb.get_battery_info()
        print(f"   - 电量: {battery.level * 100 // battery.scale}%")
        print(f"   - 状态: {battery.status}")

        print("\n5. 获取屏幕信息...")
        resolution = client.adb.get_screen_resolution()
        print(f"   - 分辨率: {resolution.width}x{resolution.height}")
        density = client.adb.get_screen_density()
        print(f"   - DPI: {density}")

        print("\n6. 获取设备属性...")
        model = client.adb.get_prop("ro.product.model")
        print(f"   - 型号: {model}")

        print("\n7. 执行 Shell 命令...")
        output = client.adb.shell("wm size")
        print(f"   - 屏幕尺寸: {output.strip()}")

        print("\n8. 推送文件到设备...")
        result = client.adb.push_file("/local/file.txt", "/sdcard/Download/file.txt")
        print(f"   - 推送成功: {result}")

        print("\n9. 从设备拉取文件...")
        result = client.adb.pull_file("/sdcard/screenshot.png", "/local/screenshot.png")
        print(f"   - 拉取成功: {result}")

        print("\n10. 截取屏幕截图...")
        result = client.adb.take_screenshot("/local/screenshot.png")
        print(f"   - 截图成功: {result}")

    except Exception as e:
        print(f"\n错误: {e}")
    finally:
        try:
            client.device.disconnect()
        except:
            pass
        client.close_sync()


if __name__ == "__main__":
    main()
