"""Android Automation SDK - Python SDK for Android Automation API."""

from .client import AndroidAutomation
from .device import DeviceClient
from .input import InputClient
from .navigation import NavigationClient
from .app import AppClient
from .adb import ADBClient
from .script import ScriptClient
from .exceptions import (
    APIError,
    DeviceNotConnectedError,
    ElementNotFoundError,
    TimeoutError,
    ScriptExecutionError,
)
from .types import SelectorType, Direction, TrajectoryType, SpeedMode

__all__ = [
    "AndroidAutomation",
    "DeviceClient",
    "InputClient",
    "NavigationClient",
    "AppClient",
    "ADBClient",
    "ScriptClient",
    "APIError",
    "DeviceNotConnectedError",
    "ElementNotFoundError",
    "TimeoutError",
    "ScriptExecutionError",
    "SelectorType",
    "Direction",
    "TrajectoryType",
    "SpeedMode",
]

__version__ = "0.1.0"
