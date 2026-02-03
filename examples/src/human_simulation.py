"""
human_simulation.py
====================
人类模拟操作示例 - 模拟真实人类行为的点击、拖拽
"""

import time
from android_automation import AndroidAutomation, SelectorType


def main():
    print("=" * 50)
    print("人类模拟操作示例")
    print("=" * 50)

    client = AndroidAutomation(base_url="http://localhost:8000")

    try:
        print("\n连接设备...")
        client.device.connect()
        print("✓ 设备已连接")

        print("\n1. 人类模拟点击（通过坐标）...")
        client.input.human_click(
            x=500, y=800,
            offset_min=5, offset_max=15,
            delay_min=0.1, delay_max=0.5
        )
        print("   ✓ 人类点击完成（带随机偏移和延迟）")

        print("\n2. 人类模拟点击（通过选择器）...")
        client.input.human_click(
            selector_type=SelectorType.ID,
            selector_value="com.example:id/button",
            offset_min=3, offset_max=10
        )
        print("   ✓ 人类点击完成")

        print("\n3. 人类模拟双击...")
        client.input.human_double_click(
            selector_type=SelectorType.TEXT,
            selector_value="确定",
            offset_min=2, offset_max=8,
            interval_min=0.1, interval_max=0.3
        )
        print("   ✓ 人类双击完成（带随机间隔）")

        print("\n4. 人类模拟长按...")
        client.input.human_long_press(
            x=500, y=800,
            duration_min=1.5, duration_max=2.5
        )
        print("   ✓ 人类长按完成（随机时长 1.5-2.5秒）")

        print("\n5. 人类模拟拖拽（贝塞尔曲线）...")
        client.input.human_drag(
            start_x=300, start_y=1200,
            end_x=300, end_y=300,
            trajectory_type="bezier",
            speed_mode="ease_in_out",
            duration=1.0
        )
        print("   ✓ 贝塞尔曲线拖拽完成（自然轨迹）")

        print("\n6. 人类模拟拖拽（直线抖动）...")
        client.input.human_drag(
            start_x=100, start_y=1500,
            end_x=100, end_y=500,
            trajectory_type="linear_jitter",
            speed_mode="random",
            duration=1.5,
            jitter_min=1, jitter_max=5
        )
        print("   ✓ 直线抖动拖拽完成（模拟手抖）")

        print("\n7. 人类模拟拖拽（元素到元素）...")
        client.input.human_drag(
            start_selector_type=SelectorType.ID,
            start_selector_value="com.example:id/source_item",
            end_selector_type=SelectorType.ID,
            end_selector_value="com.example:id/target_area",
            trajectory_type="bezier",
            speed_mode="ease_in_out",
            duration=1.2
        )
        print("   ✓ 元素到元素拖拽完成")

        print("\n8. 不同速度模式...")
        for mode in ["ease_in_out", "ease_in", "ease_out", "linear", "random"]:
            client.input.human_drag(
                start_x=200, start_y=1000, end_x=200, end_y=400,
                speed_mode=mode, duration=0.8
            )
            print(f"   - {mode}: ✓")

    except Exception as e:
        print(f"\n错误: {e}")
    finally:
        client.device.disconnect()
        client.close_sync()


if __name__ == "__main__":
    main()
