# Eval 3 Review

## Eval Prompt

我要写一个校级科研项目申请书，题目暂定为“面向高校教师科研写作的智能交互支持机制研究”。已有 project_card，但还没有正式框架。请按 build_outline 帮我生成章节蓝图、推荐写作顺序，并指出哪些章节因为证据不足还不适合直接起草。

## Manual Output

```json
{
  "skill_name": "基金申报全流程协同写作 Skill",
  "status": "ok",
  "confidence": "medium",
  "selected_subskill": "S3",
  "project_card": {},
  "questions": [],
  "framework": [
    {
      "section_name": "立项依据",
      "section_goal": "说明高校教师科研写作支持的现实需求、现有研究进展、主要不足以及本项目的切入点。",
      "available_materials": [
        "项目主题已明确聚焦高校教师科研写作支持",
        "已有‘智能交互支持机制’这一方向性定位"
      ],
      "missing_materials": [
        "近五年国内外相关系统或研究综述",
        "现实需求或政策导向证据",
        "同类研究的局限与本项目切入点比较"
      ],
      "ready_to_draft": false,
      "recommended_word_count": 1200,
      "order": 1
    },
    {
      "section_name": "研究目标与研究内容",
      "section_goal": "明确项目总目标、分目标、研究任务模块及其关系。",
      "available_materials": [
        "项目聚焦高校教师科研写作场景",
        "初步设想包含选题、提纲、修订和反馈整合支持"
      ],
      "missing_materials": [
        "更精确的分目标",
        "任务模块之间的闭环关系",
        "评价指标与方法依据"
      ],
      "ready_to_draft": true,
      "recommended_word_count": 1000,
      "order": 2
    },
    {
      "section_name": "创新点",
      "section_goal": "说明项目相对已有写作支持系统或研究工作的差异化贡献。",
      "available_materials": [
        "初步设想强调交互式支持机制，而不只是单次生成"
      ],
      "missing_materials": [
        "与现有系统的系统比较",
        "可辩护创新点的支撑依据",
        "每条创新点的风险与边界"
      ],
      "ready_to_draft": false,
      "recommended_word_count": 500,
      "order": 3
    },
    {
      "section_name": "研究方案与技术路线",
      "section_goal": "说明系统设计思路、研究步骤、关键方法和验证逻辑。",
      "available_materials": [
        "已有交互式系统方向设想"
      ],
      "missing_materials": [
        "模块化方案设计",
        "技术路线图",
        "验证方式与实施流程"
      ],
      "ready_to_draft": false,
      "recommended_word_count": 1000,
      "order": 4
    },
    {
      "section_name": "研究基础与可行性",
      "section_goal": "说明团队基础、已有积累、实施条件和样本来源。",
      "available_materials": [],
      "missing_materials": [
        "团队相关研究基础",
        "已有系统、课程或数据基础",
        "实施场景和样本来源"
      ],
      "ready_to_draft": false,
      "recommended_word_count": 700,
      "order": 5
    },
    {
      "section_name": "预期成果与进度安排",
      "section_goal": "明确成果形式、阶段任务和时间安排。",
      "available_materials": [
        "项目可能产出系统原型、研究框架与应用建议"
      ],
      "missing_materials": [
        "分阶段里程碑",
        "成果形态细化",
        "可考核的时间安排"
      ],
      "ready_to_draft": true,
      "recommended_word_count": 500,
      "order": 6
    }
  ],
  "recommended_writing_order": [
    "立项依据",
    "研究目标与研究内容",
    "研究方案与技术路线",
    "创新点",
    "研究基础与可行性",
    "预期成果与进度安排"
  ],
  "goal_content_bundle": {},
  "innovation_bundle": {},
  "review_bundle": {},
  "priority_revisions": [],
  "research_needs": [
    {
      "need_id": "R1",
      "topic": "高校教师科研写作支持研究的现状、代表性系统与主要不足",
      "why_needed": "用于支撑立项依据和创新点章节，避免对研究现状和研究空白做无依据判断。",
      "evidence_type": "研究现状综述 + 系统比较",
      "priority": 1,
      "retrieval_route": "external_deep_research",
      "notebooklm_applicability": {
        "suitable_if_sources_already_loaded": true,
        "recommended_notebook_scope": "若已有学术写作支持、AWE、LLM教育应用等 notebook，可先核验",
        "query_goal": "synthesize"
      },
      "source_requirements": {
        "preferred_source_types": [
          "高质量综述",
          "高水平期刊论文",
          "代表性系统论文",
          "教育技术研究",
          "写作研究论文"
        ],
        "avoid_source_types": [
          "无署名网页",
          "营销内容",
          "低可信二手转载",
          "无原始出处的总结文"
        ],
        "recency_requirement": "近5年为主，必要时补经典系统研究",
        "authority_requirement": "优先核心期刊、高水平会议和权威综述",
        "language_scope": "中英均可",
        "min_source_count": 5
      },
      "citation_expectations": {
        "must_provide_traceable_citations": true,
        "must_distinguish_fact_from_inference": true,
        "must_include_source_for_key_claims": true,
        "preferred_citation_granularity": "至少提供作者、年份、题目、来源；如可行，补充 DOI 或链接"
      },
      "suggested_prompt": "请优先检索近五年高校教师科研写作支持、学术写作辅助系统、AWE 和 LLM 写作支持相关研究。请梳理：1. 代表性系统或研究；2. 主要支持对象和支持环节；3. 常见方法与评价指标；4. 现有研究的主要不足；5. 哪些差异可用于本项目立项依据与创新性定位。请优先使用可靠来源，包括高质量综述、权威期刊/会议论文、官方政策文件、官方统计数据库、代表性项目资料。请避免将无署名网页、营销内容、低可信转载作为核心依据。请在输出中尽量提供可追溯出处，并明确区分：1. 已证实事实 2. 基于资料的归纳 3. 尚待验证的推断。对于关键判断，请附上对应来源信息。",
      "expected_use": "用于立项依据和创新点章节。"
    },
    {
      "need_id": "R2",
      "topic": "科研写作支持项目的评价设计、实施条件与可行性依据",
      "why_needed": "用于补强研究方案、研究基础与可行性章节，避免框架看起来完整但方法与实施条件空心化。",
      "evidence_type": "方法依据 + 可行性支撑",
      "priority": 2,
      "retrieval_route": "either",
      "notebooklm_applicability": {
        "suitable_if_sources_already_loaded": true,
        "recommended_notebook_scope": "若已有教育评估、系统验证或教学改革实施案例 notebook，可先核验",
        "query_goal": "extract"
      },
      "source_requirements": {
        "preferred_source_types": [
          "高质量综述",
          "方法论文",
          "教育评估研究",
          "实证研究设计论文",
          "代表性教改项目案例"
        ],
        "avoid_source_types": [
          "无署名网页",
          "营销内容",
          "低可信二手转载",
          "无原始出处的总结文"
        ],
        "recency_requirement": "近5年为主，必要时补经典方法框架",
        "authority_requirement": "优先核心期刊、权威案例与方法综述",
        "language_scope": "中英均可",
        "min_source_count": 5
      },
      "citation_expectations": {
        "must_provide_traceable_citations": true,
        "must_distinguish_fact_from_inference": true,
        "must_include_source_for_key_claims": true,
        "preferred_citation_granularity": "至少提供作者、年份、题目、来源；如可行，补充 DOI、链接或项目编号"
      },
      "suggested_prompt": "请仅基于当前 notebook 已收录的 sources 回答，不要引入外部资料。请围绕‘科研写作支持项目的评价设计、实施条件与可行性依据’完成以下任务：1. 提取最直接相关研究或案例；2. 总结已证实的评价设计和实施条件；3. 归纳哪些依据可直接用于研究方案与可行性章节；4. 明确证据不足部分；5. 给出可追溯出处。若 notebook 内证据不足，请明确指出哪些部分需要转外部 deep research。",
      "expected_use": "用于研究方案、研究基础与可行性章节。"
    }
  ],
  "evidence_status": {
    "overall": "partially_verified",
    "citation_needed": true,
    "citation_notes": [
      "当前 framework 已给出写作结构，但立项依据、创新点、研究方案和可行性章节仍依赖外部证据补齐。",
      "ready_to_draft=true 仅表示结构上可以先写，不表示事实性内容已具备引用支撑。"
    ]
  },
  "notes": [
    "该样例专门验证 S3，因此 framework 为主对象。",
    "goal_content_bundle、innovation_bundle、review_bundle 留空是阶段性设计，不代表字段缺失。"
  ]
}
```

## Evaluation

- Trigger correctness: Pass
- Framework completeness: Pass
- Writing-order usefulness: Pass
- Evidence discipline: Pass
- Residual issues:
  - `recommended_writing_order` 与 `framework[].order` 可以同时存在：前者服务写作推进，后者服务章节蓝图排序；后续 benchmark 不应误判为重复字段。
  - `ready_to_draft=true` 的章节在实际使用时仍需配合 `evidence_status` 阅读，不能被理解成已可直接写成事实性正文。
  - 若后续做自动 benchmark，需要允许 `framework` 中同时出现 ready 和 not-ready 章节，这恰恰是该子技能应做出的区分。

## Verdict

该样例符合 S3 的职责定义，能够给出章节蓝图、推荐写作顺序和 evidence-aware 的开写判断，并把证据缺口转成 research_needs。