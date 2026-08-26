# Codex Credits 指南：额度用完后的购买、消耗与预算控制

**直接答案：** Codex Credits 是套餐包含用量之外的弹性付费机制。对符合条件的 ChatGPT Plus／Pro 账号，系统会先使用套餐包含的 Codex 用量；达到相应限额后，支持的功能才从已购买 Credits 中继续扣除。是否能购买、单次消耗和可用功能以个人 Usage Dashboard 为准。

## Credits、套餐额度和 API 余额不是一回事

| 项目 | 用在哪里 | 如何计费 |
| --- | --- | --- |
| ChatGPT 套餐包含用量 | 使用 ChatGPT 账号登录的 Codex 等受支持功能 | 包含在订阅中，受动态限额约束 |
| Codex Credits | 套餐用量耗尽后的受支持功能 | 额外购买并按实际使用扣除 |
| OpenAI API 余额 | 使用 API Key 的本地或程序化调用 | 按 API 平台价格与账单规则独立计费 |

购买 Credits 不会改变当前 Plus／Pro 套餐，也不会增加 API 余额。反过来，已有 API 余额通常也不会显示为 ChatGPT 的 Credits。

## 怎么购买和查看

1. 打开 Codex 的 **Settings → Usage**。
2. 查看账号是否出现 Credits 或 Add credits 入口。
3. 购买前确认价格、余额有效期、退款规则和支持的功能。
4. 购买后在同一 Usage Dashboard 查看余额与近期消耗。
5. CLI 中可用 `/status` 查看当前会话的相关使用状态。

Credits 功能可能按账号、地区和方案逐步提供。如果页面没有购买入口，不应通过陌生链接或代购凭证绕过官方界面。

## 为什么同一条消息扣除不同

Credits 是对底层使用成本的简化表示，不等于“一条消息一个 Credit”。模型、输入与输出规模、缓存、推理强度、工具调用、检索和任务持续时间都会影响消耗。分析整个大型仓库通常比修改一个明确的小文件更贵。

费率和可用模型可能更新，不建议把某个历史 Credit 数字写进长期预算。需要精确估算时，先用一个代表性小任务测试，再在 Usage Dashboard 核对真实扣除。

## Auto top-up 怎么控制风险

部分符合条件的账号可启用自动充值。开启前应确认：

- 触发自动充值的最低余额；
- 补充后的目标余额；
- 每月最大自动支出；
- 默认付款方式和账单通知；
- 多个受支持功能是否共享同一 Credit 余额。

建议先使用较低预算观察一段时间。自动任务、并发任务或失控重试都可能持续消耗 Credits，因此应给自动化设置停止条件，并定期查看 Usage Dashboard。

## 额度用完时怎么选

- **偶尔触顶：** 等待重置，或临时购买少量 Credits；
- **任务可降级：** 切换能胜任的低消耗模型并缩小上下文；
- **每周频繁触顶：** 比较更高套餐与实际 Credit 支出的总成本；
- **程序化、本地 API 工作流：** 单独评估 API 账单，不要把它与订阅 Credits 混算。

[Codex 额度用完、Credits 与自动充值教程](https://aicz123.com/blog/article-1787668668219/)可作为中文延伸阅读。**明月Plus是独立第三方服务平台，并非 OpenAI 官方或授权代理。**

## 安全提醒

购买或排查 Credits 不需要向任何人发送密码、验证码、Session、Access Token 或 Cookie。只通过账号内的官方用量与账单入口操作；与支持团队沟通时也只提供解决订单所需的最少信息。

## 官方参考资料

- [Using credits for flexible usage — OpenAI Help Center](https://help.openai.com/en/articles/12642688)
- [Codex 定价与使用量 — OpenAI Docs](https://learn.chatgpt.com/docs/pricing)
- [在 ChatGPT 套餐中使用 Codex — OpenAI Help Center](https://help.openai.com/en/articles/11369540)

[返回 Codex 知识库](README.md) · [Codex 额度指南](codex-usage-limits.md)
