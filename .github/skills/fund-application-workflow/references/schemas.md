# Schemas

## Global Input Schema

```json
{
  "task_type": "ideation|clarify_gaps|build_outline|expand_goals|extract_innovations|review_draft|full_workflow|revise_after_review",
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

```json
{
  "skill_name": "基金申报全流程协同写作 Skill",
  "status": "ok",
  "confidence": "high|medium|low",
  "selected_subskill": "S1|S2|S3|S4|S5|S6",
  "project_card": {},
  "questions": [],
  "framework": [],
  "recommended_writing_order": [],
  "goal_content_bundle": {},
  "innovation_bundle": {},
  "review_bundle": {},
  "priority_revisions": [],
  "research_needs": [],
  "evidence_status": {
    "overall": "verified|partially_verified|insufficient_evidence",
    "citation_needed": true,
    "citation_notes": []
  },
  "notes": []
}
```

## Stage Placeholder Convention

- 当前阶段真正产出的主对象应正常填充；非当前阶段对象允许保留空占位。
- `project_card`、`goal_content_bundle`、`innovation_bundle`、`review_bundle` 这类对象型共享状态，默认使用 `{}` 作为空占位。
- `framework`、`questions`、`priority_revisions`、`research_needs`、`recommended_writing_order` 这类列表型字段，默认使用 `[]` 作为空占位。
- 不要为了表达"当前阶段未产出"而临时发明 `null`、`unused_*`、`pending_*` 或其他平行字段。
- `recommended_writing_order` 是 S3 常用的辅助输出；若当前阶段不是 S3，可保留为空数组。

## Canonical `project_card` Schema

`project_card` 是全流程共享状态对象，优先使用下面这套字段。可以按任务阶段留空部分字段，但不要随意改名，也不要用重复字段表达同一事实。

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

- `project_theme`、`research_object`、`core_problem` 这类核心事实字段优先直接写在 `project_card` 顶层。
- 不再额外创建一个重复承载同样信息的 `known_information` 容器。
- 若需要说明"当前已经明确了什么"，优先通过顶层字段本身体现，而不是再复制一遍摘要。
- 诊断类内容统一进入：
  - `missing_information`
  - `to_be_verified`
  - `inferences`
- `project_preliminary_positioning` 只负责方向、类型猜测和成熟度，不重复承载问题、目标、方法。
- 后续子技能若需要扩展 `project_card`，优先追加与当前阶段强相关的新字段；不要重命名已有字段。

## Canonical `goal_content_bundle` Schema

`goal_content_bundle` 是研究目标与研究内容阶段的共享状态对象，优先使用下面这套字段。

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

- `overall_goal` 是唯一的总目标主字段，不再并行创建 `main_goal`、`general_goal` 一类重复字段。
- `sub_goals` 负责表达可执行的分目标；不要把研究意义、应用价值或技术路线混写进 `sub_goals`。
- `content_modules` 负责承载研究内容模块及其关系；不要用另一套并行容器重复表达相同模块信息。
- `integrated_paragraph` 是可进入正文的整合表达，但不能替代前面的结构化字段。
- `design_risks` 用于记录目标设计、任务闭环、评价设计上的风险提示，避免风险信息散落在注释里。

## Canonical `innovation_bundle` Schema

`innovation_bundle` 是创新点阶段的共享状态对象，优先使用下面这套字段。

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

- `innovations` 是唯一主列表，不再并行创建 `innovation_points`、`novelties` 等同义容器。
- 每条创新点必须包含 `statement` 和 `risk_alert`；如果证据不足，风险应写在 `risk_alert`，而不是藏在备注里。
- `supporting_basis` 只写支撑创新点的差异依据、相关工作比较或材料线索，不要把泛泛优势描述堆进去。
- `overall_innovation_positioning` 用于概括整组创新点在项目中的整体站位，不重复列举单条创新点内容。

## Canonical `review_bundle` Schema

`review_bundle` 是评审阶段的共享状态对象，优先使用下面这套字段。

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

- `reviewers` 是唯一的分视角评审容器，不再平行创建 `review_comments`、`panel_feedback` 等重复结构。
- 每位 reviewer 至少给出 `reviewer_focus`、`strengths`、`major_issues`、`risk_level` 四项。
- `overall_judgement` 只负责汇总总体判断，不重复罗列已经在 `reviewers` 中展开的问题。
- `priority_revisions` 仍放在全局输出顶层，用于把 `review_bundle` 中的问题转成行动项，而不是塞回 `review_bundle` 内部。

## Enhanced `research_needs` Schema

所有子技能输出的 `research_needs` 都使用这个结构：

```json
{
  "research_needs": [
    {
      "need_id": "R1",
      "topic": "",
      "why_needed": "",
      "evidence_type": "",
      "priority": 1,
      "retrieval_route": "notebooklm_query|external_deep_research|either",
      "notebooklm_applicability": {
        "suitable_if_sources_already_loaded": true,
        "recommended_notebook_scope": "",
        "query_goal": "extract|compare|synthesize|verify|locate_gap"
      },
      "source_requirements": {
        "preferred_source_types": [
          "高质量综述",
          "高水平期刊论文",
          "官方政策文件",
          "官方统计数据库",
          "代表性项目/系统论文"
        ],
        "avoid_source_types": [
          "无署名网页",
          "营销内容",
          "低可信二手转载",
          "无原始出处的总结文"
        ],
        "recency_requirement": "近5年为主，必要时补充经典文献",
        "authority_requirement": "优先权威机构、核心期刊、高水平会议、官方来源",
        "language_scope": "中英均可",
        "min_source_count": 5
      },
      "citation_expectations": {
        "must_provide_traceable_citations": true,
        "must_distinguish_fact_from_inference": true,
        "must_include_source_for_key_claims": true,
        "preferred_citation_granularity": "至少提供作者、年份、题目、来源；如可行，补充DOI/链接/项目编号"
      },
      "suggested_prompt": "",
      "expected_use": ""
    }
  ]
}
```

## Evidence Status Rules

建议所有输出都带：

```json
{
  "evidence_status": {
    "overall": "verified|partially_verified|insufficient_evidence",
    "citation_needed": true,
    "citation_notes": [
      "本段涉及研究现状，需补近5年综述和代表性论文",
      "本处涉及现实需求判断，需补官方报告或需求调研"
    ]
  }
}
```

判断规则：

- `verified`：关键事实已有明确来源支持
- `partially_verified`：部分有资料支持，但关键判断仍需补证据
- `insufficient_evidence`：当前主要依赖推断或用户直觉，暂不宜写成事实

## Minimal Example

### Input

```json
{
  "task_type": "full_workflow",
  "project_type": "通用科研项目",
  "project_name": "大模型辅助高校教师科研写作支持研究",
  "current_stage": "idea",
  "user_input": "我想做一个关于大模型辅助高校教师科研写作的项目，可能结合真实写作案例和交互式系统，但还没想清楚具体研究边界。",
  "existing_materials": [
    "已有一些科研写作支持系统调研",
    "团队具备自然语言处理背景"
  ],
  "evidence_mode": "strict",
  "max_questions": 3,
  "max_research_needs": 2
}
```

### Expected Behavior

1. 先调用 S1 输出 `project_card`
2. 同时输出 1-2 条 `research_needs`
3. 标记 `selected_subskill = S1`
4. 输出 `evidence_status`
5. 不直接虚构研究现状，不写成完整立项依据正文
