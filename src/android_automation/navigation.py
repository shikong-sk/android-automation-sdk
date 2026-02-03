"""导航控制客户端."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .client import AndroidAutomation


class NavigationClient:
    """导航控制客户端.

    提供 Home、返回、菜单等导航操作。
    """

    def __init__(self, client: "AndroidAutomation"):
        self._client = client

    def _make_request(self, path: str, sync: bool = False):
        """发送请求."""
        if sync:
            return self._client._sync_request("POST", f"navigation/{path}")
        else:
            import asyncio
            return asyncio.run(self._client._request("POST", f"navigation/{path}"))

    def home(self, sync: bool = False):
        """返回主屏幕.

        Args:
            sync: 是否使用同步请求
        """
        self._make_request("home", sync=sync)

    def back(self, sync: bool = False):
        """返回上一页.

        Args:
            sync: 是否使用同步请求
        """
        self._make_request("back", sync=sync)

    def menu(self, sync: bool = False):
        """打开菜单.

        Args:
            sync: 是否使用同步请求
        """
        self._make_request("menu", sync=sync)

    def go_home(self, sync: bool = False):
        """确保返回主页.

        Args:
            sync: 是否使用同步请求
        """
        self._make_request("go-home", sync=sync)

    def recent_apps(self, sync: bool = False):
        """打开最近应用.

        Args:
            sync: 是否使用同步请求
        """
        self._make_request("recent-apps", sync=sync)
