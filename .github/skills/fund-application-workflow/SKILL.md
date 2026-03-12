---
name: fund-application-workflow
description: Plan, research, structure, draft, review, and revise Chinese grant applications, project proposals, and research plans. Use this skill whenever the user is preparing a 基金申报书、项目申请书、研究计划书、教改项目申报书、横向课题 proposal, or any formal research-oriented application document, especially when they need to turn scattered ideas into a project card, identify evidence gaps, generate NotebookLM or deep-research prompts, build an outline, expand goals and research content, extract defensible innovations, or simulate reviewer feedback.
argument-hint: task_type + project context or current draft
---

# 基金申报全流程协同写作 Skill

这个 skill 是一个顶层总控 skill，不是一次性自动写完整篇申报书的正文生成器。它负责把零散想法逐步推进为可辩护、可补证据、可修订的项目申报底稿。

## 何时使用

遇到以下任务时优先使用本 skill：

- 用户要准备基金、科研、教改、合作课题或其他正式 proposal 类文档
- 用户只有模糊想法，需要先梳理项目主题、对象、问题、目标、方法、基础和产出
- 用户需要先识别缺失信息，再决定哪些问题该问用户，哪些问题该转成调研任务
- 用户需要生成 NotebookLM 可直接使用的查询 prompt，或外部 deep research prompt
- 用户需要搭建申报书框架，而不是立刻生成完整正文
- 用户需要展开研究目标、研究内容、任务模块、技术路线边界
- 用户需要提炼创新点，并验证这些创新点是否真正建立在与已有工作的差异之上
- 用户需要从评审视角识别草稿硬伤、优点、风险和优先修订项

## 总体原则

### 1. 证据优先

- 涉及研究现状、发展趋势、政策、数据、方法比较、创新性判断、代表性工作、研究空白、效果判断时，必须基于可靠来源。
- 不得编造事实、文献、出处、数据、引文、政策依据、项目案例或所谓"已有研究结论"。
- 证据不足时，必须明确标注"证据不足"或"待核实"，不要把猜测写成事实。
- 默认区分三类内容：已证实信息、基于资料的归纳、推断性判断。
- 若当前任务仍缺外部调研，不要把"可能如此"的内容写成"已经证实"的表述。

### 2. 输出中间结果优先

- 默认中文输出。
- 除非用户明确要求正文段落，否则优先输出项目卡片、问题清单、章节蓝图、研究内容模块、创新点包、评审意见包、修订重点、research_needs。
- 若继续写作必须先补资料，就明确输出 `research_needs`，不要为了显得完整而强行写满。

### 3. 双路由调研

每当识别出信息缺口时，都要判断它更适合走哪条路由：

- `notebooklm_query`：资料大概率已经在用户现有 NotebookLM notebook 中，任务更像"从已有 sources 里提取、比较、综合、核验"。
- `external_deep_research`：需要新增外部文献、最新政策、最新趋势、最新案例，或当前 notebook 大概率没有相关资料。
- `either`：先建议用 NotebookLM 核验已有资料，证据仍不足时再转外部 deep research。

NotebookLM 相关 prompt 必须要求"仅基于当前 notebook 已收录的 sources 回答，不引入外部资料"。

## 顶层路由

支持的 `task_type`：

- `ideation`
- `clarify_gaps`
- `build_outline`
- `expand_goals`
- `extract_innovations`
- `review_draft`
- `full_workflow`
- `revise_after_review`

路由规则：

- `ideation` -> S1 项目信息梳理器
- `clarify_gaps` -> S2 缺失信息追问器
- `build_outline` -> S3 申报书框架生成器
- `expand_goals` -> S4 研究目标与研究内容展开器
- `extract_innovations` -> S5 创新点提炼器
- `review_draft` -> S6 评审意见模拟器
- `revise_after_review` -> 以 S6 为主，必要时回到 S2、S4、S5
- `full_workflow` -> 按状态自动选择下一步

`full_workflow` 默认推进顺序：

1. 若 `project_card` 为空，先做 S1。
2. 若 `project_card` 仍有明显缺口，做 S2。
3. 若 `framework` 为空，做 S3。
4. 若 `goal_content_bundle` 为空，做 S4。
5. 若 `innovation_bundle` 为空，做 S5。
6. 若已经有摘要、初稿、章节文本或用户要求审查，做 S6。

每一步结束后都要：

- 输出当前阶段结果
- 输出 `research_needs`
- 若 `evidence_mode = strict`，补 `evidence_status`

## 子技能职责

### S1 项目信息梳理器

把用户零散输入整理成结构化项目底稿，输出 `project_card` 的雏形，并标记：

- 已知信息
- 缺失信息
- 待核实信息
- 推断性判断
- 最值得补的背景资料需求

### S2 缺失信息追问器

判断哪些缺口应该追问用户，哪些缺口应该转成调研。问题要具体，可直接回答，不重复追问已有信息。

### S3 申报书框架生成器

生成正式申报书章节蓝图，并判断每一章是否已具备开写条件。若缺少立项依据、研究现状、方法依据、创新性比较材料，则输出 `research_needs`。

### S4 研究目标与研究内容展开器

把模糊设想转成：

- 总目标
- 分目标
- 任务模块
- 模块关系
- 可直接进入正文的整合段落

注意不要把研究意义写成研究目标，也不要把技术路线写成研究内容。

### S5 创新点提炼器

从目标、内容与已有工作的差异中提炼可辩护创新点。每条创新点都要说明：

- 属于哪类创新
- 依据是什么
- 最可能被评审质疑什么
- 缺哪些对比文献或支撑材料

### S6 评审意见模拟器

默认至少模拟三类 reviewer：

- 问题与创新性
- 目标与方法闭环
- 研究基础与可行性

输出优点、主要问题、风险等级、总体判断、优先修订项，并把可通过补资料解决的问题转成 `research_needs`。

## 输出协议

默认优先返回结构化 JSON 风格内容。若用户只是想讨论思路，可以先给简洁中文说明，再附结构化块。完整 schema、`research_needs` 协议、`evidence_status` 规则见 [schemas](./references/schemas.md)。

S3 除 `framework` 外，可额外输出 `recommended_writing_order` 作为辅助写作顺序字段；其他阶段若未使用该字段，保持 `[]` 即可。

`project_card` 必须尽量使用统一字段集合，不要把同一信息同时写成顶层字段和重复的摘要字段。例如已经有 `project_theme`、`research_object`、`core_problem` 时，不要再额外复制出一套语义重复的 `known_information.project_theme`。诊断性内容统一进入 `missing_information`、`to_be_verified`、`inferences`。

`goal_content_bundle`、`innovation_bundle`、`review_bundle` 也应视为共享状态对象，优先使用固定字段集合。不要在不同阶段为相同概念反复改名，例如已经有 `overall_goal` 时，不要再平行创建一套 `main_goal`；已经有 `overall_judgement` 时，不要再平行创建一套语义重复的 `summary_assessment`。

非当前阶段的共享状态对象应保留为空占位，而不是通过临时字段名表达"暂未产出"。对象型字段默认用 `{}`，列表型字段默认用 `[]`。

子技能详细定义、输入输出字段和行为规则见 [subskills](./references/subskills.md)。

NotebookLM prompt 模板、外部 deep research 证据尾约束、总控系统提示见 [prompt-templates](./references/prompt-templates.md)。

## 执行要求

- 若用户要求高可靠性，默认按 `evidence_mode = strict` 执行。
- 任何准备进入申报书正文的事实性表述，都要优先具备准确出处或明确标注"此处需补引用"。
- 若信息不足，不要臆造研究现状、政策背景、行业数据或代表性工作。
- 若用户只给一句模糊想法，不要直接展开成大段申报书正文；先生成 `project_card` 和 `research_needs`。
- 若用户已经有草稿，不要重复从头梳理；优先进入评审、修订、创新性核验或证据补强。
- 若某个问题本质上是结构性设计缺陷，不要把它伪装成"补几篇文献就能解决"。
- 顶层输出中只放当前阶段真正产出的主对象；不要把同一批信息拆成多个重复容器。
- `project_card` 优先视为全流程共享状态对象，后续 S2-S6 应在其基础上推进，而不是重新发明一套字段。
- `goal_content_bundle`、`innovation_bundle`、`review_bundle` 也应在后续轮次中持续复用和增量更新，而不是每轮重新换一套命名。

## 最小工作方式

收到任务后，先做三件事：

1. 判断当前 `task_type` 或最接近的阶段。
2. 选择一个主子技能。
3. 输出当前阶段结果 + `research_needs` + `evidence_status`。

如果用户没有提供足够字段，就根据已有信息尽量补一个最小可用状态对象，但必须把推断与已知分开。
