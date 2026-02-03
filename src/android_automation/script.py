"""脚本管理客户端."""

import asyncio
from typing import TYPE_CHECKING, Optional, Dict, Any, List, AsyncIterator

if TYPE_CHECKING:
    from .client import AndroidAutomation

from .types import (
    ScriptInfo,
    ScriptContent,
    ExecutionResult,
    ScriptValidation,
)


class ScriptClient:
    """脚本管理客户端.

    提供脚本的创建、编辑、执行和管理功能。
    """

    def __init__(self, client: "AndroidAutomation"):
        self._client = client

    def _make_request(
        self,
        method: str,
        path: str,
        params: dict = None,
        json_data: dict = None,
        sync: bool = False,
    ):
        """发送请求."""
        if sync:
            return self._client._sync_request(method, f"script/{path}", params=params, json_data=json_data)
        else:
            import asyncio
            return asyncio.run(self._client._request(method, f"script/{path}", params=params, json_data=json_data))

    def list(self, sync: bool = False) -> List[ScriptInfo]:
        """获取脚本列表.

        Args:
            sync: 是否使用同步请求

        Returns:
            脚本信息列表
        """
        data = self._make_request("GET", "list", sync=sync)
        return [ScriptInfo(**script) for script in data]

    def get(self, name: str, sync: bool = False) -> Dict[str, str]:
        """获取脚本内容.

        Args:
            name: 脚本文件名
            sync: 是否使用同步请求

        Returns:
            包含脚本内容的字典
        """
        return self._make_request("GET", f"get/{name}", sync=sync)

    def save(self, name: str, content: str, sync: bool = False) -> Dict[str, str]:
        """保存脚本.

        Args:
            name: 脚本文件名
            content: 脚本内容
            sync: 是否使用同步请求

        Returns:
            操作结果
        """
        return self._make_request(
            "POST", "save",
            json_data={"name": name, "content": content},
            sync=sync
        )

    def delete(self, name: str, sync: bool = False) -> Dict[str, str]:
        """删除脚本.

        Args:
            name: 脚本文件名
            sync: 是否使用同步请求

        Returns:
            操作结果
        """
        return self._make_request("DELETE", f"delete/{name}", sync=sync)

    def execute(
        self,
        content: str,
        variables: Optional[Dict[str, Any]] = None,
        sync: bool = False,
    ) -> ExecutionResult:
        """执行脚本内容.

        Args:
            content: 脚本内容
            variables: 初始变量
            sync: 是否使用同步请求

        Returns:
            执行结果
        """
        data = self._make_request(
            "POST", "execute",
            json_data={"content": content, "variables": variables},
            sync=sync
        )
        return ExecutionResult(**data)

    def execute_file(
        self,
        name: str,
        variables: Optional[Dict[str, Any]] = None,
        sync: bool = False,
    ) -> ExecutionResult:
        """执行脚本文件.

        Args:
            name: 脚本文件名
            variables: 初始变量
            sync: 是否使用同步请求

        Returns:
            执行结果
        """
        params = {}
        if variables:
            params["variables"] = variables
        data = self._make_request("POST", f"execute/{name}", params=params, sync=sync)
        return ExecutionResult(**data)

    def validate(
        self,
        content: str,
        sync: bool = False,
    ) -> ScriptValidation:
        """验证脚本语法.

        Args:
            content: 脚本内容
            sync: 是否使用同步请求

        Returns:
            验证结果
        """
        data = self._make_request(
            "POST", "validate",
            json_data={"content": content},
            sync=sync
        )
        return ScriptValidation(**data)

    def stop(self, session_id: str, sync: bool = False) -> Dict[str, str]:
        """停止正在执行的脚本.

        Args:
            session_id: 执行会话 ID
            sync: 是否使用同步请求

        Returns:
            操作结果
        """
        return self._make_request("POST", f"stop/{session_id}", sync=sync)

    def execute_stream(
        self,
        content: str,
        variables: Optional[Dict[str, Any]] = None,
    ) -> AsyncIterator[Dict[str, Any]]:
        """执行脚本并通过 SSE 实时返回日志.

        Args:
            content: 脚本内容
            variables: 初始变量

        Yields:
            事件字典
        """
        import httpx
        import json

        async def event_generator():
            url = f"{self._client.base_url}/api/v1/script/execute/stream"
            async with httpx.AsyncClient(timeout=self._client.timeout) as http_client:
                async with http_client.stream(
                    "POST",
                    url,
                    json={"content": content, "variables": variables},
                ) as response:
                    async for line in response.aiter_lines():
                        if line.startswith("data: "):
                            event_data = line[6:]
                            try:
                                event = json.loads(event_data)
                                yield event
                                if event.get("type") == "end":
                                    break
                            except json.JSONDecodeError:
                                pass

        return event_generator()

    def execute_file_stream(
        self,
        name: str,
        variables: Optional[Dict[str, Any]] = None,
    ) -> AsyncIterator[Dict[str, Any]]:
        """执行脚本文件并通过 SSE 实时返回日志.

        Args:
            name: 脚本文件名
            variables: 初始变量

        Yields:
            事件字典
        """
        import httpx
        import json
        from urllib.parse import urlencode

        async def event_generator():
            url = f"{self._client.base_url}/api/v1/script/execute/stream/{name}"
            if variables:
                url += f"?{urlencode(variables)}"

            async with httpx.AsyncClient(timeout=self._client.timeout) as http_client:
                async with http_client.stream("POST", url) as response:
                    async for line in response.aiter_lines():
                        if line.startswith("data: "):
                            event_data = line[6:]
                            try:
                                event = json.loads(event_data)
                                yield event
                                if event.get("type") == "end":
                                    break
                            except json.JSONDecodeError:
                                pass

        return event_generator()
