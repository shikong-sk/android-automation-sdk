"""
comprehensive_workflow.py
==========================
综合自动化流程示例
"""

import time
from android_automation import AndroidAutomation, SelectorType


def login_workflow(client, username, password):
    print("\n   执行登录流程...")
    
    client.input.set_text(resource_id="com.example:id/username", text=username)
    print(f"   - 输入用户名: {username}")
    
    client.input.set_text(resource_id="com.example:id/password", text=password)
    print("   - 输入密码: ***")
    
    client.input.click(resource_id="com.example:id/login_button")
    print("   - 点击登录按钮")
    
    time.sleep(3)
    
    if client.input.exists(resource_id="com.example:id/welcome_message"):
        welcome = client.input.get_text(resource_id="com.example:id/welcome_message")
        print(f"   - 登录成功: {welcome}")
        return True
    else:
        print("   - 登录可能失败")
        return False


def data_collection_workflow(client):
    print("\n   执行数据采集流程...")
    
    client.app.start("com.example.dataapp")
    time.sleep(2)
    print("   - 启动数据应用")

    if client.input.wait_appear(resource_id="com.example:id/list_view", timeout=10):
        print("   - 列表已加载")
    else:
        print("   - 列表加载超时")
        return

    for page in range(3):
        print(f"   - 采集第 {page + 1} 页数据...")
        elements = client.input.find_elements_by_class(class_name="android.widget.TextView")
        print(f"     找到 {elements.count} 个元素")

        if page < 2:
            client.input.human_drag(
                start_x=400, start_y=800,
                end_x=400, end_y=200,
                trajectory_type="bezier",
                speed_mode="ease_in_out",
                duration=1.5
            )
            time.sleep(1)

    print("   - 数据采集完成")
    client.navigation.home()


def settings_workflow(client):
    print("\n   执行系统设置流程...")
    
    client.app.start("com.android.settings")
    time.sleep(2)
    print("   - 打开系统设置")

    if client.input.exists(text="WLAN"):
        client.input.click_by_text(text="WLAN")
        time.sleep(1)
        print("   - 进入 WLAN 设置")
        client.navigation.back()

    if client.input.exists(text="蓝牙"):
        client.input.click_by_text(text="蓝牙")
        time.sleep(1)
        print("   - 进入蓝牙设置")
        client.navigation.back()

    client.navigation.go_home()
    print("   - 设置流程完成")


def main():
    print("=" * 50)
    print("综合自动化流程示例")
    print("=" * 50)

    client = AndroidAutomation(base_url="http://localhost:8000")

    try:
        print("\n连接设备...")
        client.device.connect()
        print("✓ 设备已连接")

        client.input.screen_on()
        client.input.unlock()
        print("✓ 屏幕已解锁")

        print("\n" + "=" * 40)
        print("示例 1: 登录流程")
        print("=" * 40)
        login_workflow(client, "test@example.com", "password123")

        print("\n" + "=" * 40)
        print("示例 2: 数据采集流程")
        print("=" * 40)
        data_collection_workflow(client)

        print("\n" + "=" * 40)
        print("示例 3: 系统设置流程")
        print("=" * 40)
        settings_workflow(client)

        print("\n" + "=" * 40)
        print("流程执行总结")
        print("=" * 40)

        battery = client.adb.get_battery_info()
        print(f"   - 当前电量: {battery.level * 100 // battery.scale}%")

        print("\n✓ 所有流程执行完成")

    except Exception as e:
        print(f"\n错误: {e}")
    finally:
        client.device.disconnect()
        client.close_sync()


if __name__ == "__main__":
    main()
