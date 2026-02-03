import sys
import io

from android_automation import AndroidAutomation

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def test_device_management(client):
    """测试设备管理功能."""
    print("\n" + "=" * 50)
    print("设备管理测试")
    print("=" * 50)

    print("\n1. 连接设备（自动选择）...")
    device_info = client.device.connect(sync=True)
    print(f"   [OK] 已连接设备: {device_info.serial}")
    print(f"   - 产品名称: {device_info.product_name}")
    print(f"   - API 级别: {device_info.api_level}")
    print(f"   - 电池电量: {device_info.battery_level}%")

    print("\n2. 获取设备状态...")
    status = client.device.get_status(sync=True)
    if status.connected:
        print(f"   [OK] 设备已连接")
        print(f"   - 序列号: {status.device_info.serial}")
    else:
        print("   [X] 设备未连接")

    return device_info


def test_input_operations(client):
    """测试输入操作功能."""
    print("\n" + "=" * 50)
    print("输入操作测试")
    print("=" * 50)

    print("\n3. 屏幕控制...")
    result = client.input.screen_on(sync=True)
    print(f"   [OK] 亮屏: {result}")

    # result = client.input.screen_off(sync=True)
    # print(f"   [OK] 锁屏: {result}")

    print("\n4. 滑动屏幕...")
    result = client.input.swipe(direction="up", percent=0.5, sync=True)
    print(f"   [OK] 向上滑动: {result}")

    result = client.input.swipe(direction="down", percent=0.3, sync=True)
    print(f"   [OK] 向下滑动: {result}")

    result = client.input.swipe(direction="left", sync=True)
    print(f"   [OK] 向左滑动: {result}")

    result = client.input.swipe(direction="right", sync=True)
    print(f"   [OK] 向右滑动: {result}")


def test_element_location(client):
    """测试元素定位功能."""
    print("\n" + "=" * 50)
    print("元素定位测试")
    print("=" * 50)

    print("\n5. 获取界面结构...")
    try:
        hierarchy = client.input.get_hierarchy(sync=True)
        print(f"   [OK] 获取到界面结构，长度: {len(hierarchy)} 字符")
    except Exception as e:
        print(f"   [X] 获取界面结构失败: {e}")

    print("\n6. 获取当前前台应用...")
    try:
        current = client.app.get_current(sync=True)
        print(f"   [OK] 当前应用包名: {current.package}")
        print(f"   - Activity: {current.activity}")
        print(f"   - PID: {current.pid}")
    except Exception as e:
        print(f"   [X] 获取当前应用失败: {e}")


def test_navigation(client):
    """测试导航控制功能."""
    print("\n" + "=" * 50)
    print("导航控制测试")
    print("=" * 50)

    print("\n7. 返回主屏幕...")
    try:
        client.navigation.home(sync=True)
        print("   [OK] 已返回主屏幕")
    except Exception as e:
        print(f"   [X] 返回主屏幕失败: {e}")

    print("\n8. 返回上一页...")
    try:
        client.navigation.back(sync=True)
        print("   [OK] 已返回上一页")
    except Exception as e:
        print(f"   [X] 返回上一页失败: {e}")


def test_app_management(client):
    """测试应用管理功能."""
    print("\n" + "=" * 50)
    print("应用管理测试")
    print("=" * 50)

    print("\n9. 获取已安装应用列表...")
    try:
        packages = client.adb.list_packages(filter_type="third_party", sync=True)
        print(f"   [OK] 第三方应用数量: {len(packages)}")
        if packages:
            print(f"   - 前3个应用: {packages[:3]}")
    except Exception as e:
        print(f"   [X] 获取应用列表失败: {e}")

    print("\n10. 获取设备信息...")
    try:
        info = client.adb.get_device_info(sync=True)
        print(f"   [OK] 设备信息:")
        print(f"   - 型号: {info.model}")
        print(f"   - 品牌: {info.brand}")
        print(f"   - Android 版本: {info.android_version}")
    except Exception as e:
        print(f"   [X] 获取设备信息失败: {e}")

    print("\n11. 获取电池信息...")
    try:
        battery = client.adb.get_battery_info(sync=True)
        print(f"   [OK] 电池信息:")
        print(f"   - 电量: {battery.level}%")
        print(f"   - 状态: {battery.status} (1=未知,2=充电,3=放电,4=未充电,5=充满)")
        print(f"   - 健康: {battery.health}")
        print(f"   - 充电方式: {battery.plugged} (0=未充电,1=AC,2=USB,4=无线)")
        print(f"   - 温度: {battery.temperature / 10:.1f}°C")
        print(f"   - 电压: {battery.voltage / 1000:.2f}V")
    except Exception as e:
        print(f"   [X] 获取电池信息失败: {e}")

    print("\n12. 获取屏幕信息...")
    try:
        resolution = client.adb.get_screen_resolution(sync=True)
        print(f"   [OK] 屏幕分辨率: {resolution.width}x{resolution.height}")

        density = client.adb.get_screen_density(sync=True)
        print(f"   [OK] 屏幕密度: {density} dpi")
    except Exception as e:
        print(f"   [X] 获取屏幕信息失败: {e}")


def test_adb_commands(client):
    """测试 ADB 命令功能."""
    print("\n" + "=" * 50)
    print("ADB 命令测试")
    print("=" * 50)

    print("\n13. 执行 Shell 命令...")
    try:
        output = client.adb.shell("echo 'Hello from ADB'", sync=True)
        print(f"   [OK] Shell 输出: {output.strip()}")
    except Exception as e:
        print(f"   [X] 执行 Shell 命令失败: {e}")

    print("\n14. 获取设备属性...")
    try:
        model = client.adb.get_prop("ro.product.model", sync=True)
        print(f"   [OK] 设备型号: {model}")

        brand = client.adb.get_prop("ro.product.brand", sync=True)
        print(f"   [OK] 设备品牌: {brand}")
    except Exception as e:
        print(f"   [X] 获取设备属性失败: {e}")


def test_script_execution(client):
    """测试脚本执行功能."""
    print("\n" + "=" * 50)
    print("脚本执行测试")
    print("=" * 50)

    print("\n15. 验证脚本语法...")
    try:
        script_content = """
        home
        wait 1
        log '测试脚本执行'
        """
        validation = client.script.validate(content=script_content, sync=True)
        print(f"   [OK] 脚本验证结果: {validation.valid}")
        print(f"   - 语句数量: {validation.statements}")
        if validation.error:
            print(f"   - 错误信息: {validation.error}")
    except Exception as e:
        print(f"   [X] 验证脚本失败: {e}")

    print("\n16. 获取脚本列表...")
    try:
        scripts = client.script.list(sync=True)
        print(f"   [OK] 脚本数量: {len(scripts)}")
        for script in scripts[:5]:
            if isinstance(script, dict):
                name = script.get('name', script.get('data', str(script)))
                print(f"   - {name}")
    except Exception as e:
        print(f"   [X] 获取脚本列表失败: {e}")


def test_human_simulation(client):
    """测试人类模拟操作."""
    print("\n" + "=" * 50)
    print("人类模拟操作测试")
    print("=" * 50)

    print("\n17. 人类模拟点击（坐标）...")
    try:
        result = client.input.human_click(x=500, y=800, sync=True)
        print(f"   [OK] 人类模拟点击: {result}")
    except Exception as e:
        print(f"   [X] 人类模拟点击失败: {e}")

    print("\n18. 人类模拟滑动...")
    try:
        result = client.input.human_drag(
            start_x=300,
            start_y=800,
            end_x=300,
            end_y=400,
            duration=0.5,
            sync=True
        )
        print(f"   [OK] 人类模拟拖拽: {result}")
    except Exception as e:
        print(f"   [X] 人类模拟拖拽失败: {e}")


def main():
    """主函数."""
    print("=" * 50)
    print("Android Automation SDK 测试")
    print("=" * 50)

    client = AndroidAutomation(base_url="http://localhost:8000")

    try:
        test_device_management(client)
        test_input_operations(client)
        test_element_location(client)
        test_navigation(client)
        test_app_management(client)
        test_adb_commands(client)
        test_script_execution(client)
        test_human_simulation(client)

        print("\n" + "=" * 50)
        print("所有测试完成!")
        print("=" * 50)

    except Exception as e:
        print(f"\n测试过程中发生错误: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("\n断开设备连接...")
        client.close_sync()
        print("测试结束.")


if __name__ == "__main__":
    main()
