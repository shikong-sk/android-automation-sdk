"""输入操作客户端."""

from typing import TYPE_CHECKING, Optional, Dict, Any, Union

if TYPE_CHECKING:
    from .client import AndroidAutomation

from .types import (
    SelectorType,
    Direction,
    TrajectoryType,
    SpeedMode,
    ElementInfo,
    ElementsResult,
)


class InputClient:
    """输入操作客户端.

    提供点击、输入文本、滑动、屏幕控制、元素定位和人类模拟操作。
    """

    def __init__(self, client: "AndroidAutomation"):
        self._client = client

    def _make_request(self, method: str, path: str, params: Dict = None, json_data: Dict = None, sync: bool = False) -> Dict:
        """发送请求."""
        if sync:
            return self._client._sync_request(method, path, params=params, json_data=json_data)
        else:
            import asyncio
            return asyncio.run(self._client._request(method, path, params=params, json_data=json_data))

    def click(
        self,
        resource_id: str,
        sync: bool = False,
    ) -> bool:
        """点击元素（通过 resource-id）.

        Args:
            resource_id: 元素的 resource-id
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        data = self._make_request(
            "POST", f"input/click",
            params={"resource_id": resource_id},
            sync=sync
        )
        return data.get("success", False)

    def click_by_text(
        self,
        text: str,
        sync: bool = False,
    ) -> bool:
        """点击元素（通过文本）.

        Args:
            text: 元素的文本内容
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        data = self._make_request(
            "POST", f"input/click-by-text",
            params={"text": text},
            sync=sync
        )
        return data.get("success", False)

    def click_by_class(
        self,
        class_name: str,
        sync: bool = False,
    ) -> bool:
        """点击元素（通过类名）.

        Args:
            class_name: 元素的类名
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        data = self._make_request(
            "POST", f"input/click-by-class",
            params={"class_name": class_name},
            sync=sync
        )
        return data.get("success", False)

    def click_by_xpath(
        self,
        xpath: str,
        sync: bool = False,
    ) -> bool:
        """点击元素（通过 XPath）.

        Args:
            xpath: XPath 表达式
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        data = self._make_request(
            "POST", f"input/click-by-xpath",
            params={"xpath": xpath},
            sync=sync
        )
        return data.get("success", False)

    def click_by_selector(
        self,
        selector_type: Union[str, SelectorType],
        selector_value: str,
        sync: bool = False,
    ) -> bool:
        """通过选择器点击元素.

        Args:
            selector_type: 选择器类型
            selector_value: 选择器值
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        data = self._make_request(
            "POST", f"input/click",
            params={
                "selector_type": selector_type.value if isinstance(selector_type, SelectorType) else selector_type,
                "selector_value": selector_value,
            },
            sync=sync
        )
        return data.get("success", False)

    def set_text(
        self,
        resource_id: str,
        text: str,
        sync: bool = False,
    ) -> bool:
        """向输入框输入文本.

        Args:
            resource_id: 输入框的 resource-id
            text: 要输入的文本
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        data = self._make_request(
            "POST", "input/set-text",
            params={"resource_id": resource_id, "text": text},
            sync=sync
        )
        return data.get("success", False)

    def clear_text(
        self,
        resource_id: str,
        sync: bool = False,
    ) -> bool:
        """清除输入框文本.

        Args:
            resource_id: 输入框的 resource-id
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        data = self._make_request(
            "POST", "input/clear-text",
            params={"resource_id": resource_id},
            sync=sync
        )
        return data.get("success", False)

    def swipe(
        self,
        direction: Union[str, Direction],
        percent: float = 0.5,
        sync: bool = False,
    ) -> bool:
        """滑动屏幕.

        Args:
            direction: 滑动方向
            percent: 滑动距离比例（0-1）
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        data = self._make_request(
            "POST", "input/swipe",
            params={
                "direction": direction.value if isinstance(direction, Direction) else direction,
                "percent": percent,
            },
            sync=sync
        )
        return data.get("success", False)

    def screen_on(self, sync: bool = False) -> bool:
        """亮屏.

        Args:
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        data = self._make_request("POST", "input/screen-on", sync=sync)
        return data.get("success", False)

    def screen_off(self, sync: bool = False) -> bool:
        """锁屏.

        Args:
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        data = self._make_request("POST", "input/screen-off", sync=sync)
        return data.get("success", False)

    def unlock(self, sync: bool = False) -> bool:
        """解锁屏幕.

        Args:
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        data = self._make_request("POST", "input/unlock", sync=sync)
        return data.get("success", False)

    def find_by_id(
        self,
        resource_id: str,
        sync: bool = False,
    ) -> ElementInfo:
        """通过 resource-id 查找元素.

        Args:
            resource_id: 元素的 resource-id
            sync: 是否使用同步请求

        Returns:
            元素信息
        """
        data = self._make_request(
            "GET", "input/find-by-id",
            params={"resource_id": resource_id},
            sync=sync
        )
        return ElementInfo(**data)

    def find_by_text(
        self,
        text: str,
        sync: bool = False,
    ) -> ElementInfo:
        """通过文本查找元素.

        Args:
            text: 元素的文本内容
            sync: 是否使用同步请求

        Returns:
            元素信息
        """
        data = self._make_request(
            "GET", "input/find-by-text",
            params={"text": text},
            sync=sync
        )
        return ElementInfo(**data)

    def find_by_class(
        self,
        class_name: str,
        sync: bool = False,
    ) -> ElementInfo:
        """通过类名查找元素.

        Args:
            class_name: 元素的类名
            sync: 是否使用同步请求

        Returns:
            元素信息
        """
        data = self._make_request(
            "GET", "input/find-by-class",
            params={"class_name": class_name},
            sync=sync
        )
        return ElementInfo(**data)

    def find_by_xpath(
        self,
        xpath: str,
        sync: bool = False,
    ) -> ElementInfo:
        """通过 XPath 查找元素.

        Args:
            xpath: XPath 表达式
            sync: 是否使用同步请求

        Returns:
            元素信息
        """
        data = self._make_request(
            "GET", "input/find-by-xpath",
            params={"xpath": xpath},
            sync=sync
        )
        return ElementInfo(**data)

    def find_elements_by_class(
        self,
        class_name: str,
        sync: bool = False,
    ) -> ElementsResult:
        """通过类名查找所有匹配元素.

        Args:
            class_name: 元素的类名
            sync: 是否使用同步请求

        Returns:
            元素列表
        """
        data = self._make_request(
            "GET", "input/find-elements-by-class",
            params={"class_name": class_name},
            sync=sync
        )
        return ElementsResult(**data)

    def exists(
        self,
        resource_id: str,
        sync: bool = False,
    ) -> bool:
        """检查元素是否存在.

        Args:
            resource_id: 元素的 resource-id
            sync: 是否使用同步请求

        Returns:
            是否存在
        """
        data = self._make_request(
            "GET", "input/exists",
            params={"resource_id": resource_id},
            sync=sync
        )
        return data.get("exists", False)

    def get_text(
        self,
        resource_id: str,
        sync: bool = False,
    ) -> str:
        """获取元素文本.

        Args:
            resource_id: 元素的 resource-id
            sync: 是否使用同步请求

        Returns:
            元素文本
        """
        data = self._make_request(
            "GET", "input/text",
            params={"resource_id": resource_id},
            sync=sync
        )
        return data.get("text", "")

    def get_bounds(
        self,
        resource_id: str,
        sync: bool = False,
    ) -> Dict[str, int]:
        """获取元素边界.

        Args:
            resource_id: 元素的 resource-id
            sync: 是否使用同步请求

        Returns:
            边界信息 {left, top, right, bottom}
        """
        data = self._make_request(
            "GET", "input/bounds",
            params={"resource_id": resource_id},
            sync=sync
        )
        return data.get("bounds", {})

    def wait_appear(
        self,
        resource_id: str,
        timeout: float = 10.0,
        sync: bool = False,
    ) -> bool:
        """等待元素出现.

        Args:
            resource_id: 元素的 resource-id
            timeout: 最大等待时间（秒）
            sync: 是否使用同步请求

        Returns:
            是否出现
        """
        data = self._make_request(
            "GET", "input/wait-appear",
            params={"resource_id": resource_id, "timeout": timeout},
            sync=sync
        )
        return data.get("appeared", False)

    def wait_gone(
        self,
        resource_id: str,
        timeout: float = 10.0,
        sync: bool = False,
    ) -> bool:
        """等待元素消失.

        Args:
            resource_id: 元素的 resource-id
            timeout: 最大等待时间（秒）
            sync: 是否使用同步请求

        Returns:
            是否消失
        """
        data = self._make_request(
            "GET", "input/wait-gone",
            params={"resource_id": resource_id, "timeout": timeout},
            sync=sync
        )
        return data.get("gone", False)

    def get_hierarchy(self, sync: bool = False) -> str:
        """获取界面 XML 结构.

        Args:
            sync: 是否使用同步请求

        Returns:
            XML 字符串
        """
        data = self._make_request("GET", "input/hierarchy", sync=sync)
        return data.get("xml", "")

    def human_click(
        self,
        x: Optional[int] = None,
        y: Optional[int] = None,
        selector_type: Optional[Union[str, SelectorType]] = None,
        selector_value: Optional[str] = None,
        offset_min: float = 3.0,
        offset_max: float = 10.0,
        delay_min: float = 0.05,
        delay_max: float = 0.3,
        duration_min: float = 0.05,
        duration_max: float = 0.15,
        sync: bool = False,
    ) -> bool:
        """模拟人类点击.

        Args:
            x: X 坐标
            y: Y 坐标
            selector_type: 选择器类型
            selector_value: 选择器值
            offset_min: 最小偏移（像素）
            offset_max: 最大偏移（像素）
            delay_min: 最小延迟（秒）
            delay_max: 最大延迟（秒）
            duration_min: 最小按压时长（秒）
            duration_max: 最大按压时长（秒）
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        data = self._make_request(
            "POST", "input/human-click",
            json_data={
                "x": x,
                "y": y,
                "selector_type": selector_type.value if isinstance(selector_type, SelectorType) else selector_type,
                "selector_value": selector_value,
                "offset_min": offset_min,
                "offset_max": offset_max,
                "delay_min": delay_min,
                "delay_max": delay_max,
                "duration_min": duration_min,
                "duration_max": duration_max,
            },
            sync=sync
        )
        return data.get("success", False)

    def human_double_click(
        self,
        x: Optional[int] = None,
        y: Optional[int] = None,
        selector_type: Optional[Union[str, SelectorType]] = None,
        selector_value: Optional[str] = None,
        offset_min: float = 3.0,
        offset_max: float = 10.0,
        interval_min: float = 0.1,
        interval_max: float = 0.2,
        duration_min: float = 0.05,
        duration_max: float = 0.15,
        sync: bool = False,
    ) -> bool:
        """模拟人类双击.

        Args:
            x: X 坐标
            y: Y 坐标
            selector_type: 选择器类型
            selector_value: 选择器值
            offset_min: 最小偏移（像素）
            offset_max: 最大偏移（像素）
            interval_min: 最小双击间隔（秒）
            interval_max: 最大双击间隔（秒）
            duration_min: 最小按压时长（秒）
            duration_max: 最大按压时长（秒）
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        data = self._make_request(
            "POST", "input/human-double-click",
            json_data={
                "x": x,
                "y": y,
                "selector_type": selector_type.value if isinstance(selector_type, SelectorType) else selector_type,
                "selector_value": selector_value,
                "offset_min": offset_min,
                "offset_max": offset_max,
                "interval_min": interval_min,
                "interval_max": interval_max,
                "duration_min": duration_min,
                "duration_max": duration_max,
            },
            sync=sync
        )
        return data.get("success", False)

    def human_long_press(
        self,
        x: Optional[int] = None,
        y: Optional[int] = None,
        selector_type: Optional[Union[str, SelectorType]] = None,
        selector_value: Optional[str] = None,
        duration_min: float = 1.0,
        duration_max: float = 2.0,
        offset_min: float = 3.0,
        offset_max: float = 10.0,
        delay_min: float = 0.05,
        delay_max: float = 0.3,
        sync: bool = False,
    ) -> bool:
        """模拟人类长按.

        Args:
            x: X 坐标
            y: Y 坐标
            selector_type: 选择器类型
            selector_value: 选择器值
            duration_min: 最小长按时间（秒）
            duration_max: 最大长按时间（秒）
            offset_min: 最小偏移（像素）
            offset_max: 最大偏移（像素）
            delay_min: 最小延迟（秒）
            delay_max: 最大延迟（秒）
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        data = self._make_request(
            "POST", "input/human-long-press",
            json_data={
                "x": x,
                "y": y,
                "selector_type": selector_type.value if isinstance(selector_type, SelectorType) else selector_type,
                "selector_value": selector_value,
                "duration_min": duration_min,
                "duration_max": duration_max,
                "offset_min": offset_min,
                "offset_max": offset_max,
                "delay_min": delay_min,
                "delay_max": delay_max,
            },
            sync=sync
        )
        return data.get("success", False)

    def human_drag(
        self,
        start_x: Optional[int] = None,
        start_y: Optional[int] = None,
        end_x: Optional[int] = None,
        end_y: Optional[int] = None,
        start_selector_type: Optional[Union[str, SelectorType]] = None,
        start_selector_value: Optional[str] = None,
        end_selector_type: Optional[Union[str, SelectorType]] = None,
        end_selector_value: Optional[str] = None,
        trajectory_type: str = "bezier",
        speed_mode: str = "ease_in_out",
        duration: float = 1.0,
        num_points: int = 50,
        offset_min: float = 3.0,
        offset_max: float = 10.0,
        jitter_min: float = 1.0,
        jitter_max: float = 5.0,
        delay_min: float = 0.05,
        delay_max: float = 0.3,
        sync: bool = False,
    ) -> bool:
        """模拟人类拖拽.

        Args:
            start_x: 起点 X 坐标
            start_y: 起点 Y 坐标
            end_x: 终点 X 坐标
            end_y: 终点 Y 坐标
            start_selector_type: 起点选择器类型
            start_selector_value: 起点选择器值
            end_selector_type: 终点选择器类型
            end_selector_value: 终点选择器值
            trajectory_type: 轨迹类型（bezier, linear_jitter）
            speed_mode: 速度模式（ease_in_out, ease_in, ease_out, linear, random）
            duration: 拖拽时间（秒）
            num_points: 轨迹采样点数量
            offset_min: 最小偏移（像素）
            offset_max: 最大偏移（像素）
            jitter_min: 最小抖动（像素）
            jitter_max: 最大抖动（像素）
            delay_min: 最小延迟（秒）
            delay_max: 最大延迟（秒）
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        data = self._make_request(
            "POST", "input/human-drag",
            json_data={
                "start_x": start_x,
                "start_y": start_y,
                "end_x": end_x,
                "end_y": end_y,
                "start_selector_type": start_selector_type.value if isinstance(start_selector_type, SelectorType) else start_selector_type,
                "start_selector_value": start_selector_value,
                "end_selector_type": end_selector_type.value if isinstance(end_selector_type, SelectorType) else end_selector_type,
                "end_selector_value": end_selector_value,
                "trajectory_type": trajectory_type.value if isinstance(trajectory_type, TrajectoryType) else trajectory_type,
                "speed_mode": speed_mode.value if isinstance(speed_mode, SpeedMode) else speed_mode,
                "duration": duration,
                "num_points": num_points,
                "offset_min": offset_min,
                "offset_max": offset_max,
                "jitter_min": jitter_min,
                "jitter_max": jitter_max,
                "delay_min": delay_min,
                "delay_max": delay_max,
            },
            sync=sync
        )
        return data.get("success", False)
