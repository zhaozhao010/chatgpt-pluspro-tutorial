# 实用工具

## Account ID 油猴脚本

[`get-account-id.user.js`](get-account-id.user.js) 在用户已登录的 ChatGPT 页面提供手动查询菜单。

1. 在 Chrome 或 Edge 安装并启用 Tampermonkey，按扩展提示开启运行用户脚本所需的浏览器权限。
2. 打开 [脚本源码](https://raw.githubusercontent.com/zhaozhao010/chatgpt-pluspro-tutorial/main/tools/get-account-id.user.js)，阅读后安装。如果没有出现安装页，可在 Tampermonkey 中新建脚本，替换默认内容并保存。
3. 登录 `https://chatgpt.com`，刷新页面，在 Tampermonkey 菜单中选择“查询 Account ID（本地）”。
4. 在弹窗中手动复制 Account ID。点击取消即可关闭弹窗。

脚本只在点击菜单后向 ChatGPT 自己的认证接口发起请求，由浏览器携带当前登录状态。它只显示返回数据中的 `account.id`，不输出完整 Session、不写入存储或剪贴板、不向第三方发送数据。请勿向任何人提供完整 Session、Access Token、Cookie、密码或验证码。

该认证接口属于网页内部实现，字段可能随更新改变。若提示“未找到”，请先确认登录状态；持续失败时停止使用，勿改成输出完整认证数据。Account ID 与账号或工作区标识的关系以当前接口实现为准。

## HTTP 连通性检查

`check_connection.py` 使用 Python 标准库检查公开网页的 HTTP 状态和响应头等待时间。适合在浏览器加载失败时辅助判断是否能收到服务器响应。

## 使用

需要 Python 3.8 或更高版本，无需安装第三方依赖。在仓库根目录运行

```shell
python tools/check_connection.py https://status.openai.com/ --timeout 10
python tools/check_connection.py https://chatgpt.com/ --timeout 15
```

Windows 也可使用 `py -3` 代替 `python`。

## 如何读结果

| 结果 | 含义 |
| --- | --- |
| HTTP 2xx | 请求成功，收到响应头 |
| HTTP 401 / 403 | 收到了 HTTP 响应，可能需要认证或被访问控制拦截 |
| HTTP 429 / 5xx | 服务返回限流或服务器错误，可稍后核对服务状态 |
| Network request failed | DNS、连接、TLS 或超时等网络问题，输出错误类型供排查 |

脚本发送一次 GET 请求并遵循重定向，不读取响应正文、不保存报告。正常请求返回退出码 0，网络错误或 HTTP 4xx/5xx 返回 1，参数错误返回 2。超时参数控制网络阻塞操作，重定向可能使总耗时超过该数值。

脚本沿用 Python 检测到的系统或环境代理，执行 TLS 证书验证。请使用公开网址，勿传入密码、验证码、Session、Access Token 或 Cookie。带用户名、密码、查询参数或片段的 URL 会被拒绝。

HTTP 成功只能说明该网址在当前网络环境下回应了请求，不能证明账号可订阅、付款可通过或带认证的 API 可调用。代理也可能返回自身的错误页面，应结合浏览器与网络配置判断。
