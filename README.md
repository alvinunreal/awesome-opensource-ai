<div align="center">

<img src="assets/osai.png" alt="Awesome Open Source AI" width="120" />

# Awesome Open Source AI

*A curated list of notable open-source AI models, libraries, infrastructure, and developer tools.*

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](./CONTRIBUTING.md)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-blue.svg?style=flat-square)](./LICENSE)

[![Managed by MoltFounders](https://img.shields.io/badge/Managed%20By-MoltFounders-F4F4F5?style=for-the-badge&labelColor=18181B&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjYzIiBoZWlnaHQ9IjEyNjMiIHZpZXdCb3g9IjAgMCAxMjYzIDEyNjMiPjxwYXRoIGZpbGw9IiNmZWZlZmUiIGQ9Ik0xMjYzLjAwMyAxNjAuNzQ2Yy01LjM4NyAxMy44Ny0yMy43MSAyNC40OTQtMzYuODg4IDI5LjUzNy0xOS40MyA3LjQ0LTUwLjg1OCAxMS42MzQtNzIuMTg1IDE2LjY2LTI4LjA5NiA2LjYyNS01Ni44MDQgMTMuMzM4LTg0LjM0MSAyMi4wNjMtMjAuODU4IDYuNjEtNDAuNDI5IDE0LjkyLTYwLjMwNiAyMy45ODktOS43MTQgNC40MzItMTkuNTU1IDguNjk0LTI4Ljg3MyAxMy45MjMtMjAuNjkgMTEuNjExLTQxLjQ2MiAyNi40NzUtNTkuNjM0IDQxLjcyOC0xMi44NTMgMTAuNzg2LTI0LjgzNiAyMi41MzItMzYuOTc0IDM0LjA5Ny04LjYzOCA4LjIyOS0xNy40NDQgMTYuMDE1LTI1LjYzMiAyNC43MjUtMTEuMDU0IDExLjc1OC0yMS4yOTkgMjQuMjI4LTMyLjA1MiAzNi4yNDgtNC4wMSA0LjQ4NC0xOC4xOTkgMTcuNjMtMTguNzA5IDIzLjUyIDIuMTcgMS40MDUgOS40NjYgMS4zOSAxMi40MTQgMi4xNDcgMjAuODIgNS4zNDUgMzAuNjk5IDE0Ljc0NCAzNC4zNjYgMzYuMDAyIDQuOTc2IDIwLjE3Ny05LjU0NyAzOC4xNTQtMjMuNzc4IDQ5LjcyMS0xNy44NjYgMTQuNTIyLTIxLjg2NiAxNS4zNDctOS44OTIgMzUuNjMzIDIuNjg0IDQuNTQ4IDMuNzAzIDIxLjUzIDcuMTE0IDI4LjczNiA0LjA5NiA4LjY1NCA4Ljk0IDE2Ljg3OCAxNC4wMjMgMjUuMTU2IDUuMDUgOS4yODMgNS45MTMgMTcuNjMzIDcuOTcgMjcuNjI4IDcuMTUyIDM0Ljc0My0yLjk2NCA2OC40MjMtMjYuNTk3IDk0LjcyNS01LjkxOCA2Ljc5Mi0yMS4zOTYgMTguNzc3LTIyLjk3MiAyNy44MTYtMy4xNyAxOC4xODQtMjAuOTczIDQwLjI2OC0yMy4xOSA1Ni4wODUtMi41MDcgMTcuODY0IDcuMTkyIDM0Ljc5NS4zODQgNTQuMzIzLTUuNjE4IDE2LjExMS0xNC4zNzggMjYuNzgzLTIwLjA3MyA0Mi4zNjktMi43OTUgOC45NTEtMi44MTggMTkuMTUyLTQuNDcgMjguMjktNC40NzQgMjUuMjctMTAuMTI4IDU0LjUxLTI1LjQyOCA3NS42MzItMTEuNzQgMTYuMjA4LTEzLjM1NyAxNS4wOS0xMC44OTQgMzUuNTAyIDEuODUzIDIzLjM0Ny0uMDA1IDM5LjE5My0xMy44NDIgNTguNTQ5LTI0LjQ4OCAzNC4yNDItNTUuMzQ3IDQ3LjczNy05My41MzYgMjQuMTg0LTIwLjg1OS0xMi44NzItMzguMzM1LTI0Ljg3LTUyLjM0Ny00NC42OS01LjMyLTcuNTI3LTkuMzI0LTMyLjIwMi0xNC41MTQtMzUuMDEtMjEuODMyLTExLjgwOC00Ni4yOTctMjEuMzM5LTY2LjE1LTM2Ljg5NC01My4xNzYtMzkuMTEtMTA3LjM4Mi04MS43ODQtMTM4LTE0MS44Mi05LjI2Ni0xOC4xNjktMTEuMjg1LTMyLjM2LTEwLjQ1OC01Mi4zNzMtLjQtMTUuNzc4IDYuNTg5LTI4Ljg1IDEwLjkxNi00My40OSAzLjkzNC0xNS4wNCA5LjE1NS0zMC40NzMgMTEuMzUyLTQ1Ljg4NCAxLjYwMy0xMS4yNDUgNS40MjktMTcuNDQxIDkuMDMxLTI3LjUzMyA3LjM1NS0yMC42MDQgMTYuNTMzLTQwLjU1IDI4LjIxNy01OS4wODkgNS40Ny04LjY4MiAxMi44OTgtMTYuOTA3IDE4Ljc5Mi0yNS4zNTggMjYuNTc5LTM5LjQ2NiA2Mi45MzgtNzEuNDYzIDk3LjA2NC0xMDQuMjE0IDEyLjI1OC0xMS4yNzggMjQuNjg2LTI0LjE3MiAzOC44NDUtMzMuMDIgMTQuMDM4LTguNzcyIDQuNzM3LTIwLjA0MyAyLjc0LTMyLjI1Mi04LjM0NC01MS4wMTQtMzIuNTIzLTg4LjE1MS02Mi44My0xMjguNDQ1YTMwOC42IDMwOC42IDAgMCAwLTEwNC42MDktODguOTE2Yy01LjE1NS0yLjcyNi0xNS41NzctOC41MDctMjAuNzkyLTEwLjQ1OC0yMy43MjYtOC44ODEtNDguNzc5LTE2LjM5Mi03My44NzEtMjAuMTUtMTQuMDE0LTIuNjQ1LTI5Ljg5LTIuMTctNDMuNzM0LTQuMDYtMTkuNTA2LTIuNjYzLTM2LjkyNy00LjI2OC01Ni43NjUtMi44MTctMTAuNTk3Ljc3NC0yMS4xMiAzLjczNS0zMS43MSA0Ljk5NC0xOC4xMjUgMi4xNTUtNDEuODEyIDUuNjczLTU4LjM3LTMuNTYtMjIuMTE1LTEyLjgyNC0yNy45MS00NC4yMDMtMTQuNTgtNjUuMzQgMTMuODI3LTIxLjkyOCA0Ny43LTI3LjcyIDcxLjY1Mi0zMi41MDQgNDEuMjUtOC4yNCA4NC4wMDUtMi4yMzMgMTI1LjUzOS0uOTUgNi4xOTMuMTg0IDEzLjAyNiAxLjc4OCAxOS4xNTQgMS45MjcgMTIuMDQxLjI3NCAyMi45NCAxLjY2MSAzNC43MjcgMy45OGEzOTguMiAzOTguMiAwIDAgMSAxMjQuODUgNDguNDdjNjkuODggNDEuMjQxIDEyMC41NiA5My43ODYgMTYxLjUyNCAxNjMuNDc0IDUuMTQ1IDguNzUyIDEwLjg2MiAyMC42MyAxNS43NzIgMjkuNzcgNi40OTggMTIuMDk5IDExLjM3NCAyOC4zNDUgMTUuMzU1IDQxLjM4NyAyLjA1NiA2LjczNyAyLjc0MiAyMy40NjUgOC43NDggMjcuNTU5IDMuMjI3LjMxNyA4LjQzOC05Ljg5NiAxMS4xMzYtMTIuNzM2IDE3Ljc2NS0xOC43MDggMzUuNDQ1LTEyLjkgNTAuODYyLTM2Ljk3IDkuNzkzLTE1LjI5IDI0LjYxNS0zMi42MTEgMzUuNzczLTQ3LjM1IDI2LjY0Mi0zNS4xOTUgNjEuMzUtNjMuNjQyIDk0Ljg5Ni05MS44ODggNy4wNTYtNS45MSAxNS40MjctMTAuODI1IDIzLjA0NS0xNS45ODQgMzguNTQtMjcuNzQ4IDgxLjQ0My00Ni45NzUgMTI1LjEzNi02NS4wMjMgOC4xNTQtMy41NTQgMTYuOTE1LTUuNSAyNS4yMzgtOC41MDggNTMuOTQ0LTE5LjQ5NSAxMTEuMTQ4LTI4LjUwNCAxNjcuMTA4LTQwLjM2NiAxNi41NTItMy41MSAzMS45MTMtNi44NTMgNDcuOTQ4LjU3IDEyLjU5OCA1LjgzOCAyMS45NSAxMS42MzUgMjcuMzA1IDI1LjE0M3oiLz48L3N2Zz4%3D)](https://moltfounders.com/jobs/09a95833-fbc1-4805-ac6c-8a45227e0ee4)

<sub>by **Boring Dystopia Development**</sub>

<p align="center">
  <a href="https://boringdystopia.ai/">
    <img src="https://img.shields.io/badge/boringdystopia.ai-111111?style=for-the-badge&logo=vercel&logoColor=white" alt="boringdystopia.ai" />
  </a>&nbsp;
  <a href="https://x.com/alvinunreal">
    <img src="https://img.shields.io/badge/X-@alvinunreal-000000?style=for-the-badge&logo=x&logoColor=white" alt="X @alvinunreal" />
  </a>&nbsp;
  <a href="https://t.me/boringdystopiadevelopment">
    <img src="https://img.shields.io/badge/Telegram-Join%20channel-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Join channel" />
  </a>
</p>

</div>

---
<div align="center">

**[ Explore the List ](#-contents)** • **[ Submission Guidelines ](#contributing)** • **[ License ](#license)**

</div>

## 📋 Contents

- [🧬 1. Core Frameworks & Libraries](#-1-core-frameworks--libraries)
- [🧠 2. Open Foundation Models](#-2-open-foundation-models)
- [⚡ 3. Inference Engines & Serving](#-3-inference-engines--serving)
- [🤖 4. Agentic AI & Multi-Agent Systems](#-4-agentic-ai--multi-agent-systems)
- [🔍 5. Retrieval-Augmented Generation (RAG) & Knowledge](#-5-retrieval-augmented-generation-rag--knowledge)
- [🎨 6. Generative Media Tools](#-6-generative-media-tools)
- [🛠️ 7. Training & Fine-tuning Ecosystem](#section-7)
- [📊 8. MLOps / LLMOps & Production](#-8-mlops--llmops--production)
- [📈 9. Evaluation, Benchmarks & Datasets](#-9-evaluation-benchmarks--datasets)
- [🛡️ 10. AI Safety, Alignment & Interpretability](#section-10)
- [🧩 11. Specialized Domains](#-11-specialized-domains)
- [🖥️ 12. User Interfaces & Self-hosted Platforms](#section-12)
- [🧪 13. Developer Tools & Integrations](#-13-developer-tools--integrations)
- [📚 14. Resources & Learning](#-14-resources--learning)

---

### 🧬 1. Core Frameworks & Libraries

> Core libraries and frameworks used to build, train, and run AI and machine learning systems.

#### Deep Learning Frameworks

- **[PyTorch](https://github.com/pytorch/pytorch)** ![GitHub stars](https://img.shields.io/github/stars/pytorch/pytorch?style=social) - Dynamic computation graphs, Pythonic API, dominant in research and production. The current standard for most frontier AI work.
- **[TensorFlow](https://github.com/tensorflow/tensorflow)** ![GitHub stars](https://img.shields.io/github/stars/tensorflow/tensorflow?style=social) - End-to-end platform with excellent production deployment, TPU support, and large-scale serving tools.
- **[JAX](https://github.com/jax-ml/jax)** ![GitHub stars](https://img.shields.io/github/stars/jax-ml/jax?style=social) + **[Flax](https://github.com/google/flax)** ![GitHub stars](https://img.shields.io/github/stars/google/flax?style=social) - High-performance numerical computing with composable transformations (JIT, vmap, grad). Rising favorite for research and scientific ML.
- **[Keras](https://github.com/keras-team/keras)** ![GitHub stars](https://img.shields.io/github/stars/keras-team/keras?style=social) - High-level, beginner-friendly API that now runs on multiple backends (TensorFlow, JAX, PyTorch). Perfect for rapid experimentation.

#### Rust ML Frameworks

- **[Burn](https://github.com/tracel-ai/burn)** ![GitHub stars](https://img.shields.io/github/stars/tracel-ai/burn?style=social) - Next-generation deep learning framework in Rust. Backend-agnostic with CPU, GPU, WebAssembly support.
- **[Candle (Hugging Face)](https://github.com/huggingface/candle)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/candle?style=social) - Minimalist ML framework for Rust. PyTorch-like API with focus on performance and simplicity.

#### NLP & Transformers

- **[Transformers (Hugging Face)](https://github.com/huggingface/transformers)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/transformers?style=social) - The de facto standard library for pretrained NLP models. 1M+ models, 250,000+ downloads/day. BERT, GPT, Llama, Qwen, and hundreds more.
- **[sentence-transformers](https://github.com/UKPLab/sentence-transformers)** ![GitHub stars](https://img.shields.io/github/stars/UKPLab/sentence-transformers?style=social) - Classic library for sentence and image embeddings.
- **[tokenizers (Hugging Face)](https://github.com/huggingface/tokenizers)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/tokenizers?style=social) - Fast state-of-the-art tokenizers for training and inference.

#### Data Processing & Manipulation

- **[Pandas](https://github.com/pandas-dev/pandas)** ![GitHub stars](https://img.shields.io/github/stars/pandas-dev/pandas?style=social) - The gold standard for data analysis and manipulation in Python.
- **[Polars](https://github.com/pola-rs/polars)** ![GitHub stars](https://img.shields.io/github/stars/pola-rs/polars?style=social) - Blazing-fast DataFrame library (Rust backend) - modern alternative to pandas for large-scale workloads.
- **[Dask](https://github.com/dask/dask)** ![GitHub stars](https://img.shields.io/github/stars/dask/dask?style=social) - Parallel computing for big data - scales pandas/NumPy/scikit-learn to clusters.
- **[NumPy](https://github.com/numpy/numpy)** ![GitHub stars](https://img.shields.io/github/stars/numpy/numpy?style=social) - Fundamental array computing library that powers almost every AI stack.
- **[SciPy](https://github.com/scipy/scipy)** ![GitHub stars](https://img.shields.io/github/stars/scipy/scipy?style=social) - Scientific computing algorithms (optimization, linear algebra, statistics, signal processing).

#### Classical ML & Gradient Boosting

- **[scikit-learn](https://github.com/scikit-learn/scikit-learn)** ![GitHub stars](https://img.shields.io/github/stars/scikit-learn/scikit-learn?style=social) - Industry-standard library for traditional machine learning (classification, regression, clustering, pipelines).
- **[XGBoost](https://github.com/dmlc/xgboost)** ![GitHub stars](https://img.shields.io/github/stars/dmlc/xgboost?style=social) - Scalable, high-performance gradient boosting library. Still dominates Kaggle and tabular competitions.
- **[LightGBM](https://github.com/microsoft/LightGBM)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/LightGBM?style=social) - Microsoft's ultra-fast gradient boosting framework, optimized for speed and memory.
- **[CatBoost](https://github.com/catboost/catboost)** ![GitHub stars](https://img.shields.io/github/stars/catboost/catboost?style=social) - Gradient boosting that handles categorical features natively with great out-of-the-box performance.

#### AutoML & Hyperparameter Optimization

- **[Optuna](https://github.com/optuna/optuna)** ![GitHub stars](https://img.shields.io/github/stars/optuna/optuna?style=social) - Modern, define-by-run hyperparameter optimization with pruning and visualizations. Extremely popular in 2026.
- **[AutoGluon](https://github.com/autogluon/autogluon)** ![GitHub stars](https://img.shields.io/github/stars/autogluon/autogluon?style=social) - AWS AutoML toolkit for tabular, image, text, and multimodal data - state-of-the-art with almost zero code.
- **[FLAML](https://github.com/microsoft/FLAML)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/FLAML?style=social) - Microsoft's fast & lightweight AutoML focused on efficiency and low compute.
- **[AutoKeras](https://github.com/keras-team/autokeras)** ![GitHub stars](https://img.shields.io/github/stars/keras-team/autokeras?style=social) - Neural architecture search on top of Keras.
- **[TPOT](https://github.com/epistasislab/tpot)** ![GitHub stars](https://img.shields.io/github/stars/epistasislab/tpot?style=social) - Genetic programming-based AutoML for full pipeline optimization.

#### Model Training & Optimization Utilities

- **[Hugging Face Accelerate](https://github.com/huggingface/accelerate)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/accelerate?style=social) - Simple API to make training scripts run on any hardware (multi-GPU, TPU, mixed precision) with minimal code changes.
- **[DeepSpeed](https://github.com/microsoft/DeepSpeed)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/DeepSpeed?style=social) - Microsoft's deep learning optimization library for extreme-scale training (ZeRO, offloading, MoE).
- **[Transformers](https://github.com/huggingface/transformers)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/transformers?style=social) - Library of pretrained transformer models and utilities for text, vision, audio, and multimodal training and inference.
- **[FlashAttention](https://github.com/Dao-AILab/flash-attention)** ![GitHub stars](https://img.shields.io/github/stars/Dao-AILab/flash-attention?style=social) - Fast exact attention kernels that reduce memory usage and accelerate transformer training and inference.
- **[xFormers](https://github.com/facebookresearch/xformers)** ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/xformers?style=social) - Optimized transformer building blocks and attention operators for PyTorch.
- **[PyTorch Lightning](https://github.com/Lightning-AI/lightning)** ![GitHub stars](https://img.shields.io/github/stars/Lightning-AI/lightning?style=social) - High-level wrapper for PyTorch that removes boilerplate and adds best practices.
- **[ONNX Runtime](https://github.com/microsoft/onnxruntime)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/onnxruntime?style=social) - High-performance inference and training for ONNX models across hardware.

---

### 🧠 2. Open Foundation Models

> Pretrained language, multimodal, speech, and video models with publicly available weights.

#### Large Language Models (Base + Chat)

- **[Qwen3.5 (Alibaba)](https://github.com/QwenLM/Qwen)** ![GitHub stars](https://img.shields.io/github/stars/QwenLM/Qwen?style=social) - Native multimodal open series spanning from small to frontier-scale models (0.8B–122B). Released Feb 2026 with 397B total MoE params (17B active), strong in coding, math, vision, and instruction following.
- **[DeepSeek-V3.2 / R1 (DeepSeek)](https://github.com/deepseek-ai/DeepSeek-V3)** ![GitHub stars](https://img.shields.io/github/stars/deepseek-ai/DeepSeek-V3?style=social) - Mixture-of-Experts family with exceptional reasoning, math, and efficient large-scale inference.
- **[Gemma 3 (Google)](https://github.com/google-deepmind/gemma)** ![GitHub stars](https://img.shields.io/github/stars/google-deepmind/gemma?style=social) - Lightweight yet powerful open models with excellent efficiency for on-device use. Strong multilingual support across 100+ languages.
- **[MiniMax-M2.1 / M1 (MiniMax)](https://github.com/MiniMax-AI/MiniMax-M1)** ![GitHub stars](https://img.shields.io/github/stars/MiniMax-AI/MiniMax-M1?style=social) - Open-weight MiniMax model line spanning long-context reasoning and agentic software tasks, with strong tool use and publicly released weights for local deployment.
- **[Kimi K2.5 (Moonshot AI)](https://github.com/MoonshotAI/Kimi-K2.5)** ![GitHub stars](https://img.shields.io/github/stars/MoonshotAI/Kimi-K2.5?style=social) - Frontier open-weight MoE model with 256K context, strong coding and reasoning performance, and native multimodal + tool-use support for agentic workflows.
- **[Mistral Large / Nemo / Small](https://github.com/mistralai)** - High-performance model family with strong multilingual capability, tool use, and efficient deployment profiles.
- **[Phi-4 / Phi-3.5 (Microsoft)](https://github.com/microsoft/PhiCookBook)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/PhiCookBook?style=social) - Small but highly capable models optimized for reasoning, edge devices, and on-device inference.
- **[GLM-5 (Zhipu AI)](https://github.com/zai-org/GLM-5)** ![GitHub stars](https://img.shields.io/github/stars/zai-org/GLM-5?style=social) - Strong open model line with solid coding, reasoning, and agentic-task performance.
- **[OLMo 2 (Allen AI)](https://github.com/allenai/OLMo)** ![GitHub stars](https://img.shields.io/github/stars/allenai/OLMo?style=social) - Fully open-source LLMs (1B–32B) with complete transparency: models, data, training code, and logs. Designed by scientists, for scientists.

#### Coding & Reasoning Models

- **[DeepSeek-Coder-V2 / R1-Coder](https://github.com/deepseek-ai/DeepSeek-Coder)** ![GitHub stars](https://img.shields.io/github/stars/deepseek-ai/DeepSeek-Coder?style=social) - Best-in-class open coding model (236B MoE). Outperforms closed models on many code benchmarks.
- **[CodeLlama / CodeGemma](https://github.com/facebookresearch/codellama)** ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/codellama?style=social) - Meta's specialized coding variants built on Llama. Still heavily used for fine-tuning.
- **[Qwen3-Coder-Next (Alibaba)](https://github.com/QwenLM/Qwen3-Coder)** ![GitHub stars](https://img.shields.io/github/stars/QwenLM/Qwen3-Coder?style=social) - Leading open coding model. Strong Pareto frontier for cost-effective agent deployment.
- **[StarCoder2 (BigCode)](https://github.com/bigcode-project/starcoder2)** ![GitHub stars](https://img.shields.io/github/stars/bigcode-project/starcoder2?style=social) - 15B model trained on 600+ programming languages. Community favorite for transparency.

#### Multimodal Models (Vision + Language)

- **[Qwen3-VL (Alibaba)](https://github.com/QwenLM/Qwen3-VL)** ![GitHub stars](https://img.shields.io/github/stars/QwenLM/Qwen3-VL?style=social) - Latest flagship VLM with native 256K context (expandable to 1M), visual agent capabilities, 3D grounding, and superior multimodal reasoning. Major leap over Qwen2.5-VL.
- **[InternVL3 (OpenGVLab)](https://github.com/OpenGVLab/InternVL)** ![GitHub stars](https://img.shields.io/github/stars/OpenGVLab/InternVL?style=social) - Native multimodal pretraining with mixed preference optimization (MPO). Superior perception and reasoning over InternVL 2.5, extends to GUI agents and 3D vision.
- **[GLM-4.5V / GLM-4.1V-Thinking (Zhipu AI)](https://github.com/zai-org/GLM-V)** ![GitHub stars](https://img.shields.io/github/stars/zai-org/GLM-V?style=social) - Strong multimodal reasoning with scalable reinforcement learning. Compares favorably with Gemini-2.5-Flash on benchmarks.
- **[LLaVA-OneVision](https://github.com/LLaVA-VL/LLaVA-NeXT)** ![GitHub stars](https://img.shields.io/github/stars/LLaVA-VL/LLaVA-NeXT?style=social) - Successor to LLaVA 1.6 with expanded capabilities across vision-language tasks.
- **[MiniCPM-V 2.6](https://github.com/OpenBMB/MiniCPM-V)** ![GitHub stars](https://img.shields.io/github/stars/OpenBMB/MiniCPM-V?style=social) - Handles images up to 1.8M pixels with top-tier OCR performance. Excellent for on-device deployment.
- **[Gemma 3 (Google)](https://github.com/google-deepmind/gemma)** ![GitHub stars](https://img.shields.io/github/stars/google-deepmind/gemma?style=social) - Lightweight multimodal supporting vision-language input, optimized for efficiency and on-device use.

#### Speech & Audio Models (TTS, STT, Music)

- **[Whisper (OpenAI → community forks)](https://github.com/openai/whisper)** ![GitHub stars](https://img.shields.io/github/stars/openai/whisper?style=social) - The gold-standard open speech-to-text model. Massive community fine-tunes available.
- **[OuteTTS / CosyVoice 2](https://github.com/edwko/OuteTTS)** ![GitHub stars](https://img.shields.io/github/stars/edwko/OuteTTS?style=social) - High-quality open TTS with natural prosody and multilingual support.
- **[Fish Speech / StyleTTS 2](https://github.com/fishaudio/fish-speech)** ![GitHub stars](https://img.shields.io/github/stars/fishaudio/fish-speech?style=social) - Zero-shot TTS with excellent voice cloning. Extremely popular in 2026.
- **[MusicGen / AudioCraft (Meta)](https://github.com/facebookresearch/audiocraft)** ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/audiocraft?style=social) - Open music and audio generation models.

#### Video & Animation Models

- **[Open-Sora / Open-Sora-Plan](https://github.com/hpcaitech/Open-Sora)** ![GitHub stars](https://img.shields.io/github/stars/hpcaitech/Open-Sora?style=social) - Fully open video generation model rivaling closed systems.
- **[CogVideoX (Zhipu AI / community)](https://github.com/THUDM/CogVideo)** ![GitHub stars](https://img.shields.io/github/stars/THUDM/CogVideo?style=social) - High-quality open text-to-video model (5B-12B).
- **[Mochi 1 (Genmo)](https://github.com/genmoai/mochi)** ![GitHub stars](https://img.shields.io/github/stars/genmoai/mochi?style=social) - 10B open video model with impressive motion and consistency.
- **[AnimateDiff / Stable Video Diffusion (community forks)](https://github.com/guoyww/AnimateDiff)** ![GitHub stars](https://img.shields.io/github/stars/guoyww/AnimateDiff?style=social) - Motion module ecosystem for turning images into video.

---

### ⚡ 3. Inference Engines & Serving

> Inference runtimes, serving systems, and optimization tools for running models locally or in production.

#### Local / On-device Inference

- **[llama.cpp](https://github.com/ggerganov/llama.cpp)** ![GitHub stars](https://img.shields.io/github/stars/ggerganov/llama.cpp?style=social) - Pure C/C++ inference engine with GGUF format support. The gold standard for CPU/GPU/Apple Silicon on-device running. Includes llama-server for OpenAI-compatible API.
- **[Ollama](https://github.com/ollama/ollama)** ![GitHub stars](https://img.shields.io/github/stars/ollama/ollama?style=social) - Dead-simple local LLM runner with a one-line install, model registry, and OpenAI-compatible API.
- **[MLX](https://github.com/ml-explore/mlx)** ![GitHub stars](https://img.shields.io/github/stars/ml-explore/mlx?style=social) (Apple) - High-performance array framework + LLM inference optimized for Apple Silicon.
- **[MLC-LLM](https://github.com/mlc-ai/mlc-llm)** ![GitHub stars](https://img.shields.io/github/stars/mlc-ai/mlc-llm?style=social) - Deployment engine that compiles and runs LLMs across browsers, mobile devices, and local hardware.
- **[llama-cpp-python](https://github.com/abetlen/llama-cpp-python)** ![GitHub stars](https://img.shields.io/github/stars/abetlen/llama-cpp-python?style=social) - Official Python bindings for llama.cpp.
- **[KoboldCpp](https://github.com/LostRuins/koboldcpp)** ![GitHub stars](https://img.shields.io/github/stars/LostRuins/koboldcpp?style=social) - User-friendly llama.cpp fork focused on role-playing and creative writing.
- **[Potato OS](https://github.com/slomin/potato-os)** ![GitHub stars](https://img.shields.io/github/stars/slomin/potato-os?style=social) - Linux distribution for fully local AI inference on Raspberry Pi 5 and 4. Optimized for running open models at the edge.

#### High-performance Serving & API Servers

- **[vLLM](https://github.com/vllm-project/vllm)** ![GitHub stars](https://img.shields.io/github/stars/vllm-project/vllm?style=social) - State-of-the-art serving engine with PagedAttention and continuous batching. Currently the fastest production-grade LLM server.
- **[Text Generation Inference (TGI)](https://github.com/huggingface/text-generation-inference)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/text-generation-inference?style=social) - Hugging Face's production-ready Rust-based server.
- **[SGLang](https://github.com/sgl-project/sglang)** ![GitHub stars](https://img.shields.io/github/stars/sgl-project/sglang?style=social) - Next-gen serving framework with RadixAttention.
- **[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)** ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/TensorRT-LLM?style=social) - NVIDIA's official high-performance inference backend.
- **[Aphrodite Engine](https://github.com/PygmalionAI/aphrodite-engine)** ![GitHub stars](https://img.shields.io/github/stars/PygmalionAI/aphrodite-engine?style=social) - vLLM fork optimized for role-play and creative writing.
- **[Open Model Engine (OME)](https://github.com/sgl-project/ome)** ![GitHub stars](https://img.shields.io/github/stars/sgl-project/ome?style=social) - Kubernetes operator for LLM serving. GPU scheduling, model lifecycle management. Works with vLLM, SGLang, TensorRT-LLM.

#### Quantization, Distillation & Optimization

- **[GGUF](https://github.com/ggerganov/llama.cpp)** ![GitHub stars](https://img.shields.io/github/stars/ggerganov/llama.cpp?style=social) (part of llama.cpp) - Modern quantized format that powers most local inference.
- **[bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes)** ![GitHub stars](https://img.shields.io/github/stars/bitsandbytes-foundation/bitsandbytes?style=social) - 8-bit and 4-bit optimizers + quantization.
- **[AutoAWQ](https://github.com/casper-hansen/AutoAWQ)** ![GitHub stars](https://img.shields.io/github/stars/casper-hansen/AutoAWQ?style=social) - Activation-aware Weight Quantization toolkit.
- **[AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ)** ![GitHub stars](https://img.shields.io/github/stars/AutoGPTQ/AutoGPTQ?style=social) - GPTQ quantization framework.
- **[HQQ](https://github.com/mobiusml/hqq)** ![GitHub stars](https://img.shields.io/github/stars/mobiusml/hqq?style=social) - Half-Quadratic Quantization - ultra-fast method rising in 2026.
- **[ExLlamaV2](https://github.com/turboderp/exllamav2)** ![GitHub stars](https://img.shields.io/github/stars/turboderp/exllamav2?style=social) - Highly optimized CUDA kernels for 4-bit/8-bit inference.
- **[Optimum](https://github.com/huggingface/optimum)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/optimum?style=social) - Hardware-specific acceleration and quantization.

---

### 🤖 4. Agentic AI & Multi-Agent Systems

> Frameworks and platforms for building agent-based systems and multi-agent workflows.

#### Single-Agent Frameworks

- **[LangGraph](https://github.com/langchain-ai/langgraph)** ![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=social) - Stateful, controllable agent orchestration.
- **[CrewAI](https://github.com/crewAIInc/crewAI)** ![GitHub stars](https://img.shields.io/github/stars/crewAIInc/crewAI?style=social) - Role-based agent framework.
- **[AutoGen (AG2)](https://github.com/microsoft/autogen)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/autogen?style=social) - Flexible multi-agent conversation framework.
- **[DSPy](https://github.com/stanfordnlp/dspy)** ![GitHub stars](https://img.shields.io/github/stars/stanfordnlp/dspy?style=social) - Framework for programming language model pipelines with modules, optimizers, and evaluation loops.
- **[Semantic Kernel](https://github.com/microsoft/semantic-kernel)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/semantic-kernel?style=social) - SDK for building and orchestrating AI agents and workflows across multiple programming languages.
- **[smolagents](https://github.com/huggingface/smolagents)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/smolagents?style=social) - Lightweight agent framework centered on tool use and code-executing workflows.
- **[LangChain](https://github.com/langchain-ai/langchain)** ![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langchain?style=social) - Foundational library for agents, chains, and memory.
- **[smolagents (Hugging Face)](https://github.com/huggingface/smolagents)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/smolagents?style=social) - Minimalist agent library. Build agents in 3 lines of code with code-first action execution.

#### Multi-Agent Orchestration

- **[MetaGPT](https://github.com/FoundationAgents/MetaGPT)** ![GitHub stars](https://img.shields.io/github/stars/FoundationAgents/MetaGPT?style=social) - Simulates an entire "AI software company".
- **[Swarm](https://github.com/openai/swarm)** ![GitHub stars](https://img.shields.io/github/stars/openai/swarm?style=social) - Lightweight multi-agent orchestration from OpenAI.
- **[Swarms](https://github.com/kyegomez/swarms)** ![GitHub stars](https://img.shields.io/github/stars/kyegomez/swarms?style=social) - Bleeding-edge enterprise multi-agent orchestration.
- **[Llama-Agents](https://github.com/run-llama/llama-agents)** ![GitHub stars](https://img.shields.io/github/stars/run-llama/llama-agents?style=social) - Async-first multi-agent system.
- **[Mastra](https://github.com/mastra-ai/mastra)** ![GitHub stars](https://img.shields.io/github/stars/mastra-ai/mastra?style=social) - TypeScript-first agent framework with built-in RAG, workflows, tool integrations, observability and observational memory.

#### Autonomous Coding Agents

- **[OpenHands (ex-OpenDevin)](https://github.com/All-Hands-AI/OpenHands)** ![GitHub stars](https://img.shields.io/github/stars/All-Hands-AI/OpenHands?style=social) - Full-featured open-source AI software engineer.
- **[Goose](https://github.com/block/goose)** ![GitHub stars](https://img.shields.io/github/stars/block/goose?style=social) - Extensible on-machine AI agent for development tasks.
- **[OpenCode](https://github.com/anomalyco/opencode)** ![GitHub stars](https://img.shields.io/github/stars/anomalyco/opencode?style=social) - Terminal-native autonomous coding agent.
- **[Aider](https://github.com/paul-gauthier/aider)** ![GitHub stars](https://img.shields.io/github/stars/paul-gauthier/aider?style=social) - Command-line pair-programming agent.
- **[Pi (badlogic)](https://github.com/badlogic/pi-mono)** ![GitHub stars](https://img.shields.io/github/stars/badlogic/pi-mono?style=social) - Terminal coding agent with hash-anchored edits, LSP integration, subagents, MCP support, and package ecosystem.
- **[Mistral-Vibe (Mistral)](https://github.com/mistralai/mistral-vibe)** ![GitHub stars](https://img.shields.io/github/stars/mistralai/mistral-vibe?style=social) - Minimal CLI coding agent by Mistral. Lightweight, fast, and designed for local development workflows.
- **[Nanocoder (Nano-Collective)](https://github.com/Nano-Collective/nanocoder)** ![GitHub stars](https://img.shields.io/github/stars/Nano-Collective/nanocoder?style=social) - Beautiful local-first coding agent running in your terminal. Built for privacy and control with support for multiple AI providers via OpenRouter.

#### Domain-Specific Agents

- **[Langflow](https://github.com/langflow-ai/langflow)** ![GitHub stars](https://img.shields.io/github/stars/langflow-ai/langflow?style=social) - Visual low-code platform for agentic workflows.
- **[Dify](https://github.com/langgenius/dify)** ![GitHub stars](https://img.shields.io/github/stars/langgenius/dify?style=social) - Production-ready agentic workflow platform.
- **[OWL (camel-ai/owl)](https://github.com/camel-ai/owl)** ![GitHub stars](https://img.shields.io/github/stars/camel-ai/owl?style=social) - Advanced multi-agent collaboration system.
- **[SuperAGI](https://github.com/TransformerOptimus/SuperAGI)** ![GitHub stars](https://img.shields.io/github/stars/TransformerOptimus/SuperAGI?style=social) - Dev-first autonomous AI agent platform.

#### Agent Memory & State

- **[Letta (ex-MemGPT)](https://github.com/letta-ai/letta)** ![GitHub stars](https://img.shields.io/github/stars/letta-ai/letta?style=social) - Platform for building stateful agents with advanced memory that learn and self-improve over time.
- **[Mem0](https://github.com/mem0ai/mem0)** ![GitHub stars](https://img.shields.io/github/stars/mem0ai/mem0?style=social) - Universal memory layer for AI agents. Persistent, multi-session memory across models and environments.
- **[Forgetful](https://github.com/ScottRBK/forgetful)** ![GitHub stars](https://img.shields.io/github/stars/ScottRBK/forgetful?style=social) - MCP server for persistent AI agent memory. Stores atomic single-concept notes and auto-links them into a knowledge graph via semantic similarity. SQLite or PostgreSQL.
- **[Hindsight](https://github.com/vectorize-io/hindsight)** ![GitHub stars](https://img.shields.io/github/stars/vectorize-io/hindsight?style=social) - State-of-the-art long-term memory for AI agents by Vectorize. Fully self-hosted, MIT-licensed, with integrations for LangChain, CrewAI, LlamaIndex, Vercel AI SDK, and more.

---

### 🔍 5. Retrieval-Augmented Generation (RAG) & Knowledge

> Retrieval systems, vector databases, embedding models, and related tooling for RAG pipelines.

#### Vector Databases & Search Engines

- **[Chroma](https://github.com/chroma-core/chroma)** ![GitHub stars](https://img.shields.io/github/stars/chroma-core/chroma?style=social) - Most popular open-source embedding database.
- **[Qdrant](https://github.com/qdrant/qdrant)** ![GitHub stars](https://img.shields.io/github/stars/qdrant/qdrant?style=social) - High-performance vector search engine in Rust.
- **[Weaviate](https://github.com/weaviate/weaviate)** ![GitHub stars](https://img.shields.io/github/stars/weaviate/weaviate?style=social) - GraphQL-native vector search engine.
- **[Milvus](https://github.com/milvus-io/milvus)** ![GitHub stars](https://img.shields.io/github/stars/milvus-io/milvus?style=social) - Scalable cloud-native vector database.
- **[Faiss](https://github.com/facebookresearch/faiss)** ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/faiss?style=social) - Similarity search and clustering library for dense vectors with CPU and GPU implementations.
- **[NornicDB](https://github.com/orneryd/NornicDB)** ![GitHub stars](https://img.shields.io/github/stars/orneryd/NornicDB?style=social) - Golang Low-latency graph + vector hybrid retrieval, Neo4j and qDrant driver compatible.
- **[LanceDB](https://github.com/lancedb/lancedb)** ![GitHub stars](https://img.shields.io/github/stars/lancedb/lancedb?style=social) - Serverless vector DB optimized for multimodal data.
- **[pgvector](https://github.com/pgvector/pgvector)** ![GitHub stars](https://img.shields.io/github/stars/pgvector/pgvector?style=social) - PostgreSQL extension for vector similarity search.

#### Embedding Models

- **[BGE (FlagEmbedding)](https://github.com/FlagOpen/FlagEmbedding)** ![GitHub stars](https://img.shields.io/github/stars/FlagOpen/FlagEmbedding?style=social) - BAAI's best-in-class embedding family.
- **[E5 (Microsoft)](https://github.com/microsoft/unilm/tree/master/e5)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/unilm?style=social) - High-performance text embeddings for retrieval.
- **[Nomic Embed](https://github.com/nomic-ai/nomic-embed)** ![GitHub stars](https://img.shields.io/github/stars/nomic-ai/nomic-embed?style=social) - Open embedding model with long-context support and reproducible training.

#### RAG Frameworks & Advanced Retrieval Tools

- **[LlamaIndex](https://github.com/run-llama/llama_index)** ![GitHub stars](https://img.shields.io/github/stars/run-llama/llama_index?style=social) - Full-featured RAG pipeline with advanced indexing.
- **[Haystack](https://github.com/deepset-ai/haystack)** ![GitHub stars](https://img.shields.io/github/stars/deepset-ai/haystack?style=social) - End-to-end NLP and RAG framework.
- **[RAGFlow](https://github.com/infiniflow/ragflow)** ![GitHub stars](https://img.shields.io/github/stars/infiniflow/ragflow?style=social) - Deep-document-understanding RAG engine.
- **[GraphRAG (Microsoft)](https://github.com/microsoft/graphrag)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/graphrag?style=social) - Knowledge-graph-based RAG.
- **[Verba (Weaviate)](https://github.com/weaviate/Verba)** ![GitHub stars](https://img.shields.io/github/stars/weaviate/Verba?style=social) - Golden RAG frontend with intuitive UI for retrieval and exploration.
- **[RAGatouille](https://github.com/bclavie/RAGatouille)** ![GitHub stars](https://img.shields.io/github/stars/bclavie/RAGatouille?style=social) - Advanced retrieval tools with late interaction models (ColBERT).
- **[Docling](https://github.com/docling-project/docling)** ![GitHub stars](https://img.shields.io/github/stars/docling-project/docling?style=social) - Document processing toolkit for turning PDFs and other files into structured data for GenAI workflows.
- **[Unstructured](https://github.com/Unstructured-IO/unstructured)** ![GitHub stars](https://img.shields.io/github/stars/Unstructured-IO/unstructured?style=social) - Best-in-class document preprocessing.
- **[ColPali / ColQwen](https://github.com/illuin-tech/colpali)** ![GitHub stars](https://img.shields.io/github/stars/illuin-tech/colpali?style=social) - Vision-language models for document retrieval.

#### Web Data Ingestion

- **[Crawl4AI](https://github.com/unclecode/crawl4ai)** ![GitHub stars](https://img.shields.io/github/stars/unclecode/crawl4ai?style=social) - LLM-friendly web crawler that turns websites into clean Markdown for RAG and agentic workflows.
- **[Lightpanda](https://github.com/lightpanda-io/browser)** ![GitHub stars](https://img.shields.io/github/stars/lightpanda-io/browser?style=social) - Machine-first headless browser in Zig; rendering-free and ultra-lightweight for AI agent browsing.

---

### 🎨 6. Generative Media Tools

> Open-source models and applications for image, video, audio, and 3D generation and editing.

#### Image Generation & Editing

- **[ComfyUI](https://github.com/Comfy-Org/ComfyUI)** ![GitHub stars](https://img.shields.io/github/stars/Comfy-Org/ComfyUI?style=social) - Node-based visual workflow editor for Stable Diffusion, FLUX, etc.
- **[Stable Diffusion WebUI Forge - Neo](https://github.com/Haoming02/sd-webui-forge-classic/tree/neo)** ![GitHub stars](https://img.shields.io/github/stars/Haoming02/sd-webui-forge-classic?style=social) - Actively maintained Forge-based Stable Diffusion web UI with the familiar extension-driven workflow.
- **[Fooocus](https://github.com/lllyasviel/Fooocus)** ![GitHub stars](https://img.shields.io/github/stars/lllyasviel/Fooocus?style=social) - Midjourney-style UI with beautiful out-of-the-box results.
- **[FLUX.1 / FLUX.2 (Black Forest Labs)](https://github.com/black-forest-labs/flux)** ![GitHub stars](https://img.shields.io/github/stars/black-forest-labs/flux?style=social) - State-of-the-art open text-to-image model family.
- **[Diffusers](https://github.com/huggingface/diffusers)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/diffusers?style=social) - PyTorch library for diffusion pipelines spanning image, video, and audio generation.
- **[InvokeAI](https://github.com/invoke-ai/InvokeAI)** ![GitHub stars](https://img.shields.io/github/stars/invoke-ai/InvokeAI?style=social) - Full-featured creative studio.
- **[Stable Diffusion 3.5 (Stability AI)](https://github.com/Stability-AI/sd3.5)** ![GitHub stars](https://img.shields.io/github/stars/Stability-AI/sd3.5?style=social) - Latest open-weight diffusion model.

#### Video Generation

- **[Wan2.2 (Alibaba)](https://github.com/Wan-Video/Wan2.1)** ![GitHub stars](https://img.shields.io/github/stars/Wan-Video/Wan2.1?style=social) - Leading open Mixture-of-Experts text-to-video model.
- **[HunyuanVideo (Tencent)](https://github.com/Tencent-Hunyuan/HunyuanVideo)** ![GitHub stars](https://img.shields.io/github/stars/Tencent-Hunyuan/HunyuanVideo?style=social) - 13B-parameter systematic video generation framework. Leading quality among open models.
- **[SkyReels V2/V3 (Skywork)](https://github.com/SkyworkAI/SkyReels-V2)** ![GitHub stars](https://img.shields.io/github/stars/SkyworkAI/SkyReels-V2?style=social) - First open-source infinite-length film generative model using AutoRegressive Diffusion-Forcing.
- **[Mochi 1 (Genmo)](https://github.com/genmoai/mochi)** ![GitHub stars](https://img.shields.io/github/stars/genmoai/mochi?style=social) - 10B-parameter open video model.
- **[LTX-Video (Lightricks)](https://github.com/Lightricks/LTX-Video)** ![GitHub stars](https://img.shields.io/github/stars/Lightricks/LTX-Video?style=social) - Fast native 4K video generation.
- **[Open-Sora 2.0 (HPC-AI Tech)](https://github.com/hpcaitech/Open-Sora)** ![GitHub stars](https://img.shields.io/github/stars/hpcaitech/Open-Sora?style=social) - Fully open training + inference pipeline.
- **[Stable Video Diffusion (Stability AI)](https://github.com/Stability-AI/generative-models)** ![GitHub stars](https://img.shields.io/github/stars/Stability-AI/generative-models?style=social) - Official image-to-video and text-to-video implementation within Stability AI's generative models repository.
- **[AnimateDiff](https://github.com/guoyww/AnimateDiff)** ![GitHub stars](https://img.shields.io/github/stars/guoyww/AnimateDiff?style=social) - Motion module ecosystem.

#### Audio / Music / Voice Generation

- **[AudioCraft / MusicGen (Meta)](https://github.com/facebookresearch/audiocraft)** ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/audiocraft?style=social) - Controllable text-to-music and audio models.
- **[ACE-Step 1.5](https://github.com/ace-step/ACE-Step-1.5)** ![GitHub stars](https://img.shields.io/github/stars/ace-step/ACE-Step-1.5?style=social) - Local-first music generation model with broad hardware support across Mac, AMD, Intel, and CUDA devices.
- **[Fish Speech](https://github.com/fishaudio/fish-speech)** ![GitHub stars](https://img.shields.io/github/stars/fishaudio/fish-speech?style=social) - Zero-shot TTS and voice cloning.
- **[CosyVoice 2](https://github.com/FunAudioLLM/CosyVoice)** ![GitHub stars](https://img.shields.io/github/stars/FunAudioLLM/CosyVoice?style=social) - Natural multilingual TTS with emotional control.
- **[StyleTTS 2](https://github.com/yl4579/StyleTTS2)** ![GitHub stars](https://img.shields.io/github/stars/yl4579/StyleTTS2?style=social) - Expressive zero-shot TTS.
- **[OuteTTS](https://github.com/edwko/OuteTTS)** ![GitHub stars](https://img.shields.io/github/stars/edwko/OuteTTS?style=social) - High-quality open TTS.
- **[RVC (Retrieval-based Voice Conversion)](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)** ![GitHub stars](https://img.shields.io/github/stars/RVC-Project/Retrieval-based-Voice-Conversion-WebUI?style=social) - Gold standard for real-time voice cloning.

#### 3D & Creative Tools

- **[Hunyuan3D-2 (Tencent)](https://github.com/Tencent-Hunyuan/Hunyuan3D-2)** ![GitHub stars](https://img.shields.io/github/stars/Tencent-Hunyuan/Hunyuan3D-2?style=social) - State-of-the-art open image-to-3D and text-to-3D.
- **[Trellis (Microsoft)](https://github.com/microsoft/TRELLIS)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/TRELLIS?style=social) - Structured 3D latents for high-quality generation.
- **[Wonder3D](https://github.com/xxlong0/Wonder3D)** ![GitHub stars](https://img.shields.io/github/stars/xxlong0/Wonder3D?style=social) - Fast multi-view consistent 3D generation.
- **[TripoSR](https://github.com/VAST-AI-Research/TripoSR)** ![GitHub stars](https://img.shields.io/github/stars/VAST-AI-Research/TripoSR?style=social) - Lightning-fast 3D reconstruction.
- **[Nerfstudio](https://github.com/nerfstudio-project/nerfstudio)** ![GitHub stars](https://img.shields.io/github/stars/nerfstudio-project/nerfstudio?style=social) - End-to-end framework for training, rendering, and experimenting with NeRF and related 3D scene representations.
- **[gsplat (3D Gaussian Splatting tools)](https://github.com/nerfstudio-project/gsplat)** ![GitHub stars](https://img.shields.io/github/stars/nerfstudio-project/gsplat?style=social) - High-performance 3D Gaussian Splatting library.

---

<a id="section-7"></a>

### 🛠️ 7. Training & Fine-tuning Ecosystem

> Tools for model training, fine-tuning, synthetic data generation, and distributed training.

#### Full Training Frameworks

- **[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)** ![GitHub stars](https://img.shields.io/github/stars/hiyouga/LLaMA-Factory?style=social) - One-stop unified framework for SFT, DPO, ORPO, KTO with web UI.
- **[Axolotl](https://github.com/axolotl-ai-cloud/axolotl)** ![GitHub stars](https://img.shields.io/github/stars/axolotl-ai-cloud/axolotl?style=social) - YAML-driven full pipeline for SFT, DPO, GRPO.
- **[Unsloth](https://github.com/unslothai/unsloth)** ![GitHub stars](https://img.shields.io/github/stars/unslothai/unsloth?style=social) - 2× faster, 70% less memory fine-tuning.
- **[LitGPT](https://github.com/Lightning-AI/litgpt)** ![GitHub stars](https://img.shields.io/github/stars/Lightning-AI/litgpt?style=social) - Clean from-scratch implementations of 20+ LLMs.
- **[torchtune](https://github.com/pytorch/torchtune)** ![GitHub stars](https://img.shields.io/github/stars/pytorch/torchtune?style=social) - PyTorch-native library for post-training, fine-tuning, and experimentation with LLMs.
- **[TRL (Transformers Reinforcement Learning)](https://github.com/huggingface/trl)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/trl?style=social) - Official library for RLHF, SFT, DPO, ORPO.

#### LoRA / PEFT Tools

- **[PEFT (Parameter-Efficient Fine-Tuning)](https://github.com/huggingface/peft)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/peft?style=social) - Official library with LoRA, QLoRA, DoRA, etc.
- **[Liger Kernel](https://github.com/linkedin/Liger-Kernel)** ![GitHub stars](https://img.shields.io/github/stars/linkedin/Liger-Kernel?style=social) - Ultra-fast custom kernels for training speedup.
- **[MergeKit](https://github.com/arcee-ai/mergekit)** ![GitHub stars](https://img.shields.io/github/stars/arcee-ai/mergekit?style=social) - Advanced model merging tools.

#### Synthetic Data Generation

- **[distilabel](https://github.com/argilla-io/distilabel)** ![GitHub stars](https://img.shields.io/github/stars/argilla-io/distilabel?style=social) - End-to-end pipeline for synthetic instruction data.
- **[Data-Juicer](https://github.com/alibaba/data-juicer)** ![GitHub stars](https://img.shields.io/github/stars/alibaba/data-juicer?style=social) - High-performance data processing for LLM training.
- **[Argilla](https://github.com/argilla-io/argilla)** ![GitHub stars](https://img.shields.io/github/stars/argilla-io/argilla?style=social) - Open-source data labeling + synthetic data platform.
- **[SDV (Synthetic Data Vault)](https://github.com/sdv-dev/SDV)** ![GitHub stars](https://img.shields.io/github/stars/sdv-dev/SDV?style=social) - High-fidelity tabular and relational synthetic data.

#### Distributed Training

- **[DeepSpeed](https://github.com/deepspeedai/DeepSpeed)** ![GitHub stars](https://img.shields.io/github/stars/deepspeedai/DeepSpeed?style=social) - Extreme-scale training optimizations.
- **[Colossal-AI](https://github.com/hpcaitech/ColossalAI)** ![GitHub stars](https://img.shields.io/github/stars/hpcaitech/ColossalAI?style=social) - Unified system for 100B+ models.
- **[Megatron-LM](https://github.com/NVIDIA/Megatron-LM)** ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/Megatron-LM?style=social) - Distributed training framework and reference codebase for large transformer models at scale.
- **[Ray Train](https://github.com/ray-project/ray)** ![GitHub stars](https://img.shields.io/github/stars/ray-project/ray?style=social) - Scalable distributed training.

---

### 📊 8. MLOps / LLMOps & Production

> Tooling for tracking, deploying, monitoring, and operating AI systems in production.

#### Experiment Tracking & Versioning

- **[MLflow](https://github.com/mlflow/mlflow)** ![GitHub stars](https://img.shields.io/github/stars/mlflow/mlflow?style=social) - End-to-end open platform for the ML/LLM lifecycle.
- **[DVC (Data Version Control)](https://github.com/iterative/dvc)** ![GitHub stars](https://img.shields.io/github/stars/iterative/dvc?style=social) - Git-like versioning for data and models.
- **[ClearML](https://github.com/clearml/clearml)** ![GitHub stars](https://img.shields.io/github/stars/clearml/clearml?style=social) - Open-source platform for experiment tracking, orchestration, data management, and model serving.
- **[Weights & Biases Weave](https://github.com/wandb/weave)** ![GitHub stars](https://img.shields.io/github/stars/wandb/weave?style=social) - Open-source tracing and experiment tracking.

#### Deployment & Orchestration

- **[BentoML](https://github.com/bentoml/BentoML)** ![GitHub stars](https://img.shields.io/github/stars/bentoml/BentoML?style=social) - Unified framework to build, ship, and scale AI apps.
- **[Ray Serve](https://github.com/ray-project/ray)** ![GitHub stars](https://img.shields.io/github/stars/ray-project/ray?style=social) - Scalable model serving library.
- **[ZenML](https://github.com/zenml-io/zenml)** ![GitHub stars](https://img.shields.io/github/stars/zenml-io/zenml?style=social) - Pipeline and orchestration framework for taking ML and LLM systems from development to production.
- **[Kubeflow](https://github.com/kubeflow/kubeflow)** ![GitHub stars](https://img.shields.io/github/stars/kubeflow/kubeflow?style=social) - Kubernetes-native ML/LLM platform.
- **[KServe](https://github.com/kserve/kserve)** ![GitHub stars](https://img.shields.io/github/stars/kserve/kserve?style=social) - Kubernetes-based model serving.

#### Monitoring, Evaluation & Observability

- **[Langfuse](https://github.com/langfuse/langfuse)** ![GitHub stars](https://img.shields.io/github/stars/langfuse/langfuse?style=social) - #1 open-source LLM observability platform.
- **[Phoenix (Arize)](https://github.com/Arize-ai/phoenix)** ![GitHub stars](https://img.shields.io/github/stars/Arize-ai/phoenix?style=social) - AI observability & evaluation platform.
- **[Evidently](https://github.com/evidentlyai/evidently)** ![GitHub stars](https://img.shields.io/github/stars/evidentlyai/evidently?style=social) - ML & LLM monitoring framework.
- **[Opik (Comet)](https://github.com/comet-ml/opik)** ![GitHub stars](https://img.shields.io/github/stars/comet-ml/opik?style=social) - Production-ready LLM evaluation platform.

#### Guardrails & Safety Tools

- **[NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)** ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/NeMo-Guardrails?style=social) - Programmable guardrails toolkit.
- **[Guardrails AI](https://github.com/guardrails-ai/guardrails)** ![GitHub stars](https://img.shields.io/github/stars/guardrails-ai/guardrails?style=social) - Structure and validation for LLM outputs.
- **[LLM Guard](https://github.com/protectai/llm-guard)** ![GitHub stars](https://img.shields.io/github/stars/protectai/llm-guard?style=social) - Comprehensive input/output scanner.
- **[Director-AI](https://github.com/anulum/director-ai)** ![GitHub stars](https://img.shields.io/github/stars/anulum/director-ai?style=social) - Real-time LLM hallucination guardrail with NLI + RAG fact-checking and token-level streaming halt.
- **[LlamaGuard (Meta)](https://github.com/meta-llama/PurpleLlama)** ![GitHub stars](https://img.shields.io/github/stars/meta-llama/PurpleLlama?style=social) - Open safety classifier models.
- **[Garak](https://github.com/leondz/garak)** ![GitHub stars](https://img.shields.io/github/stars/leondz/garak?style=social) - LLM vulnerability scanner.
- **[Promptfoo](https://github.com/promptfoo/promptfoo)** ![GitHub stars](https://img.shields.io/github/stars/promptfoo/promptfoo?style=social) - LLM testing and red-teaming framework.

---

### 📈 9. Evaluation, Benchmarks & Datasets

> Benchmarks, evaluation frameworks, datasets, and supporting tools for model assessment.

#### Benchmark Suites

- **[lm-evaluation-harness (EleutherAI)](https://github.com/EleutherAI/lm-evaluation-harness)** ![GitHub stars](https://img.shields.io/github/stars/EleutherAI/lm-evaluation-harness?style=social) - De-facto standard for generative model evaluation.
- **[HELM (Stanford)](https://github.com/stanford-crfm/helm)** ![GitHub stars](https://img.shields.io/github/stars/stanford-crfm/helm?style=social) - Holistic Evaluation of Language Models.
- **[GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA)** - Real-world multi-step agentic benchmark.
- **[LiveCodeBench](https://github.com/livecodebench/livecodebench)** ![GitHub stars](https://img.shields.io/github/stars/livecodebench/livecodebench?style=social) - Contamination-free coding benchmark.
- **[MMLU-Pro / GPQA](https://github.com/TIGER-AI-Lab/MMLU-Pro)** ![GitHub stars](https://img.shields.io/github/stars/TIGER-AI-Lab/MMLU-Pro?style=social) - Hardened expert-level benchmarks.
- **[OpenCompass](https://github.com/open-compass/opencompass)** ![GitHub stars](https://img.shields.io/github/stars/open-compass/opencompass?style=social) - Evaluation platform for benchmarking language and multimodal models across large benchmark suites.
- **[SWE-rebench (Nebius)](https://huggingface.co/datasets/nebius/SWE-rebench)** - Continuously updated benchmark with 21,000+ real-world SWE tasks for evaluating agentic LLMs. Decontaminated, mined from GitHub.

#### Evaluation Frameworks

- **[DeepEval](https://github.com/confident-ai/deepeval)** ![GitHub stars](https://img.shields.io/github/stars/confident-ai/deepeval?style=social) - The "Pytest for LLMs".
- **[RAGAs](https://github.com/explodinggradients/ragas)** ![GitHub stars](https://img.shields.io/github/stars/explodinggradients/ragas?style=social) - End-to-end RAG evaluation framework.
- **[Lighteval](https://github.com/huggingface/lighteval)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/lighteval?style=social) - Evaluation toolkit for LLMs across multiple backends with reusable tasks, metrics, and result tracking.
- **[Hugging Face Evaluate](https://github.com/huggingface/evaluate)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/evaluate?style=social) - Standardized evaluation metrics.

#### High-quality Open Datasets & Data Tools

- **[Hugging Face Datasets](https://github.com/huggingface/datasets)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/datasets?style=social) - Largest open repository of datasets.
- **[FineWeb / FineWeb-2 (Hugging Face)](https://huggingface.co/datasets/HuggingFaceFW/fineweb)** - Curated 15T+ token web dataset for pre-training.
- **[RedPajama](https://github.com/togethercomputer/RedPajama-Data)** ![GitHub stars](https://img.shields.io/github/stars/togethercomputer/RedPajama-Data?style=social) - Clean, reproducible Llama training data mix.
- **[OSWorld](https://github.com/xlang-ai/OSWorld)** ![GitHub stars](https://img.shields.io/github/stars/xlang-ai/OSWorld?style=social) - Multimodal agent benchmark dataset.

---

<a id="section-10"></a>

### 🛡️ 10. AI Safety, Alignment & Interpretability

> Tools for alignment, interpretability, safety evaluation, and adversarial testing.

#### Alignment & RLHF Tools

- **[Safe-RLHF](https://github.com/PKU-Alignment/safe-rlhf)** ![GitHub stars](https://img.shields.io/github/stars/PKU-Alignment/safe-rlhf?style=social) - Safe reinforcement learning from human feedback.
- **[Alignment Handbook](https://github.com/huggingface/alignment-handbook)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/alignment-handbook?style=social) - Complete recipes for full-stack alignment.
- **[OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)** ![GitHub stars](https://img.shields.io/github/stars/OpenRLHF/OpenRLHF?style=social) - High-performance distributed RLHF framework.

#### Interpretability & Explainability

- **[TransformerLens](https://github.com/TransformerLensOrg/TransformerLens)** ![GitHub stars](https://img.shields.io/github/stars/TransformerLensOrg/TransformerLens?style=social) - Gold-standard for mechanistic interpretability.
- **[nnsight](https://github.com/ndif-team/nnsight)** ![GitHub stars](https://img.shields.io/github/stars/ndif-team/nnsight?style=social) - Scalable library for intervening on neural networks.
- **[SAELens](https://github.com/jbloomAus/SAELens)** ![GitHub stars](https://img.shields.io/github/stars/jbloomAus/SAELens?style=social) - Sparse autoencoders for interpretable features.
- **[Captum](https://github.com/pytorch/captum)** ![GitHub stars](https://img.shields.io/github/stars/pytorch/captum?style=social) - PyTorch's official interpretability library.

#### Adversarial & Red-teaming Tools

- **[Garak](https://github.com/NVIDIA/garak)** ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/garak?style=social) - Automated LLM vulnerability scanner.
- **[PyRIT (Python Risk Identification Tool)](https://github.com/Azure/PyRIT)** ![GitHub stars](https://img.shields.io/github/stars/Azure/PyRIT?style=social) - Framework for custom adversarial testing.
- **[Promptfoo](https://github.com/promptfoo/promptfoo)** ![GitHub stars](https://img.shields.io/github/stars/promptfoo/promptfoo?style=social) - Systematic prompt testing and red-teaming.
- **[LLM Guard](https://github.com/protectai/llm-guard)** ![GitHub stars](https://img.shields.io/github/stars/protectai/llm-guard?style=social) - Input/output scanner for LLMs.

---

### 🧩 11. Specialized Domains

#### Computer Vision

- **[OpenCV](https://github.com/opencv/opencv)** ![GitHub stars](https://img.shields.io/github/stars/opencv/opencv?style=social) - World's most widely used computer vision library.
- **[Ultralytics YOLO](https://github.com/ultralytics/ultralytics)** ![GitHub stars](https://img.shields.io/github/stars/ultralytics/ultralytics?style=social) - State-of-the-art real-time object detection.
- **[Detectron2](https://github.com/facebookresearch/detectron2)** ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/detectron2?style=social) - High-performance object detection library.
- **[SAM 2](https://github.com/facebookresearch/sam2)** ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/sam2?style=social) - Promptable image and video segmentation model with released checkpoints and training code.
- **[Kornia](https://github.com/kornia/kornia)** ![GitHub stars](https://img.shields.io/github/stars/kornia/kornia?style=social) - Differentiable computer vision library.
- **[MediaPipe](https://github.com/google-ai-edge/mediapipe)** ![GitHub stars](https://img.shields.io/github/stars/google-ai-edge/mediapipe?style=social) - Cross-platform multimodal pipelines.

#### Reinforcement Learning & Robotics

- **[Stable-Baselines3](https://github.com/DLR-RM/stable-baselines3)** ![GitHub stars](https://img.shields.io/github/stars/DLR-RM/stable-baselines3?style=social) - Production-ready RL algorithms.
- **[CleanRL](https://github.com/vwxyzjn/cleanrl)** ![GitHub stars](https://img.shields.io/github/stars/vwxyzjn/cleanrl?style=social) - Single-file readable RL implementations.
- **[JaxMARL](https://github.com/FLAIROx/JaxMARL)** ![GitHub stars](https://img.shields.io/github/stars/FLAIROx/JaxMARL?style=social) - Multi-Agent Reinforcement Learning with JAX. Accelerated environments and baselines.
- **[Isaac Lab](https://github.com/isaac-sim/IsaacLab)** ![GitHub stars](https://img.shields.io/github/stars/isaac-sim/IsaacLab?style=social) - GPU-accelerated robot learning framework.
- **[Gymnasium (ex-OpenAI Gym)](https://github.com/Farama-Foundation/Gymnasium)** ![GitHub stars](https://img.shields.io/github/stars/Farama-Foundation/Gymnasium?style=social) - Standard RL environment API.

#### Time Series & Scientific AI

- **[Time Series Library (TSLib)](https://github.com/thuml/Time-Series-Library)** ![GitHub stars](https://img.shields.io/github/stars/thuml/Time-Series-Library?style=social) - Comprehensive benchmark for time-series models.
- **[Chronos (Amazon)](https://github.com/amazon-science/chronos-forecasting)** ![GitHub stars](https://img.shields.io/github/stars/amazon-science/chronos-forecasting?style=social) - Pretrained foundation models for time-series forecasting.
- **[Darts](https://github.com/unit8co/darts)** ![GitHub stars](https://img.shields.io/github/stars/unit8co/darts?style=social) - Easy-to-use time-series forecasting library.
- **[AutoTS](https://github.com/winedarksea/AutoTS)** ![GitHub stars](https://img.shields.io/github/stars/winedarksea/AutoTS?style=social) - Automated time series forecasting with broad model selection, ensembling, anomaly detection, and holiday effects. Designed for production deployment with minimal setup.

#### Edge / On-device AI

- **[TensorFlow Lite](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite)** ![GitHub stars](https://img.shields.io/github/stars/tensorflow/tensorflow?style=social) - Lightweight on-device ML.
- **[ONNX Runtime](https://github.com/microsoft/onnxruntime)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/onnxruntime?style=social) - Cross-platform high-performance inference.
- **[ExecuTorch](https://github.com/pytorch/executorch)** ![GitHub stars](https://img.shields.io/github/stars/pytorch/executorch?style=social) - PyTorch runtime and toolchain for deploying AI models on mobile, embedded, and edge devices.
- **[OpenVINO](https://github.com/openvinotoolkit/openvino)** ![GitHub stars](https://img.shields.io/github/stars/openvinotoolkit/openvino?style=social) - Intel's toolkit for edge deployment.
- **[MicroTVM (Apache TVM)](https://github.com/apache/tvm)** ![GitHub stars](https://img.shields.io/github/stars/apache/tvm?style=social) - Compiler stack for microcontrollers.

---

<a id="section-12"></a>

### 🖥️ 12. User Interfaces & Self-hosted Platforms

#### Local AI Chat UIs & Personal Assistants

- **[OpenClaw](https://github.com/openclaw/openclaw)** ![GitHub stars](https://img.shields.io/github/stars/openclaw/openclaw?style=social) - Local-first personal AI assistant with multi-channel integrations and full agentic task execution.
- **[Open WebUI](https://github.com/open-webui/open-webui)** ![GitHub stars](https://img.shields.io/github/stars/open-webui/open-webui?style=social) - Most popular self-hosted ChatGPT-style interface.
- **[text-generation-webui](https://github.com/oobabooga/text-generation-webui)** ![GitHub stars](https://img.shields.io/github/stars/oobabooga/text-generation-webui?style=social) - Web UI for running local LLMs with multiple backends, extensions, and model formats.
- **[LobeChat](https://github.com/lobehub/lobe-chat)** ![GitHub stars](https://img.shields.io/github/stars/lobehub/lobe-chat?style=social) - Sleek modern chat UI.
- **[LibreChat](https://github.com/danny-avila/LibreChat)** ![GitHub stars](https://img.shields.io/github/stars/danny-avila/LibreChat?style=social) - Feature-packed multi-LLM interface.
- **[HuggingChat (self-hosted)](https://github.com/huggingface/chat-ui)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/chat-ui?style=social) - Official open-source codebase for HuggingChat.
- **[Khoj](https://github.com/khoj-ai/khoj)** ![GitHub stars](https://img.shields.io/github/stars/khoj-ai/khoj?style=social) - Self-hostable personal AI assistant for search, chat, automation, and workflows over local and web data.
- **[Newelle](https://github.com/qwersyk/Newelle)** ![GitHub stars](https://img.shields.io/github/stars/qwersyk/Newelle?style=social) - GNOME/Linux desktop virtual assistant with integrated file editor, global hotkeys, and profile manager.

#### Full Self-hosted AI Platforms

- **[AnythingLLM](https://github.com/Mintplex-Labs/anything-llm)** ![GitHub stars](https://img.shields.io/github/stars/Mintplex-Labs/anything-llm?style=social) - All-in-one RAG + agents platform.
- **[Dify](https://github.com/langgenius/dify)** ![GitHub stars](https://img.shields.io/github/stars/langgenius/dify?style=social) - Complete AI application platform with visual builder.
- **[Langflow](https://github.com/langflow-ai/langflow)** ![GitHub stars](https://img.shields.io/github/stars/langflow-ai/langflow?style=social) - Visual low-code platform for LangChain flows.
- **[Flowise](https://github.com/FlowiseAI/Flowise)** ![GitHub stars](https://img.shields.io/github/stars/FlowiseAI/Flowise?style=social) - Drag-and-drop LLM app builder.

#### Desktop & Mobile AI Apps

- **[GPT4All](https://github.com/nomic-ai/gpt4all)** ![GitHub stars](https://img.shields.io/github/stars/nomic-ai/gpt4all?style=social) - Privacy-first local desktop chatbot.
- **[Jan](https://github.com/janhq/jan)** ![GitHub stars](https://img.shields.io/github/stars/janhq/jan?style=social) - Local-first AI app framework.
- **[SillyTavern](https://github.com/SillyTavern/SillyTavern)** ![GitHub stars](https://img.shields.io/github/stars/SillyTavern/SillyTavern?style=social) - Highly customizable role-playing frontend.

---

### 🧪 13. Developer Tools & Integrations

#### AI Coding Assistants (open-source)

- **[Continue](https://github.com/continuedev/continue)** ![GitHub stars](https://img.shields.io/github/stars/continuedev/continue?style=social) - Open-source AI coding autopilot for VS Code & JetBrains.
- **[Tabby](https://github.com/TabbyML/tabby)** ![GitHub stars](https://img.shields.io/github/stars/TabbyML/tabby?style=social) - Self-hosted AI coding assistant.
- **[Cline](https://github.com/cline/cline)** ![GitHub stars](https://img.shields.io/github/stars/cline/cline?style=social) - Open-source IDE coding agent that can edit files, run commands, and use tools with user approval.
- **[Open Interpreter](https://github.com/OpenInterpreter/open-interpreter)** ![GitHub stars](https://img.shields.io/github/stars/OpenInterpreter/open-interpreter?style=social) - Lets LLMs run code locally.
- **[Roo Code](https://github.com/RooCodeInc/Roo-Code)** ![GitHub stars](https://img.shields.io/github/stars/RooCodeInc/Roo-Code?style=social) - Open-source editor-based coding agent with multiple modes and tool integrations.
- **[Aider](https://github.com/paul-gauthier/aider)** ![GitHub stars](https://img.shields.io/github/stars/paul-gauthier/aider?style=social) - Terminal-based AI pair programmer.

#### IDE Plugins & Extensions

- **[llama.vim](https://github.com/ggml-org/llama.vim)** ![GitHub stars](https://img.shields.io/github/stars/ggml-org/llama.vim?style=social) - Local LLM-powered code completion plugin for Vim/Neovim using llama.cpp. Fast, privacy-first, no API key needed.
- **[CodeCompanion.nvim](https://github.com/olimorris/codecompanion.nvim)** ![GitHub stars](https://img.shields.io/github/stars/olimorris/codecompanion.nvim?style=social) - AI-powered coding assistant for Neovim. Inline code generation, chat, actions, and tool use with support for multiple LLM providers.
- **[Continue VS Code / JetBrains](https://github.com/continuedev/continue)** ![GitHub stars](https://img.shields.io/github/stars/continuedev/continue?style=social) - Most installed open-source AI extension.
- **[Jupyter AI](https://github.com/jupyterlab/jupyter-ai)** ![GitHub stars](https://img.shields.io/github/stars/jupyterlab/jupyter-ai?style=social) - Chat and code generation inside notebooks.

#### Testing & Debugging Tools

- **[Promptfoo](https://github.com/promptfoo/promptfoo)** ![GitHub stars](https://img.shields.io/github/stars/promptfoo/promptfoo?style=social) - Systematic LLM testing framework.
- **[DeepEval](https://github.com/confident-ai/deepeval)** ![GitHub stars](https://img.shields.io/github/stars/confident-ai/deepeval?style=social) - LLM unit-testing framework.
- **[Garak](https://github.com/NVIDIA/garak)** ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/garak?style=social) - LLM vulnerability scanner.
- **[Phoenix (Arize)](https://github.com/Arize-ai/phoenix)** ![GitHub stars](https://img.shields.io/github/stars/Arize-ai/phoenix?style=social) - AI observability for development.

---

### 📚 14. Resources & Learning

#### Papers with Open Implementations

- **[Papers with Code](https://paperswithcode.com)** - Definitive database linking papers to open code and datasets.
- **[Hugging Face Papers](https://huggingface.co/papers)** - Daily-updated feed of the latest arXiv papers with open weights.
- **[Open LLM Leaderboard (Hugging Face)](https://huggingface.co/spaces/open-llm-leaderboard)** - Real-time ranking of open models.

#### Communities, Forums & Newsletters

- **[Hugging Face Discussions](https://discuss.huggingface.co)** - Largest open AI forum.
- **[r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA)** - Go-to subreddit for local/open-source LLM topics.

#### Courses & Interactive Playgrounds

- **[Hugging Face Course](https://huggingface.co/learn)** - Free hands-on courses using only open models.
- **[Fast.ai](https://github.com/fastai/fastai)** ![GitHub stars](https://img.shields.io/github/stars/fastai/fastai?style=social) - Legendary practical deep learning course.
- **[LangChain Academy](https://academy.langchain.com)** - Free courses on agents and RAG.
- **[ComfyUI Examples & Workflows](https://github.com/Comfy-Org/example_workflows)** ![GitHub stars](https://img.shields.io/github/stars/Comfy-Org/example_workflows?style=social) - Massive collection of generative media workflows.

#### Starter Projects & Examples

- **[PyTorch Examples](https://github.com/pytorch/examples)** ![GitHub stars](https://img.shields.io/github/stars/pytorch/examples?style=social) - Official tutorials: image classification, NLP, reinforcement learning.
- **[TensorFlow Tutorials](https://github.com/tensorflow/docs/tree/master/site/en/tutorials)** - Official guides for beginners to advanced users.
- **[Hugging Face Transformers Notebooks](https://github.com/huggingface/notebooks)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/notebooks?style=social) - Run Transformers, Datasets, and more in Colab.
- **[Deep Learning Examples (NVIDIA)](https://github.com/NVIDIA/DeepLearningExamples)** ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/DeepLearningExamples?style=social) - Production-quality reference implementations.

---

## Contributing

Contributions are **highly welcome**!
Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines (quality standards, formatting, license requirements, etc.).

- Only **OSI-approved** licenses
- Projects must be actively maintained (commits in last 6 months)
- High-quality, well-documented, real adoption

## License

This list itself is licensed under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).
Feel free to use it for any purpose.

---

**Made with ❤️ for the open-source AI community.**
Star the repo if you find it useful - it helps more people discover the best open tools!

---
