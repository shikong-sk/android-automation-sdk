"""设备管理客户端."""
import asyncio
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .client import AndroidAutomation

from .types import DeviceInfo, DeviceStatus


class DeviceClient:
    """设备管理客户端.

    Args:
        client: AndroidAutomation 实例
    """

    def __init__(self, client: "AndroidAutomation"):
        self._client = client

    def connect(
        self,
        device_serial: Optional[str] = None,
        sync: bool = False,
    ) -> DeviceInfo:
        """连接设备.

        连接到指定的安卓设备或自动选择第一个可用设备。

        Args:
            device_serial: 设备序列号。如果为 None，则自动选择设备。
            sync: 是否使用同步请求

        Returns:
            DeviceInfo: 已连接设备信息
        """
        if sync:
            data = self._client._sync_request(
                "POST",
                "device/connect",
                json_data={"device_serial": device_serial} if device_serial else None,
            )
        else:
            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            data = loop.run_until_complete(
                self._client._request(
                    "POST",
                    "device/connect",
                    json_data={"device_serial": device_serial} if device_serial else None,
                )
            )

        return DeviceInfo(**data)

    def get_status(self, sync: bool = False) -> DeviceStatus:
        """获取设备状态.

        Args:
            sync: 是否使用同步请求

        Returns:
            DeviceStatus: 设备状态
        """
        if sync:
            data = self._client._sync_request("GET", "device/status")
        else:
            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            data = loop.run_until_complete(self._client._request("GET", "device/status"))

        return DeviceStatus(**data)

    def disconnect(self, sync: bool = False):
        """断开设备连接.

        Args:
            sync: 是否使用同步请求
        """
        if sync:
            self._client._sync_request("POST", "device/disconnect")
        else:
            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            loop.run_until_complete(self._client._request("POST", "device/disconnect"))
