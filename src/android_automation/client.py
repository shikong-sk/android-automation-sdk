"""Android Automation API 客户端."""

import asyncio
from typing import Optional, AsyncIterator, Dict, Any
from contextlib import asynccontextmanager

import httpx
from pydantic import BaseModel

from .device import DeviceClient
from .input import InputClient
from .navigation import NavigationClient
from .app import AppClient
from .adb import ADBClient
from .script import ScriptClient
from .exceptions import APIError


class AndroidAutomation:
    """Android Automation API 客户端主类.

    Args:
        base_url: API 服务器地址
        timeout: 请求超时时间（秒）
        verify: 是否验证 SSL 证书
    """

    def __init__(
        self,
        base_url: str = "http://localhost:8000",
        timeout: float = 30.0,
        verify: bool = True,
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.verify = verify

        self._client: Optional[httpx.AsyncClient] = None
        self._sync_client: Optional[httpx.Client] = None

        self.device = DeviceClient(self)
        self.input = InputClient(self)
        self.navigation = NavigationClient(self)
        self.app = AppClient(self)
        self.adb = ADBClient(self)
        self.script = ScriptClient(self)

    def _get_client(self) -> httpx.AsyncClient:
        """获取异步客户端."""
        if self._client is None:
            self._client = httpx.AsyncClient(
                timeout=self.timeout,
                verify=self.verify,
            )
        return self._client

    def _get_sync_client(self) -> httpx.Client:
        """获取同步客户端."""
        if self._sync_client is None:
            self._sync_client = httpx.Client(
                timeout=self.timeout,
                verify=self.verify,
            )
        return self._sync_client

    async def _request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """发送异步请求.

        Args:
            method: HTTP 方法
            path: 请求路径
            params: 查询参数
            json_data: JSON 请求体

        Returns:
            响应数据
        """
        client = self._get_client()
        url = f"{self.base_url}/api/v1/{path}"

        response = await client.request(
            method=method,
            url=url,
            params=params,
            json=json_data,
        )

        if response.status_code >= 400:
            try:
                error_data = response.json()
                message = error_data.get("detail", response.text)
            except Exception:
                message = response.text
            raise APIError(response.status_code, message, response.text)

        return response.json()

    def _sync_request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """发送同步请求.

        Args:
            method: HTTP 方法
            path: 请求路径
            params: 查询参数
            json_data: JSON 请求体

        Returns:
            响应数据
        """
        client = self._get_sync_client()
        url = f"{self.base_url}/api/v1/{path}"

        response = client.request(
            method=method,
            url=url,
            params=params,
            json=json_data,
        )

        if response.status_code >= 400:
            try:
                error_data = response.json()
                message = error_data.get("detail", response.text)
            except Exception:
                message = response.text
            raise APIError(response.status_code, message, response.text)

        return response.json()

    async def close(self):
        """关闭异步客户端."""
        if self._client:
            await self._client.aclose()
            self._client = None

    def __aenter__(self):
        """异步上下文管理器入口."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """异步上下文管理器退出."""
        await self.close()

    def __enter__(self):
        """同步上下文管理器入口."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """同步上下文管理器退出."""
        self.close_sync()

    def close_sync(self):
        """关闭同步客户端."""
        if self._sync_client:
            self._sync_client.close()
            self._sync_client = None
