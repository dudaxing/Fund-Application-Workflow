# Eval 6 Review

## Eval Prompt

我已经写了一版摘要："本项目拟面向高校教师科研写作场景，构建基于大模型的智能辅助平台，提升写作效率与成果质量，并形成可推广的教学与科研支持方案。"请按 review_draft 模拟评审，从创新性、目标与方法闭环、研究基础与可行性三个视角指出主要问题、风险等级和优先修订项。若有问题需要靠补文献或政策数据解决，请直接转成 research_needs。

## Manual Output

```json
{
  "skill_name": "基金申报全流程协同写作 Skill",
  "status": "ok",
  "confidence": "medium",
  "selected_subskill": "S6",
  "project_card": {},
  "questions": [],
  "framework": [],
  "goal_content_bundle": {},
  "innovation_bundle": {},
  "review_bundle": {
    "reviewers": [
      {
        "reviewer_focus": "问题与创新性",
        "strengths": [
          "选题具有现实相关性，回应了高校教师科研写作支持场景中的实际需求。",
          "摘要已经初步呈现'平台 + 支持方案'的应用方向。"
        ],
        "major_issues": [
          "摘要中的创新性尚未体现，'构建基于大模型的智能辅助平台'容易被评审理解为技术堆砌或常规应用。",
          "没有说明与现有写作支持系统、AWE 系统或通用 LLM 写作辅助方案相比的实质差异。",
          "'提升写作效率与成果质量'属于目标口号，不等于创新点。"
        ],
        "risk_level": "high"
      },
      {
        "reviewer_focus": "目标与方法闭环",
        "strengths": [
          "摘要至少给出了一个明确应用场景，即高校教师科研写作。"
        ],
        "major_issues": [
          "研究目标、研究内容、技术方案和评价方式没有形成闭环。",
          "摘要没有说明是做机制研究、系统设计研究、干预实验研究，还是效果评价研究。",
          "'提升效率与质量'缺乏可评估指标和验证方法。"
        ],
        "risk_level": "high"
      },
      {
        "reviewer_focus": "研究基础与可行性",
        "strengths": [
          "该主题具备一定可实施性，只要团队已有相关技术或写作支持基础，就有展开空间。"
        ],
        "major_issues": [
          "摘要完全没有体现研究基础、样本来源、应用场景或已有工作积累。",
          "没有说明平台建设依托什么资源、服务对象是谁、如何开展验证。",
          "若申报文本后续仍维持这一抽象程度，可行性部分会明显偏弱。"
        ],
        "risk_level": "medium"
      }
    ],
    "overall_judgement": "该摘要具备选题方向，但当前更像一个宽泛设想，而不是可提交评审的项目摘要。核心风险在于创新性未被证明、目标与方法不闭环、研究基础不可见。若不补足比较文献、评价设计和实施基础，评审很可能认为项目泛化、落不实。"
  },
  "priority_revisions": [
    {
      "revision_item": "明确项目的核心研究问题和创新点，不要只写平台建设目标",
      "reason": "当前表述缺少与现有工作的差异化定位，容易被评审认为创新性不足。",
      "priority": 1
    },
    {
      "revision_item": "补出目标—内容—方法—评价指标的闭环结构",
      "reason": "摘要目前没有说明如何验证所谓'效率与质量提升'，缺少可评估性。",
      "priority": 2
    },
    {
      "revision_item": "增加研究基础与实施条件线索",
      "reason": "若没有团队基础、样本来源和场景依托，可行性会明显不足。",
      "priority": 3
    }
  ],
  "research_needs": [
    {
      "need_id": "R1",
      "topic": "近五年高校教师或学术写作支持系统的代表性研究、功能边界与局限",
      "why_needed": "用于证明本项目与现有写作支持系统相比的差异，并为创新点表述提供比较基础。",
      "evidence_type": "代表性系统比较 + 研究现状综述",
      "priority": 1,
      "retrieval_route": "external_deep_research",
      "notebooklm_applicability": {
        "suitable_if_sources_already_loaded": true,
        "recommended_notebook_scope": "若已有写作支持系统或学术写作研究 notebook，可先核验已有来源",
        "query_goal": "compare"
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
        "recency_requirement": "近5年为主，必要时补经典系统论文",
        "authority_requirement": "优先高水平期刊、会议与权威综述",
        "language_scope": "中英均可",
        "min_source_count": 5
      },
      "citation_expectations": {
        "must_provide_traceable_citations": true,
        "must_distinguish_fact_from_inference": true,
        "must_include_source_for_key_claims": true,
        "preferred_citation_granularity": "至少提供作者、年份、题目、来源；如可行，补充 DOI 或链接"
      },
      "suggested_prompt": "请系统检索近五年高校教师科研写作支持、学术写作辅助系统、AWE 与 LLM 写作支持相关的代表性研究和综述。请比较：1. 主要支持对象；2. 支持环节；3. 评价指标；4. 已知局限；5. 哪些空白可以支撑一个新的项目创新点。请优先使用可靠来源，包括高质量综述、权威期刊/会议论文、官方政策文件、官方统计数据库、代表性项目资料。请避免将无署名网页、营销内容、低可信转载作为核心依据。请在输出中尽量提供可追溯出处，并明确区分：1. 已证实事实 2. 基于资料的归纳 3. 尚待验证的推断。对于关键判断，请附上对应来源信息。",
      "expected_use": "用于压实创新性论证与现有工作比较部分。"
    },
    {
      "need_id": "R2",
      "topic": "科研写作效率与质量提升的常用评价指标、测量方式与实证研究设计",
      "why_needed": "用于把摘要中的'提升效率与成果质量'落成可验证的研究闭环，避免目标口号化。",
      "evidence_type": "方法依据 + 指标设计 + 实证评价参考",
      "priority": 2,
      "retrieval_route": "either",
      "notebooklm_applicability": {
        "suitable_if_sources_already_loaded": true,
        "recommended_notebook_scope": "若已有教育评估、写作评价、研究设计类 notebook，可先核验",
        "query_goal": "extract"
      },
      "source_requirements": {
        "preferred_source_types": [
          "高质量综述",
          "方法论文",
          "教育评估研究",
          "实验设计论文",
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
      "suggested_prompt": "请仅基于当前 notebook 已收录的 sources 回答，不要引入外部资料。请围绕'科研写作效率与质量提升的评价指标和研究设计'完成以下任务：1. 提取最相关研究；2. 总结已证实的常用指标与方法；3. 归纳这些指标适合写作支持项目的哪些环节；4. 明确哪些判断只是推断或证据不足；5. 给出可追溯出处。若 notebook 证据不足，请明确指出应转外部 deep research。",
      "expected_use": "用于补强目标与方法闭环，以及摘要或正文中的评价设计。"
    }
  ],
  "evidence_status": {
    "overall": "partially_verified",
    "citation_needed": true,
    "citation_notes": [
      "摘要中的风险判断来自结构分析，不是基于完整项目材料的最终结论。",
      "创新性比较和评价设计仍需补文献支撑，才能进入正式申报书正文。"
    ]
  },
  "notes": [
    "该评审输出侧重发现硬伤和后续修订方向。",
    "如果用户补充 project_card、研究基础和相关工作摘要，评审结果可进一步细化。"
  ]
}
```

## Evaluation

- Trigger correctness: Pass
- Reviewer coverage: Pass
- Actionability: Pass
- Evidence discipline: Pass
- Residual issues:
 - 该输出在无完整草稿条件下，评审深度合理，但仍偏摘要级，后续要结合更长文本复核。
 - 若正式做自动 benchmark，需要明确允许 `evidence_status.overall = partially_verified`，因为这里的评审问题并非全部依赖外部事实本身。
 - `review_bundle` 已符合 canonical schema；`goal_content_bundle` 与 `innovation_bundle` 留空是因为本样例专门验证 S6，不强行补写其他阶段对象。

## Verdict

该样例符合 canonical `review_bundle` schema 和 S6 的职责定义，能够给出三类 reviewer 视角、优先修订项，并将可补强的问题转成 research_needs，没有把结构性问题伪装成单纯补文献即可解决。
