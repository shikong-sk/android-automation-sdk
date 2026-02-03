"""
input_operations.py
==================
输入操作示例 - 点击、输入文本、滑动、屏幕控制
"""

from android_automation import AndroidAutomation, SelectorType, Direction


def main():
    print("=" * 50)
    print("输入操作示例")
    print("=" * 50)

    client = AndroidAutomation(base_url="http://localhost:8000")

    try:
        print("\n连接设备...")
        client.device.connect()
        print("✓ 设备已连接")

        print("\n1. 点击元素（通过 resource-id）...")
        client.input.click(resource_id="com.example:id/button")
        print("   ✓ 点击成功")

        print("\n2. 点击元素（通过文本）...")
        client.input.click_by_text(text="确定")
        print("   ✓ 点击成功")

        print("\n3. 点击元素（通过 XPath）...")
        client.input.click_by_xpath(xpath="//Button[@text='确定']")
        print("   ✓ 点击成功")

        print("\n4. 使用通用选择器点击...")
        client.input.click_by_selector(
            selector_type=SelectorType.ID,
            selector_value="com.example:id/submit"
        )
        print("   ✓ 点击成功")

        print("\n5. 输入文本...")
        client.input.set_text(resource_id="com.example:id/input", text="Hello World")
        print("   ✓ 文本输入成功")

        print("\n6. 清除文本...")
        client.input.clear_text(resource_id="com.example:id/input")
        print("   ✓ 文本已清除")

        print("\n7. 滑动屏幕...")
        client.input.swipe(direction=Direction.UP, percent=0.5)
        print("   ✓ 向上滑动 50%")

        client.input.swipe(direction=Direction.LEFT)
        print("   ✓ 向左滑动")

        print("\n8. 屏幕控制...")
        client.input.screen_off()
        print("   ✓ 屏幕已关闭")

        client.input.screen_on()
        print("   ✓ 屏幕已点亮")

        client.input.unlock()
        print("   ✓ 屏幕已解锁")

    except Exception as e:
        print(f"\n错误: {e}")
    finally:
        client.device.disconnect()
        client.close_sync()


if __name__ == "__main__":
    main()
