# Research Loop Rules (Hourly Category Rotation with State Tracking)

## Purpose

Aggressively fill the awesome-opensource-ai list by cycling through all 14 categories with deep research. Runs hourly to maximize discovery speed while the repo is new.

## Frequency

Run **hourly** at Europe/Amsterdam timezone. Each run targets ONE specific category, rotating through the 14-category cycle.

## State Tracking

**CRITICAL: Read and update `research-state.json` every run.**

The state file tracks:
- `currentCycle` — array of 14 categories with research timestamps
- `lastCategoryIndex` — which category was last researched
- `lastRunTime` — when research last ran
- `minHoursBetweenRuns` — minimum hours before same category (set to 1 for hourly)

### Rotation Logic (Follow Exactly)

1. **Read `research-state.json`** at start of every run
2. **Check `lastRunTime`**: If less than 1 hour ago → skip this run, post "Research on cooldown, next run in X min"
3. **Find next category**: 
   - If `lastCategoryIndex` is null → start at index 0
   - Else → increment by 1 (wrap to 0 after index 13)
4. **Research that category** following the protocol below
5. **Update state**:
   - Set `lastCategoryIndex` to the category just researched
   - Set `lastRunTime` to current ISO timestamp
   - Set `currentCycle[index].lastResearched` to current ISO timestamp
6. **Write updated `research-state.json`**

### Category Cycle (14 categories, hourly rotation)

| Index | Category | Target Section |
|-------|----------|----------------|
| 0 | Core Frameworks & Libraries | §1 |
| 1 | Open Foundation Models | §2 |
| 2 | Inference Engines & Serving | §3 |
| 3 | Agentic AI & Multi-Agent Systems | §4 |
| 4 | RAG & Knowledge | §5 |
| 5 | Generative Media Tools | §6 |
| 6 | Training & Fine-tuning | §7 |
| 7 | MLOps / LLMOps | §8 |
| 8 | Evaluation & Benchmarks | §9 |
| 9 | AI Safety & Interpretability | §10 |
| 10 | Specialized Domains | §11 |
| 11 | User Interfaces & Platforms | §12 |
| 12 | Developer Tools | §13 |
| 13 | Resources & Learning | §14 |

**Cycle repeats after index 13 → back to 0.**

## Deep Research Protocol (Per Category)

Don't just scan trending. Do targeted discovery for the specific category:

### Category-Specific Sources

**§1 Core Frameworks:**
- PyTorch ecosystem repos (torchvision, torchaudio, torchtext)
- JAX/Flax adjacent tools
- Hugging Face ecosystem beyond transformers
- Data processing libraries (beyond pandas/polars)
- New ML frameworks (Julia, Rust, C++)

**§2 Foundation Models:**
- Hugging Face model hub trending
- LLM leaderboard new entries
- Paper releases with open weights
- Regional model labs (Europe, Asia)
- Small/edge models (<7B params)

**§3 Inference & Serving:**
- vLLM forks and alternatives
- New quantization methods
- Edge/mobile inference tools
- Kubernetes operators for LLMs
- New GGUF/ONNX tooling

**§4 Agentic AI:**
- New agent frameworks (check GitHub tags: agent, autonomous)
- Multi-agent orchestration tools
- Agent memory systems
- Tool-use libraries
- Agent eval benchmarks

**§5 RAG & Knowledge:**
- Vector DBs beyond Chroma/Qdrant/Pinecone
- New embedding models
- Document parsers
- Graph RAG tools
- Hybrid search systems

**§6 Generative Media:**
- New diffusion models (image/video/3D)
- Audio generation (music, speech, SFX)
- Animation tools
- Real-time generation systems
- LoRA/training tools for media

**§7 Training & Fine-tuning:**
- New training frameworks
- RLHF tools
- Fine-tuning UIs
- Dataset curation tools
- Synthetic data generators

**§8 MLOps/LLMOps:**
- Prompt management tools
- LLM observability
- Cost tracking
- A/B testing for models
- Feature stores for ML

**§9 Evaluation:**
- New benchmarks
- Evaluation harnesses
- Red-teaming tools
- Model comparison UIs
- Safety eval suites

**§10 Safety & Alignment:**
- Interpretability tools
- Alignment training methods
- Adversarial testing
- Constitutional AI tools
- Guardrails frameworks

**§11 Specialized Domains:**
- Scientific AI (protein, drug, materials)
- Code-specific tools
- Legal/medical/finance AI
- Robotics simulators
- Game AI

**§12 User Interfaces:**
- New ChatGPT alternatives (self-hosted)
- Mobile apps
- Voice interfaces
- Desktop assistants
- Browser extensions

**§13 Developer Tools:**
- IDE plugins beyond Continue/Cline
- Testing frameworks for AI
- Documentation generators
- API clients
- CLI tools

**§14 Resources:**
- New courses/bootcamps
- Active communities
- Newsletters/podcasts
- Benchmark leaderboards
- Model cards repositories

### Handling Version Families ("Current Best" Principle)

For rapidly evolving projects (foundation models, frameworks with numbered releases):

1. **Check if family already exists** in README (search for "Qwen", "Gemma", "PyTorch", etc.)
2. **If newer major version found:**
   - Prepare PR to **replace** existing entry, not add alongside
   - Update the description to reflect new version (e.g., "3.6 series" → "4 series")
   - Don't list both unless they serve different use cases (see CONTRIBUTING.md exceptions)
3. **If same/older version:** Skip — already covered

**Remember:** This is "what you should know about now" — not a version archive.

## Qualification Criteria

### Elite Tier (README.md)
All discovered projects must meet the **elite tier criteria** defined in [CONTRIBUTING.md](../CONTRIBUTING.md#elite-tier-criteria-must-meet-all):

- ⭐ **1000+ GitHub stars**
- 🔄 **Active development** (meaningful commits within last 30 days)
- 🏭 **Production usage evidence** (case studies, integrations, production issues/PRs)
- 📚 **Quality standards** (proper docs, tests, releases)
- ✅ **OSI-approved license**
- ❌ **Not already in the list**
- 📂 **Fits the target category**

### Emerging Tier (EMERGING.md)
Projects that show promise but fall below elite thresholds:

- ⭐ **100+ GitHub stars** (or 50+ with exceptional backing)
- 🔄 **Active development** (commits within last 60 days)
- 📝 **Clear innovation** (unique approach, not a "me too" project)
- 📚 **Basic quality** (working code, basic docs)
- ✅ **OSI-approved license**
- ❌ **Not already in Elite or Emerging**

**Dual-track approach:** During research, evaluate projects against both tiers. Projects that don't meet Elite criteria but show genuine innovation should be flagged for Emerging list.

## Output: Single Category-Focused PR

**One PR per day** targeting today's category only.

Format:
```
[Research] Add N entries to {Category} - {Date}
```

PR body template:
```markdown
## Category: {Category}

Adding {N} qualifying projects discovered through targeted research.

| Project | Stars | License | Why It Fits |
|---------|-------|---------|-------------|
| {name} | {stars} | {license} | {one-line justification} |

### Research Sources
- Source 1: {what was checked}
- Source 2: {what was checked}
- Source 3: {what was checked}

### Verification
All projects checked for:
- [x] OSI-approved license
- [x] Active development
- [x] >500 stars or notable backing
- [x] Not already in README
- [x] Fits {Category} section
```

## Limits

- Max **5 entries per category per day**
- If <3 qualifying projects found, still open PR with what you found
- If 0 qualifying projects found, skip opening PR (post checkin noting "no qualifying projects found for {Category} today")

## Edge Cases

- **Project overlaps multiple categories:** Pick the best fit, note overlap in PR body
- **Category already has 50+ entries:** Be more selective (focus on newest/highest quality)
- **Duplicate found during research:** Note it in PR body, pick the better one
- **Stars <500 but clearly significant:** Include with justification (e.g., "just launched, backed by Anthropic")

## Remember

This is a **14-day cycle**. By April 17, every category should have been deeply researched once. Then we cycle again with fresh eyes and new projects that emerged.
