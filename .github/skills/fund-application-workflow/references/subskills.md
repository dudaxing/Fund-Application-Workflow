# Subskills

## Routing Logic

### Step 1: Decide Subskill

- `ideation` -> S1
- `clarify_gaps` -> S2
- `build_outline` -> S3
- `expand_goals` -> S4
- `extract_innovations` -> S5
- `review_draft` -> S6
- `draft_section` -> S7
- `revise_after_review` -> 以 S6 为主，必要时回到 S2、S4、S5
- `full_workflow` -> 自动判断：
  - 无 `project_card` -> S1
  - 有明显缺口 -> S2
  - 无 `framework` -> S3
  - 无 `goal_content_bundle` -> S4
  - 无 `innovation_bundle` -> S5
  - 有初稿、摘要或章节文本需审查 -> S6
  - framework 已就绪且有章节标记为 ready_to_draft -> S7

### Step 2: Decide Retrieval Route

#### 何时用 `internal`

- 主题属于用户已收集、已导入资料库的范围
- 任务是从已有资料中提取、比较、综合、核验
- 目标是"从已有资料里找依据"

#### 何时用 `external`

- 需要最新文献、最新政策、最新趋势、最新案例
- 当前明显缺乏相关资料
- 目标是补新资料

#### 何时用 `either`

- 先建议在已有资料中核验
- 若证据仍不足，再转外部检索

## 素材输入处理（全子技能通用）

当用户提供文件路径或目录作为输入素材时，执行以下处理流程：

1. **格式识别**：扫描指定路径下的 `.md`、`.pdf`、`.docx` 文件。
2. **完整读取**：对每个文件使用对应工具完整提取内容——Markdown 直接读取，PDF 使用 PDF 读取工具（确认所有页面均已提取），Word 使用 Word 读取工具。
3. **来源关联**：将提取内容与来源文件名绑定，后续引用时可追溯到具体文件和章节。
4. **不静默跳过**：若某文件格式无法读取，明确告知用户并建议转换格式。

`existing_materials` 字段接受文件路径列表或目录路径，支持混合格式。

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

`existing_materials` 可包含文件路径（`.md` / `.pdf` / `.docx`）或目录路径，skill 将自动识别格式并完整提取内容。

### Output

```json
{
  "project_card": { "...见 schemas.md" },
  "research_needs": []
}
```

### Behavior

1. 只整理，不编造。
2. 核心已知信息直接写入 `project_card` 顶层字段。
3. 诊断性内容分成 `missing_information`、`to_be_verified`、`inferences`。
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
2. 对研究趋势、方法比较、评价指标、政策数据、同类方案，优先生成 `research_needs`。
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
2. 章节至少覆盖：立项依据、研究目标与研究内容、创新点、技术路线或研究方案、研究基础、预期成果与进度。
3. 对证据不足的部分输出 `research_needs`。

## S4 研究目标与研究内容展开器

### Goal

把模糊设想转成"总目标—分目标—任务模块—整合段落"，并识别方法与设计支撑所需的外部证据。可附带生成研究内容模块关系图。

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
  "goal_content_bundle": { "...见 schemas.md" },
  "research_needs": [],
  "diagrams": []
}
```

### Behavior

1. 目标必须具体、可执行、可评审。
2. 不把研究意义写成研究目标。
3. 不把技术路线写成研究内容。
4. 使用 `overall_goal`、`sub_goals`、`content_modules` 固定命名。
5. 如目标与任务设计缺少方法依据，生成 `research_needs`，并在 `design_risks` 中记录风险。
6. 若内容模块关系复杂，可生成 `diagrams`（Mermaid mindmap 或 graph）。

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
  "innovation_bundle": { "...见 schemas.md" },
  "research_needs": []
}
```

### Behavior

1. 创新点必须建立在与已有工作的差异之上。
2. 不把工作量、热门技术、应用价值当创新点。
3. 对每条创新点判断最可能被评审质疑的点。
4. 若创新点可辩护性不足，优先输出对比文献型 `research_needs`。
5. `evidence_mode = strict` 时，若无材料支撑，必须显式标记风险。

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
  "review_bundle": { "...见 schemas.md" },
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
3. 若问题可通过补证据解决，转成 `research_needs`。
4. 若问题属于结构性设计缺陷，不伪装成"补几篇文献就能解决"。

## S7 正文撰写器

### Goal

基于已有中间产物（`project_card`、`framework`、`goal_content_bundle`、`innovation_bundle` 等），按章节生成可直接用于申报书的中文正文。

### Input

```json
{
  "project_card": {},
  "framework": [],
  "goal_content_bundle": {},
  "innovation_bundle": {},
  "review_bundle": {},
  "target_section": "",
  "evidence_mode": "strict|normal",
  "word_limit": 0,
  "style_reference": ""
}
```

### Output

```json
{
  "section_draft": {
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
  },
  "evidence_status": {},
  "diagrams": []
}
```

### Behavior

1. **只写 `target_section` 指定的章节**，不跨章节扩散。
2. **优先使用已有中间产物和用户提供的调研素材**。`goal_content_bundle.integrated_paragraph` 可作为研究目标与内容章节的起点；`innovation_bundle.innovations` 可作为创新点章节的骨架。用户提供的调研报告（无论 `.md`、`.pdf` 还是 `.docx` 格式）中的数据和结论应作为正文论据的主要来源。
3. **逐条追溯引用**。正文中每个事实性论述（数据、趋势、结论、对比）都必须在行文中明确标注可追溯的来源——可以是调研报告中引用的原始文献（标注作者/机构、年份、标题），也可以是调研报告本身（标注报告名称和章节）。不接受无来源的事实性陈述。若某处需要引用但当前无来源，在正文中标记 `[待补引用: 主题]`，并记入 `citation_placeholders`。
4. **不虚构文献、数据、政策**。若材料不足以支撑完整章节，写到可写的部分为止，剩余用 `evidence_gaps` 标记。
5. **语言风格**：正式学术中文，符合基金申报书的表述惯例。避免口语化、营销化表达。若用户通过 `style_reference` 提供了范文片段，对齐其风格。
6. **字数控制**：若 `word_limit > 0`，正文长度控制在目标字数 ±10% 范围内。若 `word_limit = 0`，参考 `framework` 中该章节的 `recommended_word_count`。
7. **可视化生成**：若当前章节是"技术路线"或"研究方案"，自动生成对应的 Mermaid 流程图并放入 `diagrams`；若是"预期成果与进度"，可生成甘特图。

### 各章节撰写要点

| 章节 | 主要依据 | 要点 |
|------|---------|------|
| 立项依据 | `project_card.core_problem`, `research_needs` 的调研结果 | 从现实需求出发，经研究现状分析，导向本项目切入点。事实性表述必须有据。 |
| 研究目标与研究内容 | `goal_content_bundle` | 可直接使用 `integrated_paragraph` 为起点，补充细节和过渡。不混入研究意义。 |
| 创新点 | `innovation_bundle` | 每条创新点转为一段论证性文字，包含"相比已有工作的差异 → 本项目的做法 → 预期价值"。 |
| 技术路线 / 研究方案 | `goal_content_bundle.content_modules`, `framework` | 按模块展开方法、步骤、验证逻辑。附 Mermaid 流程图。 |
| 研究基础与可行性 | `project_card.existing_foundation` | 团队积累、已有成果、实施条件。不要编造。 |
| 预期成果与进度 | `framework`, `project_card.expected_outputs` | 成果形式、考核指标、阶段划分。可附甘特图。 |
