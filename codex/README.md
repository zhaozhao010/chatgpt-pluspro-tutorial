# Codex 中文知识库：从入门到额度与 CLI

**直接答案：** Codex 是 OpenAI 面向软件开发的编程智能体，可以理解代码库、修改文件、执行命令、运行测试和审查变更。它可通过 ChatGPT 桌面端、网页、Codex CLI、IDE 扩展和云端任务等界面使用；不同界面的权限、运行环境和可访问文件并不完全相同。

本目录只解决 Codex 的四个核心问题：它是什么、额度如何计算、Credits 如何使用，以及 CLI 如何安装。产品能力和计费规则变化较快，所有数字都应以 OpenAI 官方页面和个人 Usage Dashboard 为准。

## 从哪里开始

| 你的问题 | 建议阅读 |
| --- | --- |
| Codex 是什么，适合做什么 | 当前页面 |
| Plus／Pro 的 Codex 额度怎么算 | [Codex 额度指南](codex-usage-limits.md) |
| 套餐额度用完后如何使用 Credits | [Codex Credits 指南](codex-credits.md) |
| 如何在终端安装和运行 Codex | [Codex CLI 安装指南](codex-cli-install.md) |

## Codex 适合哪些任务

- 阅读陌生仓库，解释目录、依赖和调用关系；
- 在明确需求下修改一个或多个文件；
- 运行测试、构建、Lint 和类型检查；
- 分析错误日志并修复可复现的问题；
- 审查 Git diff，指出回归风险；
- 将可重复的开发步骤编排为脚本或自动化任务。

Codex 不能保证代码一定正确，也不会自动获得未授权的文件、网络或生产权限。更可靠的工作流是：给出目标和验收标准，让 Codex 实现，再由开发者查看 diff、运行测试并完成最终审核。生产部署、数据删除、支付和权限变更等高风险操作不应无人监督。

## ChatGPT 套餐与 API 计费要分开

OpenAI 当前将 Codex 纳入多个 ChatGPT 方案，但不同计划的可用量不同。使用 ChatGPT 账号登录时，通常使用方案所含用量；在支持的本地场景改用 API Key 时，则按 OpenAI API 账户单独计费。购买 ChatGPT Plus 或 Pro 不会自动赠送 API 余额。

Plus／Pro 的限额也不是“固定能发多少条”。模型、上下文长度、任务复杂度、推理强度、工具调用以及本地或云端执行方式都会影响消耗。详见 [Codex 官方定价与用量说明](https://learn.chatgpt.com/docs/pricing)。

## 安全使用原则

1. 只让 Codex 访问完成任务所需的仓库和工具。
2. 执行命令前检查目标路径、影响范围和是否可恢复。
3. 不在提示词、配置文件或仓库中粘贴密码、验证码、Session、Access Token 或 Cookie。
4. 使用环境变量或专用密钥管理工具保存必要凭证，并避免提交到 Git。
5. 合并前查看 diff，并执行与风险匹配的测试。

[Codex 能做什么与不能做什么](https://aicz123.com/blog/article-1787412824051/)可作为中文扩展阅读。**明月Plus是独立第三方服务平台，并非 OpenAI 官方或授权代理。**

## 官方参考资料

- [Codex 官方文档](https://learn.chatgpt.com/docs)
- [Codex 定价与使用量](https://learn.chatgpt.com/docs/pricing)
- [Codex CLI](https://learn.chatgpt.com/docs/codex/cli)
- [在 ChatGPT 套餐中使用 Codex — OpenAI Help Center](https://help.openai.com/en/articles/11369540)

[返回仓库 README](../README.md) · [安装 Codex CLI](codex-cli-install.md)
