"""
element_location.py
===================
元素定位和查找示例
"""

from android_automation import AndroidAutomation


def main():
    print("=" * 50)
    print("元素定位示例")
    print("=" * 50)

    client = AndroidAutomation(base_url="http://localhost:8000")

    try:
        print("\n连接设备...")
        client.device.connect()
        print("✓ 设备已连接")

        print("\n1. 通过 resource-id 查找元素...")
        element = client.input.find_by_id(resource_id="com.example:id/button")
        print(f"   - 元素存在: {element.exists}")
        if element.exists:
            print(f"   - 文本: {element.text}")
            print(f"   - 可点击: {element.clickable}")

        print("\n2. 通过文本查找元素...")
        element = client.input.find_by_text(text="确定")
        print(f"   - 元素存在: {element.exists}")

        print("\n3. 通过类名查找元素...")
        element = client.input.find_by_class(class_name="android.widget.Button")
        print(f"   - 元素存在: {element.exists}")

        print("\n4. 通过 XPath 查找元素...")
        element = client.input.find_by_xpath(xpath="//Button[@text='提交']")
        print(f"   - 元素存在: {element.exists}")

        print("\n5. 查找所有匹配元素...")
        elements = client.input.find_elements_by_class(class_name="android.widget.TextView")
        print(f"   - 找到 {elements.count} 个 TextView 元素")

        print("\n6. 检查元素是否存在...")
        exists = client.input.exists(resource_id="com.example:id/button")
        print(f"   - 元素存在: {exists}")

        print("\n7. 获取元素文本...")
        text = client.input.get_text(resource_id="com.example:id/title")
        print(f"   - 标题文本: {text}")

        print("\n8. 获取元素边界位置...")
        bounds = client.input.get_bounds(resource_id="com.example:id/button")
        if bounds:
            width = bounds.get('right', 0) - bounds.get('left', 0)
            height = bounds.get('bottom', 0) - bounds.get('top', 0)
            print(f"   - 宽度: {width}, 高度: {height}")

        print("\n9. 等待元素出现（最多 10 秒）...")
        appeared = client.input.wait_appear(resource_id="com.example:id/dialog", timeout=10.0)
        print(f"   - 元素已出现: {appeared}")

        print("\n10. 等待元素消失（最多 10 秒）...")
        gone = client.input.wait_gone(resource_id="com.example:id/loading", timeout=10.0)
        print(f"   - 元素已消失: {gone}")

        print("\n11. 获取当前界面 XML 结构...")
        xml = client.input.get_hierarchy()
        print(f"   - XML 长度: {len(xml)} 字符")

    except Exception as e:
        print(f"\n错误: {e}")
    finally:
        client.device.disconnect()
        client.close_sync()


if __name__ == "__main__":
    main()
