# Benchmark Guide

本文件是 `evals.json` 的人类可读版说明，用于人工 review、跨 agent 对齐、以及后续脚本化 benchmark 的判定参考。

## Scope

- 评测目标不是比较文风，而是验证该 skill 是否按阶段正确路由、产出正确主对象、保持证据纪律，并遵守共享状态对象的命名与占位约定。
- 评测对象是 `fund-application-workflow` skill 的分阶段工作流能力，而不是一次性生成整篇申报书正文的能力。
- 如果输出把阶段性任务直接写成整段申报书正文，通常应判为偏离 workflow 设计。

## Global Pass Rules

- 必须 evidence-aware，不能编造文献、政策、数据、代表性系统或所谓"已有研究结论"。
- `selected_subskill` 应与 prompt 的主阶段一致；`full_workflow` 允许落到当前最合理的下一步子技能。
- 当前阶段主对象必须被实质性填充，不能只有字段空壳。
- 非当前阶段对象允许为空占位，不应因此判错。
- `research_needs` 必须结构化，不能退化成泛泛而谈的"建议再查文献"。
- 若问题本质是结构性设计缺陷，不能伪装成"补几篇文献即可解决"。

## Placeholder Policy

- 对象型共享状态字段默认空占位为 `{}`：`project_card`、`goal_content_bundle`、`innovation_bundle`、`review_bundle`。
- 列表型字段默认空占位为 `[]`：`questions`、`framework`、`recommended_writing_order`、`priority_revisions`、`research_needs`。
- 不应引入 `pending_*`、`unused_*`、`null` 或其他平行字段来表达"当前阶段未产出"。

## Rating Workflow

1. 先检查 `selected_subskill` 是否合理。
2. 再检查当前阶段主对象是否存在并使用 canonical 字段名。
3. 再检查 `research_needs` 和 `evidence_status` 是否反映真实证据缺口。
4. 最后检查是否出现阶段越界，例如把 outline 任务直接写成完整正文。

## Common Fail Patterns

- 把 `full_workflow` 直接写成完整立项依据或整篇申报书。
- 在 S1 中重新发明 `known_information` 一类重复容器。
- 在 S4 中把研究意义写成目标，或把技术路线误写为研究内容模块。
- 在 S5 中把"大模型""热门技术"本身当创新点，而没有与既有工作比较。
- 在 S6 或 `revise_after_review` 中只给泛泛评价，没有优先修订项或回流路径。
- 用非结构化建议替代 `research_needs`。

## Eval Checklist

### Eval 1: `full_workflow` kickoff

- 目标路由：S1。
- 主检查点：`project_card` 应包含 `missing_information`、`to_be_verified`、`inferences`。
- 通过重点：像 workflow 首步那样先搭底稿，而不是直接起草正文。
- 失败信号：把推测写成已证实的研究现状，或生成完整立项依据段落。

### Eval 2: `clarify_gaps`

- 目标路由：S2。
- 主检查点：`questions` 具体、可回答、不超过 5 个；需要证据的缺口转成 `research_needs`。
- 通过重点：能区分"该问用户"与"该查资料"。
- 失败信号：把所有缺口都变成追问，或问题过于空泛。

### Eval 3: `build_outline`

- 目标路由：S3。
- 主检查点：`framework` 覆盖主要章节，并给出 `ready_to_draft`；`recommended_writing_order` 可与章节顺序并存。
- 通过重点：能区分结构上可先写的章节和被证据卡住的章节。
- 失败信号：所有章节都标成 ready，或直接输出整篇框架正文。

### Eval 4: `expand_goals`

- 目标路由：S4。
- 主检查点：`goal_content_bundle` 使用固定字段名，且 `design_risks` 可非空。
- 通过重点：把模糊想法压实成可评审的目标、模块和整合段落。
- 失败信号：把研究意义、技术路线、应用愿景混写进目标层。

### Eval 5: `extract_innovations`

- 目标路由：S5。
- 主检查点：`innovation_bundle.innovations` 中每条都有 `statement`、`supporting_basis`、`risk_alert`。
- 通过重点：创新点必须建立在与已有工作的差异上，并承认证据不足时的风险。
- 失败信号：只因为列出了 2-4 条项目就判通过，或把技术热词当创新。

### Eval 6: `review_draft`

- 目标路由：S6。
- 主检查点：至少三类 reviewer 视角，且 `priority_revisions` 可执行。
- 通过重点：评审意见必须具体，不把结构问题伪装成纯补文献问题。
- 失败信号：只有空泛褒贬，没有具体 major issues 和修订动作。

### Eval 7: `revise_after_review`

- 目标路由：以 S6 为主。
- 主检查点：除了评审与修订优先级，还必须明确回流到 S2、S4、S5 的路径。
- 通过重点：先编排修订顺序，再决定回到哪些阶段，而不是直接改写正文。
- 失败信号：把它当普通 `review_draft` 处理，完全不指出回流方向。

## Manual Review Coverage

- 已有人工样例：`eval-1-full_workflow-review.md`
- 已有人工样例：`eval-3-build_outline-review.md`
- 已有人工样例：`eval-4-expand_goals-review.md`
- 已有人工样例：`eval-5-extract_innovations-review.md`
- 已有人工样例：`eval-6-review_draft-review.md`
- 已有人工样例：`eval-7-revise_after_review-review.md`
- 当前缺口：Eval 2 还没有独立人工样例，当前主要依赖 `evals.json` 里的断言说明进行判定。

## Recommended Scoring Use

- 对单条 eval，可按四维快速打分：路由正确性、主对象合规性、证据纪律、行动可用性。
- 若其中任一维度明显失败，建议整条 eval 判为不通过，而不是用文风或篇幅抵消结构性缺陷。
- 若输出满足主对象要求且证据纪律可靠，即使非当前阶段对象为空，也应判为通过。

## Maintenance Notes

- 每次新增 canonical 字段、共享状态对象或新的阶段辅助字段时，应同步更新本文件和 `evals.json`。
- 若后续补上 Eval 2 的人工样例，应在本文件的 Manual Review Coverage 中补齐对应映射。
- 若未来引入自动脚本判定，可直接把本文件中的 fail patterns 和 pass rules 映射为脚本规则或 reviewer rubric。
