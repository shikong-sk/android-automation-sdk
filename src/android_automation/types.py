"""类型定义."""

from enum import Enum
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field


class SelectorType(str, Enum):
    """元素选择器类型."""

    ID = "id"
    TEXT = "text"
    CLASS = "class"
    XPATH = "xpath"


class Direction(str, Enum):
    """滑动方向."""

    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class TrajectoryType(str, Enum):
    """拖拽轨迹类型."""

    BEZIER = "bezier"
    LINEAR_JITTER = "linear_jitter"


class SpeedMode(str, Enum):
    """速度模式."""

    EASE_IN_OUT = "ease_in_out"
    EASE_IN = "ease_in"
    EASE_OUT = "ease_out"
    LINEAR = "linear"
    RANDOM = "random"


class DeviceInfo(BaseModel):
    """设备信息."""

    serial: str = Field(..., description="设备序列号")
    product_name: str = Field(..., description="产品名称")
    api_level: int = Field(..., description="API 级别")
    battery_level: Optional[int] = Field(None, description="电池电量")


class DeviceStatus(BaseModel):
    """设备状态."""

    connected: bool = Field(..., description="是否已连接")
    device_info: Optional[DeviceInfo] = Field(None, description="设备信息")


class ElementInfo(BaseModel):
    """元素信息."""

    exists: bool = Field(..., description="元素是否存在")
    text: Optional[str] = Field(None, description="元素文本")
    class_name: Optional[str] = Field(None, description="元素类名")
    resource_id: Optional[str] = Field(None, description="资源 ID")
    bounds: Optional[Dict[str, int]] = Field(None, description="边界位置")
    enabled: Optional[bool] = Field(None, description="是否可用")
    focused: Optional[bool] = Field(None, description="是否获得焦点")
    selected: Optional[bool] = Field(None, description="是否被选中")
    clickable: Optional[bool] = Field(None, description="是否可点击")


class ElementsResult(BaseModel):
    """多元素查询结果."""

    elements: List[ElementInfo] = Field(default_factory=list)
    count: int = Field(..., description="元素数量")


class AppInfo(BaseModel):
    """应用信息."""

    package: str = Field(..., description="包名")
    version: Optional[str] = Field(None, description="版本号")


class AppStatus(BaseModel):
    """应用状态."""

    package: str = Field(..., description="包名")
    running: bool = Field(..., description="是否运行中")


class CurrentApp(BaseModel):
    """当前前台应用."""

    package: Optional[str] = Field(None, description="包名")
    activity: Optional[str] = Field(None, description="Activity 名称")
    pid: Optional[int] = Field(None, description="进程 ID")


class BatteryInfo(BaseModel):
    """电池信息."""

    level: int = Field(..., description="电量百分比")
    scale: int = Field(..., description="电量刻度")
    status: str = Field(..., description="状态")
    health: str = Field(..., description="健康状况")
    plugged: str = Field(..., description="充电方式")
    temperature: float = Field(..., description="温度")
    voltage: int = Field(..., description="电压")


class ScreenResolution(BaseModel):
    """屏幕分辨率."""

    width: int = Field(..., description="宽度")
    height: int = Field(..., description="高度")


class DeviceInfoResult(BaseModel):
    """设备详细信息."""

    serial: str = Field(..., description="序列号")
    product_name: Optional[str] = Field(None, description="产品名称")
    device_name: Optional[str] = Field(None, description="设备名称")
    model: Optional[str] = Field(None, description="型号")
    brand: Optional[str] = Field(None, description="品牌")
    manufacturer: Optional[str] = Field(None, description="制造商")
    android_version: Optional[str] = Field(None, description="Android 版本")
    sdk_version: Optional[int] = Field(None, description="SDK 版本")


class ScriptInfo(BaseModel):
    """脚本信息."""

    name: str = Field(..., description="脚本名称")
    size: int = Field(..., description="文件大小")
    modified: float = Field(..., description="修改时间")


class ScriptContent(BaseModel):
    """脚本内容."""

    content: str = Field(..., description="脚本内容")
    variables: Optional[Dict[str, Any]] = Field(None, description="变量")


class ExecutionResult(BaseModel):
    """脚本执行结果."""

    success: bool = Field(..., description="是否成功")
    logs: List[str] = Field(default_factory=list, description="执行日志")
    error: Optional[str] = Field(None, description="错误信息")
    variables: Dict[str, Any] = Field(default_factory=dict, description="变量")


class ScriptValidation(BaseModel):
    """脚本验证结果."""

    valid: bool = Field(..., description="语法是否正确")
    statements: int = Field(..., description="语句数量")
    error: Optional[str] = Field(None, description="错误信息")
