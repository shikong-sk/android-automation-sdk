# API 参考

## 目录

- [设备管理](#设备管理)
- [输入操作](#输入操作)
- [元素定位](#元素定位)
- [人类模拟操作](#人类模拟操作)
- [导航控制](#导航控制)
- [应用管理](#应用管理)
- [ADB 命令](#adb-命令)
- [脚本执行](#脚本执行)
- [通用选择器](#通用选择器)

## 设备管理

### connect

连接设备。

```python
device_info = client.device.connect(device_serial=None)
```

**参数:**
- `device_serial` (str, optional): 设备序列号。为 None 时自动选择第一个可用设备。

**返回:** DeviceInfo

```python
# 自动选择设备
device_info = client.device.connect()

# 通过序列号连接
device_info = client.device.connect(device_serial="emulator-5554")

# WiFi 连接
device_info = client.device.connect(device_serial="192.168.1.100:5555")
```

### disconnect

断开设备连接。

```python
client.device.disconnect()
```

### get_status

获取设备状态。

```python
status = client.device.get_status()
```

**返回:** DeviceConnectionStatus

**属性:**
- `connected`: bool - 是否已连接
- `device_info`: DeviceInfo - 设备信息

---

## 输入操作

### click

点击元素。

```python
client.input.click(resource_id=None, text=None, class_name=None, xpath=None)
```

### click_by_text

通过文本点击元素。

```python
client.input.click_by_text(text)
```

### click_by_class

通过类名点击元素。

```python
client.input.click_by_class(class_name)
```

### click_by_xpath

通过 XPath 点击元素。

```python
client.input.click_by_xpath(xpath)
```

### set_text

输入文本。

```python
client.input.set_text(resource_id=None, text=None, class_name=None, xpath=None, text_content="")
```

### clear_text

清除文本。

```python
client.input.clear_text(resource_id=None, text=None, class_name=None, xpath=None)
```

### swipe

滑动屏幕。

```python
client.input.swipe(direction, percent=0.5)
```

**参数:**
- `direction`: str - 方向 ("up", "down", "left", "right")
- `percent`: float - 滑动距离百分比 (0-1)

```python
client.input.swipe(direction="up", percent=0.5)    # 向上滑动 50%
client.input.swipe(direction="down", percent=0.3)  # 向下滑动 30%
client.input.swipe(direction="left")               # 向左滑动
client.input.swipe(direction="right")              # 向右滑动
```

### screen_on

亮屏。

```python
client.input.screen_on()
```

### screen_off

锁屏。

```python
client.input.screen_off()
```

### unlock

解锁。

```python
client.input.unlock()
```

---

## 元素定位

### find_by_id

通过 resource-id 查找元素。

```python
element = client.input.find_by_id(resource_id)
```

### find_by_text

通过文本查找元素。

```python
element = client.input.find_by_text(text)
```

### find_by_class

通过类名查找元素。

```python
element = client.input.find_by_class(class_name)
```

### find_by_xpath

通过 XPath 查找元素。

```python
element = client.input.find_by_xpath(xpath)
```

### find_elements_by_class

查找所有匹配的元素。

```python
elements = client.input.find_elements_by_class(class_name)
```

### exists

检查元素是否存在。

```python
exists = client.input.exists(resource_id=None, text=None, class_name=None, xpath=None)
```

### exists_by_text

通过文本检查元素是否存在。

```python
exists = client.input.exists_by_text(text)
```

### get_text

获取元素文本。

```python
text = client.input.get_text(resource_id=None, text=None, class_name=None, xpath=None)
```

### get_bounds

获取元素边界。

```python
bounds = client.input.get_bounds(resource_id=None, text=None, class_name=None, xpath=None)
```

### wait_appear

等待元素出现。

```python
client.input.wait_appear(resource_id=None, text=None, class_name=None, xpath=None, timeout=10.0)
```

### wait_gone

等待元素消失。

```python
client.input.wait_gone(resource_id=None, text=None, class_name=None, xpath=None, timeout=10.0)
```

### get_hierarchy

获取界面结构。

```python
hierarchy = client.input.get_hierarchy()
```

---

## 人类模拟操作

### human_click

模拟人类点击。

```python
client.input.human_click(x=None, y=None, selector_type=None, selector_value=None, offset_min=5, offset_max=15, delay_min=0.1, delay_max=0.5)
```

### human_double_click

模拟人类双击。

```python
client.input.human_double_click(selector_type=None, selector_value=None, interval_min=0.1, interval_max=0.3)
```

### human_long_press

模拟人类长按。

```python
client.input.human_long_press(x=None, y=None, selector_type=None, selector_value=None, duration_min=1.0, duration_max=2.0)
```

### human_drag

模拟人类拖拽。

```python
client.input.human_drag(start_x=None, start_y=None, end_x=None, end_y=None, start_selector_type=None, start_selector_value=None, end_selector_type=None, end_selector_value=None, trajectory_type="bezier", speed_mode="ease_in_out", duration=1.0)
```

---

## 导航控制

### home

返回主屏幕。

```python
client.navigation.home()
```

### back

返回上一页。

```python
client.navigation.back()
```

### menu

打开菜单。

```python
client.navigation.menu()
```

### go_home

确保返回主页。

```python
client.navigation.go_home()
```

### recent_apps

打开最近应用。

```python
client.navigation.recent_apps()
```

---

## 应用管理

### start

启动应用。

```python
client.app.start(package_name)
```

### stop

停止应用。

```python
client.app.stop(package_name)
```

### clear

清除应用数据。

```python
client.app.clear(package_name)
```

### get_version

获取应用版本。

```python
version = client.app.get_version(package_name)
```

### get_status

检查应用运行状态。

```python
status = client.app.get_status(package_name)
```

### get_current

获取当前前台应用。

```python
current = client.app.get_current()
```

---

## ADB 命令

### list_packages

获取已安装应用列表。

```python
packages = client.adb.list_packages(filter_type=None)
```

**参数:**
- `filter_type`: str - 过滤类型 ("third_party", "system", None)

### get_package_info

获取应用详细信息。

```python
info = client.adb.get_package_info(package_name)
```

### install_apk

安装 APK。

```python
client.adb.install_apk(file_path, reinstall=False, grant_permissions=True)
```

### uninstall_package

卸载应用。

```python
client.adb.uninstall_package(package_name, keep_data=False)
```

### get_device_info

获取设备信息。

```python
info = client.adb.get_device_info()
```

### get_battery_info

获取电池信息。

```python
battery = client.adb.get_battery_info()
```

### get_screen_resolution

获取屏幕分辨率。

```python
resolution = client.adb.get_screen_resolution()
```

### get_screen_density

获取屏幕密度。

```python
density = client.adb.get_screen_density()
```

### get_prop

获取设备属性。

```python
value = client.adb.get_prop(prop_name)
```

### shell

执行 Shell 命令。

```python
output = client.adb.shell(command)
```

### push_file

推送文件到设备。

```python
client.adb.push_file(local_path, remote_path)
```

### pull_file

从设备拉取文件。

```python
client.adb.pull_file(remote_path, local_path)
```

### take_screenshot

截取屏幕截图。

```python
client.adb.take_screenshot(file_path)
```

### reboot

重启设备。

```python
client.adb.reboot(mode=None)
```

**参数:**
- `mode`: str - 重启模式 (None, "recovery", "bootloader")

---

## 脚本执行

### execute

执行脚本内容。

```python
result = client.script.execute(content)
```

### execute_file

执行脚本文件。

```python
result = client.script.execute_file(file_path)
```

### validate

验证脚本语法。

```python
validation = client.script.validate(content)
```

### execute_stream

流式执行脚本（SSE）。

```python
for event in client.script.execute_stream(content):
    print(event)
```

### stop

停止正在执行的脚本。

```python
client.script.stop(session_id)
```

### list

获取脚本列表。

```python
scripts = client.script.list()
```

### get

获取脚本内容。

```python
script = client.script.get(name)
```

### save

保存脚本。

```python
client.script.save(name, content)
```

### delete

删除脚本。

```python
client.script.delete(name)
```

---

## 通用选择器

所有输入操作都支持多种选择器类型：

```python
from android_automation import SelectorType

client.input.click_by_selector(
    selector_type=SelectorType.ID,
    selector_value="com.example:id/button"
)

client.input.click_by_selector(
    selector_type=SelectorType.TEXT,
    selector_value="确定"
)

client.input.click_by_selector(
    selector_type=SelectorType.CLASS,
    selector_value="android.widget.Button"
)

client.input.click_by_selector(
    selector_type=SelectorType.XPATH,
    selector_value="//Button[@text='确定']"
)
```

## 异常处理

```python
from android_automation import AndroidAutomation
from android_automation.exceptions import (
    APIError,
    DeviceNotConnectedError,
    ElementNotFoundError,
    TimeoutError,
)

try:
    client.device.connect()
    client.input.click(resource_id="com.example:id/button")
except DeviceNotConnectedError:
    print("设备未连接")
except ElementNotFoundError:
    print("元素未找到")
except TimeoutError:
    print("操作超时")
except APIError as e:
    print(f"API 错误: {e.status_code} - {e.message}")
```
