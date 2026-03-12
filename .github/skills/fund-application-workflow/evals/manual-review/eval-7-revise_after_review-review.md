# Eval 7 Review

## Eval Prompt

我们刚收到内部预审意见，主要问题有三条：一是"创新点写得像功能堆砌"，二是"缺少近五年国内外相关系统对比"，三是"研究内容和技术路线边界不清"。请按 revise_after_review 帮我梳理优先修订重点，并判断哪些问题要回到 clarify_gaps、expand_goals、extract_innovations。还请生成对应的 research_needs。

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
          "预审意见已经明确指出了当前文本最脆弱的创新性表达位置。"
        ],
        "major_issues": [
          "'创新点像功能堆砌'说明当前文本把系统功能列表误写成了创新性论证。",
          "缺少近五年国内外相关系统比较，导致创新点没有差异参照系。"
        ],
        "risk_level": "high"
      },
      {
        "reviewer_focus": "目标与方法闭环",
        "strengths": [
          "预审意见已经把问题收敛到'研究内容和技术路线边界不清'这一核心结构缺陷。"
        ],
        "major_issues": [
          "研究内容与技术路线边界不清，意味着当前文本很可能把任务、方法、系统功能混写在一起。",
          "若不回到目标与内容展开阶段重整结构，后续即使补文献，也难以真正解决闭环问题。"
        ],
        "risk_level": "high"
      },
      {
        "reviewer_focus": "研究基础与可行性",
        "strengths": [
          "当前问题主要集中在论证与结构层面，尚未直接暴露不可实施的硬伤。"
        ],
        "major_issues": [
          "如果相关系统比较和研究边界不清，可行性章节也会被拖弱，因为评审无法判断项目究竟是在做何种类型的研究。"
        ],
        "risk_level": "medium"
      }
    ],
    "overall_judgement": "当前修订任务的重点不是微调措辞，而是先通过相关工作比较和结构重整，重新建立'研究问题—研究内容—技术路线—创新点'之间的对应关系。若只在原文上局部润色，预审意见中的三类问题很可能会继续保留。"
  },
  "priority_revisions": [
    {
      "revision_item": "先补近五年相关系统和研究的比较材料，再重写创新点",
      "reason": "没有差异参照，创新点只能落成'功能堆砌'，这是当前最核心的问题。",
      "priority": 1
    },
    {
      "revision_item": "回到 expand_goals，重整研究内容模块与技术路线边界",
      "reason": "研究内容和技术路线边界不清属于结构性缺陷，不能靠局部润色解决。",
      "priority": 2
    },
    {
      "revision_item": "回到 clarify_gaps，明确项目究竟聚焦哪些支持环节和评价逻辑",
      "reason": "若对象边界、支持环节和评价逻辑不明确，后续创新点和方案都会继续漂移。",
      "priority": 3
    }
  ],
  "research_needs": [
    {
      "need_id": "R1",
      "topic": "近五年国内外科研写作支持系统、AWE 和 LLM 写作辅助研究的系统比较",
      "why_needed": "用于重写创新点，明确本项目到底与哪些已有做法不同，以及哪些差异是可辩护的。",
      "evidence_type": "相关工作比较 + 代表性系统综述",
      "priority": 1,
      "retrieval_route": "external_deep_research",
      "notebooklm_applicability": {
        "suitable_if_sources_already_loaded": true,
        "recommended_notebook_scope": "若已有写作支持系统、AWE 或 LLM 教育应用 notebook，可先核验已有来源",
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
      "suggested_prompt": "请系统检索近五年国内外科研写作支持系统、AWE、LLM 写作辅助与交互式写作反馈研究。请重点输出：1. 代表性系统及其支持环节；2. 各研究的核心方法与评价方式；3. 现有研究的共同不足；4. 哪些差异可以真正支撑新项目创新点，哪些只是功能层面的不同。请优先使用可靠来源，包括高质量综述、权威期刊/会议论文、官方政策文件、官方统计数据库、代表性项目资料。请避免将无署名网页、营销内容、低可信转载作为核心依据。请在输出中尽量提供可追溯出处，并明确区分：1. 已证实事实 2. 基于资料的归纳 3. 尚待验证的推断。对于关键判断，请附上对应来源信息。",
      "expected_use": "用于回到 extract_innovations，重写创新点。"
    },
    {
      "need_id": "R2",
      "topic": "科研写作支持项目中研究内容、技术路线与评价设计的常见边界划分",
      "why_needed": "用于解决'研究内容和技术路线边界不清'的问题，帮助重新组织申请书结构。",
      "evidence_type": "方法结构参考 + 研究设计依据",
      "priority": 2,
      "retrieval_route": "either",
      "notebooklm_applicability": {
        "suitable_if_sources_already_loaded": true,
        "recommended_notebook_scope": "若已有研究设计、系统验证、教育评估类 notebook，可先核验",
        "query_goal": "synthesize"
      },
      "source_requirements": {
        "preferred_source_types": [
          "高质量综述",
          "方法论文",
          "教育评估研究",
          "系统设计研究",
          "代表性实证研究"
        ],
        "avoid_source_types": [
          "无署名网页",
          "营销内容",
          "低可信二手转载",
          "无原始出处的总结文"
        ],
        "recency_requirement": "近5年为主，必要时补经典方法框架",
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
      "suggested_prompt": "请仅基于当前 notebook 已收录的 sources 回答，不要引入外部资料。请围绕'科研写作支持项目中研究内容、技术路线与评价设计的边界划分'完成以下任务：1. 提取最相关研究或案例；2. 总结已证实的结构组织方式；3. 归纳哪些内容应归入研究内容，哪些应归入技术路线或评价设计；4. 指出证据不足部分；5. 提供可追溯出处。若 notebook 内证据不足，请明确指出哪些部分需要转外部 deep research。",
      "expected_use": "用于回到 expand_goals，重整研究内容与技术路线边界。"
    }
  ],
  "evidence_status": {
    "overall": "partially_verified",
    "citation_needed": true,
    "citation_notes": [
      "当前输出基于预审意见进行结构诊断，修订优先级判断可靠，但相关工作比较和结构重整仍需文献依据支撑。",
      "revision 路由已明确，但进入下一轮写作前应先完成 R1 和 R2 对应的调研或核验。"
    ]
  },
  "notes": [
    "该样例专门验证 revise_after_review 场景，因此 selected_subskill 仍为 S6，但明确给出了应回到的后续子技能方向。",
    "该阶段的关键不在于直接重写正文，而在于先决定修订顺序和回流路径。",
    "建议回流顺序：先 S2 clarify_gaps，再 S4 expand_goals，最后 S5 extract_innovations。"
  ]
}
```

## Evaluation

- Trigger correctness: Pass
- Cross-stage routing clarity: Pass
- Revision prioritization: Pass
- Evidence discipline: Pass
- Residual issues:
  - 该样例已经体现应回到 S2、S4、S5，但如果后续要做自动 benchmark，需要把"是否指出回流路径"也纳入断言范围。
  - 当前 `questions` 留空是合理的，因为本样例更偏修订编排；如果在真实运行中信息缺口更大，也可能同时产出追问问题。

## Verdict

该样例符合 revise_after_review 场景的预期，能够以 S6 为主输出评审后修订编排，并明确指出哪些问题要回到 clarify_gaps、expand_goals、extract_innovations，形成真正的跨阶段协同回路。
