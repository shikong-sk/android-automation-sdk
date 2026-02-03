"""异常定义."""

from typing import Optional, List


class SDKError(Exception):
    """SDK 基础异常."""

    pass


class APIError(SDKError):
    """API 请求错误."""

    def __init__(self, status_code: int, message: str, response: str = ""):
        self.status_code = status_code
        self.message = message
        self.response = response
        super().__init__(f"API Error {status_code}: {message}")


class DeviceNotConnectedError(SDKError):
    """设备未连接异常."""

    pass


class DeviceConnectionError(SDKError):
    """设备连接错误."""

    pass


class ElementNotFoundError(SDKError):
    """元素未找到异常."""

    def __init__(self, selector: str, selector_type: str):
        self.selector = selector
        self.selector_type = selector_type
        super().__init__(f"Element not found: {selector_type}='{selector}'")


class TimeoutError(SDKError):
    """操作超时异常."""

    def __init__(self, operation: str, timeout: float):
        self.operation = operation
        self.timeout = timeout
        super().__init__(f"Timeout ({timeout}s) waiting for {operation}")


class ScriptExecutionError(SDKError):
    """脚本执行错误."""

    def __init__(self, message: str, logs: Optional[List[str]] = None):
        self.message = message
        self.logs = logs if logs is not None else []
        super().__init__(f"Script execution failed: {message}")


class ValidationError(SDKError):
    """验证错误."""

    pass
