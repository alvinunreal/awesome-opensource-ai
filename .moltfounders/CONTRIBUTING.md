# Contributing to Awesome Open Source AI

Thank you for considering contributing to this curated list. We maintain **elite-tier quality standards** - this list is for battle-tested tools that have proven their value in production environments.

---

## Quality Bar: Battle-Tested & Production-Proven

This is not a directory of every open-source AI project. We curate tools that have survived real-world usage, earned community trust, and demonstrate sustained excellence.

### Elite Tier Criteria (Must Meet ALL)

Projects must satisfy **ALL of the following criteria** to be considered elite-tier. No exceptions except under maintainer discretion for truly exceptional cases.

| Criterion | Threshold | Why It Matters |
|-----------|-----------|----------------|
| **⭐ GitHub Stars** | 1000+ | Indicates broad community adoption and trust |
| **🔄 Active Development** | Meaningful commits within last 30 days | Continuously evolving, not abandoned |
| **🏭 Production Usage** | Evidence of real-world deployment | Case studies, integrations, production issues/PRs |
| **📚 Quality Standards** | Proper docs, tests, releases | Not a thrown-together experiment |

### No Exceptions Except Maintainer Discretion

Meeting 3/4 is **not acceptable**. Projects must meet all criteria. The only path for projects falling short:

- **Maintainer Override** - Reserved for truly exceptional cases with extraordinary production traction or major organizational backing

---

## Curation Philosophy: "Current Best"

This list represents **"what you should know about now"** — not a historical archive.

### Replace, Don't Accumulate

When a newer version clearly supersedes an existing entry in the same category:

| Scenario | Action | Example |
|----------|--------|---------|
| **New major version** | Update existing entry | PyTorch 2.4 → 2.5: Edit the line, don't add both |
| **Minor bump** | Skip unless significant | v1.2 → v1.3: Not worth a PR |
| **Both versions warranted** | Rare exception | Python 3.11/3.12 both deployed; SD 1.5 vs XL (different use cases) |

**The test:** Would a practitioner looking at this list today care about *both* versions, or just the current one?

For rapidly evolving families (foundation models, frameworks with numbered releases), always update the existing entry rather than appending. The list stays lean and relevant.

---

## What We're Looking For

### ✅ Elite Indicators

- **Sustained adoption** - Growing star count over time, not a spike
- **Production testimonials** - Companies/teams using it in production
- **Ecosystem integration** - Referenced by other major projects
- **Responsive maintenance** - Active issue resolution, regular releases
- **Clear differentiation** - Solves a specific problem better than alternatives
- **Documentation quality** - Proper setup guides, API docs, examples

### 🚩 Disqualifying Red Flags

- Marketing-heavy descriptions without substance
- "Revolutionary" / "next-gen" / "game-changing" hype language
- Single-contributor repos with manufactured star counts
- Forks with minor feature additions claiming to be new projects
- No production users or real-world usage evidence
- Abandoned projects seeking attention
- AI-generated slop (low-effort boilerplate projects)

---

## Submission Process

### Before Submitting

1. **Verify your project meets ALL elite criteria** - if not, don't submit here (the Emerging & Innovations list is coming soon for newer projects!)
2. **Check for duplicates** - search the README first
3. **Ensure correct categorization** - place in the most specific section
4. **Write a factual description** - one sentence, no fluff

### PR Requirements

```markdown
- **[Project Name](https://github.com/owner/repo)** ![GitHub stars](https://img.shields.io/github/stars/owner/repo?style=social) - Factual one-sentence description.
```

**Good:**
> "High-performance vector search engine built in Rust with hybrid filtering and cloud-native architecture."

**Bad:**
> "The revolutionary next-generation AI-powered vector database disrupting the industry with bleeding-edge performance."

### Required PR Description

Your PR must include:

```markdown
## Project: [Name]

### Elite Criteria Checklist (ALL Required)

- [ ] **Elite Criteria:** ALL criteria met
  - ⭐ Stars: [count] (threshold: 1000+)
  - 🔄 Active: [last commit date] (within 30 days)
  - 🏭 Production: [evidence link] (case study/integration)
  - 📚 Quality: [docs link] (tests/releases)

### Evidence of Production Usage
<!-- Links to case studies, integrations, or production usage -->

### Why This Belongs in Elite Tier
<!-- Explain which criteria you meet and why the project is battle-tested -->

### Category
<!-- Which section this belongs in -->
```

---

## Categories & Quality Benchmarks

Each category has established elite-tier benchmarks. Your submission should be comparable in quality to existing entries:

### 1. Core Frameworks & Libraries
- **Benchmarks:** PyTorch (80K+ ⭐), Transformers (150K+ ⭐), LangChain (90K+ ⭐)
- **Bar:** Industry-standard adoption or clear performance advantage

### 2. Open Foundation Models
- **Benchmarks:** DeepSeek-V3 (90K+ ⭐), Qwen (50K+ ⭐), llama.cpp (100K+ ⭐)
- **Bar:** State-of-the-art performance or unique architectural innovation

### 3. Inference Engines & Serving
- **Benchmarks:** vLLM (50K+ ⭐), Ollama (100K+ ⭐), TGI (30K+ ⭐)
- **Bar:** Production-grade performance, scalable architecture

### 4. Agentic AI & Multi-Agent Systems
- **Benchmarks:** LangGraph (10K+ ⭐), AutoGen (35K+ ⭐), CrewAI (25K+ ⭐)
- **Bar:** Real agent deployments, not just agent-themed projects

### 5. Vector Databases & RAG
- **Benchmarks:** Chroma (20K+ ⭐), Qdrant (25K+ ⭐), Weaviate (15K+ ⭐)
- **Bar:** Performance benchmarks, production deployments

### 6. Generative Media
- **Benchmarks:** ComfyUI (60K+ ⭐), Stable Diffusion (80K+ ⭐), AnimateDiff (15K+ ⭐)
- **Bar:** Professional-grade output quality, artist community adoption

### 7. Training & Fine-tuning
- **Benchmarks:** LLaMA-Factory (40K+ ⭐), Unsloth (25K+ ⭐), Axolotl (15K+ ⭐)
- **Bar:** Proven training efficiency gains, adoption by AI labs

### 8. MLOps & Production
- **Benchmarks:** MLflow (20K+ ⭐), Kubeflow (15K+ ⭐), BentoML (10K+ ⭐)
- **Bar:** Enterprise deployment patterns, observability features

### 9. Evaluation & Benchmarks
- **Benchmarks:** lm-evaluation-harness (10K+ ⭐), DeepEval (5K+ ⭐)
- **Bar:** Credible evaluation methodology, research community usage

### 10. AI Safety & Interpretability
- **Benchmarks:** TransformerLens (10K+ ⭐), Garak (5K+ ⭐)
- **Bar:** Published research backing, security community adoption

### 11. Specialized Domains
- **Benchmarks:** OpenCV (80K+ ⭐), YOLO (40K+ ⭐), Gymnasium (10K+ ⭐)
- **Bar:** Domain expertise, professional practitioner adoption

### 12. User Interfaces & Platforms
- **Benchmarks:** Open WebUI (50K+ ⭐), AnythingLLM (30K+ ⭐), LibreChat (20K+ ⭐)
- **Bar:** Active user community, polished UX, stable releases

### 13. Developer Tools
- **Benchmarks:** Continue (20K+ ⭐), Aider (25K+ ⭐), Tabby (25K+ ⭐)
- **Bar:** Daily developer workflow integration, IDE ecosystem presence

---

## Maintainer Discretion

The maintainer reserves final judgment on all submissions, including:

- **Rejecting** projects that technically meet criteria but lack production substance
- **Accepting** exceptional projects that may fall short on one criterion but demonstrate unique innovation with strong backing
- **Removing** existing entries if quality degrades or project becomes abandoned
- **Elevating** tools from emerging to elite tier as they mature

**Remember:** Meeting ALL criteria guarantees consideration, not acceptance. This list is about trust and proven value. Maintainer override is reserved for truly exceptional cases only.

---

## Emerging & Experimental Projects

Have a promising project that doesn't meet elite criteria yet?

We maintain the **[EMERGING.md](./EMERGING.md)** list for:
- Innovative concepts with **100+ stars** (or 50+ with exceptional backing)
- Early-stage projects with strong potential
- Experimental research implementations
- Niche tools solving specific problems
- Newer repos that haven't been around long but show promise

### Emerging Tier Criteria

| Criterion | Threshold | Why It Matters |
|-----------|-----------|----------------|
| **⭐ GitHub Stars** | 100+ (50+ with backing) | Early traction signal |
| **🔄 Active Development** | Commits in last 60 days | Alive and evolving |
| **📝 Innovation** | Clear unique approach | Not a "me too" project |
| **📚 Quality** | Basic docs, working code | Professional intent |
| **🔮 Potential** | Maintainer discretion | Gut check on future elite |

### Emerging → Elite Promotion Path

Projects can graduate from Emerging to Elite when they meet **all** elite-tier criteria:

| Criterion | Emerging | Elite |
|-----------|----------|-------|
| Stars | 100+ | 1000+ |
| Activity | 60 days | 30 days |
| Production | Early adopters | Real deployments |
| Quality | Basic | Full (docs/tests/releases) |

**Promotion process:**
1. Maintainer identifies project as ready (or author opens "Promotion Request" issue)
2. Project is added to Elite Tier in appropriate category
3. Project stays in Emerging for 30 days with a "🎓 Graduated" badge
4. Then removed from Emerging to keep the list fresh

### How to Submit to Emerging

Same process as Elite, but lower thresholds. In your PR, specify this is for Emerging:

```markdown
## Project: [Name]

### Emerging Criteria Checklist

- [ ] **100+ stars** (or justification for 50+)
- [ ] **Active** in last 60 days
- [ ] **Innovation** - what's unique about this approach
- [ ] **Quality** - basic docs and working code
- [ ] **License** - OSI-approved

### Target List
- [ ] Elite Tier (1000+ stars, production usage)
- [x] Emerging List (100+ stars, promising)

### Why This Belongs in Emerging
<!-- Explain the concept, innovation, and potential -->
```

### Emerging List Philosophy

- **Curated, not exhaustive** — still say no to low-effort projects
- **Fresh eyes welcome** — newer projects can get visibility
- **Quality over quantity** — 5 good entries > 50 mediocre ones
- **Promotion ready** — design entries to smoothly graduate to Elite

---

---

## Questions?

Open an issue for discussion before submitting borderline cases. We're happy to help evaluate whether your project fits the elite tier or should wait for the emerging list.

---

*Last updated: April 2025*  
*Quality standard: Battle-tested & production-proven*