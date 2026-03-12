# Fund-Application-Workflow

基金申报全流程协同写作 Skill — A VS Code Copilot skill for planning, researching, structuring, drafting, reviewing, and revising Chinese grant applications and research proposals.

## Overview

This is a **VS Code GitHub Copilot custom skill** that guides researchers through the full lifecycle of preparing a formal grant application (基金申报书), project proposal (项目申请书), or research plan (研究计划书).

The skill is **not** a one-shot proposal generator. Instead, it acts as a top-level orchestrator that progressively transforms scattered ideas into a defensible, evidence-backed project draft.

## Features

- **S1 — Project Card Builder**: Structures raw ideas into a `project_card` with known/missing/inferred information
- **S2 — Gap Clarifier**: Identifies which gaps need user input vs. external research
- **S3 — Outline Generator**: Builds a section blueprint with draft-readiness assessment
- **S4 — Goal & Content Expander**: Converts vague goals into structured objectives, task modules, and integrated paragraphs
- **S5 — Innovation Extractor**: Derives defensible innovation claims with risk alerts and comparative evidence needs
- **S6 — Review Simulator**: Simulates multi-perspective peer review with actionable revision priorities

## Core Principles

1. **Evidence First** — Never fabricates facts, citations, data, or policy references
2. **Structured Intermediates** — Outputs project cards, gap lists, frameworks, and research needs rather than premature prose
3. **Dual-Route Research** — Distinguishes NotebookLM queries (existing sources) from external deep research (new evidence needed)

## Installation

Copy the `.github/skills/fund-application-workflow/` directory into your workspace's `.github/skills/` folder.

```
your-workspace/
└── .github/
    └── skills/
        └── fund-application-workflow/
            ├── SKILL.md
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
| `revise_after_review` | S6 + backflow | Post-review revision planning |
| `full_workflow` | Auto | Automatically advance to the next needed stage |

## License

MIT
