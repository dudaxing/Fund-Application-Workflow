# Fund-Application-Workflow

基金申报全流程协同写作 Skill — An AI coding assistant skill for planning, researching, structuring, drafting, reviewing, and revising Chinese grant applications and research proposals.

## Overview

This is an **AI coding assistant custom skill** that guides researchers through the full lifecycle of preparing a formal grant application (基金申报书), project proposal (项目申请书), or research plan (研究计划书).

The skill is **not** a one-shot proposal generator. Instead, it acts as a top-level orchestrator that progressively transforms scattered ideas into a defensible, evidence-backed project draft.

Supports **GitHub Copilot**, **Cursor**, **Claude Code**, and **Codex (OpenAI)**.

## Features

- **S1 — Project Card Builder**: Structures raw ideas into a `project_card` with known/missing/inferred information
- **S2 — Gap Clarifier**: Identifies which gaps need user input vs. external research
- **S3 — Outline Generator**: Builds a section blueprint with draft-readiness assessment
- **S4 — Goal & Content Expander**: Converts vague goals into structured objectives, task modules, and integrated paragraphs; supports Mermaid module-relation diagrams
- **S5 — Innovation Extractor**: Derives defensible innovation claims with risk alerts and comparative evidence needs
- **S6 — Review Simulator**: Simulates multi-perspective peer review with actionable revision priorities
- **S7 — Prose Drafter**: Generates publication-ready Chinese prose for each section based on accumulated intermediates; auto-generates Mermaid flowcharts and Gantt charts where appropriate

## Core Principles

1. **Evidence First** — Never fabricates facts, citations, data, or policy references; unsupported claims are marked `[待补引用]`
2. **Prose First, Structure Second** — Responds in Chinese prose by default; structured data (project cards, frameworks) are presented as Markdown tables/lists; pure JSON mode available on request
3. **Tri-Route Research** — Classifies every information gap as `internal` (user's existing sources), `external` (new literature needed), or `either` (verify internally first); not tied to any specific tool
4. **Bilingual Research Strategy** — Research prompts instruct the model to think and search in English for broader coverage, then respond in Chinese with key terms preserved in English

## Installation

### Automated (recommended)

Use the bundled `install.py` to auto-detect your environment and set up the skill:

```bash
python .github/skills/fund-application-workflow/install.py
```

The installer supports:

| Platform | What it does |
|----------|-------------|
| **GitHub Copilot** | Copies skill to `.github/skills/` (default location) |
| **Cursor** | Creates `.cursor/rules/fund-application-workflow.mdc` |
| **Claude Code** | Appends skill reference to `CLAUDE.md` |
| **Codex (OpenAI)** | Appends skill reference to `AGENTS.md` |

Options: `--dry-run` (preview only), `--uninstall` (remove).

### Manual

Copy the `.github/skills/fund-application-workflow/` directory into your workspace:

```
your-workspace/
└── .github/
    └── skills/
        └── fund-application-workflow/
            ├── SKILL.md
            ├── install.py
            ├── references/
            │   ├── prompt-templates.md
            │   ├── schemas.md
            │   └── subskills.md
            └── evals/
                ├── BENCHMARK.md
                ├── evals.json
                └── manual-review/
                    └── *.md
```

## State Persistence

The skill saves project progress to `.fund-workflow/state.json` across sessions. Each stage incrementally updates the state file, so you never lose context between conversations.

## Visualization

Supports Mermaid diagrams:

| Diagram Type | Purpose | When |
|-------------|---------|------|
| Flowchart | Technical roadmap & dependencies | S7 writing methodology sections |
| Graph | Module relationships | S4 expanding research content |
| Gantt | Timeline & milestones | S7 writing deliverables sections |
| Mindmap | Goal decomposition | S4 expanding objectives |

## Evaluation

The `evals/` directory contains:
- `evals.json` — 7 structured evaluation scenarios with assertions and pass criteria
- `BENCHMARK.md` — Human-readable benchmark guide and evaluation checklist
- `manual-review/` — Gold-standard manual review outputs for 6 of the 7 evals

## Supported Task Types

| Task Type | Route | Description |
|-----------|-------|-------------|
| `ideation` | S1 | Turn raw ideas into a project card |
| `clarify_gaps` | S2 | Identify and triage information gaps |
| `build_outline` | S3 | Generate section blueprint |
| `expand_goals` | S4 | Expand goals and research content |
| `extract_innovations` | S5 | Extract defensible innovation claims |
| `review_draft` | S6 | Simulate peer review |
| `draft_section` | S7 | Draft publication-ready prose by section |
| `revise_after_review` | S6 + backflow | Post-review revision planning |
| `full_workflow` | Auto | Automatically advance to the next needed stage |

## License

MIT
