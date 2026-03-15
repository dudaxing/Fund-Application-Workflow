#!/usr/bin/env python3
"""
Fund-Application-Workflow Skill — 多平台自动安装脚本

自动检测当前环境支持的 AI 编程助手平台，并将 skill 安装到对应位置。

支持平台：
  - GitHub Copilot  (.github/skills/)
  - Cursor          (.cursor/rules/)
  - Claude Code     (CLAUDE.md)
  - Codex / OpenAI  (AGENTS.md)

用法：
  python install.py                     # 自动检测并安装到所有可用平台
  python install.py --platform cursor   # 只安装到指定平台
  python install.py --platform all      # 强制安装到所有平台
  python install.py --dry-run           # 预览将执行的操作
  python install.py --uninstall         # 卸载
"""

import argparse
import json
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

SKILL_NAME = "fund-application-workflow"
SKILL_DISPLAY_NAME = "基金申报全流程协同写作 Skill"

PLATFORMS = ["copilot", "cursor", "claude", "codex"]


def find_skill_source(script_dir: Path) -> Path:
    """定位 skill 源文件目录。"""
    if (script_dir / "SKILL.md").exists():
        return script_dir
    candidate = script_dir / ".github" / "skills" / SKILL_NAME
    if (candidate / "SKILL.md").exists():
        return candidate
    print(f"错误：找不到 SKILL.md，请在 skill 目录下运行此脚本。")
    sys.exit(1)


def find_workspace_root(start: Path) -> Path:
    """向上查找工作区根目录（含 .git 或为磁盘根）。"""
    current = start.resolve()
    while current != current.parent:
        if (current / ".git").exists():
            return current
        for marker in [".github", ".cursor", ".claude", "CLAUDE.md", "AGENTS.md"]:
            if (current / marker).exists():
                return current
        current = current.parent
    return start.resolve()


def detect_platforms(workspace: Path) -> list[str]:
    """自动检测工作区中已存在的平台标记。"""
    detected = []
    if (workspace / ".github").exists():
        detected.append("copilot")
    if (workspace / ".cursor").exists():
        detected.append("cursor")
    if (workspace / "CLAUDE.md").exists() or (workspace / ".claude").exists():
        detected.append("claude")
    if (workspace / "AGENTS.md").exists() or (workspace / ".codex").exists():
        detected.append("codex")
    return detected


def copy_skill_files(source: Path, dest: Path, dry_run: bool = False):
    """递归复制 skill 文件（排除 install.py 自身和 __pycache__）。"""
    exclude = {"install.py", "__pycache__", ".pyc", "state"}
    if dry_run:
        print(f"  [预览] 复制 {source} -> {dest}")
        return
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(
        source, dest,
        ignore=shutil.ignore_patterns(*exclude)
    )


# ─────────────────────────── Platform Installers ───────────────────────────

def install_copilot(source: Path, workspace: Path, dry_run: bool):
    """GitHub Copilot: 复制到 .github/skills/{name}/"""
    dest = workspace / ".github" / "skills" / SKILL_NAME
    print(f"\n[GitHub Copilot] 安装到 {dest}")
    if source.resolve() == dest.resolve():
        print("  skill 已在正确位置，跳过复制。")
        return
    copy_skill_files(source, dest, dry_run)
    if not dry_run:
        print("  [OK] 已安装。Copilot 将自动识别 .github/skills/ 下的 SKILL.md。")


def install_cursor(source: Path, workspace: Path, dry_run: bool):
    """Cursor: 在 .cursor/rules/ 下创建规则文件指向 skill。"""
    rules_dir = workspace / ".cursor" / "rules"
    rule_file = rules_dir / f"{SKILL_NAME}.mdc"

    skill_in_workspace = workspace / ".github" / "skills" / SKILL_NAME
    if not skill_in_workspace.exists() and not dry_run:
        copy_skill_files(source, skill_in_workspace)

    try:
        rel_skill_path = skill_in_workspace.relative_to(workspace).as_posix()
    except ValueError:
        rel_skill_path = skill_in_workspace.as_posix()

    rule_content = f"""---
description: {SKILL_DISPLAY_NAME} — 基金/项目申报书全流程写作辅助
globs:
alwaysApply: false
---

# {SKILL_DISPLAY_NAME}

当用户需要准备基金申报书、项目申请书、研究计划书或教改项目申报书时，请读取并遵循以下 skill 文件中的指令：

- 主文件: `{rel_skill_path}/SKILL.md`
- Schema 定义: `{rel_skill_path}/references/schemas.md`
- 子技能定义: `{rel_skill_path}/references/subskills.md`
- 模板与风格指引: `{rel_skill_path}/references/prompt-templates.md`

## 快速路由

收到相关任务后：

1. 读取 `.fund-workflow/state.json`（若存在）加载历史状态。
2. 根据用户意图选择子技能（S1-S7）。
3. 按 SKILL.md 中的输出协议回应：散文优先，结构化数据辅助。
4. 执行后更新 `.fund-workflow/state.json`。
"""

    print(f"\n[Cursor] 创建规则文件 {rule_file}")
    if dry_run:
        print(f"  [预览] 写入 {rule_file}")
        return

    rules_dir.mkdir(parents=True, exist_ok=True)
    rule_file.write_text(rule_content, encoding="utf-8")
    print("  [OK] 已创建。在 Cursor 中使用 @rules 或通过 Agent 模式自动触发。")


def install_claude(source: Path, workspace: Path, dry_run: bool):
    """Claude Code: 将 skill 指引追加到 CLAUDE.md。"""
    claude_file = workspace / "CLAUDE.md"

    skill_in_workspace = workspace / ".github" / "skills" / SKILL_NAME
    if not skill_in_workspace.exists() and not dry_run:
        copy_skill_files(source, skill_in_workspace)

    try:
        rel_skill_path = skill_in_workspace.relative_to(workspace).as_posix()
    except ValueError:
        rel_skill_path = skill_in_workspace.as_posix()

    marker = f"<!-- {SKILL_NAME} -->"
    block = f"""
{marker}
## {SKILL_DISPLAY_NAME}

当用户需要准备基金申报书、项目申请书、研究计划书时，读取并遵循 `{rel_skill_path}/SKILL.md` 中的完整指令。

核心参考文件：
- `{rel_skill_path}/references/schemas.md` — 数据结构定义
- `{rel_skill_path}/references/subskills.md` — S1-S7 子技能详细规则
- `{rel_skill_path}/references/prompt-templates.md` — 模板与风格指引

状态持久化文件：`.fund-workflow/state.json`
{marker}
"""

    print(f"\n[Claude Code] 更新 {claude_file}")
    if dry_run:
        print(f"  [预览] 追加 skill 指引到 CLAUDE.md")
        return

    if claude_file.exists():
        existing = claude_file.read_text(encoding="utf-8")
        if marker in existing:
            import re
            pattern = re.escape(marker) + r".*?" + re.escape(marker)
            existing = re.sub(pattern, block.strip(), existing, flags=re.DOTALL)
            claude_file.write_text(existing, encoding="utf-8")
            print("  [OK] 已更新（替换旧版 skill 指引）。")
            return
        claude_file.write_text(existing.rstrip() + "\n" + block, encoding="utf-8")
    else:
        claude_file.write_text(f"# Project Instructions\n{block}", encoding="utf-8")
    print("  [OK] 已追加到 CLAUDE.md。")


def install_codex(source: Path, workspace: Path, dry_run: bool):
    """Codex / OpenAI: 将 skill 指引追加到 AGENTS.md。"""
    agents_file = workspace / "AGENTS.md"

    skill_in_workspace = workspace / ".github" / "skills" / SKILL_NAME
    if not skill_in_workspace.exists() and not dry_run:
        copy_skill_files(source, skill_in_workspace)

    try:
        rel_skill_path = skill_in_workspace.relative_to(workspace).as_posix()
    except ValueError:
        rel_skill_path = skill_in_workspace.as_posix()

    marker = f"<!-- {SKILL_NAME} -->"
    block = f"""
{marker}
## {SKILL_DISPLAY_NAME}

当用户需要准备基金申报书、项目申请书、研究计划书时，读取并遵循 `{rel_skill_path}/SKILL.md` 中的完整指令。

核心参考文件：
- `{rel_skill_path}/references/schemas.md` — 数据结构定义
- `{rel_skill_path}/references/subskills.md` — S1-S7 子技能详细规则
- `{rel_skill_path}/references/prompt-templates.md` — 模板与风格指引

状态持久化文件：`.fund-workflow/state.json`
{marker}
"""

    print(f"\n[Codex] 更新 {agents_file}")
    if dry_run:
        print(f"  [预览] 追加 skill 指引到 AGENTS.md")
        return

    if agents_file.exists():
        existing = agents_file.read_text(encoding="utf-8")
        if marker in existing:
            import re
            pattern = re.escape(marker) + r".*?" + re.escape(marker)
            existing = re.sub(pattern, block.strip(), existing, flags=re.DOTALL)
            agents_file.write_text(existing, encoding="utf-8")
            print("  [OK] 已更新（替换旧版 skill 指引）。")
            return
        agents_file.write_text(existing.rstrip() + "\n" + block, encoding="utf-8")
    else:
        agents_file.write_text(f"# Agents\n{block}", encoding="utf-8")
    print("  [OK] 已追加到 AGENTS.md。")


# ──────────────────────────── Uninstall ────────────────────────────

def uninstall(workspace: Path, dry_run: bool):
    """卸载所有平台的 skill 安装。"""
    print("\n== 卸载 ==")

    copilot_dir = workspace / ".github" / "skills" / SKILL_NAME
    if copilot_dir.exists():
        print(f"  删除 {copilot_dir}")
        if not dry_run:
            shutil.rmtree(copilot_dir)

    cursor_rule = workspace / ".cursor" / "rules" / f"{SKILL_NAME}.mdc"
    if cursor_rule.exists():
        print(f"  删除 {cursor_rule}")
        if not dry_run:
            cursor_rule.unlink()

    marker = f"<!-- {SKILL_NAME} -->"
    for fname in ["CLAUDE.md", "AGENTS.md"]:
        fpath = workspace / fname
        if fpath.exists():
            content = fpath.read_text(encoding="utf-8")
            if marker in content:
                import re
                pattern = r"\n?" + re.escape(marker) + r".*?" + re.escape(marker) + r"\n?"
                content = re.sub(pattern, "\n", content, flags=re.DOTALL)
                if not dry_run:
                    fpath.write_text(content.strip() + "\n", encoding="utf-8")
                print(f"  从 {fname} 中移除 skill 指引")

    state_dir = workspace / ".fund-workflow"
    if state_dir.exists():
        print(f"  删除状态目录 {state_dir}")
        if not dry_run:
            shutil.rmtree(state_dir)

    print("\n[OK] 卸载完成。" if not dry_run else "\n[预览] 卸载预览完成。")


# ──────────────────────────── Main ────────────────────────────

INSTALLER_MAP = {
    "copilot": install_copilot,
    "cursor": install_cursor,
    "claude": install_claude,
    "codex": install_codex,
}


def main():
    parser = argparse.ArgumentParser(
        description=f"{SKILL_DISPLAY_NAME} — 多平台安装脚本"
    )
    parser.add_argument(
        "--platform",
        choices=PLATFORMS + ["all"],
        default=None,
        help="指定目标平台（默认自动检测）",
    )
    parser.add_argument(
        "--workspace",
        type=str,
        default=None,
        help="工作区根目录（默认自动检测）",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只预览操作，不实际执行",
    )
    parser.add_argument(
        "--uninstall",
        action="store_true",
        help="卸载 skill",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).parent.resolve()
    source = find_skill_source(script_dir)

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        workspace = find_workspace_root(script_dir)

    print(f"{'=' * 60}")
    print(f"  {SKILL_DISPLAY_NAME}")
    print(f"  {'卸载' if args.uninstall else '安装'}脚本")
    print(f"{'=' * 60}")
    print(f"\nSkill 源目录: {source}")
    print(f"工作区根目录: {workspace}")

    if args.uninstall:
        uninstall(workspace, args.dry_run)
        return

    if args.platform == "all":
        targets = PLATFORMS
    elif args.platform:
        targets = [args.platform]
    else:
        targets = detect_platforms(workspace)
        if not targets:
            print("\n未检测到已知平台标记。")
            print("  提示：可用 --platform 手动指定，支持: " + ", ".join(PLATFORMS))
            print("  或使用 --platform all 安装到所有平台。")
            targets = PLATFORMS
            print(f"\n将安装到所有平台: {', '.join(targets)}")

    print(f"\n目标平台: {', '.join(targets)}")
    if args.dry_run:
        print("模式: 预览（不实际执行）")

    state_dir = workspace / ".fund-workflow"
    if not state_dir.exists() and not args.dry_run:
        state_dir.mkdir(parents=True, exist_ok=True)
        print(f"\n已创建状态目录: {state_dir}")

    for platform in targets:
        INSTALLER_MAP[platform](source, workspace, args.dry_run)

    print(f"\n{'=' * 60}")
    if args.dry_run:
        print("预览完成。去掉 --dry-run 执行实际安装。")
    else:
        print("安装完成！")
        print(f"\n状态持久化目录: {state_dir}")
        print("使用时，skill 会自动在此目录维护跨轮次状态。")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
