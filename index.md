---
layout: default
title: "2026 国内 ChatGPT充值与ChatGPT代充指南：微信/支付宝开通 Plus、Pro"
description: "面向国内用户的 ChatGPT充值与ChatGPT代充实测教程，介绍小羊Plus微信支付宝开通、官网订阅、付款排查、Account ID 与账号安全。"
permalink: /
readme_home: true
date_modified: "2026-10-30"
---

{% capture readme_content %}{% include_relative README.md %}{% endcapture %}

{% assign codex_index_url = '/codex/' | relative_url %}
{% assign limits_url = '/codex/codex-usage-limits.html' | relative_url %}
{% assign credits_url = '/codex/codex-credits.html' | relative_url %}
{% assign cli_url = '/codex/codex-cli-install.html' | relative_url %}

{% capture codex_index_target %}({{ codex_index_url }}){% endcapture %}
{% capture limits_target %}({{ limits_url }}){% endcapture %}
{% capture credits_target %}({{ credits_url }}){% endcapture %}
{% capture cli_target %}({{ cli_url }}){% endcapture %}

{% assign readme_content = readme_content | replace: '(codex/README.md)', codex_index_target %}
{% assign readme_content = readme_content | replace: '(codex/codex-usage-limits.md)', limits_target %}
{% assign readme_content = readme_content | replace: '(codex/codex-credits.md)', credits_target %}
{% assign readme_content = readme_content | replace: '(codex/codex-cli-install.md)', cli_target %}

{{ readme_content | markdownify }}
