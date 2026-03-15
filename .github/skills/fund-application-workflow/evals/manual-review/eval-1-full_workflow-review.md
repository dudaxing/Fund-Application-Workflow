# Eval 1 Review

## Eval Prompt

我准备申报一个省教育厅教改项目，方向是"大模型支持研究生学术写作训练"，现在只有一些零散想法：想结合真实写作任务、反馈循环和教师干预，但还没想清楚研究对象、边界和成果形式。请按 full_workflow 先帮我整理成 project_card，并识别最值得优先补的 research_needs。要求高可靠性，不要直接替我编造研究现状。

## Manual Output

```json
{
  "skill_name": "基金申报全流程协同写作 Skill",
  "status": "ok",
  "confidence": "medium",
  "selected_subskill": "S1",
  "project_card": {
    "project_name": "",
    "project_theme": "大模型支持研究生学术写作训练",
    "project_type": "省教育厅教改项目",
    "research_object": [
      "研究生学术写作训练过程",
      "大模型支持下的写作反馈与教师干预机制"
    ],
    "core_problem": "当前项目想法已经指向'真实写作任务 + 反馈循环 + 教师干预'的训练模式，但尚未明确研究对象边界、干预单元、效果评价口径和最终成果形态，暂时不足以直接展开为正式申报书正文。",
    "scope_boundary": [
      "当前尚未明确训练对象是硕士、博士还是混合群体",
      "当前尚未明确训练任务聚焦开题、综述、初稿还是全过程修订",
      "当前尚未明确项目更偏教学模式研究、系统设计研究还是成效评价研究"
    ],
    "possible_goals": [
      "构建面向研究生学术写作训练的大模型支持方案",
      "研究大模型反馈、教师反馈与学生修订行为之间的协同机制",
      "形成可用于教改项目申报的训练模式、工具原型或课程实施方案"
    ],
    "possible_methods": [
      "真实写作任务驱动的教学设计",
      "过程性写作样本收集与修订轨迹分析",
      "教师干预与大模型反馈对比或协同实验"
    ],
    "existing_foundation": [],
    "expected_outputs": [
      "研究生学术写作训练模式",
      "交互式支持流程或工具原型",
      "教改项目申请书中的研究框架与实施方案"
    ],
    "missing_information": [
      "研究对象的具体范围，如硕士/博士、学科类型、年级阶段",
      "写作训练面向的具体任务类型，如开题、摘要、文献综述、论文初稿、修订",
      "项目边界是教学模式研究、系统设计研究还是教学成效评价研究",
      "预期成果形式及考核口径",
      "已有课程基础、样本来源与实施条件"
    ],
    "to_be_verified": [
      "该方向在近五年教改和学术写作支持研究中的代表性工作与空白",
      "大模型用于学术写作训练的有效性与风险证据",
      "类似项目在政策层面或高校实践层面的现实需求支撑"
    ],
    "inferences": [
      "该项目更适合定位为'教学模式与支持机制研究'，而不是纯算法创新项目",
      "若后续缺少权威文献和政策支撑，立项依据部分会明显偏弱"
    ],
    "project_preliminary_positioning": {
      "direction": "研究生学术写作训练中的大模型支持机制",
      "type_guess": "教改项目 / 教学支持机制研究",
      "maturity_level": "idea"
    }
  },
  "questions": [],
  "framework": [],
  "goal_content_bundle": {},
  "innovation_bundle": {},
  "review_bundle": {},
  "priority_revisions": [],
  "research_needs": [
    {
      "need_id": "R1",
      "topic": "近五年大模型或智能写作系统支持研究生/高校学术写作训练的代表性研究、主要做法与不足",
      "why_needed": "用于建立立项依据，说明该方向已有探索到什么程度、还缺什么，以及本项目的切入点是否成立。",
      "evidence_type": "研究现状综述 + 代表性系统/课程研究比较",
      "priority": 1,
      "retrieval_route": "external_deep_research",
      "notebooklm_applicability": {
        "suitable_if_sources_already_loaded": true,
        "recommended_notebook_scope": "若用户已有学术写作支持系统、AWE、LLM教育应用等文献 notebook，可先在其中核验",
        "query_goal": "compare"
      },
      "source_requirements": {
        "preferred_source_types": [
          "高质量综述",
          "高水平期刊论文",
          "教育技术与写作研究代表性论文",
          "代表性系统/课程论文",
          "权威机构报告"
        ],
        "avoid_source_types": [
          "无署名网页",
          "营销内容",
          "低可信二手转载",
          "无原始出处的总结文"
        ],
        "recency_requirement": "近5年为主，必要时补充经典写作支持研究",
        "authority_requirement": "优先 SSCI/CSSCI、教育技术核心期刊、权威会议与综述",
        "language_scope": "中英均可",
        "min_source_count": 5
      },
      "citation_expectations": {
        "must_provide_traceable_citations": true,
        "must_distinguish_fact_from_inference": true,
        "must_include_source_for_key_claims": true,
        "preferred_citation_granularity": "至少提供作者、年份、题目、来源；如可行，补充 DOI 或链接"
      },
      "suggested_prompt": "请优先检索近五年关于大模型、智能写作系统或自动写作反馈支持研究生/高校学术写作训练的高质量综述、核心论文和代表性系统研究。请梳理：1. 主要研究对象与训练场景；2. 常见支持方式，如反馈、修订、教师协同；3. 已有研究的主要效果证据；4. 现有研究的不足与空白；5. 哪些结论可直接用于教改项目立项依据。请优先使用可靠来源，包括高质量综述、权威期刊/会议论文、官方政策文件、官方统计数据库、代表性项目资料。请避免将无署名网页、营销内容、低可信转载作为核心依据。请在输出中尽量提供可追溯出处，并明确区分：1. 已证实事实 2. 基于资料的归纳 3. 尚待验证的推断。对于关键判断，请附上对应来源信息。",
      "expected_use": "用于撰写立项依据中的研究现状、差距定位和项目切入点。"
    },
    {
      "need_id": "R2",
      "topic": "研究生学术写作训练的现实痛点、政策导向与教学需求证据",
      "why_needed": "用于说明该教改项目的现实必要性，避免把常识性判断直接写成已证实事实。",
      "evidence_type": "政策依据 + 教学需求证据 + 权威报告",
      "priority": 2,
      "retrieval_route": "either",
      "notebooklm_applicability": {
        "suitable_if_sources_already_loaded": true,
        "recommended_notebook_scope": "若 notebook 已包含研究生培养政策、学术写作课程、教育数字化资料，可先核验",
        "query_goal": "synthesize"
      },
      "source_requirements": {
        "preferred_source_types": [
          "官方政策文件",
          "高校研究生培养文件",
          "官方统计数据库",
          "高质量综述",
          "教学改革研究论文"
        ],
        "avoid_source_types": [
          "无署名网页",
          "营销内容",
          "低可信二手转载",
          "无原始出处的总结文"
        ],
        "recency_requirement": "近5年为主，必要时补充仍在生效的重要政策",
        "authority_requirement": "优先教育部、学位与研究生教育相关官方来源、高校正式文件、核心期刊",
        "language_scope": "中文为主，必要时补英文教育研究",
        "min_source_count": 5
      },
      "citation_expectations": {
        "must_provide_traceable_citations": true,
        "must_distinguish_fact_from_inference": true,
        "must_include_source_for_key_claims": true,
        "preferred_citation_granularity": "至少提供机构、年份、文件或论文题目、来源；如可行，补充链接"
      },
      "suggested_prompt": "请优先基于当前 notebook 已收录的 sources 回答，不要引入外部资料。请围绕'研究生学术写作训练的现实痛点、政策导向与教学需求'完成以下任务：1. 提取最直接相关的政策、报告和研究；2. 总结已经证实的事实性信息；3. 归纳这些资料共同支持的需求判断；4. 明确哪些判断仍只是推断；5. 给出可追溯的出处线索。若 notebook 内证据不足，请明确指出哪些部分需要转外部 deep research。",
      "expected_use": "用于支撑项目必要性、教学改革现实意义和问题提出部分。"
    }
  ],
  "evidence_status": {
    "overall": "insufficient_evidence",
    "citation_needed": true,
    "citation_notes": [
      "当前仅有用户口头设想，研究现状和现实需求尚未完成外部核验。",
      "立项依据部分至少需要补近5年代表性研究、政策依据或教学需求证据。"
    ]
  },
  "notes": [
    "当前结果定位为项目底稿，不是正式申报书正文。",
    "下一步宜先补证据，再进入 clarifying gaps 或 build outline。"
  ]
}
```

## Evaluation

- Trigger correctness: Pass
- Structure compliance: Pass
- Evidence discipline: Pass
- Research routing quality: Pass
- Residual issues:
 - 如果后续要做自动断言，需明确允许 `research_needs` 为 1 到 3 条，而不是固定 2 条。
 - `goal_content_bundle`、`innovation_bundle`、`review_bundle` 为空是符合当前阶段预期的，因为该样例只验证 S1 起步梳理，不要求提前产出后续阶段对象。

## Verdict

该样例符合收敛后的 canonical `project_card` schema，且保留了空的后续 bundle 作为阶段占位，没有越界提前产出不属于 S1 的对象。
