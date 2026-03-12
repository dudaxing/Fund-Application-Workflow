# Eval 4 Review

## Eval Prompt

我现在最卡的是"研究目标与研究内容"。项目大意是：构建一个支持高校教师科研写作选题、提纲、修订和反馈整合的交互式系统，并研究其对写作效率和质量的影响。请按 expand_goals，把它展开成总目标、分目标、任务模块和可直接进入申请书的整合段落，同时指出还需要补哪些方法或评估依据。

## Manual Output

```json
{
  "skill_name": "基金申报全流程协同写作 Skill",
  "status": "ok",
  "confidence": "medium",
  "selected_subskill": "S4",
  "project_card": {},
  "questions": [],
  "framework": [],
  "goal_content_bundle": {
    "overall_goal": "围绕高校教师科研写作场景，构建一个覆盖选题、提纲、修订与反馈整合的交互式支持系统，并研究该系统如何通过任务分解、反馈协同与过程支撑提升科研写作效率与质量。",
    "sub_goals": [
      {
        "sub_goal": "识别高校教师科研写作过程中的关键阻滞环节与支持需求。",
        "related_tasks": [
          "梳理科研写作中选题、结构组织、初稿生成、修订反馈等关键环节",
          "提炼高校教师在不同环节中的典型困难与支持需求"
        ],
        "expected_result": "形成科研写作支持需求图谱和系统设计依据。"
      },
      {
        "sub_goal": "设计并实现支持连续写作过程的交互式系统原型。",
        "related_tasks": [
          "设计选题支持、提纲支持、修订建议与反馈整合模块",
          "明确大模型、用户输入与人工反馈的交互机制"
        ],
        "expected_result": "形成具备多环节支持能力的系统原型与功能说明。"
      },
      {
        "sub_goal": "评估该系统对科研写作效率与质量的实际影响。",
        "related_tasks": [
          "设计对照或过程性评价方案",
          "建立写作效率、文本质量、修订质量或用户感知等评估指标"
        ],
        "expected_result": "形成系统有效性证据与可推广的应用建议。"
      }
    ],
    "content_modules": [
      {
        "module_name": "需求识别与场景建模",
        "module_purpose": "明确高校教师科研写作过程中的核心任务链与支持痛点。",
        "module_relation": "为后续系统功能设计与评价指标设定提供依据。"
      },
      {
        "module_name": "交互式支持系统设计",
        "module_purpose": "围绕选题、提纲、修订和反馈整合构建连续写作支持机制。",
        "module_relation": "承接需求分析结果，是项目的核心设计模块。"
      },
      {
        "module_name": "应用验证与效果评估",
        "module_purpose": "检验系统是否真正改善写作效率、质量和修订过程表现。",
        "module_relation": "对前两个模块的有效性进行验证，并反向修正系统设计。"
      }
    ],
    "integrated_paragraph": "本项目拟围绕高校教师科研写作的连续过程支持展开研究。首先，通过梳理选题、提纲建构、初稿生成、修订与反馈整合等关键环节，识别高校教师科研写作中的典型困难与支持需求；在此基础上，设计一个面向连续写作任务的交互式支持系统，重点探索大模型生成建议、用户主动输入与人工反馈之间的协同机制；最后，通过应用验证与效果评估，考察该系统在提升科研写作效率、文本质量与修订质量方面的作用，并据此形成可推广的科研写作支持模式与实施建议。",
    "design_risks": [
      "当前'效率'与'质量'仍是概括性目标，尚未落实到可测量指标。",
      "尚未说明评价设计是实验对照、准实验设计还是过程性追踪分析。",
      "系统支持边界较宽，若不收束场景，研究内容可能显得过大。"
    ]
  },
  "innovation_bundle": {},
  "review_bundle": {},
  "priority_revisions": [],
  "research_needs": [
    {
      "need_id": "R1",
      "topic": "科研写作效率与质量的可操作评价指标及其测量方式",
      "why_needed": "当前目标中的'效率'与'质量'尚未落到可评估指标，需要方法依据支撑目标与评价闭环。",
      "evidence_type": "评价指标框架 + 实证测量方法",
      "priority": 1,
      "retrieval_route": "either",
      "notebooklm_applicability": {
        "suitable_if_sources_already_loaded": true,
        "recommended_notebook_scope": "若已有教育评估、写作评价或系统评测相关 notebook，可先核验",
        "query_goal": "extract"
      },
      "source_requirements": {
        "preferred_source_types": [
          "高质量综述",
          "方法论文",
          "教育评估研究",
          "写作评价研究",
          "代表性实证研究"
        ],
        "avoid_source_types": [
          "无署名网页",
          "营销内容",
          "低可信二手转载",
          "无原始出处的总结文"
        ],
        "recency_requirement": "近5年为主，必要时补经典评价框架",
        "authority_requirement": "优先核心期刊、高水平会议和方法综述",
        "language_scope": "中英均可",
        "min_source_count": 5
      },
      "citation_expectations": {
        "must_provide_traceable_citations": true,
        "must_distinguish_fact_from_inference": true,
        "must_include_source_for_key_claims": true,
        "preferred_citation_granularity": "至少提供作者、年份、题目、来源；如可行，补充 DOI 或链接"
      },
      "suggested_prompt": "请仅基于当前 notebook 已收录的 sources 回答，不要引入外部资料。请围绕'科研写作效率与质量的评价指标及测量方式'完成以下任务：1. 提取最直接相关研究；2. 总结已证实的常用指标；3. 区分哪些指标适合写作效率、文本质量、修订质量和用户体验；4. 明确证据不足部分；5. 提供可追溯出处。若 notebook 内证据不足，请指出哪些部分应转外部 deep research。",
      "expected_use": "用于把总目标和分目标落成可评审、可测量的研究设计。"
    },
    {
      "need_id": "R2",
      "topic": "交互式科研写作支持系统的研究设计与验证范式",
      "why_needed": "当前系统设计已形成模块，但缺少成功案例、方法依据和评价范式支撑。",
      "evidence_type": "系统设计案例 + 验证研究范式",
      "priority": 2,
      "retrieval_route": "external_deep_research",
      "notebooklm_applicability": {
        "suitable_if_sources_already_loaded": true,
        "recommended_notebook_scope": "若 notebook 已有交互式写作支持系统或教育技术系统研究，可先核验",
        "query_goal": "synthesize"
      },
      "source_requirements": {
        "preferred_source_types": [
          "高质量综述",
          "高水平期刊论文",
          "代表性系统论文",
          "教育技术研究",
          "人机交互研究"
        ],
        "avoid_source_types": [
          "无署名网页",
          "营销内容",
          "低可信二手转载",
          "无原始出处的总结文"
        ],
        "recency_requirement": "近5年为主，必要时补经典案例",
        "authority_requirement": "优先教育技术、人机交互和写作研究领域代表性来源",
        "language_scope": "中英均可",
        "min_source_count": 5
      },
      "citation_expectations": {
        "must_provide_traceable_citations": true,
        "must_distinguish_fact_from_inference": true,
        "must_include_source_for_key_claims": true,
        "preferred_citation_granularity": "至少提供作者、年份、题目、来源；如可行，补充 DOI 或链接"
      },
      "suggested_prompt": "请优先检索近五年交互式写作支持系统、教育技术系统与大模型支持写作场景中的代表性研究。请归纳：1. 常见系统模块；2. 用户交互机制；3. 验证方法；4. 研究设计局限；5. 哪些做法可直接支持本项目的研究内容设计。请优先使用可靠来源，包括高质量综述、权威期刊/会议论文、官方政策文件、官方统计数据库、代表性项目资料。请避免将无署名网页、营销内容、低可信转载作为核心依据。请在输出中尽量提供可追溯出处，并明确区分：1. 已证实事实 2. 基于资料的归纳 3. 尚待验证的推断。对于关键判断，请附上对应来源信息。",
      "expected_use": "用于补强内容模块设计和研究方案可行性。"
    }
  ],
  "evidence_status": {
    "overall": "partially_verified",
    "citation_needed": true,
    "citation_notes": [
      "当前 goal_content_bundle 主要基于任务结构化推演，评价指标与系统设计依据仍需文献支撑。",
      "若直接进入正文，需要先补方法依据、成功案例与评估框架引用。"
    ]
  },
  "notes": [
    "该样例专门验证 S4，因此 goal_content_bundle 为主对象。",
    "project_card、innovation_bundle、review_bundle 留空是阶段性设计，不代表字段缺失。"
  ]
}
```

## Evaluation

- Trigger correctness: Pass
- Goal bundle completeness: Pass
- Design risk visibility: Pass
- Evidence discipline: Pass
- Residual issues:
  - `project_card` 为空意味着这是纯 S4 样例；若实际运行 full_workflow，通常应带着已有 project_card 进入本阶段。
  - 若正式做自动 benchmark，需要允许 `goal_content_bundle.design_risks` 非空且不把它误判为负面输出噪音。

## Verdict

该样例符合 canonical `goal_content_bundle` schema 和 S4 的职责定义，能够把模糊设想收敛成目标、模块、整合段落和设计风险，并把方法与评估缺口转成 research_needs。
