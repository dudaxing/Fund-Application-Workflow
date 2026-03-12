# Eval 5 Review

## Eval Prompt

下面是我目前概括的项目内容：研究大模型如何支持高校教师在选题、文献整合、初稿生成、修订反馈中的连续写作过程，并设计一个交互式支持系统。请按 extract_innovations 提炼 2 到 4 条可辩护创新点，不要把热门技术本身当创新点；如果某条创新点站不住，请明确标风险并告诉我缺什么对比文献。

## Manual Output

```json
{
  "skill_name": "基金申报全流程协同写作 Skill",
  "status": "ok",
  "confidence": "medium",
  "selected_subskill": "S5",
  "project_card": {},
  "questions": [],
  "framework": [],
  "goal_content_bundle": {},
  "innovation_bundle": {
    "innovations": [
      {
        "title": "面向连续科研写作过程的支持对象重构",
        "innovation_type": "object",
        "statement": "相较于将写作支持聚焦于单次文本生成或单环节反馈的已有方案，本项目尝试把支持对象重构为'选题—文献整合—初稿生成—修订反馈'的连续科研写作过程。",
        "supporting_basis": [
          "用户当前项目内容明确强调连续过程而非单次生成",
          "若已有研究大多集中在单轮反馈或局部写作任务，则该对象重构具备差异化潜力"
        ],
        "risk_alert": "该创新点是否成立，高度依赖对现有写作支持系统覆盖范围的系统比较；若已有研究已经覆盖全过程支持，则此点会被削弱。"
      },
      {
        "title": "大模型建议、用户操作与修订反馈的协同机制设计",
        "innovation_type": "mechanism",
        "statement": "项目的潜在创新不在于使用大模型本身，而在于如何设计大模型建议、用户主动操作与修订反馈之间的协同机制，使系统真正服务于科研写作过程中的多轮迭代。",
        "supporting_basis": [
          "项目描述中不仅提到生成支持，还强调修订反馈与交互式系统",
          "若现有研究更偏一次性建议生成，而较少关注多轮协同，则该机制创新具有可辩护空间"
        ],
        "risk_alert": "如果后续无法把'协同机制'落成明确流程、功能或评价逻辑，这条创新点容易停留在抽象口号层面。"
      },
      {
        "title": "科研写作支持效果的过程性评价框架",
        "innovation_type": "integration",
        "statement": "项目有机会将写作效率、文本质量、修订质量与用户过程行为整合为一套过程性评价框架，而不只是报告一个泛化的'效果提升'结论。",
        "supporting_basis": [
          "项目内容天然涉及多阶段支持与多轮修订",
          "若现有研究通常只考察最终文本表现，该过程性评价框架可形成整合性创新"
        ],
        "risk_alert": "该点需要扎实的方法论和评价指标文献支撑；否则评审可能认为这只是'研究方案完整'而非真正创新。"
      }
    ],
    "overall_innovation_positioning": "这组创新点更适合被定位为'支持对象重构 + 协同机制设计 + 过程性评价整合'的组合式创新，而不是算法创新。"
  },
  "review_bundle": {},
  "priority_revisions": [],
  "research_needs": [
    {
      "need_id": "R1",
      "topic": "现有科研写作支持系统或学术写作辅助研究覆盖了哪些写作环节，是否已经存在全过程支持方案",
      "why_needed": "用于验证'连续科研写作过程支持'是否真构成对象层面的创新，而不是已有做法的重复表述。",
      "evidence_type": "相关工作比较 + 代表性系统覆盖范围核验",
      "priority": 1,
      "retrieval_route": "external_deep_research",
      "notebooklm_applicability": {
        "suitable_if_sources_already_loaded": true,
        "recommended_notebook_scope": "若已有写作支持系统、AWE、LLM写作辅助相关 notebook，可先核验",
        "query_goal": "verify"
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
        "authority_requirement": "优先高水平期刊、会议和权威综述",
        "language_scope": "中英均可",
        "min_source_count": 5
      },
      "citation_expectations": {
        "must_provide_traceable_citations": true,
        "must_distinguish_fact_from_inference": true,
        "must_include_source_for_key_claims": true,
        "preferred_citation_granularity": "至少提供作者、年份、题目、来源；如可行，补充 DOI 或链接"
      },
      "suggested_prompt": "请系统检索近五年科研写作支持系统、学术写作辅助系统、AWE 和 LLM 写作支持研究。请重点核验：1. 现有系统覆盖哪些写作环节；2. 是否已有全过程支持方案；3. 多数研究聚焦单环节还是连续过程；4. 哪些差异足以支撑对象层面的创新点。请优先使用可靠来源，包括高质量综述、权威期刊/会议论文、官方政策文件、官方统计数据库、代表性项目资料。请避免将无署名网页、营销内容、低可信转载作为核心依据。请在输出中尽量提供可追溯出处，并明确区分：1. 已证实事实 2. 基于资料的归纳 3. 尚待验证的推断。对于关键判断，请附上对应来源信息。",
      "expected_use": "用于验证第一条创新点是否可成立。"
    },
    {
      "need_id": "R2",
      "topic": "多轮反馈协同机制与过程性评价框架的代表性研究依据",
      "why_needed": "用于支撑机制创新和评价框架创新，避免把完整方案误写成创新点。",
      "evidence_type": "机制设计比较 + 评价框架依据",
      "priority": 2,
      "retrieval_route": "either",
      "notebooklm_applicability": {
        "suitable_if_sources_already_loaded": true,
        "recommended_notebook_scope": "若已有交互式写作反馈、教育评估或修订研究 notebook，可先核验",
        "query_goal": "compare"
      },
      "source_requirements": {
        "preferred_source_types": [
          "高质量综述",
          "方法论文",
          "交互机制研究",
          "教育评估研究",
          "代表性实证研究"
        ],
        "avoid_source_types": [
          "无署名网页",
          "营销内容",
          "低可信二手转载",
          "无原始出处的总结文"
        ],
        "recency_requirement": "近5年为主，必要时补经典机制与评价研究",
        "authority_requirement": "优先核心期刊、高水平会议与方法综述",
        "language_scope": "中英均可",
        "min_source_count": 5
      },
      "citation_expectations": {
        "must_provide_traceable_citations": true,
        "must_distinguish_fact_from_inference": true,
        "must_include_source_for_key_claims": true,
        "preferred_citation_granularity": "至少提供作者、年份、题目、来源；如可行，补充 DOI 或链接"
      },
      "suggested_prompt": "请仅基于当前 notebook 已收录的 sources 回答，不要引入外部资料。请围绕'多轮反馈协同机制与过程性评价框架'完成以下任务：1. 提取与交互式写作支持最相关研究；2. 总结已证实的协同机制设计与评价维度；3. 归纳哪些做法可支撑机制层或整合层创新；4. 明确哪些部分仍证据不足；5. 提供可追溯出处。若 notebook 内证据不足，请说明应转外部 deep research。",
      "expected_use": "用于压实第二、第三条创新点的可辩护性。"
    }
  ],
  "evidence_status": {
    "overall": "insufficient_evidence",
    "citation_needed": true,
    "citation_notes": [
      "当前 innovation_bundle 基于结构分析与差异化推演，尚未完成对现有工作的系统核验。",
      "若未补充对比文献，创新点只能视为待验证命题，不能写成已证实结论。"
    ]
  },
  "notes": [
    "该样例专门验证 S5，因此 innovation_bundle 为主对象。",
    "project_card、goal_content_bundle、review_bundle 留空是阶段性设计，不代表字段缺失。"
  ]
}
```

## Evaluation

- Trigger correctness: Pass
- Innovation bundle completeness: Pass
- Risk marking discipline: Pass
- Evidence discipline: Pass
- Residual issues:
  - 当前三条创新点都仍依赖后续文献核验，自动 benchmark 不能把'创新点数量够了'误判为通过。
  - 若实际运行时已有 `related_work_summary`，输出还应进一步引用这些现有材料，而不是只给方向性判断。

## Verdict

该样例符合 canonical `innovation_bundle` schema 和 S5 的职责定义，创新点没有把热门技术本身当创新，且每条都带了 `risk_alert` 与对比文献型 research_needs。
