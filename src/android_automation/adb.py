"""ADB 命令客户端."""

from typing import TYPE_CHECKING, Optional, Dict, Any

if TYPE_CHECKING:
    from .client import AndroidAutomation

from .types import (
    DeviceInfoResult,
    BatteryInfo,
    ScreenResolution,
)


class ADBClient:
    """ADB 命令客户端.

    提供 ADB 相关的操作，包括 Shell 命令、文件传输、设备信息查询等。
    """

    def __init__(self, client: "AndroidAutomation"):
        self._client = client

    def _make_request(self, method: str, path: str, params: dict = None, json_data: dict = None, sync: bool = False):
        """发送请求."""
        if sync:
            return self._client._sync_request(method, f"adb/{path}", params=params, json_data=json_data)
        else:
            import asyncio
            return asyncio.run(self._client._request(method, f"adb/{path}", params=params, json_data=json_data))

    def list_packages(
        self,
        filter_type: Optional[str] = None,
        sync: bool = False,
    ) -> list:
        """获取已安装应用列表.

        Args:
            filter_type: 过滤类型 (third_party, system, None)
            sync: 是否使用同步请求

        Returns:
            应用包名列表
        """
        params = {}
        if filter_type:
            params["filter_type"] = filter_type
        data = self._make_request("GET", "packages", params=params, sync=sync)
        return data.get("packages", [])

    def get_package_info(
        self,
        package_name: str,
        sync: bool = False,
    ) -> Dict[str, Any]:
        """获取应用详细信息.

        Args:
            package_name: 应用包名
            sync: 是否使用同步请求

        Returns:
            应用详细信息
        """
        return self._make_request("GET", f"packages/{package_name}", sync=sync)

    def install_apk(
        self,
        apk_path: str,
        reinstall: bool = False,
        grant_permissions: bool = True,
        sync: bool = False,
    ) -> bool:
        """安装 APK.

        Args:
            apk_path: APK 文件路径
            reinstall: 是否重新安装
            grant_permissions: 是否授予权限
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        self._make_request(
            "POST", "install",
            json_data={
                "apk_path": apk_path,
                "reinstall": reinstall,
                "grant_permissions": grant_permissions,
            },
            sync=sync
        )
        return True

    def uninstall_package(
        self,
        package_name: str,
        keep_data: bool = False,
        sync: bool = False,
    ) -> bool:
        """卸载应用.

        Args:
            package_name: 应用包名
            keep_data: 是否保留数据
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        self._make_request(
            "DELETE", f"packages/{package_name}",
            params={"keep_data": keep_data},
            sync=sync
        )
        return True

    def get_device_info(self, sync: bool = False) -> DeviceInfoResult:
        """获取设备详细信息.

        Args:
            sync: 是否使用同步请求

        Returns:
            设备信息
        """
        data = self._make_request("GET", "device-info", sync=sync)
        return DeviceInfoResult(**data)

    def get_battery_info(self, sync: bool = False) -> BatteryInfo:
        """获取电池信息.

        Args:
            sync: 是否使用同步请求

        Returns:
            电池信息
        """
        data = self._make_request("GET", "battery", sync=sync)
        return BatteryInfo(**data)

    def get_screen_resolution(self, sync: bool = False) -> ScreenResolution:
        """获取屏幕分辨率.

        Args:
            sync: 是否使用同步请求

        Returns:
            屏幕分辨率
        """
        data = self._make_request("GET", "screen/resolution", sync=sync)
        return ScreenResolution(**data)

    def get_screen_density(self, sync: bool = False) -> int:
        """获取屏幕密度.

        Args:
            sync: 是否使用同步请求

        Returns:
            屏幕密度 (dpi)
        """
        data = self._make_request("GET", "screen/density", sync=sync)
        return data.get("density", 0)

    def get_prop(self, prop_name: str, sync: bool = False) -> str:
        """获取设备属性.

        Args:
            prop_name: 属性名称
            sync: 是否使用同步请求

        Returns:
            属性值
        """
        data = self._make_request("GET", f"prop/{prop_name}", sync=sync)
        return data.get("value", "")

    def shell(self, command: str, sync: bool = False) -> str:
        """执行 Shell 命令.

        Args:
            command: Shell 命令
            sync: 是否使用同步请求

        Returns:
            命令输出
        """
        data = self._make_request("POST", "shell", json_data={"command": command}, sync=sync)
        return data.get("output", "")

    def push_file(
        self,
        local_path: str,
        remote_path: str,
        sync: bool = False,
    ) -> bool:
        """推送文件到设备.

        Args:
            local_path: 本地文件路径
            remote_path: 设备目标路径
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        self._make_request(
            "POST", "push",
            json_data={"local_path": local_path, "remote_path": remote_path},
            sync=sync
        )
        return True

    def pull_file(
        self,
        remote_path: str,
        local_path: str,
        sync: bool = False,
    ) -> bool:
        """从设备拉取文件.

        Args:
            remote_path: 设备文件路径
            local_path: 本地目标路径
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        self._make_request(
            "POST", "pull",
            json_data={"local_path": local_path, "remote_path": remote_path},
            sync=sync
        )
        return True

    def take_screenshot(self, local_path: str, sync: bool = False) -> bool:
        """截取屏幕截图.

        Args:
            local_path: 保存截图的本地路径
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        self._make_request(
            "POST", "screenshot",
            params={"local_path": local_path},
            sync=sync
        )
        return True

    def reboot(self, mode: Optional[str] = None, sync: bool = False) -> bool:
        """重启设备.

        Args:
            mode: 重启模式 (recovery, bootloader, None)
            sync: 是否使用同步请求

        Returns:
            是否成功
        """
        self._make_request(
            "POST", "reboot",
            params={"mode": mode} if mode else None,
            sync=sync
        )
        return True
