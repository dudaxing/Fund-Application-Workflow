# Subskills

## Routing Logic

### Step 1: Decide Subskill

- `ideation` -> S1
- `clarify_gaps` -> S2
- `build_outline` -> S3
- `expand_goals` -> S4
- `extract_innovations` -> S5
- `review_draft` -> S6
- `revise_after_review` -> 以 S6 为主，必要时回到 S2、S4、S5
- `full_workflow` -> 自动判断：
  - 无 `project_card` -> S1
  - 有明显缺口 -> S2
  - 无 `framework` -> S3
  - 无 `goal_content_bundle` -> S4
  - 无 `innovation_bundle` -> S5
  - 有初稿、摘要或章节文本 -> S6

### Step 2: Decide Retrieval Route

#### 何时用 `notebooklm_query`

- 主题明显属于用户已收集、已导入 notebook 的资料范围
- 任务更适合从已有 sources 中提取、比较、综合、核验
- 目标是"从已有资料里找依据"，而不是新增资料

#### 何时用 `external_deep_research`

- 主题要求最新文献、最新政策、最新趋势、最新案例，而 notebook 未必具备
- 当前明显缺乏相关 sources
- 目标是补新资料，而不是整理旧资料

#### 何时用 `either`

- 先建议在 notebook 内核验已有资料
- 若证据仍不足，再转外部 deep research

## S1 项目信息梳理器

### Goal

把用户零散输入整理成结构化项目底稿，并识别当前最值得补的背景资料需求。

### Input

```json
{
  "project_type": "",
  "user_input": "",
  "existing_materials": [],
  "context_history": [],
  "evidence_mode": "strict|normal",
  "max_research_needs": 3
}
```

### Output

```json
{
  "project_card": {
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
  },
  "research_needs": []
}
```

### Behavior

1. 只整理，不编造。
2. 核心已知信息直接写入 `project_card` 顶层字段，不再复制到语义重复的 `known_information` 容器里。
3. 把诊断性内容分成缺失、待核实、推断。
4. 若关键背景、领域现状、需求证据缺失，生成 `research_needs`。
5. `evidence_mode = strict` 时，优先提出高质量资料需求，而不是替用户补事实。

## S2 缺失信息追问器

### Goal

提出最关键的问题；若缺口需要外部资料而不是用户主观补充，则同时输出 `research_needs`。

### Input

```json
{
  "project_card": {},
  "current_stage": "idea|outline|draft|revision",
  "current_section": "",
  "max_questions": 5,
  "evidence_mode": "strict|normal",
  "max_research_needs": 3
}
```

### Output

```json
{
  "questions": [
    {
      "question": "",
      "purpose": "",
      "used_for": "",
      "priority": 1
    }
  ],
  "research_needs": []
}
```

### Behavior

1. 先判断哪些缺口该问用户，哪些缺口该转成调研。
2. 对最新研究趋势、方法比较、评价指标、政策数据、同类方案，优先生成 `research_needs`。
3. 不重复追问 `project_card` 里已有信息。
4. 问题必须具体、可直接回答。

## S3 申报书框架生成器

### Goal

根据项目底稿生成正式申报书章节蓝图，并识别哪些章节因资料不足不宜直接起草。

### Input

```json
{
  "project_type": "",
  "project_card": {},
  "format_constraint": {
    "word_limit": 0,
    "required_sections": []
  },
  "evidence_mode": "strict|normal",
  "max_research_needs": 3
}
```

### Output

```json
{
  "framework": [
    {
      "section_name": "",
      "section_goal": "",
      "available_materials": [],
      "missing_materials": [],
      "ready_to_draft": true,
      "recommended_word_count": 0,
      "order": 1
    }
  ],
  "recommended_writing_order": [],
  "research_needs": []
}
```

### Behavior

1. 若项目类型不明确，采用通用科研项目结构。
2. 章节至少覆盖：立项依据、研究目标与研究内容、创新点、技术路线或研究方案、研究基础、预期成果与进度（如适用）。
3. 对立项依据、研究现状、创新点、技术路线中证据不足的部分输出 `research_needs`。

## S4 研究目标与研究内容展开器

### Goal

把模糊设想转成"总目标—分目标—任务模块—整合段落"，并识别方法与设计支撑所需的外部证据。

### Input

```json
{
  "project_card": {},
  "framework": [],
  "current_section": "研究目标与研究内容",
  "evidence_mode": "strict|normal",
  "max_research_needs": 3
}
```

### Output

```json
{
  "goal_content_bundle": {
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
  },
  "research_needs": []
}
```

### Behavior

1. 目标必须具体、可执行、可评审。
2. 不把研究意义写成研究目标。
3. 不把技术路线写成研究内容。
4. `overall_goal`、`sub_goals`、`content_modules` 使用固定命名，不再为同一含义创建平行字段。
5. 如目标与任务设计缺少方法依据、成功案例、评估方式，则生成 `research_needs`，并在 `design_risks` 中显式记录主要设计风险。

## S5 创新点提炼器

### Goal

从目标、内容和相关工作差异中提炼可辩护创新点，并指出每条创新点还缺什么对比文献或支撑证据。

### Input

```json
{
  "project_card": {},
  "goal_content_bundle": {},
  "related_work_summary": [],
  "evidence_mode": "strict|normal",
  "max_research_needs": 3
}
```

### Output

```json
{
  "innovation_bundle": {
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
  },
  "research_needs": []
}
```

### Behavior

1. 创新点必须建立在与已有工作的差异之上。
2. 不把工作量、热门技术、应用价值当创新点。
3. 对每条创新点判断最可能被评审质疑的点。
4. `innovations` 使用固定列表命名，不再并行创建同义容器。
5. 若创新点可辩护性不足，优先输出对比文献型 `research_needs`。
6. `evidence_mode = strict` 时，若无材料支撑，必须显式标记风险。

## S6 评审意见模拟器

### Goal

从评审视角识别项目硬伤、优点、风险等级，并把需要靠外部证据补强的问题转成 `research_needs`。

### Input

```json
{
  "project_type": "",
  "current_text": "",
  "project_card": {},
  "innovation_bundle": {},
  "evidence_mode": "strict|normal",
  "max_research_needs": 3
}
```

### Output

```json
{
  "review_bundle": {
    "reviewers": [
      {
        "reviewer_focus": "",
        "strengths": [],
        "major_issues": [],
        "risk_level": "low|medium|high"
      }
    ],
    "overall_judgement": ""
  },
  "priority_revisions": [
    {
      "revision_item": "",
      "reason": "",
      "priority": 1
    }
  ],
  "research_needs": []
}
```

### Behavior

1. 默认至少模拟三类 reviewer：问题与创新性、目标与方法闭环、研究基础与可行性。
2. 审稿意见必须具体、可操作。
3. `reviewers` 与 `overall_judgement` 使用固定命名，不再并行创建语义重复的评审容器。
4. 若问题可通过补文献、政策、案例、方法证据解决，则转成 `research_needs`。
5. 若问题属于结构性设计缺陷，不要伪装成"补几篇文献就能解决"。
