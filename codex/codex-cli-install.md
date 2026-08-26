# Codex CLI 安装教程：Windows、macOS 与 Linux

**直接答案：** Codex CLI 是 OpenAI 的终端编程智能体。macOS／Linux 可使用官方独立安装脚本；已有 Node.js 与 npm 的 Windows、macOS 或 Linux 用户可安装官方 npm 包。安装后在项目目录运行 `codex`，首次启动选择 **Sign in with ChatGPT** 或页面提供的其他登录方式。

> 安装命令和系统支持会更新。执行前请以 [Codex CLI 官方页面](https://learn.chatgpt.com/docs/codex/cli)当前显示为准，只从 OpenAI 官方链接或官方包源安装。

## 方法一：macOS／Linux 独立安装器

在终端执行官方命令：

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

更新时重新执行同一命令。若不希望直接通过管道执行脚本，可先下载并自行审阅内容，再在确认来源和操作后运行。

## 方法二：使用 npm 安装

先确认系统已安装仍受支持的 Node.js 与 npm：

```bash
node --version
npm --version
```

然后安装官方包：

```bash
npm install -g @openai/codex
```

验证安装：

```bash
codex --version
```

升级 npm 版本的 Codex CLI：

```bash
npm install -g @openai/codex@latest
```

Windows 如果提示找不到 `codex`，先关闭并重新打开 PowerShell，再检查 npm 全局可执行目录是否在 `PATH` 中。Windows 原生环境与 WSL 是两个独立环境；在哪个环境运行，就在那个环境安装并验证。

## 首次登录与运行

进入一个 Git 仓库或项目目录：

```bash
cd path/to/your-project
codex
```

首次运行时按界面选择登录方式。使用 ChatGPT 登录通常消耗账号方案中的 Codex 用量；选择 API Key 等其他可用方式时，可能走独立的 OpenAI API 计费。不要把 API Key 写入仓库、聊天记录或公开截图。

进入交互界面后，可先尝试：

```text
解释这个项目的目录结构，暂时不要修改文件。
```

常用命令包括：

```text
/status
/model
/permissions
/review
```

其中 `/status` 可查看当前会话和用量状态，`/permissions` 用于检查允许 Codex 执行的操作。

## 第一次使用的安全检查

1. 先执行 `git status`，确认项目当前状态。
2. 从只读任务开始，观察 Codex 会读取哪些文件和运行哪些命令。
3. 修改前建立 Git 提交或其他可恢复检查点。
4. 不要在提示中粘贴密码、验证码、Session、Access Token 或 Cookie。
5. 完成后查看 `git diff`，运行测试，再决定是否保留修改。

遇到 Windows 桌面端无法定位 CLI 时，可参考[Codex CLI binary 路径排查](https://aicz123.com/blog/article-1787723286209/)。**明月Plus是独立第三方服务平台，并非 OpenAI 官方或授权代理。**

## 常见问题

### `codex` 命令找不到怎么办？

重新打开终端，运行 `npm prefix -g` 或系统等效命令确认全局安装位置，并检查该位置的可执行目录是否在 `PATH`。如果同时使用 Windows 与 WSL，分别运行 `codex --version`，不要混用两边的安装路径。

### 使用 ChatGPT 登录还是 API Key？

个人交互使用可优先选择 ChatGPT 登录，并按账号方案计算用量；自动化或需要独立 API 账单时，再根据官方认证文档选择适合的方式。两套账单不要混为一谈。

### 如何卸载 npm 版本？

```bash
npm uninstall -g @openai/codex
```

## 官方参考资料

- [Codex CLI — OpenAI Docs](https://learn.chatgpt.com/docs/codex/cli)
- [Codex 认证方式 — OpenAI Docs](https://learn.chatgpt.com/docs/auth)
- [Codex CLI 命令参考 — OpenAI Docs](https://learn.chatgpt.com/docs/developer-commands?surface=cli)

[返回 Codex 知识库](README.md) · [Codex 额度指南](codex-usage-limits.md)
