// ==UserScript==
// @name         ChatGPT Account ID 本地查询
// @namespace    https://github.com/zhaozhao010/chatgpt-pluspro-tutorial
// @version      1.0.0
// @description  点击油猴菜单，在已登录的 ChatGPT 页面查询并显示 Account ID。
// @match        https://chatgpt.com/*
// @grant        GM_registerMenuCommand
// @run-at       document-idle
// @noframes
// ==/UserScript==

(() => {
  'use strict';

  let querying = false;

  GM_registerMenuCommand('查询 Account ID（本地）', async () => {
    if (querying) return;
    querying = true;
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 15000);

    try {
      const response = await fetch('https://chatgpt.com/api/auth/session', {
        credentials: 'same-origin',
        cache: 'no-store',
        redirect: 'error',
        signal: controller.signal,
      });
      if (!response.ok) {
        alert(`查询失败（HTTP ${response.status}）。请确认已登录 ChatGPT，再重试。`);
        return;
      }

      const session = await response.json();
      const accountId = session?.account?.id;
      if (typeof accountId !== 'string' || !accountId.trim()) {
        alert('未找到 Account ID。请确认登录状态；页面接口也可能已经变化。');
        return;
      }

      // Only display the requested identifier, never the full session response.
      prompt('Account ID（可手动复制）\n仅提供该标识，不外传其他敏感登录信息。', accountId);
    } catch (error) {
      alert(error.name === 'AbortError'
        ? '查询超时，请稍后重试。'
        : '查询失败，请检查网络或稍后重试。');
    } finally {
      clearTimeout(timeout);
      querying = false;
    }
  });
})();
