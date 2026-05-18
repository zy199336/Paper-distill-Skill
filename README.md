# Paper distill Skill Builder 文章蒸馏 skill

## 中文说明

本项目用于从一组精选的高质量论文 PDF 中，构建两个可复用的 Codex/Claude/OpenCode 写作技能：

- `writing-paper-outline`：根据研究主题、论文想法、方法、数据或初步设想，生成论文大纲、章节结构、图表规划、实验规划和审稿风险检查。
- `writing-paper`：根据大纲、草稿、bullet points 或某一小节“大概要写什么”，生成、改写、润色或重构论文正文。

本项目不是普通文献综述工具。它的目标是从论文中抽取可迁移的结构规则、写作规则、章节功能、问题建模方式、方法组织方式、实验设计模式、图表功能、claim control 和 reviewer risk。

### 自动构建流程

#### 1. 安装 `paper-skill-builder`

告诉 Codex/Claude/OpenCode：

```text
请安装当前项目文件夹下的 paper-skill-builder skill。
```

安装后先重启一次 Codex/Claude/OpenCode，让 `paper-skill-builder` 被识别。

#### 2. 放置参考论文

将高质量学术论文 PDF 放入：

```text
input_papers/
```

<p><strong><span style="color:red;">PDF 数量应精，不宜多。请选取和你想写文章最相关、质量最高的论文,建议控制在 30 篇以内。</span></strong></p>
`PDF 数量应精，不宜多。请选取和你想写文章最相关、质量最高的论文,建议控制在 30 篇以内。`

也可以使用绝对路径。如果提供 `input_papers`，脚本会在需要时递归扫描其中的 PDF。

#### 3. 让 Codex/Claude/OpenCode 自动创建两个关键 skill

重启 Codex/Claude/OpenCode 并确认 `paper-skill-builder` 可用后，可以这样说：

```text
请使用 @paper-skill-builder。
我的参考文件都放在 input_papers 文件夹下，帮我按 paper-skill-builder 创建两个关键 skill。
```

预期行为：

- 如果没有提供论文目录，Codex/Claude/OpenCode 会先询问论文目录。
- Codex/Claude/OpenCode 运行 `python scripts/build_manifest.py --paper-dir "<paper-folder>"`。
- Codex/Claude/OpenCode 运行 `python scripts/create_extract_templates.py`。
- Codex/Claude/OpenCode 使用 `paper-corpus-analyzer` 工作流填写所有 included papers 的 `data/extracts/combined/PAPER_ID.md`。
- Codex/Claude/OpenCode 运行 `python scripts/validate_extracts.py`；如果抽取文件不完整，应补齐后重新校验。
- Codex/Claude/OpenCode 运行 `python scripts/synthesize_rules.py`。
- Codex/Claude/OpenCode 运行 `python scripts/sync_skills_from_synthesis.py`。
- Codex/Claude/OpenCode 运行 `python scripts/install_generated_skills.py`。
- Codex/Claude/OpenCode 运行 `python scripts/run_basic_checks.py --paper-dir "<paper-folder>"`。
- Codex/Claude/OpenCode 汇报 manifest、extracts、synthesis、已安装 skill 名称，并提醒重启。

成功安装后，Codex/Claude/OpenCode 应提示：

```text
已安装 writing-paper-outline 和 writing-paper。请重启 Codex/Claude/OpenCode，让新安装的两个 skill 被识别。
```

#### 4. 重启 Codex/Claude/OpenCode

生成的两个 skill 安装完成后，需要重启 Codex/Claude/OpenCode。重启后可以直接调用：

```text
@writing-paper-outline
@writing-paper
```

### 重启后的调用示例

#### 1. 使用 `@writing-paper-outline` 架构文章框架

```text
请使用 @writing-paper-outline，帮我为论文设计大纲。

主题是：面向通航空域有人/无人协同运行的动态风险管控与轨迹规划。

方法包括风险场建模、TLS约束、战术冲突解脱和仿真验证。

重点帮我设计 Problem Formulation、Methodology、Experiment Design 和图表规划。
```

预期输出：

- 文章定位；
- 叙事主线；
- section / subsection 结构；
- Problem Formulation 设计；
- Methodology 设计；
- Experiment Design；
- 图表规划；
- Main text vs Appendix 建议；
- 审稿风险检查。

#### 2. 使用 `@writing-paper` 写作草稿

```text
请使用 @writing-paper skill。

下面是论文大纲中的一个小节：

Section 3.1 Operational scenario and problem description

本小节要写的内容：
- 描述通航机场管制空域中的有人/无人协同运行场景；
- 有人机包括训练飞机、通航飞机和直升机；
- 无人机包括中大型无人机试飞、巡检和物流任务；
- 不同飞行器在速度、机动能力、通信链路、监视能力和运行意图上存在异质性；
- 现有基于固定间隔或单一冲突检测的方法难以支撑动态风险管控；
- 本文需要把该场景抽象为一个时空耦合、风险约束下的轨迹规划问题。

请写成英文论文正文，要求：
1. 不要直接上公式；
2. 先用通俗但学术的语言描述场景和问题；
3. 最后一段自然过渡到 mathematical formulation；
4. 输出修改说明和审稿风险提醒。
```

预期输出：

- 英文论文正文；
- 修改说明；
- 与大纲的对应关系；
- 风格适配说明；
- 仍需补充的信息；
- 审稿风险提醒。

#### 3. 使用 `@writing-paper` 润色或改写草稿

```text
请使用 @writing-paper skill。

目标小节：Methodology overview

请把下面这段中文草稿改写成英文论文正文，并增强可复现性、模块清晰度和输入输出逻辑。

中文草稿：
本文提出一种面向低空空域动态风险管控的轨迹规划方法。首先根据无人机、有人机和地面风险源构建风险场，然后用风险场指导轨迹搜索。为了避免轨迹进入高风险区域，我们加入了 TLS 约束。同时，为了提高实时性，我们采用网格化搜索和局部重规划机制。当出现冲突风险时，系统会根据风险大小选择绕飞、等待或者高度调整等解脱动作。

请输出：
1. 英文正文；
2. 结构修改说明；
3. 还需要补充哪些技术细节；
4. 审稿风险提醒。
```

预期输出：

- 英文正文；
- 结构修改说明；
- 需要补充的技术细节；
- 审稿风险提醒；
- 对输入、输出、模块顺序、TLS 约束、风险场、局部重规划和冲突解脱逻辑的可复现性提示。

### 额外说明

- 可以通过修改 `data/paper_manifest.xlsx` 中的权重和 inclusion 字段，自适应控制不同论文对文章蒸馏结果的影响强度。
- Manifest 主要用于记录、追踪和人工可选筛选，不作为默认筛选机制。
- 无法判断的期刊、领域、论文类型等信息应标记为 `unknown`，不要编造。
- 不要复制论文长段原文。
- 不要生成普通文献综述。

---

## English README

This project builds two reusable Codex/Claude/OpenCode writing skills from a focused set of high-quality academic paper PDFs:

- `writing-paper-outline`: generates manuscript outlines, section structures, figure/table plans, experiment plans, and reviewer-risk checks from a research topic, paper idea, method, data, or preliminary concept.
- `writing-paper`: generates, rewrites, polishes, or restructures manuscript prose from an outline, draft, bullet points, or a short description of what a section should cover.

This project is not a normal literature-review tool. Its purpose is to extract transferable structural rules, writing rules, section functions, problem-formulation patterns, method-organization patterns, experiment-design patterns, figure/table functions, claim-control rules, and reviewer-risk signals from selected papers.

### Automatic Build Workflow

#### 1. Install `paper-skill-builder`

Tell Codex/Claude/OpenCode:

```text
Please install the paper-skill-builder skill from the current project folder.
```

After installation, restart Codex/Claude/OpenCode once so `paper-skill-builder` can be discovered.

#### 2. Place Reference Papers

Put high-quality academic PDF papers in:

```text
input_papers/
```

PDF quantity should be selective, not large. Choose the papers that are most relevant to the manuscript you want to write and highest in quality. A focused set of around 30 or fewer papers is recommended, but this is a quality suggestion rather than a hard limit.

You can also use an absolute folder path. If you provide `input_papers`, the scripts will recursively scan it for PDFs when needed.

#### 3. Ask Codex/Claude/OpenCode To Create The Two Key Skills

After restarting Codex/Claude/OpenCode and confirming that `paper-skill-builder` is available, use a prompt like:

```text
Please use @paper-skill-builder.
My reference papers are stored in the input_papers folder. Please use paper-skill-builder to create the two key skills.
```

Expected behavior:

- If no paper folder is provided, Codex/Claude/OpenCode asks for the paper folder first.
- Codex/Claude/OpenCode runs `python scripts/build_manifest.py --paper-dir "<paper-folder>"`.
- Codex/Claude/OpenCode runs `python scripts/create_extract_templates.py`.
- Codex/Claude/OpenCode uses the `paper-corpus-analyzer` workflow to fill `data/extracts/combined/PAPER_ID.md` for all included papers.
- Codex/Claude/OpenCode runs `python scripts/validate_extracts.py`; if extraction files are incomplete, it should fix them and rerun validation.
- Codex/Claude/OpenCode runs `python scripts/synthesize_rules.py`.
- Codex/Claude/OpenCode runs `python scripts/sync_skills_from_synthesis.py`.
- Codex/Claude/OpenCode runs `python scripts/install_generated_skills.py`.
- Codex/Claude/OpenCode runs `python scripts/run_basic_checks.py --paper-dir "<paper-folder>"`.
- Codex/Claude/OpenCode reports the manifest, extracts, synthesis files, installed skill names, and restart reminder.

After successful installation, Codex/Claude/OpenCode should report:

```text
Installed writing-paper-outline and writing-paper. Please restart Codex/Claude/OpenCode so the two newly installed skills can be discovered.
```

#### 4. Restart Codex/Claude/OpenCode

After the two generated skills are installed, restart Codex/Claude/OpenCode. After restart, you can call:

```text
@writing-paper-outline
@writing-paper
```

### Example Calls After Restart

#### 1. Use `@writing-paper-outline` To Structure A Manuscript

```text
Please use @writing-paper-outline to design a manuscript outline for my paper.

Topic: Dynamic risk management and trajectory planning for manned-unmanned collaborative operations in general aviation airspace.

Methods include risk-field modeling, TLS constraints, tactical conflict resolution, and simulation validation.

Please focus on Problem Formulation, Methodology, Experiment Design, and figure/table planning.
```

#### 2. Use `@writing-paper` To Draft A Section

```text
Please use @writing-paper skill.

The following is one subsection from the manuscript outline:

Section 3.1 Operational scenario and problem description

This subsection should cover:
- the manned-unmanned collaborative operation scenario in controlled airspace around a general aviation airport;
- manned aircraft, including training aircraft, general aviation aircraft, and helicopters;
- unmanned aircraft, including medium-to-large UAV test flights, inspection missions, and logistics missions;
- heterogeneity in speed, maneuverability, communication links, surveillance capability, and operational intent;
- why existing methods based on fixed separation or single conflict-detection logic are insufficient for dynamic risk management;
- how this scenario should be abstracted as a spatiotemporally coupled trajectory-planning problem under risk constraints.

Please write this as English manuscript prose. Requirements:
1. Do not start directly with equations.
2. First describe the scenario and problem in clear but academic language.
3. Let the final paragraph naturally transition to the mathematical formulation.
4. Output revision notes and reviewer-risk reminders.
```

#### 3. Use `@writing-paper` To Polish Or Rewrite A Draft

```text
Please use @writing-paper skill.

Target subsection: Methodology overview

Please rewrite the following draft into English manuscript prose and strengthen reproducibility, module clarity, and input-output logic.

Draft:
This paper proposes a trajectory-planning method for dynamic risk management in low-altitude airspace. First, a risk field is constructed based on UAVs, manned aircraft, and ground risk sources, and the risk field is then used to guide trajectory search. To avoid trajectories entering high-risk regions, TLS constraints are introduced. Meanwhile, to improve real-time performance, grid-based search and local replanning are adopted. When conflict risk occurs, the system selects resolution actions such as detouring, waiting, or altitude adjustment according to the risk level.

Please output:
1. English manuscript prose;
2. structural revision notes;
3. technical details that still need to be added;
4. reviewer-risk reminders.
```

### Additional Note

You can adjust the weights and inclusion fields in `data/paper_manifest.xlsx` to control how strongly different papers influence the distillation process.
