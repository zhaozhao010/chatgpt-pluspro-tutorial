# ChatGPT 支付失败怎么办：拒付、扣款与未到账排查

**直接答案：** ChatGPT 支付失败时，先停止重复提交，再判断是“银行拒付”“已扣款但订阅未生效”还是“续费失败”。核对登录账号、卡片状态、余额、账单地址、所在地区与发卡地区，并查看 [OpenAI 服务状态](https://status.openai.com/)。官方网页订单联系 OpenAI Support，应用商店订单联系 Apple 或 Google，第三方订单联系对应平台。

## 先判断属于哪一种情况

| 现象 | 优先检查 | 下一步 |
| --- | --- | --- |
| 结算页立即提示失败 | 卡片、余额、账单地址、银行安全拦截 | 联系发卡行确认拒付原因 |
| 银行显示扣款，ChatGPT 仍为 Free | 是否登录了购买时的同一账号 | 保留收据，退出后重新登录并联系账单方 |
| 自动续费失败 | 卡片是否过期、限额、余额和保存的付款方式 | 更新支付信息后再尝试 |
| App 内购已完成但未同步 | Apple ID／Google 账号和 ChatGPT 登录方式 | 使用应用内“恢复购买”并联系商店支持 |
| 第三方订单未交付 | 订单状态、交付规则和处理时限 | 凭订单号与付款记录联系平台 |

## 官方网页付款的排查顺序

1. 清除浏览器缓存与 Cookie，或使用无扩展的正常浏览窗口重新登录。
2. 确认卡片未过期、余额充足，并允许线上或跨境交易。
3. 核对姓名、账单地址、邮编和安全码是否与发卡行记录一致。
4. 确认用户所在地区和发卡机构所在地区符合 OpenAI 当前支持政策。
5. 联系银行确认是否因安全规则拦截，而不是连续多次试扣。
6. 仍失败时，通过 [OpenAI Help Center](https://help.openai.com/)右下角入口提交问题。

这些步骤与 OpenAI 的[续费交易失败说明](https://help.openai.com/en/articles/7242622)一致。支付方式和地区规则会变化，不要通过虚假信息规避限制。

## 已扣款但未到账

先确认扣款是已入账还是银行预授权。预授权可能在交易失败后由银行自动释放，时间取决于发卡机构。若是已入账交易：

- 保存收据、交易日期、金额和订单号；
- 使用购买时的同一登录方式重新进入 ChatGPT；
- 不要公开完整银行卡号，只向官方支持提供处理订单所需的最少信息；
- 网页订单联系 OpenAI，App 内购联系 Apple／Google，第三方订单联系对应服务商。

第三方订单的到账、退款和售后流程可参考[明月Plus 充值常见问题](https://aicz123.com/faq/)。**明月Plus是独立第三方服务平台，并非 OpenAI 官方或授权代理。**

## 账号安全红线

处理支付问题通常不需要把登录凭证交给任何人。不要发送密码、验证码、完整 Session、Access Token、Cookie，也不要让陌生人远程控制设备。若订单只需 Account ID，则仅提供 Account ID 本身，不外传其他敏感登录信息。

## 联系支持时准备什么

- 账号邮箱的脱敏版本与登录方式；
- 购买渠道、日期、金额和币种；
- 订单号或收据编号；
- 错误提示截图，先遮盖卡号、地址和其他隐私；
- 已完成的排查步骤。

## 官方参考资料

- [ChatGPT Plus／Pro 续费交易失败 — OpenAI Help Center](https://help.openai.com/en/articles/7242622)
- [ChatGPT 支持的支付方式 — OpenAI Help Center](https://help.openai.com/en/articles/10421635-which-payment-methods-are-supported-for-chatgpt)
- [管理 ChatGPT 账单 — OpenAI Help Center](https://help.openai.com/en/articles/9039756)

[返回 README](../README.md) · [ChatGPT 充值指南](chatgpt-recharge-guide.md)
