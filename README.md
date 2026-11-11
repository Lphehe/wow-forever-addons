# 魔兽世界：无限插件 | WoW Forever Addons

本仓库收录 WoW Forever（魔兽世界：无限）的简体中文插件和本地化文件。

## Controller Forever 简体中文语言包 0.4.1-rc

独立汉化，匹配原版 Controller Forever 3.9.44。

### 下载

[ControllerForever_ZH-0.4.1-rc.zip](releases/ControllerForever_ZH-0.4.1-rc.zip)

### 目前检查结果

- 上游翻译清单中的 2,289 条英文键均已检查。
- 旧版被标记为待审查的 1,230 条已逐条核对，其中 783 条被实质性修改，其余保留既有中文。
- 额外从源码中找到 653 个界面标签、标题、说明候选，均已制作中文映射。
- 额外审查了 477 个 name 字段，其中 415 个可读名称添加汉化；其余多为内部标识、错误代码和测试角色名称，不宜直接替换。
- 翻译表合计 3,357 条；经过 Lua 5.1 语法检查、格式占位符顺序检查、颜色控制符检查、压缩包检查。
- 使用上游 3.9.44 的原始语言注册模块进行了脱离游戏的运行时测试；语言切换与 190 个格式化示例均通过。
- **未完成 WoW 客户端内逐菜单实测。** 部分源码直接显示字符串，不一定经过官方翻译函数；建立映射不等于能保证对应文字已经在游戏中汉化。

**注意：这是 Release Candidate，不是已实机验收的最终正式版。**

### 安装（Mac / Windows）

1. 先安装原版 [Controller Forever](https://www.curseforge.com/wow/addons/controllerforever)（建议 3.9.44）。
2. 将 ZIP 解压到 WoW Forever 的 _forever_/Interface/AddOns/ 目录。
3. 检查原插件文件夹 ControllerForever 和汉化文件夹 ControllerForever_ZH 是并列的。
4. 彻底重启游戏，启用原插件及汉化插件。
5. 简体中文客户端通常自动使用 zhCN；也可输入 /cr lang zhCN，输入 /cr menu 查看设置。
6. 回退原语言可输入 /cr lang auto，或禁用 ControllerForever_ZH。

仅汉化文字，不会修改游戏宏、按键绑定、战斗行为或原插件文件。

### 发布和授权说明

本项目是非官方社区语言包，与原作者、暴雪或 CurseForge 没有官方关联。原版插件使用 All Rights Reserved。本仓库不分发原版完整插件、代码和素材；翻译英文原文可能涉及派生作品授权。正式上架 CurseForge 前需要核实作者许可。

### 目录

- addons/controller-forever-zhcn/ControllerForever_ZH/: 可读的 Lua 源码和 TOC
- releases/: 可安装 ZIP
- QA_REPORT.md: 检查结果、通过项和未通过验证项
- TRANSLATION_STATS.json: 可机读的数字
- GLOSSARY.md: 手柄和魔兽术语
- scripts/check_package.py: 静态测试
- .github/workflows/validate.yml: GitHub Actions 自动检查
