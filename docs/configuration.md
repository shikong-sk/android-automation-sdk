# 配置指南

## 客户端配置

### 基本配置

```python
from android_automation import AndroidAutomation

# 创建客户端
client = AndroidAutomation(
    base_url="http://localhost:8000",  # API 服务地址
    timeout=30.0,                       # 请求超时时间（秒）
    verify=True,                        # SSL 验证
)
```

### 配置参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `base_url` | str | 必填 | API 服务地址 |
| `timeout` | float | 30.0 | 请求超时时间（秒） |
| `verify` | bool | True | 是否验证 SSL 证书 |

### 使用配置文件

```python
import json
from android_automation import AndroidAutomation

# 从配置文件加载
with open("config.json", "r") as f:
    config = json.load(f)

client = AndroidAutomation(**config)
```

**config.json 示例:**

```json
{
    "base_url": "http://localhost:8000",
    "timeout": 30.0,
    "verify": true
}
```

### 使用环境变量

```python
import os
from android_automation import AndroidAutomation

client = AndroidAutomation(
    base_url=os.getenv("ANDROID_API_URL", "http://localhost:8000"),
    timeout=float(os.getenv("ANDROID_API_TIMEOUT", "30.0")),
)
```

---

## 上下文管理器

使用上下文管理器确保资源正确释放：

```python
from android_automation import AndroidAutomation

with AndroidAutomation(base_url="http://localhost:8000") as client:
    client.device.connect()
    # 执行操作...
# 自动断开连接
```

---

## 超时配置

### 全局超时

```python
client = AndroidAutomation(base_url="http://localhost:8000", timeout=60.0)
```

### 单独操作超时

```python
# 大多数方法支持 timeout 参数
client.input.wait_appear(resource_id="com.example:id/button", timeout=30.0)
client.input.wait_gone(resource_id="com.example:id/loading", timeout=30.0)
```

---

## 高级配置

### 自定义 HTTP 客户端

```python
import httpx
from android_automation import AndroidAutomation

# 自定义 HTTP 客户端
http_client = httpx.Client(
    timeout=60.0,
    verify=False,
    proxies={
        "http": "http://proxy:8080",
        "https": "http://proxy:8080",
    }
)

client = AndroidAutomation(
    base_url="http://localhost:8000",
    http_client=http_client,
)
```

### 异步客户端

```python
import asyncio
from android_automation import AndroidAutomation

async def main():
    async with AndroidAutomation(
        base_url="http://localhost:8000",
        timeout=30.0,
    ) as client:
        await client.device.connect()
        # 异步操作...

asyncio.run(main())
```

---

## 连接配置

### 设备连接选项

```python
from android_automation import AndroidAutomation

client = AndroidAutomation(base_url="http://localhost:8000")

# 自动选择第一个可用设备
device_info = client.device.connect()

# 指定设备序列号
device_info = client.device.connect(device_serial="emulator-5554")

# WiFi 连接
device_info = client.device.connect(device_serial="192.168.1.100:5555")
```

### 设备连接状态

```python
status = client.device.get_status()

if status.connected:
    print(f"已连接: {status.device_info.serial}")
    print(f"设备信息: {status.device_info}")
else:
    print("未连接设备")
```

---

## 代理配置

### 通过环境变量

```bash
export HTTP_PROXY="http://proxy:8080"
export HTTPS_PROXY="http://proxy:8080"
```

### 在代码中配置

```python
import httpx
from android_automation import AndroidAutomation

http_client = httpx.Client(
    proxies={
        "http": "http://proxy:8080",
        "https": "http://proxy:8080",
    }
)

client = AndroidAutomation(
    base_url="http://localhost:8000",
    http_client=http_client,
)
```

---

## SSL 配置

### 禁用 SSL 验证

```python
client = AndroidAutomation(
    base_url="https://localhost:8000",
    verify=False,
)
```

### 自定义证书

```python
import httpx
from android_automation import AndroidAutomation

http_client = httpx.Client(verify="/path/to/cert.pem")

client = AndroidAutomation(
    base_url="https://localhost:8000",
    http_client=http_client,
)
```

---

## 重试配置

```python
import httpx
from android_automation import AndroidAutomation
from urllib3.util.retry import Retry
from httpx import Limits

# 配置重试策略
retry_strategy = Retry(
    total=3,
    backoff_factor=0.5,
    status_forcelist=[500, 502, 503, 504],
)

http_client = httpx.Client(
    timeout=30.0,
    retry_strategy=retry_strategy,
)

client = AndroidAutomation(
    base_url="http://localhost:8000",
    http_client=http_client,
)
```

---

## 最佳实践

### 生产环境配置

```python
import os
import json
import logging
from android_automation import AndroidAutomation

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 从环境变量加载配置
config = {
    "base_url": os.getenv("ANDROID_API_URL", "http://localhost:8000"),
    "timeout": float(os.getenv("ANDROID_API_TIMEOUT", "30.0")),
    "verify": os.getenv("ANDROID_API_VERIFY", "True").lower() == "true",
}

try:
    client = AndroidAutomation(**config)
    logger.info("客户端创建成功")

    # 连接设备
    device_info = client.device.connect()
    logger.info(f"设备已连接: {device_info.serial}")

except Exception as e:
    logger.error(f"错误: {e}")
finally:
    try:
        client.device.disconnect()
    except:
        pass
```

### 开发环境配置

```python
from android_automation import AndroidAutomation

# 开发环境使用更长的超时和调试模式
client = AndroidAutomation(
    base_url="http://localhost:8000",
    timeout=120.0,  # 2分钟超时
    verify=False,   # 禁用 SSL 验证（开发环境）
)

# 启用详细日志
import httpx
import logging

httpx_logger = logging.getLogger("httpx")
httpx_logger.setLevel(logging.DEBUG)
```

---

## 故障排除

### 连接超时

```python
# 增加超时时间
client = AndroidAutomation(
    base_url="http://localhost:8000",
    timeout=120.0,
)
```

### SSL 证书错误

```python
# 禁用 SSL 验证（仅限开发环境）
client = AndroidAutomation(
    base_url="https://localhost:8000",
    verify=False,
)

# 或提供正确的证书路径
client = AndroidAutomation(
    base_url="https://localhost:8000",
    verify="/path/to/cert.pem",
)
```

### 代理问题

```python
# 不使用代理
import os
os.environ.pop("HTTP_PROXY", None)
os.environ.pop("HTTPS_PROXY", None)

client = AndroidAutomation(base_url="http://localhost:8000")
```
