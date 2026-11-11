# 魔兽世界：无限插件 | WoW Forever Addons

公开仓库收录 WoW Forever 的社区插件、简体中文语言包和 Mac / Windows 安装说明。

## Controller Forever 简体中文语言包

**0.3.0-beta** | 适配原版 Controller Forever **3.9.44** | 独立加载，不修改原版插件。

### 汉化真实进度

- 参照上游德语本地化文件中的 2,289 条英文键，全部已有 zhCN 翻译映射。
- 已由 AI 逐项重新编写或专项校对 1059 条，涵盖治疗、背键、任务选怪、按键绑定、动作条、拍卖行和物品操作。
- 仍有 1230 条沿用早期机器翻译草稿，尚未经过逐条语言复核；不代表专业汉化完成。
- 动态格式占位符（例如 %s、%d）已进行顺序核对。Lua 语法和 ZIP 完整性也经过静态检查。
- 客户端实测未完成；上游可能还有未收录进参考语言表的动态文字。

**参考键覆盖率 100% 不是翻译质量验收 100%。当前仍是 Beta。**

### 下载

[下载 ControllerForever_ZH-0.3.0-beta.zip](releases/ControllerForever_ZH-0.3.0-beta.zip)

### 安装

1. 先安装原版 Controller Forever：https://www.curseforge.com/wow/addons/controllerforever
2. 把 ZIP 里面的 ControllerForever_ZH 文件夹解压到游戏的 _forever_/Interface/AddOns/。
3. 确保 ControllerForever_ZH 与 ControllerForever 是两个并列文件夹，不能把语言包放进原插件目录里。
4. 完全重启游戏，在插件列表启用原插件和汉化包。
5. 输入 /cr menu 打开设置。简体中文客户端会自动使用中文；其他客户端可以输入 /cr lang zhCN，输入 /cr lang auto 恢复自动语言。

本语言包只增加语言映射，不改变任何手柄按键、技能宏、施法与移动行为。删除汉化插件目录即可恢复原版界面，玩家原有配置会保留。

### 主要文件

- addons/controller-forever-zhcn/ControllerForever_ZH/：语言文件和 TOC
- releases/：直接安装的 ZIP 包
- QA_REPORT.md：翻译质量和静态校验说明
- REVIEW_REMAINING.tsv：仍需人工语言复核的中英对照
- GLOSSARY.md：魔兽与手柄术语规范
- scripts/check_package.py：格式、重复键、压缩包校验
- .github/workflows/validate.yml：GitHub 自动化语法校验

### 版权与发布

非官方项目。Controller Forever 原版采用 All Rights Reserved，本仓库不分发其源代码和美术资源，仅提供独立 zhCN 语言包。对英文界面的翻译可能涉及派生作品权利，正式上架 CurseForge 前仍应确认必要的上游授权。与原作者、暴雪及 CurseForge 均无官方关联。
