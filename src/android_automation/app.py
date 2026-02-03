"""应用管理客户端."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .client import AndroidAutomation

from .types import AppInfo, AppStatus, CurrentApp


class AppClient:
    """应用管理客户端.

    提供应用的启动、停止、状态查询等操作。
    """

    def __init__(self, client: "AndroidAutomation"):
        self._client = client

    def _make_request(self, method: str, path: str, params: dict = None, sync: bool = False):
        """发送请求."""
        if sync:
            return self._client._sync_request(method, f"app/{path}", params=params)
        else:
            import asyncio
            return asyncio.run(self._client._request(method, f"app/{path}", params=params))

    def start(self, package_name: str, sync: bool = False):
        """启动应用.

        Args:
            package_name: 应用包名
            sync: 是否使用同步请求
        """
        self._make_request("POST", f"start/{package_name}", sync=sync)

    def stop(self, package_name: str, sync: bool = False):
        """停止应用.

        Args:
            package_name: 应用包名
            sync: 是否使用同步请求
        """
        self._make_request("POST", f"stop/{package_name}", sync=sync)

    def clear(self, package_name: str, sync: bool = False):
        """清除应用数据.

        Args:
            package_name: 应用包名
            sync: 是否使用同步请求
        """
        self._make_request("POST", f"clear/{package_name}", sync=sync)

    def get_version(self, package_name: str, sync: bool = False) -> AppInfo:
        """获取应用版本.

        Args:
            package_name: 应用包名
            sync: 是否使用同步请求

        Returns:
            应用信息
        """
        data = self._make_request("GET", f"version/{package_name}", sync=sync)
        return AppInfo(**data)

    def get_status(self, package_name: str, sync: bool = False) -> AppStatus:
        """检查应用运行状态.

        Args:
            package_name: 应用包名
            sync: 是否使用同步请求

        Returns:
            应用状态
        """
        data = self._make_request("GET", f"status/{package_name}", sync=sync)
        return AppStatus(**data)

    def get_current(self, sync: bool = False) -> CurrentApp:
        """获取当前前台应用.

        Args:
            sync: 是否使用同步请求

        Returns:
            当前应用信息
        """
        data = self._make_request("GET", "current", sync=sync)
        return CurrentApp(**data)
