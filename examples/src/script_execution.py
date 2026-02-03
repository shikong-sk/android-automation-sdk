"""
script_execution.py
====================
脚本执行示例 - 执行自动化 DSL 脚本
"""

from android_automation import AndroidAutomation


def main():
    print("=" * 50)
    print("脚本执行示例")
    print("=" * 50)

    client = AndroidAutomation(base_url="http://localhost:8000")

    try:
        print("\n连接设备...")
        client.device.connect()
        print("✓ 设备已连接")

        simple_script = """
        home
        wait 1
        log "完成基础操作"
        """

        print("\n1. 执行简单脚本...")
        result = client.script.execute(content=simple_script)
        print(f"   - 执行成功: {result.success}")
        print(f"   - 日志: {result.logs}")

        complex_script = """
        start_app "com.android.settings"
        wait 2

        if exists text:"WLAN"
            click text:"WLAN"
            wait 1
            log "已打开 WLAN"
        end

        home
        log "任务完成"
        """

        print("\n2. 执行复杂脚本...")
        result = client.script.execute(content=complex_script)
        print(f"   - 执行成功: {result.success}")
        for log in result.logs:
            print(f"   - {log}")

        print("\n3. 验证脚本语法...")
        validation = client.script.validate(content="click id:button\nwait 1")
        print(f"   - 语法正确: {validation.valid}")
        print(f"   - 语句数量: {validation.statements}")

        print("\n4. 保存脚本...")
        result = client.script.save("test.script", content=simple_script)
        print(f"   - 保存结果: {result}")

        print("\n5. 获取脚本列表...")
        scripts = client.script.list()
        print(f"   - 脚本数量: {len(scripts)}")

        print("\n6. 执行脚本文件...")
        result = client.script.execute_file("test.script")
        print(f"   - 执行成功: {result.success}")

        print("\n7. 删除脚本...")
        result = client.script.delete("test.script")
        print(f"   - 删除结果: {result}")

    except Exception as e:
        print(f"\n错误: {e}")
    finally:
        client.device.disconnect()
        client.close_sync()


if __name__ == "__main__":
    main()
