# Schemas

## Global Input Schema

```json
{
  "task_type": "ideation|clarify_gaps|build_outline|expand_goals|extract_innovations|review_draft|draft_section|full_workflow|revise_after_review",
  "project_type": "",
  "project_name": "",
  "current_stage": "idea|outline|draft|revision",
  "current_section": "",
  "user_input": "",
  "context_history": [],
  "existing_materials": [],
  "current_text": "",
  "project_card": {},
  "framework": [],
  "goal_content_bundle": {},
  "innovation_bundle": {},
  "review_bundle": {},
  "known_gaps": [],
  "format_constraint": {
    "word_limit": 0,
    "required_sections": []
  },
  "evidence_mode": "strict|normal",
  "max_questions": 5,
  "max_research_needs": 3
}
```

## Global Output Schema

输出只包含当前阶段实际产出的字段，不携带空占位。以下为所有可能出现的顶层字段；每次输出只使用其中与当前子技能相关的部分。

```json
{
  "selected_subskill": "S1|S2|S3|S4|S5|S6|S7",
  "project_card": {},
  "questions": [],
  "framework": [],
  "recommended_writing_order": [],
  "goal_content_bundle": {},
  "innovation_bundle": {},
  "review_bundle": {},
  "priority_revisions": [],
  "section_draft": {},
  "diagrams": [],
  "research_needs": [],
  "evidence_status": {
    "overall": "verified|partially_verified|insufficient_evidence",
    "citation_needed": true,
    "citation_notes": []
  }
}
```

### 各子技能输出的典型字段组合

| 子技能 | 主对象 | 可选附加 |
|-------|--------|---------|
| S1 | `project_card` | `research_needs`, `evidence_status` |
| S2 | `questions` | `research_needs`, `evidence_status` |
| S3 | `framework`, `recommended_writing_order` | `research_needs`, `evidence_status` |
| S4 | `goal_content_bundle` | `research_needs`, `evidence_status`, `diagrams` |
| S5 | `innovation_bundle` | `research_needs`, `evidence_status` |
| S6 | `review_bundle`, `priority_revisions` | `research_needs`, `evidence_status` |
| S7 | `section_draft` | `evidence_status`, `diagrams` |

不在上表中的字段直接省略，不输出 `{}` 或 `[]` 占位。

## Canonical `project_card` Schema

```json
{
  "project_name": "",
  "project_type": "",
  "project_theme": "",
  "research_object": [],
  "core_problem": "",
  "scope_boundary": [],
  "possible_goals": [],
  "possible_methods": [],
  "existing_foundation": [],
  "expected_outputs": [],
  "project_preliminary_positioning": {
    "direction": "",
    "type_guess": "",
    "maturity_level": "idea|outline|draft|revision"
  },
  "missing_information": [],
  "to_be_verified": [],
  "inferences": []
}
```

### Normalization Rules

- 核心事实字段直接写在 `project_card` 顶层，不另建 `known_information` 容器。
- 诊断类内容统一进入 `missing_information`、`to_be_verified`、`inferences`。
- `project_preliminary_positioning` 只负责方向、类型猜测和成熟度。
- 后续子技能若需扩展 `project_card`，追加新字段，不重命名已有字段。

## Canonical `goal_content_bundle` Schema

```json
{
  "overall_goal": "",
  "sub_goals": [
    {
      "sub_goal": "",
      "related_tasks": [],
      "expected_result": ""
    }
  ],
  "content_modules": [
    {
      "module_name": "",
      "module_purpose": "",
      "module_relation": ""
    }
  ],
  "integrated_paragraph": "",
  "design_risks": []
}
```

### Normalization Rules

- `overall_goal` 是唯一的总目标主字段。
- `sub_goals` 只放可执行的分目标，不混入研究意义或技术路线。
- `content_modules` 承载研究内容模块，不用并行容器重复。
- `design_risks` 显式记录目标设计、任务闭环、评价设计上的风险。

## Canonical `innovation_bundle` Schema

```json
{
  "innovations": [
    {
      "title": "",
      "innovation_type": "problem|object|method|mechanism|data|scenario|integration",
      "statement": "",
      "supporting_basis": [],
      "risk_alert": ""
    }
  ],
  "overall_innovation_positioning": ""
}
```

### Normalization Rules

- `innovations` 是唯一主列表。每条必须包含 `statement` 和 `risk_alert`。
- `supporting_basis` 只写差异依据和比较线索，不堆泛泛优势。

## Canonical `review_bundle` Schema

```json
{
  "reviewers": [
    {
      "reviewer_focus": "",
      "strengths": [],
      "major_issues": [],
      "risk_level": "low|medium|high"
    }
  ],
  "overall_judgement": ""
}
```

### Normalization Rules

- `reviewers` 是唯一的分视角评审容器。
- `priority_revisions` 放在全局输出顶层，不塞回 `review_bundle` 内部。

## Canonical `section_draft` Schema

S7 正文撰写器的输出对象。

```json
{
  "target_section": "",
  "prose": "",
  "word_count": 0,
  "citation_placeholders": [
    {
      "location": "",
      "needed_citation": ""
    }
  ],
  "evidence_gaps": []
}
```

### 字段说明

- `target_section`：本次撰写的章节名称。
- `prose`：可直接用于申报书的中文正文段落。
- `citation_placeholders`：正文中标记了"待补引用"的位置及其所需引用类型。
- `evidence_gaps`：本章节正文中因证据不足而无法展开的部分。

## Canonical `diagrams` Schema

可视化输出对象，使用 Mermaid 语法。

```json
{
  "diagrams": [
    {
      "diagram_type": "flowchart|mindmap|gantt|graph",
      "title": "",
      "purpose": "",
      "mermaid_code": ""
    }
  ]
}
```

### 适用场景

| 图表类型 | 典型用途 |
|---------|---------|
| `flowchart` | 技术路线图、研究流程图 |
| `mindmap` | 研究内容模块分解、子目标展开 |
| `gantt` | 研究进度与里程碑 |
| `graph` | 模块关系图、概念关系图 |

## Simplified `research_needs` Schema

每条调研需求只保留核心字段。通用的来源要求和引用规范由全局默认约束覆盖，不在每条中重复。

```json
{
  "research_needs": [
    {
      "need_id": "R1",
      "topic": "",
      "why_needed": "",
      "priority": 1,
      "retrieval_route": "internal|external|either",
      "suggested_prompt": "",
      "expected_use": ""
    }
  ]
}
```

### 字段说明

| 字段 | 说明 |
|------|------|
| `need_id` | 编号，如 R1、R2 |
| `topic` | 需要调研的主题 |
| `why_needed` | 为什么需要这条调研 |
| `priority` | 优先级，1 最高 |
| `retrieval_route` | `internal`（用户已有资料库）/ `external`（需新增外部文献）/ `either`（先内部核验再外部补充）|
| `suggested_prompt` | 可直接用于文献检索或资料查询的 prompt |
| `expected_use` | 该调研结果将用于申报书的哪个部分 |

### 调研需求全局默认约束

以下约束适用于所有 `research_needs` 的 `suggested_prompt` 生成，无需在每条中重复：

- **优先来源**：高质量综述、权威期刊/会议论文、官方政策文件、官方统计数据库、代表性项目资料
- **避免来源**：无署名网页、营销内容、低可信二手转载、无原始出处的总结文
- **时效性**：近 5 年为主，必要时补充经典文献
- **引用粒度**：至少提供作者、年份、题目、来源；如可行补充 DOI/链接
- **证据区分**：输出中必须区分已证实事实、基于资料的归纳、尚待验证的推断
- **语言策略**：使用英文进行思考、检索和资料查找，最终以中文作答；关键术语保留英文原文并附中文译注

### `retrieval_route` 判断规则

- `internal`：主题属于用户大概率已收集的资料范围，任务是从已有资料中提取、比较、综合、核验。
- `external`：需要最新文献、最新政策、最新趋势、最新案例，用户现有资料大概率不覆盖。
- `either`：先建议在已有资料中核验，若证据不足再转外部检索。

当 `retrieval_route = internal` 时，`suggested_prompt` 应在开头加上"请仅基于已有资料回答，不要引入外部资料"。

## Evidence Status Rules

```json
{
  "evidence_status": {
    "overall": "verified|partially_verified|insufficient_evidence",
    "citation_needed": true,
    "citation_notes": []
  }
}
```

判断规则：

- `verified`：关键事实已有明确来源支持
- `partially_verified`：部分有资料支持，但关键判断仍需补证据
- `insufficient_evidence`：当前主要依赖推断或用户直觉，暂不宜写成事实

## State Persistence Schema

跨轮次状态文件 `.fund-workflow/state.json` 的结构：

```json
{
  "last_updated": "",
  "current_stage": "idea|outline|draft|revision",
  "last_subskill": "S1|S2|S3|S4|S5|S6|S7",
  "project_card": {},
  "framework": [],
  "goal_content_bundle": {},
  "innovation_bundle": {},
  "review_bundle": {},
  "accumulated_research_needs": []
}
```

只存储有实质内容的字段。未产出的阶段对象不写入状态文件。
