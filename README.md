# 魔兽世界：无限插件 | WoW Forever Addons

面向 World of Warcraft: Forever（魔兽世界：无限）的中文插件、汉化包与兼容性改进项目。

## Controller Forever 简体中文独立汉化

**v0.2.0-beta · 上游 Controller Forever 3.9.44 · WoW Forever 1.60.1**

- 本地化覆盖 2,090 / 2,289 个上游参考文本键，其余回退英文。
- 在机器翻译初稿基础上，重点精修手柄背键、小队治疗、队友选择轮盘、冷却、目标选择及提示语。
- 基于上游预留的语言注册 API 制作独立插件。不会覆盖原版 Controller Forever 文件、按键配置或游戏角色存档。
- 适用于 Mac 和 Windows：本汉化包只有游戏内 Lua 语言表，没有平台驱动。
- **仍属 Beta：已通过 Lua 静态语法检查和 ZIP 完整性检查，尚未进行游戏内逐页实测；少量翻译可能不准确。**

### 下载

[下载 ControllerForever_ZH v0.2.0-beta](releases/ControllerForever_ZH-0.2.0-beta.zip)

### 安装

1. 先安装原版 [Controller Forever](https://www.curseforge.com/wow/addons/controllerforever) 3.9.44。
2. 下载上面的 ZIP，将其中的 **ControllerForever_ZH** 文件夹解压到 **World of Warcraft/_forever_/Interface/AddOns/** 目录。
3. 确保 **ControllerForever_ZH** 和 **ControllerForever** 并列，不要把 ZIP 解压到原版插件文件夹内部。
4. 彻底重启游戏，在插件列表中启用这两个插件。
5. 简体中文客户端自动使用汉化；其他语言客户端可输入命令 /cr lang zhCN。输入 /cr menu 打开设置；/cr lang auto 恢复自动语言。

### 更新 / 卸载

停用或删除 **ControllerForever_ZH** 文件夹即可停止汉化，不会修改原版插件。上游插件更新后，如有文本键变化，对应内容会自动回退英文。

### 项目目录

- addons/controller-forever-zhcn/：汉化 Lua 源码与 TOC 描述
- releases/：可以直接解压安装的 ZIP 包
- scripts/check_package.py：基础结构及翻译键校验
- CHANGELOG.md：汉化更新说明
- COPYRIGHT.md：版权及上架注意事项
- TOPICS.md：GitHub Topics 建议标签

### 版权与 CurseForge 上架

**非官方汉化项目。** 原版 Controller Forever 版权属于原作者，授权为 All Rights Reserved。本仓库不重新分发原插件代码、图像或音频，仅发布使用其公开本地化接口的翻译语言包。外部上架前仍需核实原作者对中文翻译的许可及平台规则。

本项目与暴雪、CurseForge 和 Controller Forever 原作者均无官方关联。欢迎在 Issues 中报告翻译错误。