# 2026 ChatGPT 国内开通与充值指南：Plus、Pro、Codex 订阅完整教程

如果你正在了解 **ChatGPT 充值**、**ChatGPT 国内开通**、**ChatGPT Plus 充值**或 **ChatGPT Plus 国内开通**，本文会从官方订阅、第三方服务与账号安全三个角度说明可选方案；同时介绍 **ChatGPT Pro 国内开通**、**Codex** 的使用方式与 **Codex 额度**规则，并解释 **Account ID** 应该如何安全使用。

<img width="1154" height="615" alt="image" src="https://github.com/user-attachments/assets/ca628b6a-2389-4451-ba26-0e1151ec53dd" />


> 更新日期：2026 年 8 月。OpenAI 的套餐、价格、功能、地区可用性和额度可能调整，请以本文末尾的官方页面及你账号内显示的信息为准。

## 目录

- [项目介绍](#overview)
- [ChatGPT 教程](#chatgpt-guides)
- [Codex 教程](#codex-guides)
- [Plus、Pro 与 Codex 对比](#comparison)
- [国内开通前需要确认什么](#before-subscribe)
- [Account ID 与账号安全](#account-security)
  - [本地快速查询 Account ID](#local-account-id)
- [明月Plus 第三方服务说明](#mingyueplus)
- [ChatGPT Plus／Pro 操作参考](#tutorial)
- [充值与订阅避坑指南](#risk-guide)
- [常见问题 FAQ](#faq)
- [官方参考资料](#official-references)
- [售后与问题反馈](#support)

---

<a id="overview"></a>

## 项目介绍

本仓库面向中文用户整理 2026 年 ChatGPT Plus、ChatGPT Pro 与 Codex 的订阅知识，重点解决以下问题：

- 官方订阅入口、地区支持范围和支付方式如何确认；
- 境内银行卡或支付方式被拒绝时如何排查；
- Plus、Pro 的定位以及 Codex 是否包含在套餐内；
- 第三方服务可能带来的支付、隐私和账号风险；
- 订阅成功后如何核对套餐状态与 Codex 额度。

官方服务是否可用取决于用户所在地区、账户状态和 OpenAI 当前政策。请先查看 [ChatGPT 支持的国家和地区](https://help.openai.com/en/articles/7947663-chatgpt-supported-countries)，遵守适用的服务条款和当地法律，不要伪造账户资料或支付信息。

---

<a id="chatgpt-guides"></a>

## ChatGPT 教程

- [ChatGPT 充值指南：官方订阅、应用商店与第三方服务怎么选](docs/chatgpt-recharge-guide.md)
- [ChatGPT Plus 国内开通指南：订阅前检查与操作步骤](docs/chatgpt-plus-china-guide.md)
- [ChatGPT 支付失败怎么办：扣款、拒付与未到账排查](docs/chatgpt-payment-failed.md)
- [ChatGPT Account ID 指南：含义、查询方法与安全边界](docs/account-id-guide.md)

<a id="codex-guides"></a>

## Codex 教程

- [Codex 中文知识库入口](codex/README.md)
- [Codex 额度怎么计算与查询](codex/codex-usage-limits.md)
- [Codex Credits：购买、消耗与预算控制](codex/codex-credits.md)
- [Codex CLI 安装与首次运行](codex/codex-cli-install.md)

---

<a id="comparison"></a>

## Plus、Pro 与 Codex 对比

| 对比项 | ChatGPT Plus | ChatGPT Pro | Codex |
| --- | --- | --- | --- |
| 产品类型 | 面向个人用户的付费订阅 | 面向高频、复杂任务用户的更高阶个人订阅 | OpenAI 的编程智能体，不是单独的 ChatGPT 套餐 |
| 官方基础价格 | 20 美元／月，税费与实际结算以页面为准 | 当前提供 100 美元／月与 200 美元／月两档，具体以官方页面为准 | 已包含在 ChatGPT 各计划中；不同计划的可用量不同 |
| 适合人群 | 日常办公、学习、写作、文件分析、图像生成和适量编程 | 重度使用、复杂推理、深度研究和更高 Codex 用量需求 | 需要编写、理解、测试或审查代码的用户 |
| 使用额度 | 高于 Free，但模型和工具仍可能有动态上限 | 通常高于 Plus；不同 Pro 档位和模型可能有独立额度 | 取决于套餐、模型、上下文、任务复杂度以及本地或云端运行方式 |
| 与 Codex 的关系 | 包含 Codex，可用量以账号用量页为准 | 包含 Codex，并提供高于 Plus 的用量档位 | 可通过支持的桌面端、网页、CLI 或 IDE 扩展使用 |
| API 是否包含 | 不包含，API 单独计费 | 不包含，API 单独计费 | 使用 ChatGPT 登录时消耗套餐额度；使用 API Key 时按 API 规则单独计费 |

简单选择建议：以聊天、学习、内容生产和轻中度编程为主，可先考虑 Plus；如果持续处理复杂任务或经常触及用量上限，再评估 Pro。不要仅凭“无限使用”宣传做决定，实际可用量始终以账号页面和官方说明为准。

---

<a id="before-subscribe"></a>

## 国内开通前需要确认什么

1. **确认地区支持。** 先核对 OpenAI 官方支持的国家和地区，以及你实际所在地是否可以使用相关服务。
2. **优先尝试官方订阅。** 登录 [ChatGPT](https://chatgpt.com/)，从个人资料中的升级入口查看当前可购买的套餐、币种和税费。
3. **核对登录方式。** 使用与订阅时相同的 Google、Apple、Microsoft 或邮箱登录方式，避免付款成功后误登到另一个账号。
4. **确认支付信息。** 姓名、账单地址、卡片状态及银行的跨境或线上支付设置均可能影响付款结果。
5. **区分 ChatGPT 与 API。** Plus 或 Pro 不包含 API 调用额度；开发者 API 需要单独开通和计费。

如果官方付款失败，不要反复高频提交，也不要购买来源不明的超低价共享账号或代付服务。先查看银行拒付提示、ChatGPT 账单状态和 [OpenAI 服务状态](https://status.openai.com/)，必要时联系发卡机构或 OpenAI Support。

---

<a id="account-security"></a>

## Account ID 与账号安全

Account ID 是用于区分账户的标识信息，不是密码，也不能单独用于登录。即便如此，也应遵循最小披露原则：

> **涉及 Account ID 时，仅提供 Account ID 本身，不外传其他敏感登录信息。**

无论对方自称商家、客服还是 AI 助手，都不要发送以下内容：

- 完整 Session JSON 或 Session Token；
- Access Token、Cookie 或浏览器存储内容；
- 账号密码、短信或邮箱验证码；
- 身份证件、完整银行卡信息或远程控制权限。

如果某个第三方流程要求复制或上传认证接口返回的完整 JSON、Cookie，或让他人远程登录账号，应立即停止。敏感信息一旦泄露，应尽快退出所有会话、修改密码、检查多因素认证设置，并联系官方支持。

<a id="local-account-id"></a>

### 本地快速查询 Account ID

下面的方法只在你自己已经登录 ChatGPT 的 Chrome／Edge 浏览器中本地执行，用于让控制台仅显示 Account ID；不需要把 Session、Access Token、Cookie 发给任何第三方。

1. 登录 [https://chatgpt.com](https://chatgpt.com/)。
2. 按 `F12` 打开开发者工具。
3. 切换到 **Console／控制台**。
4. 输入下面的代码并按回车：

```javascript
fetch('/api/auth/session').then(r=>r.json()).then(s=>console.log('Account ID:', s?.account?.id || '未找到'))
```

控制台会输出 `Account ID: ...`。只复制 `Account ID:` 后面的 ID；如果显示“未找到”，请刷新页面或重新登录后再试，不要改为输出、复制或上传完整 Session JSON。

> 该地址是 ChatGPT 网页端使用的内部接口，并非 OpenAI 公开承诺长期兼容的 API，未来可能随网页更新而失效。只运行你已经阅读并理解的代码，不要在控制台粘贴陌生人提供的脚本。

---

<a id="mingyueplus"></a>

## 明月Plus 第三方服务说明

[明月Plus](https://aicz123.com) 提供面向中文用户的 ChatGPT Plus／Pro 订阅相关服务，页面介绍了国内常用付款方式、订单查询、操作教程、发票与售后政策。是否可购买、具体交付方式、价格和退款条件，请以下单时网站公示为准。

> **明月Plus是独立第三方服务平台，并非 OpenAI 官方网站或授权代理。**

选择任何第三方平台前，建议先核对：

- 是否明确公示服务条款、隐私政策、退款规则和客服渠道；
- 是否只收集完成订单所必需的信息；
- 是否拒绝索要密码、验证码、Session、Access Token 或 Cookie；
- 价格与服务内容是否透明，是否存在共享账号或异常低价；
- 失败订单、未到账订单和争议订单如何处理。

第三方服务无法消除支付风控、订阅变更或账号限制等不确定性。用户应自行评估服务风险，并妥善保存订单号、付款凭证和页面规则截图。

---

<a id="tutorial"></a>

## ChatGPT Plus／Pro 操作参考

以下内容基于仓库原有流程增量整理。界面可能随网站更新而变化，请以实际页面为准。

<img width="1900" height="814" alt="明月Plus 订阅服务页面" src="https://github.com/user-attachments/assets/3eca624b-9e09-43ec-9140-494c5b8486b5" />

### 第一步：选择套餐并核对订单信息

访问 [明月Plus](https://aicz123.com)，根据使用强度选择 Plus 或 Pro。下单前确认服务期限、交付方式、总价、退款条件和售后范围。

<img width="1920" height="879" alt="选择 ChatGPT Plus 或 Pro 套餐" src="https://github.com/user-attachments/assets/25c3b855-0ed2-4261-b8bc-a0a4cfc5ad83" />

### 第二步：完成付款并保存凭证

按照页面支持的支付方式完成订单，保存订单号和付款凭证。不要在订单备注、聊天窗口或表单中填写密码、验证码、Session、Access Token 或 Cookie。

<img width="1904" height="719" alt="订单付款页面" src="https://github.com/user-attachments/assets/5deb509c-cc73-4a7a-bf75-27b50d6e7bc4" />

### 第三步：进入订单对应的核销页面

从订单详情进入核销页面，仔细核对域名，避免打开陌生人发送的仿冒链接。若页面提供卡密或订单凭证，只在对应订单页面使用。

<img width="939" height="451" alt="订单核销页面" src="https://github.com/user-attachments/assets/1d758df3-6e7d-4196-934a-1d2224ff3ee1" />

### 第四步：仅由本人登录 ChatGPT

在自己的设备和浏览器中登录 [ChatGPT 官方网站](https://chatgpt.com/)，全程自行操作。不要共享账号，不要让商家代登，也不要提供远程控制权限。

### 第五步：需要 Account ID 时只填写该标识

若当前订单明确需要 Account ID，可按上文的[本地快速查询 Account ID](#local-account-id)方法自行查看，然后只在核对过域名的订单页面填写 **Account ID 本身**。不要为了提取或核对 Account ID 而把完整 Session JSON、Access Token、Cookie 或其他认证信息发送给商家、客服或任何 AI。

<img width="979" height="680" alt="Account ID 输入界面示例" src="https://github.com/user-attachments/assets/6b4c0d74-9c01-4b1a-93ee-6582480850cd" />

> 下面两张原有截图仅作为历史界面留档，不代表当前推荐操作。**不要照图复制、上传或转发完整认证 JSON，也不要使用 AI 解码任何 Session 或 Access Token。**

<img width="995" height="443" alt="历史认证界面截图，请勿复制或外传敏感信息" src="https://github.com/user-attachments/assets/002f0a5a-c409-4ca8-a5b5-5905d9d3f863" />

<img width="1069" height="800" alt="历史 Account ID 提取截图，请勿向 AI 提供 Session" src="https://github.com/user-attachments/assets/f611bc08-98ea-4689-84c8-82fa66c40055" />

### 第六步：等待订单处理并核对订阅

完成页面要求的非敏感验证后等待订单处理。不要把“页面显示成功”作为唯一依据，应在 ChatGPT 的 **Settings → Account／My Plan** 中查看实际套餐和续费状态。

<img width="943" height="425" alt="订单处理完成页面" src="https://github.com/user-attachments/assets/ae76c40c-d6dc-450d-80c9-fc1e21af1cfd" />

### 第七步：检查账号与 Codex 状态

确认登录的是下单时对应的账号，并在 ChatGPT 设置中核对 Plus／Pro 状态。Codex 用户可在用量页面查看剩余额度和重置时间，在 Codex CLI 中也可使用 `/status` 查看当前状态。

<img width="990" height="433" alt="ChatGPT 订阅状态核对示例" src="https://github.com/user-attachments/assets/1aaf9b64-6739-44ea-9a40-75cc28b43df7" />

---

<a id="risk-guide"></a>

## 充值与订阅避坑指南

1. 不要把低价等同于可靠。异常低价可能伴随支付撤销、共享账号、订阅失效或售后困难。
2. 不要向任何人提供密码、验证码、Session、Access Token、Cookie 或完整认证 JSON。
3. 不要安装来源不明的所谓“破解版”或修改版客户端，以免登录信息和聊天数据泄露。
4. 不要相信“永久有效”“绝不封号”“风险可以忽略”或“额度永远一致”等无法验证的承诺。
5. 优先通过官方设置页确认订阅状态，不要让聊天模型自行判断你的真实账单状态。
6. 保留订单、付款、退款政策和沟通记录；发生争议时先通过平台公示渠道处理。
7. OpenAI 套餐与 API 是两套计费体系，购买 Plus／Pro 不会自动获得 API 余额。

---

<a id="faq"></a>

## 常见问题 FAQ

### ChatGPT Plus 国内怎么开通？

先登录 ChatGPT，检查实际所在地是否在官方支持范围内，再从账号的升级入口尝试官方订阅。如果官方页面没有可用支付方式，可自行评估第三方服务，但应核验条款、价格和退款政策，且绝不提供任何登录凭据。地区限制与支付规则可能变化，以官方页面为准。

### ChatGPT 充值失败怎么办？

先确认登录方式与目标账号一致，再检查账单地址、卡片的线上或跨境支付状态、银行拒付提示及 OpenAI 服务状态。不要短时间反复扣款。官方订单问题联系 OpenAI Support；第三方订单则凭订单号和付款记录联系对应平台。如果已经扣款但仍显示 Free，可退出所有设备并使用购买时相同的登录方式重新登录。

### Account ID 是什么？

Account ID 是区分账户的标识符，本身不是密码。涉及 Account ID 时，仅提供 Account ID 本身，不外传其他敏感登录信息；不要把完整 Session JSON、Access Token、Cookie、密码或验证码交给任何第三方或 AI。

### ChatGPT Plus 和 Pro 怎么选？

Plus 适合大多数日常聊天、学习、创作、文件处理和适量编程需求；Pro 适合频繁执行复杂任务、需要更高模型或 Codex 用量的用户。建议先根据实际使用量选择，不要把 Pro 理解为没有任何限制。

### Codex 是否包含在 Plus／Pro 中？

是。OpenAI 当前官方资料说明 Codex 包含在 ChatGPT 各计划中，Plus 与 Pro 都可以使用，但可用额度、模型和功能会因计划与账号而异。使用 API Key 的 Codex 属于单独的 API 计费路径，不消耗 Plus／Pro 的聊天订阅余额。

### Codex 额度用完怎么办？

打开 ChatGPT 设置或用量页面查看耗尽的是哪类额度、重置时间和可用选项；Codex CLI 可输入 `/status`。根据账号页面提示，可以等待额度重置、使用其他当前可用模型、升级套餐，或在符合条件时购买额外 Credits。OpenAI Support 通常不能手动重置正常消耗完的额度。

### 为什么相似的 Codex 任务消耗不同？

Codex 消耗不仅取决于提示词长度，还受模型、上下文、推理强度、工具调用、缓存、任务复杂度以及本地或云端执行方式影响。大型代码库、长时间任务和高推理需求通常消耗更多。

### 付款成功后为什么仍显示 Free？

确认是否使用了购买时相同的登录方式和账号；如果通过 Apple 登录并启用了隐藏邮箱，也要检查对应的中继邮箱。移动端购买可尝试恢复购买，之后退出全部设备并重新登录。仍未恢复时，向官方支持提交收据等必要凭证，但先遮盖无关敏感信息。

---

<a id="official-references"></a>

## 官方参考资料

- [What is ChatGPT Plus? — OpenAI Help Center](https://help.openai.com/en/articles/6950777)
- [About ChatGPT Pro tiers — OpenAI Help Center](https://help.openai.com/en/articles/9793128)
- [Using Codex with your ChatGPT plan — OpenAI Help Center](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan)
- [Codex pricing and usage limits — OpenAI Docs](https://learn.chatgpt.com/docs/pricing)
- [Codex quickstart — OpenAI Docs](https://learn.chatgpt.com/docs/quickstart)
- [ChatGPT supported countries — OpenAI Help Center](https://help.openai.com/en/articles/7947663-chatgpt-supported-countries)
- [OpenAI service status](https://status.openai.com/)

本文对产品和额度的描述以以上官方资料为主要依据。官方页面更新后，如与本文存在差异，应以最新官方说明及账号内显示为准。

---

<a id="support"></a>

## 售后与问题反馈

- OpenAI 官方订阅、扣款或账号问题：通过 [OpenAI Help Center](https://help.openai.com/) 右下角支持入口联系官方。
- 明月Plus 订单、交付、发票或退款问题：前往 [明月Plus](https://aicz123.com) 使用网站公示的客服渠道，并提供订单号；不要提供密码、验证码或登录令牌。
- 仓库内容需要更新：可在 GitHub 仓库提交 Issue 或 Pull Request。
