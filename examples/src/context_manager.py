"""
context_manager.py
====================
上下文管理器使用示例
"""

from android_automation import AndroidAutomation


def sync_context_example():
    print("\n同步上下文管理器示例:")
    print("-" * 40)
    
    with AndroidAutomation(base_url="http://localhost:8000") as client:
        print("1. 连接设备...")
        client.device.connect()
        print("   ✓ 设备已连接")
        
        print("2. 执行操作...")
        client.input.swipe(direction="up", percent=0.3)
        print("   ✓ 滑动完成")
        
        print("3. 检查状态...")
        status = client.device.get_status()
        print(f"   ✓ 连接状态: {status.connected}")
    
    print("   ✓ 资源已自动释放")


async def async_context_example():
    print("\n异步上下文管理器示例:")
    print("-" * 40)
    
    async with AndroidAutomation(base_url="http://localhost:8000") as client:
        print("1. 连接设备...")
        await client.device.connect()
        print("   ✓ 设备已连接")
        
        print("2. 执行异步操作...")
        await client.input.swipe(direction="down", percent=0.3)
        print("   ✓ 滑动完成")
    
    print("   ✓ 资源已自动释放")


def error_handling_example():
    print("\n错误处理示例:")
    print("-" * 40)
    
    from android_automation.exceptions import (
        APIError,
        DeviceNotConnectedError,
        ElementNotFoundError,
    )
    
    client = AndroidAutomation(base_url="http://localhost:8000")
    
    try:
        print("1. 测试设备未连接错误...")
        client.input.click(resource_id="com.example:id/button")
    except DeviceNotConnectedError as e:
        print(f"   ✓ 捕获设备未连接错误")
    
    try:
        print("\n2. 测试元素未找到...")
        client.device.connect()
        client.input.click(resource_id="com.example:id/nonexistent")
    except (ElementNotFoundError, APIError) as e:
        print(f"   ✓ 捕获错误: {type(e).__name__}")
    finally:
        client.device.disconnect()
    
    client.close_sync()


def main():
    print("=" * 50)
    print("上下文管理器和错误处理示例")
    print("=" * 50)
    
    sync_context_example()
    
    import asyncio
    asyncio.run(async_context_example())
    
    error_handling_example()


if __name__ == "__main__":
    main()
