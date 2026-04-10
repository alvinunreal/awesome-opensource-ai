<div align="center">

<img src="assets/osai.png" alt="Awesome Open Source AI" width="120" />

# Awesome Open Source AI

*A curated list of **battle-tested, production-proven** open-source AI models, libraries, infrastructure, and developer tools. Only elite-tier projects make this list.*

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](./CONTRIBUTING.md)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-blue.svg?style=flat-square)](./LICENSE)

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

**[ 🌱 Emerging ](./EMERGING.md)** • **[ Explore the List ](#-contents)** • **[ Submission Guidelines ](#contributing)** • **[ License ](#license)**

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
- **[NumPyro](https://github.com/pyro-ppl/numpyro)** ![GitHub stars](https://img.shields.io/github/stars/pyro-ppl/numpyro?style=social) - Probabilistic programming with NumPy powered by JAX for autograd and JIT compilation. Bayesian modeling and inference at scale.
- **[Keras](https://github.com/keras-team/keras)** ![GitHub stars](https://img.shields.io/github/stars/keras-team/keras?style=social) - High-level, beginner-friendly API that now runs on multiple backends (TensorFlow, JAX, PyTorch). Perfect for rapid experimentation.
- **[tinygrad](https://github.com/tinygrad/tinygrad)** ![GitHub stars](https://img.shields.io/github/stars/tinygrad/tinygrad?style=social) - Minimalist deep learning framework with tiny code footprint. The "you like pytorch? you like micrograd? you love tinygrad!" philosophy - simple yet powerful.
- **[PyTorch Geometric](https://github.com/pyg-team/pytorch_geometric)** ![GitHub stars](https://img.shields.io/github/stars/pyg-team/pytorch_geometric?style=social) - Library for deep learning on irregular input data such as graphs, point clouds, and manifolds. Part of the PyTorch ecosystem.

#### Rust ML Frameworks

- **[Burn](https://github.com/tracel-ai/burn)** ![GitHub stars](https://img.shields.io/github/stars/tracel-ai/burn?style=social) - Next-generation deep learning framework in Rust. Backend-agnostic with CPU, GPU, WebAssembly support.
- **[Candle (Hugging Face)](https://github.com/huggingface/candle)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/candle?style=social) - Minimalist ML framework for Rust. PyTorch-like API with focus on performance and simplicity.
- **[linfa](https://github.com/rust-ml/linfa)** ![GitHub stars](https://img.shields.io/github/stars/rust-ml/linfa?style=social) - Comprehensive Rust ML toolkit with classical algorithms. scikit-learn equivalent for Rust with clustering, regression, and preprocessing.

#### Julia ML Frameworks

- **[Flux.jl](https://github.com/FluxML/Flux.jl)** ![GitHub stars](https://img.shields.io/github/stars/FluxML/Flux.jl?style=social) - 100% pure-Julia ML stack with lightweight abstractions on top of native GPU and AD support. Elegant, hackable, and fully integrated with Julia's scientific computing ecosystem.
- **[MLJ.jl](https://github.com/JuliaAI/MLJ.jl)** ![GitHub stars](https://img.shields.io/github/stars/JuliaAI/MLJ.jl?style=social) - Comprehensive Julia machine learning framework providing a unified interface to 200+ models with meta-algorithms for selection, tuning, and evaluation. MIT licensed.

#### NLP & Transformers

- **[spaCy (Explosion AI)](https://github.com/explosion/spaCy)** ![GitHub stars](https://img.shields.io/github/stars/explosion/spaCy?style=social) - Industrial-strength natural language processing with 75+ languages, transformer pipelines, and production-grade NER, parsing, and text classification.
- **[Transformers (Hugging Face)](https://github.com/huggingface/transformers)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/transformers?style=social) - The de facto standard library for pretrained NLP models. 1M+ models, 250,000+ downloads/day. BERT, GPT, Llama, Qwen, and hundreds more.
- **[sentence-transformers](https://github.com/UKPLab/sentence-transformers)** ![GitHub stars](https://img.shields.io/github/stars/UKPLab/sentence-transformers?style=social) - Classic library for sentence and image embeddings.
- **[tokenizers (Hugging Face)](https://github.com/huggingface/tokenizers)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/tokenizers?style=social) - Fast state-of-the-art tokenizers for training and inference.

#### Data Processing & Manipulation

- **[Pandas](https://github.com/pandas-dev/pandas)** ![GitHub stars](https://img.shields.io/github/stars/pandas-dev/pandas?style=social) - The gold standard for data analysis and manipulation in Python.
- **[Polars](https://github.com/pola-rs/polars)** ![GitHub stars](https://img.shields.io/github/stars/pola-rs/polars?style=social) - Blazing-fast DataFrame library (Rust backend) - modern alternative to pandas for large-scale workloads.
- **[cuDF](https://github.com/rapidsai/cudf)** ![GitHub stars](https://img.shields.io/github/stars/rapidsai/cudf?style=social) - GPU DataFrame library from RAPIDS. Accelerates pandas workflows on NVIDIA GPUs with zero code changes using cuDF.pandas accelerator mode.
- **[Modin](https://github.com/modin-project/modin)** ![GitHub stars](https://img.shields.io/github/stars/modin-project/modin?style=social) - Parallel pandas DataFrames. Scale pandas workflows by changing a single line of code - distributes data and computation automatically.
- **[Dask](https://github.com/dask/dask)** ![GitHub stars](https://img.shields.io/github/stars/dask/dask?style=social) - Parallel computing for big data - scales pandas/NumPy/scikit-learn to clusters.
- **[NumPy](https://github.com/numpy/numpy)** ![GitHub stars](https://img.shields.io/github/stars/numpy/numpy?style=social) - Fundamental array computing library that powers almost every AI stack.
- **[SciPy](https://github.com/scipy/scipy)** ![GitHub stars](https://img.shields.io/github/stars/scipy/scipy?style=social) - Scientific computing algorithms (optimization, linear algebra, statistics, signal processing).
- **[NetworkX](https://github.com/networkx/networkx)** ![GitHub stars](https://img.shields.io/github/stars/networkx/networkx?style=social) - Creation, manipulation, and study of complex networks. The foundational graph analysis library for Python data science.
- **[cuGraph](https://github.com/rapidsai/cugraph)** ![GitHub stars](https://img.shields.io/github/stars/rapidsai/cugraph?style=social) - GPU graph analytics library with NetworkX-compatible API. 10-100x faster than CPU for large-scale graph algorithms. Apache 2.0 licensed.
- **[Vaex](https://github.com/vaexio/vaex)** ![GitHub stars](https://img.shields.io/github/stars/vaexio/vaex?style=social) - Out-of-Core hybrid Apache Arrow/NumPy DataFrame for Python. Visualize and explore billion-row datasets at millions of rows per second. MIT licensed.
- **[Datashader](https://github.com/holoviz/datashader)** ![GitHub stars](https://img.shields.io/github/stars/holoviz/datashader?style=social) - High-performance large data visualization. Renders billions of points interactively without aggregation artifacts. BSD-3-Clause licensed.
- **[Zarr](https://github.com/zarr-developers/zarr-python)** ![GitHub stars](https://img.shields.io/github/stars/zarr-developers/zarr-python?style=social) - Chunked, compressed, N-dimensional array storage. Scalable tensor data format optimized for cloud and parallel computing. MIT licensed.
- **[NVIDIA DALI](https://github.com/NVIDIA/DALI)** ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/DALI?style=social) - GPU-accelerated data loading and augmentation library with highly optimized building blocks for deep learning applications. Apache 2.0 licensed.
- **[Narwhals](https://github.com/narwhals-dev/narwhals)** ![GitHub stars](https://img.shields.io/github/stars/narwhals-dev/narwhals?style=social) - Lightweight compatibility layer between DataFrame libraries. Write Polars-like code that works seamlessly across pandas, Polars, cuDF, Modin, and more. MIT licensed.

#### Classical ML & Gradient Boosting

- **[scikit-learn](https://github.com/scikit-learn/scikit-learn)** ![GitHub stars](https://img.shields.io/github/stars/scikit-learn/scikit-learn?style=social) - Industry-standard library for traditional machine learning (classification, regression, clustering, pipelines).
- **[XGBoost](https://github.com/dmlc/xgboost)** ![GitHub stars](https://img.shields.io/github/stars/dmlc/xgboost?style=social) - Scalable, high-performance gradient boosting library. Still dominates Kaggle and tabular competitions.
- **[LightGBM](https://github.com/microsoft/LightGBM)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/LightGBM?style=social) - Microsoft's ultra-fast gradient boosting framework, optimized for speed and memory.
- **[CatBoost](https://github.com/catboost/catboost)** ![GitHub stars](https://img.shields.io/github/stars/catboost/catboost?style=social) - Gradient boosting that handles categorical features natively with great out-of-the-box performance.
- **[sktime](https://github.com/sktime/sktime)** ![GitHub stars](https://img.shields.io/github/stars/sktime/sktime?style=social) - Unified framework for machine learning with time series. Scikit-learn compatible API for forecasting, classification, clustering, and anomaly detection.
- **[StatsForecast](https://github.com/Nixtla/statsforecast)** ![GitHub stars](https://img.shields.io/github/stars/Nixtla/statsforecast?style=social) - Lightning-fast statistical forecasting with ARIMA, ETS, CES, and Theta models. Optimized for high-performance time series workloads.
- **[cuML](https://github.com/rapidsai/cuml)** ![GitHub stars](https://img.shields.io/github/stars/rapidsai/cuml?style=social) - GPU-accelerated machine learning algorithms with scikit-learn compatible API. 10-50x faster than CPU implementations for large datasets. Apache 2.0 licensed.
- **[SynapseML](https://github.com/microsoft/SynapseML)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/SynapseML?style=social) - Distributed machine learning on Apache Spark. Scalable, composable APIs for text analytics, vision, anomaly detection with seamless Python/Scala/R/.NET integration. MIT licensed.

#### AutoML & Hyperparameter Optimization

- **[Optuna](https://github.com/optuna/optuna)** ![GitHub stars](https://img.shields.io/github/stars/optuna/optuna?style=social) - Modern, define-by-run hyperparameter optimization with pruning and visualizations. Extremely popular in 2026.
- **[AutoGluon](https://github.com/autogluon/autogluon)** ![GitHub stars](https://img.shields.io/github/stars/autogluon/autogluon?style=social) - AWS AutoML toolkit for tabular, image, text, and multimodal data - state-of-the-art with almost zero code.
- **[FLAML](https://github.com/microsoft/FLAML)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/FLAML?style=social) - Microsoft's fast & lightweight AutoML focused on efficiency and low compute.
- **[AutoKeras](https://github.com/keras-team/autokeras)** ![GitHub stars](https://img.shields.io/github/stars/keras-team/autokeras?style=social) - Neural architecture search on top of Keras.

#### Model Training & Optimization Utilities

- **[Hugging Face Accelerate](https://github.com/huggingface/accelerate)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/accelerate?style=social) - Simple API to make training scripts run on any hardware (multi-GPU, TPU, mixed precision) with minimal code changes.
- **[DeepSpeed](https://github.com/microsoft/DeepSpeed)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/DeepSpeed?style=social) - Microsoft's deep learning optimization library for extreme-scale training (ZeRO, offloading, MoE).
- **[Transformers](https://github.com/huggingface/transformers)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/transformers?style=social) - Library of pretrained transformer models and utilities for text, vision, audio, and multimodal training and inference.
- **[FlashAttention](https://github.com/Dao-AILab/flash-attention)** ![GitHub stars](https://img.shields.io/github/stars/Dao-AILab/flash-attention?style=social) - Fast exact attention kernels that reduce memory usage and accelerate transformer training and inference.
- **[xFormers](https://github.com/facebookresearch/xformers)** ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/xformers?style=social) - Optimized transformer building blocks and attention operators for PyTorch.
- **[PyTorch Lightning](https://github.com/Lightning-AI/lightning)** ![GitHub stars](https://img.shields.io/github/stars/Lightning-AI/lightning?style=social) - High-level wrapper for PyTorch that removes boilerplate and adds best practices.
- **[ONNX Runtime](https://github.com/microsoft/onnxruntime)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/onnxruntime?style=social) - High-performance inference and training for ONNX models across hardware.
- **[einops](https://github.com/arogozhnikov/einops)** ![GitHub stars](https://img.shields.io/github/stars/arogozhnikov/einops?style=social) - Flexible, powerful tensor operations for readable and reliable code. Supports PyTorch, JAX, TensorFlow, NumPy, MLX.
- **[safetensors](https://github.com/huggingface/safetensors)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/safetensors?style=social) - Simple, safe way to store and distribute tensors. Fast, secure alternative to pickle for model serialization.
- **[torchmetrics](https://github.com/Lightning-AI/torchmetrics)** ![GitHub stars](https://img.shields.io/github/stars/Lightning-AI/torchmetrics?style=social) - Machine learning metrics for distributed, scalable PyTorch applications. 80+ metrics with built-in distributed synchronization.
- **[torchao](https://github.com/pytorch/ao)** ![GitHub stars](https://img.shields.io/github/stars/pytorch/ao?style=social) - PyTorch native quantization and sparsity for training and inference. Drop-in optimizations for production deployment.
- **[SHAP](https://github.com/shap/shap)** ![GitHub stars](https://img.shields.io/github/stars/shap/shap?style=social) - Game theoretic approach to explain the output of any machine learning model. Industry standard for model interpretability.

---

### 🧠 2. Open Foundation Models

> Pretrained language, multimodal, speech, and video models with publicly available weights.

#### Large Language Models (Base + Chat)

- **[RWKV-7 "Goose" (BlinkDL)](https://github.com/BlinkDL/RWKV-LM)** ![GitHub stars](https://img.shields.io/github/stars/BlinkDL/RWKV-LM?style=social) - Novel RNN architecture with transformer-level LLM performance. 100% attention-free, linear-time, constant-space (no kv-cache), infinite ctx_len. Linux Foundation AI project with runtime already deployed in Windows & Office.
- **[Qwen3.6-Plus (Alibaba)](https://github.com/QwenLM/Qwen)** ![GitHub stars](https://img.shields.io/github/stars/QwenLM/Qwen?style=social) - Latest flagship series released April 2026 with 1M context window, agentic coding performance competitive with Claude 4.5 Opus, and enhanced multimodal capabilities.
- **[Gemma 4 (Google)](https://github.com/google-deepmind/gemma)** ![GitHub stars](https://img.shields.io/github/stars/google-deepmind/gemma?style=social) - Released April 2026 in four sizes (E2B, E4B, 26B MoE, 31B Dense). First major update in a year with Apache 2.0 license, complex logic, and agentic workflows.
- **[Kimi K2 (Moonshot AI)](https://github.com/MoonshotAI/Kimi-K2)** ![GitHub stars](https://img.shields.io/github/stars/MoonshotAI/Kimi-K2?style=social) - State-of-the-art 1T parameter MoE model with 32B activated parameters and 128K context. Trained with Muon optimizer for exceptional reasoning and coding performance.
- **[Kimi K2.5 (Moonshot AI)](https://github.com/MoonshotAI/Kimi-K2.5)** ![GitHub stars](https://img.shields.io/github/stars/MoonshotAI/Kimi-K2.5?style=social) - Frontier open-weight MoE model with 256K context, strong coding and reasoning performance, and native multimodal + tool-use support for agentic workflows.
- **[Phi-4 (Microsoft)](https://github.com/microsoft/PhiCookBook)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/PhiCookBook?style=social) - Small but highly capable models optimized for reasoning, edge devices, and on-device inference. Includes Phi-4-reasoning variants with thinking capabilities.
- **[GLM-5 (Zhipu AI)](https://github.com/zai-org/GLM-5)** ![GitHub stars](https://img.shields.io/github/stars/zai-org/GLM-5?style=social) - Strong open model line with solid coding, reasoning, and agentic-task performance.
- **[OLMo 2 (Allen AI)](https://github.com/allenai/OLMo)** ![GitHub stars](https://img.shields.io/github/stars/allenai/OLMo?style=social) - Fully open-source LLMs (1B–32B) with complete transparency: models, data, training code, and logs. Designed by scientists, for scientists.
- **[Llama 4 (Meta)](https://github.com/meta-llama/llama-models)** ![GitHub stars](https://img.shields.io/github/stars/meta-llama/llama-models?style=social) - First native multimodal MoE open-source models (Scout: 10M context, Maverick: 400B+ params). Released April 2025 with enterprise-grade capabilities.
- **[GPT-OSS (OpenAI)](https://github.com/openai/gpt-oss)** ![GitHub stars](https://img.shields.io/github/stars/openai/gpt-oss?style=social) - OpenAI's first open-weight models since GPT-2 (120B and 20B MoE). Apache 2.0 licensed with state-of-the-art performance for their size class. Released August 2025.

#### Coding & Reasoning Models

- **[DeepSeek-Coder-V2 / R1-Coder](https://github.com/deepseek-ai/DeepSeek-Coder)** ![GitHub stars](https://img.shields.io/github/stars/deepseek-ai/DeepSeek-Coder?style=social) - Best-in-class open coding model (236B MoE). Outperforms closed models on many code benchmarks.
- **[Qwen3-Coder-Next (Alibaba)](https://github.com/QwenLM/Qwen3-Coder)** ![GitHub stars](https://img.shields.io/github/stars/QwenLM/Qwen3-Coder?style=social) - Leading open coding model. Strong Pareto frontier for cost-effective agent deployment.

#### Multimodal Models (Vision + Language)

- **[MMaDA (Gen-Verse)](https://github.com/Gen-Verse/MMaDA)** ![GitHub stars](https://img.shields.io/github/stars/Gen-Verse/MMaDA?style=social) - Open-sourced multimodal large diffusion language model with unified architecture for text, image generation and multimodal reasoning. MIT licensed, NeurIPS 2025.
- **[Qwen3-VL (Alibaba)](https://github.com/QwenLM/Qwen3-VL)** ![GitHub stars](https://img.shields.io/github/stars/QwenLM/Qwen3-VL?style=social) - Latest flagship VLM with native 256K context (expandable to 1M), visual agent capabilities, 3D grounding, and superior multimodal reasoning. Major leap over Qwen2.5-VL.
- **[GLM-4.5V / GLM-4.1V-Thinking (Zhipu AI)](https://github.com/zai-org/GLM-V)** ![GitHub stars](https://img.shields.io/github/stars/zai-org/GLM-V?style=social) - Strong multimodal reasoning with scalable reinforcement learning. Compares favorably with Gemini-2.5-Flash on benchmarks.
- **[MiniCPM-V 2.6](https://github.com/OpenBMB/MiniCPM-V)** ![GitHub stars](https://img.shields.io/github/stars/OpenBMB/MiniCPM-V?style=social) - Handles images up to 1.8M pixels with top-tier OCR performance. Excellent for on-device deployment.
- **[Gemma 4 (Google)](https://github.com/google-deepmind/gemma)** ![GitHub stars](https://img.shields.io/github/stars/google-deepmind/gemma?style=social) - Multimodal model supporting vision-language input, optimized for efficiency, complex logic, and on-device use.
- **[Magma (Microsoft)](https://github.com/microsoft/Magma)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/Magma?style=social) - Foundation model for multimodal AI agents that perceives the world and takes goal-driven actions across digital and physical environments. CVPR 2025.

#### Speech & Audio Models (TTS, STT, Music)

- **[Whisper (OpenAI → community forks)](https://github.com/openai/whisper)** ![GitHub stars](https://img.shields.io/github/stars/openai/whisper?style=social) - The gold-standard open speech-to-text model. Massive community fine-tunes available.
- **[faster-whisper (SYSTRAN)](https://github.com/SYSTRAN/faster-whisper)** ![GitHub stars](https://img.shields.io/github/stars/SYSTRAN/faster-whisper?style=social) - Reimplementation of Whisper using CTranslate2 for up to 4x faster inference with same accuracy. Supports batched processing and 8-bit quantization.
- **[OuteTTS / CosyVoice 2](https://github.com/edwko/OuteTTS)** ![GitHub stars](https://img.shields.io/github/stars/edwko/OuteTTS?style=social) - High-quality open TTS with natural prosody and multilingual support.
- **[Fish Speech / StyleTTS 2](https://github.com/fishaudio/fish-speech)** ![GitHub stars](https://img.shields.io/github/stars/fishaudio/fish-speech?style=social) - Zero-shot TTS with excellent voice cloning. Extremely popular in 2026.
- **[MusicGen / AudioCraft (Meta)](https://github.com/facebookresearch/audiocraft)** ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/audiocraft?style=social) - Open music and audio generation models.
- **[VibeVoice (Microsoft)](https://github.com/microsoft/VibeVoice)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/VibeVoice?style=social) - Open-source frontier voice AI with expressive, longform conversational speech synthesis. 7B parameter TTS with streaming support.
- **[Chatterbox (Resemble AI)](https://github.com/resemble-ai/chatterbox)** ![GitHub stars](https://img.shields.io/github/stars/resemble-ai/chatterbox?style=social) - State-of-the-art open TTS family with 350M parameter Turbo variant. Single-step generation with native paralinguistic tags for realistic dialogue.
- **[Dia (Nari Labs)](https://github.com/nari-labs/dia)** ![GitHub stars](https://img.shields.io/github/stars/nari-labs/dia?style=social) - 1.6B parameter TTS generating ultra-realistic dialogue in one pass with nonverbal communications (laughter, coughing). Emotion and tone control via audio conditioning.
- **[Step-Audio (StepFun)](https://github.com/stepfun-ai/Step-Audio)** ![GitHub stars](https://img.shields.io/github/stars/stepfun-ai/Step-Audio?style=social) - 130B-parameter production-ready audio LLM for intelligent speech interaction. Supports multilingual conversations (Chinese, English, Japanese), emotional tones, regional dialects (Cantonese, Sichuanese), adjustable speech rates, and prosodic styles including rap. Apache 2.0 licensed.
- **[Voxtral TTS (Mistral)](https://github.com/mistralai/mistral-inference)** ![GitHub stars](https://img.shields.io/github/stars/mistralai/mistral-inference?style=social) - 4B parameter state-of-the-art TTS with zero-shot voice cloning, 9-language support, and ~90ms time-to-first-audio for voice agents.
- **[WhisperSpeech](https://github.com/WhisperSpeech/WhisperSpeech)** ![GitHub stars](https://img.shields.io/github/stars/WhisperSpeech/WhisperSpeech?style=social) - Open source text-to-speech system built by inverting Whisper. High-quality voice cloning with zero-shot capabilities. MIT licensed.

#### Video & Animation Models

- **[CogVideoX (Zhipu AI / community)](https://github.com/THUDM/CogVideo)** ![GitHub stars](https://img.shields.io/github/stars/THUDM/CogVideo?style=social) - High-quality open text-to-video model (5B-12B).
- **[Mochi 1 (Genmo)](https://github.com/genmoai/mochi)** ![GitHub stars](https://img.shields.io/github/stars/genmoai/mochi?style=social) - 10B open video model with impressive motion and consistency.

---

### ⚡ 3. Inference Engines & Serving

> Inference runtimes, serving systems, and optimization tools for running models locally or in production.

#### Local / On-device Inference

- **[llama.cpp](https://github.com/ggerganov/llama.cpp)** ![GitHub stars](https://img.shields.io/github/stars/ggerganov/llama.cpp?style=social) - Pure C/C++ inference engine with GGUF format support. The gold standard for CPU/GPU/Apple Silicon on-device running. Includes llama-server for OpenAI-compatible API.
- **[Ollama](https://github.com/ollama/ollama)** ![GitHub stars](https://img.shields.io/github/stars/ollama/ollama?style=social) - Dead-simple local LLM runner with a one-line install, model registry, and OpenAI-compatible API.
- **[MLX](https://github.com/ml-explore/mlx)** ![GitHub stars](https://img.shields.io/github/stars/ml-explore/mlx?style=social) (Apple) - High-performance array framework + LLM inference optimized for Apple Silicon.
- **[MLC-LLM](https://github.com/mlc-ai/mlc-llm)** ![GitHub stars](https://img.shields.io/github/stars/mlc-ai/mlc-llm?style=social) - Deployment engine that compiles and runs LLMs across browsers, mobile devices, and local hardware.
- **[WebLLM](https://github.com/mlc-ai/web-llm)** ![GitHub stars](https://img.shields.io/github/stars/mlc-ai/web-llm?style=social) - High-performance in-browser LLM inference engine. Runs models directly in the browser with WebGPU acceleration.
- **[llama-cpp-python](https://github.com/abetlen/llama-cpp-python)** ![GitHub stars](https://img.shields.io/github/stars/abetlen/llama-cpp-python?style=social) - Official Python bindings for llama.cpp.
- **[KoboldCpp](https://github.com/LostRuins/koboldcpp)** ![GitHub stars](https://img.shields.io/github/stars/LostRuins/koboldcpp?style=social) - User-friendly llama.cpp fork focused on role-playing and creative writing.
- **[RamaLama](https://github.com/containers/ramalama)** ![GitHub stars](https://img.shields.io/github/stars/containers/ramalama?style=social) - Container-centric tool for simplifying local AI model serving. Automatically detects GPUs, pulls optimized container images, and runs models securely in rootless containers with enterprise-grade isolation.

#### High-performance Serving & API Servers

- **[llm-d](https://github.com/llm-d/llm-d)** ![GitHub stars](https://img.shields.io/github/stars/llm-d/llm-d?style=social) - Kubernetes-native distributed LLM inference framework. Donated to CNCF by RedHat, Google, and IBM. Intelligent scheduling, KV-cache optimization, and state-of-the-art performance across accelerators.
- **[LMDeploy](https://github.com/InternLM/lmdeploy)** ![GitHub stars](https://img.shields.io/github/stars/InternLM/lmdeploy?style=social) - Toolkit for compressing, deploying, and serving LLMs from OpenMMLab. 4-bit inference with 2.4x higher performance than FP16, distributed multi-model serving across machines.
- **[vLLM](https://github.com/vllm-project/vllm)** ![GitHub stars](https://img.shields.io/github/stars/vllm-project/vllm?style=social) - State-of-the-art serving engine with PagedAttention and continuous batching. Currently the fastest production-grade LLM server.
- **[SGLang](https://github.com/sgl-project/sglang)** ![GitHub stars](https://img.shields.io/github/stars/sgl-project/sglang?style=social) - Next-gen serving framework with RadixAttention. Powers xAI's production workloads at 100K+ GPUs scale.
- **[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)** ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/TensorRT-LLM?style=social) - NVIDIA's official high-performance inference backend.
- **[Aphrodite Engine](https://github.com/PygmalionAI/aphrodite-engine)** ![GitHub stars](https://img.shields.io/github/stars/PygmalionAI/aphrodite-engine?style=social) - vLLM fork optimized for role-play and creative writing.
- **[Triton Inference Server](https://github.com/triton-inference-server/server)** ![GitHub stars](https://img.shields.io/github/stars/triton-inference-server/server?style=social) - NVIDIA's production-grade open-source inference serving software. Supports multiple frameworks (TensorRT, PyTorch, ONNX) with optimized cloud and edge deployment.
- **[mistral.rs](https://github.com/EricLBuehler/mistral.rs)** ![GitHub stars](https://img.shields.io/github/stars/EricLBuehler/mistral.rs?style=social) - Fast, flexible Rust-native LLM inference engine built on Candle. Supports text, vision, audio, image generation, and embeddings with hardware-aware auto-tuning.
- **[KTransformers](https://github.com/kvcache-ai/ktransformers)** ![GitHub stars](https://img.shields.io/github/stars/kvcache-ai/ktransformers?style=social) - Flexible framework for heterogeneous CPU-GPU LLM inference and fine-tuning. Enables running large MoE models by offloading experts to CPU with BF16/FP8 precision support.
- **[llamafile](https://github.com/mozilla-ai/llamafile)** ![GitHub stars](https://img.shields.io/github/stars/mozilla-ai/llamafile?style=social) - Mozilla's single-file distributable LLM solution. Bundle model weights, inference engine, and runtime into one portable executable that runs on six OSes without installation.
- **[Xinference](https://github.com/xorbitsai/inference)** ![GitHub stars](https://img.shields.io/github/stars/xorbitsai/inference?style=social) - Unified, production-ready inference API for LLMs, speech, and multimodal models. Drop-in GPT replacement with single-line code changes. Supports thousands of models with auto-batching and distributed inference.
- **[LightLLM](https://github.com/ModelTC/LightLLM)** ![GitHub stars](https://img.shields.io/github/stars/ModelTC/LightLLM?style=social) - Pure Python-based LLM inference and serving framework with lightweight design, easy extensibility, and high-speed performance. Integrates optimizations from FasterTransformer, TGI, vLLM, and SGLang.
- **[TabbyAPI](https://github.com/theroyallab/tabbyAPI)** ![GitHub stars](https://img.shields.io/github/stars/theroyallab/tabbyAPI?style=social) - FastAPI-based API server for ExLlamaV2/V3 backends. OpenAI-compatible API with support for model loading/unloading, embeddings, speculative decoding, multi-LoRA, and streaming.
- **[GPUStack](https://github.com/gpustack/gpustack)** ![GitHub stars](https://img.shields.io/github/stars/gpustack/gpustack?style=social) - GPU cluster manager that orchestrates inference engines like vLLM and SGLang. Automated engine selection, parameter optimization, and distributed multi-GPU deployment for high-performance AI workloads.
- **[One-API](https://github.com/songquanpeng/one-api)** ![GitHub stars](https://img.shields.io/github/stars/songquanpeng/one-api?style=social) - LLM API management and key redistribution system. Unifies multiple providers (OpenAI, Anthropic, Azure, etc.) under a single OpenAI-compatible API with built-in rate limiting, quota management, and cost tracking. MIT licensed.
- **[Text Generation Inference (Hugging Face)](https://github.com/huggingface/text-generation-inference)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/text-generation-inference?style=social) - Production-grade serving engine powering Hugging Chat and Inference API. Rust/Python server with continuous batching, tensor parallelism, and optimized transformer architectures. Apache 2.0 licensed.
- **[OpenLLM (BentoML)](https://github.com/bentoml/OpenLLM)** ![GitHub stars](https://img.shields.io/github/stars/bentoml/OpenLLM?style=social) - Production-grade platform for running any open-source LLMs as OpenAI-compatible API endpoints. Supports 50+ models with built-in streaming, batching, and auto-acceleration. Apache 2.0 licensed.

#### Quantization, Distillation & Optimization

- **[GGUF](https://github.com/ggerganov/llama.cpp)** ![GitHub stars](https://img.shields.io/github/stars/ggerganov/llama.cpp?style=social) (part of llama.cpp) - Modern quantized format that powers most local inference.
- **[bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes)** ![GitHub stars](https://img.shields.io/github/stars/bitsandbytes-foundation/bitsandbytes?style=social) - 8-bit and 4-bit optimizers + quantization.
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
- **[Hermes Agent (NousResearch)](https://github.com/NousResearch/hermes-agent)** ![GitHub stars](https://img.shields.io/github/stars/NousResearch/hermes-agent?style=social) - The agent that grows with you. Autonomous server-side agent with persistent memory that learns and improves over time.
- **[Agno](https://github.com/agno-agi/agno)** ![GitHub stars](https://img.shields.io/github/stars/agno-agi/agno?style=social) - Build, run, and manage agentic software at scale. High-performance framework for multi-agent systems with memory, knowledge, and tools.
- **[Upsonic](https://github.com/Upsonic/Upsonic)** ![GitHub stars](https://img.shields.io/github/stars/Upsonic/Upsonic?style=social) - Agent framework for fintech and banking with built-in MCP support, guardrails, and tool server architecture.
- **[VoltAgent](https://github.com/VoltAgent/voltagent)** ![GitHub stars](https://img.shields.io/github/stars/VoltAgent/voltagent?style=social) - TypeScript-first AI agent engineering platform with memory, RAG, workflows, MCP integration, and voice support.
- **[PocketFlow](https://github.com/The-Pocket/PocketFlow)** ![GitHub stars](https://img.shields.io/github/stars/The-Pocket/PocketFlow?style=social) - 100-line minimalist LLM framework for building agent workflows. Lightweight, extensible architecture for tool use and autonomous task execution.

#### Multi-Agent Orchestration

- **[MetaGPT](https://github.com/FoundationAgents/MetaGPT)** ![GitHub stars](https://img.shields.io/github/stars/FoundationAgents/MetaGPT?style=social) - Simulates an entire "AI software company".
- **[CAMEL](https://github.com/camel-ai/camel)** ![GitHub stars](https://img.shields.io/github/stars/camel-ai/camel?style=social) - First and best multi-agent framework for building scalable agent systems. Apache 2.0 licensed with extensive tooling for agent communication and task automation.
- **[Swarms](https://github.com/kyegomez/swarms)** ![GitHub stars](https://img.shields.io/github/stars/kyegomez/swarms?style=social) - Bleeding-edge enterprise multi-agent orchestration.
- **[Llama-Agents](https://github.com/run-llama/llama-agents)** ![GitHub stars](https://img.shields.io/github/stars/run-llama/llama-agents?style=social) - Async-first multi-agent system.
- **[Mastra](https://github.com/mastra-ai/mastra)** ![GitHub stars](https://img.shields.io/github/stars/mastra-ai/mastra?style=social) - TypeScript-first agent framework with built-in RAG, workflows, tool integrations, observability and observational memory.
- **[Deer-Flow (ByteDance)](https://github.com/bytedance/deer-flow)** ![GitHub stars](https://img.shields.io/github/stars/bytedance/deer-flow?style=social) - Open-source long-horizon SuperAgent harness that researches, codes, and creates. Handles tasks from minutes to hours with sandboxes, memories, tools, skills, subagents, and message gateway.
- **[OpenAI Agents SDK](https://github.com/openai/openai-agents-python)** ![GitHub stars](https://img.shields.io/github/stars/openai/openai-agents-python?style=social) - Production-ready lightweight framework for multi-agent workflows. The evolution of Swarm with enhanced orchestration capabilities and enterprise-grade features.
- **[AgentScope](https://github.com/agentscope-ai/agentscope)** ![GitHub stars](https://img.shields.io/github/stars/agentscope-ai/agentscope?style=social) - Alibaba's production-ready multi-agent framework with 23K+ stars. Features built-in MCP and A2A support, message hub for flexible orchestration, and AgentScope Runtime for production deployment.
- **[Microsoft Agent Framework](https://github.com/microsoft/agent-framework)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/agent-framework?style=social) - Microsoft's official framework combining AutoGen's agent abstractions with Semantic Kernel's enterprise features. Supports Python and .NET with graph-based workflows.
- **[Agency Swarm](https://github.com/VRSEN/agency-swarm)** ![GitHub stars](https://img.shields.io/github/stars/VRSEN/agency-swarm?style=social) - Reliable multi-agent orchestration framework built on top of the OpenAI Assistants API with organizational structure modeling.
- **[elizaOS](https://github.com/elizaOS/eliza)** ![GitHub stars](https://img.shields.io/github/stars/elizaOS/eliza?style=social) - Autonomous multi-agent framework for building and deploying AI-powered applications. Features Discord/Telegram/Farcaster connectors, RAG support, and a modern web dashboard.
- **[Agent Squad (AWS Labs)](https://github.com/awslabs/agent-squad)** ![GitHub stars](https://img.shields.io/github/stars/awslabs/agent-squad?style=social) - Flexible multi-agent orchestration framework with intelligent intent classification and context management. Supports Python and TypeScript with pre-built agents for Bedrock, Lex, and custom integrations. Apache 2.0 licensed.
- **[DeepResearchAgent](https://github.com/SkyworkAI/DeepResearchAgent)** ![GitHub stars](https://img.shields.io/github/stars/SkyworkAI/DeepResearchAgent?style=social) - Hierarchical multi-agent system for deep research tasks with automated task decomposition and execution across complex domains.
- **[BeeAI Framework (IBM)](https://github.com/i-am-bee/bee-agent-framework)** ![GitHub stars](https://img.shields.io/github/stars/i-am-bee/bee-agent-framework?style=social) - Production-ready multi-agent framework in Python and TypeScript. Features workflow orchestration, ACP/MCP protocol support, and deep watsonx integration. Part of Linux Foundation AI & Data program.

#### Autonomous Coding Agents

- **[OpenHands (ex-OpenDevin)](https://github.com/All-Hands-AI/OpenHands)** ![GitHub stars](https://img.shields.io/github/stars/All-Hands-AI/OpenHands?style=social) - Full-featured open-source AI software engineer.
- **[Goose](https://github.com/block/goose)** ![GitHub stars](https://img.shields.io/github/stars/block/goose?style=social) - Extensible on-machine AI agent for development tasks.
- **[OpenCode](https://github.com/anomalyco/opencode)** ![GitHub stars](https://img.shields.io/github/stars/anomalyco/opencode?style=social) - Terminal-native autonomous coding agent.
- **[Aider](https://github.com/paul-gauthier/aider)** ![GitHub stars](https://img.shields.io/github/stars/paul-gauthier/aider?style=social) - Command-line pair-programming agent.
- **[Pi (badlogic)](https://github.com/badlogic/pi-mono)** ![GitHub stars](https://img.shields.io/github/stars/badlogic/pi-mono?style=social) - Terminal coding agent with hash-anchored edits, LSP integration, subagents, MCP support, and package ecosystem.
- **[Mistral-Vibe (Mistral)](https://github.com/mistralai/mistral-vibe)** ![GitHub stars](https://img.shields.io/github/stars/mistralai/mistral-vibe?style=social) - Minimal CLI coding agent by Mistral. Lightweight, fast, and designed for local development workflows.
- **[Nanocoder (Nano-Collective)](https://github.com/Nano-Collective/nanocoder)** ![GitHub stars](https://img.shields.io/github/stars/Nano-Collective/nanocoder?style=social) - Beautiful local-first coding agent running in your terminal. Built for privacy and control with support for multiple AI providers via OpenRouter.
- **[Gemini CLI (Google)](https://github.com/google-gemini/gemini-cli)** ![GitHub stars](https://img.shields.io/github/stars/google-gemini/gemini-cli?style=social) - Open-source AI agent that brings Gemini's power directly into your terminal. Supports code generation, shell execution, and file editing with full Apache 2.0 licensing.

#### Domain-Specific Agents

- **[Composio](https://github.com/ComposioHQ/composio)** ![GitHub stars](https://img.shields.io/github/stars/ComposioHQ/composio?style=social) - Tool integration layer for AI agents with 1000+ toolkits, authentication management, and sandboxed workbench. Powers tool use across major frameworks.
- **[Langflow](https://github.com/langflow-ai/langflow)** ![GitHub stars](https://img.shields.io/github/stars/langflow-ai/langflow?style=social) - Visual low-code platform for agentic workflows.
- **[Dify](https://github.com/langgenius/dify)** ![GitHub stars](https://img.shields.io/github/stars/langgenius/dify?style=social) - Production-ready agentic workflow platform.
- **[OWL (camel-ai/owl)](https://github.com/camel-ai/owl)** ![GitHub stars](https://img.shields.io/github/stars/camel-ai/owl?style=social) - Advanced multi-agent collaboration system.
- **[AI-Scientist-v2 (SakanaAI)](https://github.com/SakanaAI/AI-Scientist-v2)** ![GitHub stars](https://img.shields.io/github/stars/SakanaAI/AI-Scientist-v2?style=social) - Workshop-level automated scientific discovery via agentic tree search. Generates novel research ideas, runs experiments, and writes papers.
- **[PraisonAI](https://github.com/MervinPraison/PraisonAI)** ![GitHub stars](https://img.shields.io/github/stars/MervinPraison/PraisonAI?style=social) - 24/7 AI employee team for automating complex challenges. Low-code multi-agent framework with handoffs, guardrails, memory, RAG, and 100+ LLM providers.
- **[Agent-S (Simular AI)](https://github.com/simular-ai/Agent-S)** ![GitHub stars](https://img.shields.io/github/stars/simular-ai/Agent-S?style=social) - Open agentic framework that uses computers like a human. SOTA on OSWorld benchmark (72.6%) for GUI automation and computer control.
- **[Browser Use](https://github.com/browser-use/browser-use)** ![GitHub stars](https://img.shields.io/github/stars/browser-use/browser-use?style=social) - Makes websites accessible for AI agents. Enables autonomous web automation, data extraction, and task completion with natural language instructions. MIT licensed.
- **[TradingAgents](https://github.com/TauricResearch/TradingAgents)** ![GitHub stars](https://img.shields.io/github/stars/TauricResearch/TradingAgents?style=social) - Multi-agent framework for financial trading. Simulates professional trading firm operations with 6+ specialized agent roles, backtesting, risk management, and portfolio optimization. Built with LangGraph, supports multiple LLM providers.

#### Agent Memory & State

- **[Letta (ex-MemGPT)](https://github.com/letta-ai/letta)** ![GitHub stars](https://img.shields.io/github/stars/letta-ai/letta?style=social) - Platform for building stateful agents with advanced memory that learn and self-improve over time.
- **[Mem0](https://github.com/mem0ai/mem0)** ![GitHub stars](https://img.shields.io/github/stars/mem0ai/mem0?style=social) - Universal memory layer for AI agents. Persistent, multi-session memory across models and environments.
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
- **[LanceDB](https://github.com/lancedb/lancedb)** ![GitHub stars](https://img.shields.io/github/stars/lancedb/lancedb?style=social) - Serverless vector DB optimized for multimodal data.
- **[Vespa](https://github.com/vespa-engine/vespa)** ![GitHub stars](https://img.shields.io/github/stars/vespa-engine/vespa?style=social) - AI + Data platform with hybrid search (vector + keyword) and real-time indexing at scale. Battle-tested serving billions of queries daily.
- **[pgvector](https://github.com/pgvector/pgvector)** ![GitHub stars](https://img.shields.io/github/stars/pgvector/pgvector?style=social) - PostgreSQL extension for vector similarity search.
- **[Quickwit](https://github.com/quickwit-oss/quickwit)** ![GitHub stars](https://img.shields.io/github/stars/quickwit-oss/quickwit?style=social) - Cloud-native search engine for observability. Open-source alternative to Datadog, Elasticsearch, Loki, and Tempo with native vector search support.
- **[Tantivy](https://github.com/quickwit-oss/tantivy)** ![GitHub stars](https://img.shields.io/github/stars/quickwit-oss/tantivy?style=social) - Full-text search engine library inspired by Apache Lucene and written in Rust. Powers Quickwit and other production search systems.
- **[Manticore Search](https://github.com/manticoresoftware/manticoresearch)** ![GitHub stars](https://img.shields.io/github/stars/manticoresoftware/manticoresearch?style=social) - Easy to use open source fast database for search. Good alternative to Elasticsearch with SQL-like interface and vector search capabilities.
- **[OpenSearch](https://github.com/opensearch-project/OpenSearch)** ![GitHub stars](https://img.shields.io/github/stars/opensearch-project/OpenSearch?style=social) - Open-source distributed and RESTful search and analytics suite with native vector search. Enterprise-grade fork of Elasticsearch with k-NN plugin for semantic search at scale.
- **[Marqo](https://github.com/marqo-ai/marqo)** ![GitHub stars](https://img.shields.io/github/stars/marqo-ai/marqo?style=social) - Multimodal vector search for text, image, and structured data. End-to-end indexing and search with built-in embedding models. Apache 2.0 licensed.
- **[Vald](https://github.com/vdaas/vald)** ![GitHub stars](https://img.shields.io/github/stars/vdaas/vald?style=social) - Highly scalable distributed vector search engine. Cloud-native architecture with automatic indexing, horizontal scaling, and multiple ANN algorithm support. Apache 2.0 licensed.
- **[Annoy](https://github.com/spotify/annoy)** ![GitHub stars](https://img.shields.io/github/stars/spotify/annoy?style=social) - Approximate nearest neighbors library optimized for memory usage and fast loading. Powers Spotify's music recommendation with C++/Python bindings. Apache 2.0 licensed.

#### Embedding Models

- **[BGE (FlagEmbedding)](https://github.com/FlagOpen/FlagEmbedding)** ![GitHub stars](https://img.shields.io/github/stars/FlagOpen/FlagEmbedding?style=social) - BAAI's best-in-class embedding family.
- **[E5 (Microsoft)](https://github.com/microsoft/unilm)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/unilm?style=social) - High-performance text embeddings for retrieval.
- **[FastEmbed (Qdrant)](https://github.com/qdrant/fastembed)** ![GitHub stars](https://img.shields.io/github/stars/qdrant/fastembed?style=social) - Lightweight, fast Python library for embedding generation with ONNX Runtime. Supports text, sparse (SPLADE), and late-interaction (ColBERT) embeddings without GPU dependencies. Apache 2.0 licensed.

#### Embedding Benchmarks

- **[MTEB](https://github.com/embeddings-benchmark/mteb)** ![GitHub stars](https://img.shields.io/github/stars/embeddings-benchmark/mteb?style=social) - Massive Text Embedding Benchmark covering 1000+ languages and diverse tasks. The industry standard for evaluating and comparing embedding models.

#### RAG Frameworks & Advanced Retrieval Tools

- **[LlamaIndex](https://github.com/run-llama/llama_index)** ![GitHub stars](https://img.shields.io/github/stars/run-llama/llama_index?style=social) - Full-featured RAG pipeline with advanced indexing.
- **[Haystack](https://github.com/deepset-ai/haystack)** ![GitHub stars](https://img.shields.io/github/stars/deepset-ai/haystack?style=social) - End-to-end NLP and RAG framework.
- **[RAGFlow](https://github.com/infiniflow/ragflow)** ![GitHub stars](https://img.shields.io/github/stars/infiniflow/ragflow?style=social) - Deep-document-understanding RAG engine.
- **[GraphRAG (Microsoft)](https://github.com/microsoft/graphrag)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/graphrag?style=social) - Knowledge-graph-based RAG.
- **[Docling](https://github.com/docling-project/docling)** ![GitHub stars](https://img.shields.io/github/stars/docling-project/docling?style=social) - Document processing toolkit for turning PDFs and other files into structured data for GenAI workflows.
- **[Unstructured](https://github.com/Unstructured-IO/unstructured)** ![GitHub stars](https://img.shields.io/github/stars/Unstructured-IO/unstructured?style=social) - Best-in-class document preprocessing.
- **[MinerU](https://github.com/opendatalab/MinerU)** ![GitHub stars](https://img.shields.io/github/stars/opendatalab/MinerU?style=social) - High-accuracy document parsing for LLM and RAG workflows. Converts PDFs, Word, PPTs, and images into structured Markdown/JSON with VLM+OCR dual engine.
- **[Marker](https://github.com/datalab-to/marker)** ![GitHub stars](https://img.shields.io/github/stars/datalab-to/marker?style=social) - Fast, accurate PDF-to-markdown converter with table extraction, equation handling, and optional LLM enhancement for RAG pipelines.
- **[ColPali / ColQwen](https://github.com/illuin-tech/colpali)** ![GitHub stars](https://img.shields.io/github/stars/illuin-tech/colpali?style=social) - Vision-language models for document retrieval.
- **[LightRAG](https://github.com/HKUDS/LightRAG)** ![GitHub stars](https://img.shields.io/github/stars/HKUDS/LightRAG?style=social) - Graph-based RAG with dual-level retrieval system. Simple and fast with comprehensive knowledge discovery (EMNLP 2025).
- **[RAG-Anything](https://github.com/HKUDS/RAG-Anything)** ![GitHub stars](https://img.shields.io/github/stars/HKUDS/RAG-Anything?style=social) - All-in-One Multimodal RAG system for seamless processing of text, images, tables, and equations. Built on LightRAG.
- **[txtai](https://github.com/neuml/txtai)** ![GitHub stars](https://img.shields.io/github/stars/neuml/txtai?style=social) - All-in-one AI framework for semantic search, LLM orchestration and language model workflows. Embeddings database with customizable pipelines.
- **[Infinity](https://github.com/michaelfeil/infinity)** ![GitHub stars](https://img.shields.io/github/stars/michaelfeil/infinity?style=social) - High-throughput, low-latency serving engine for text-embeddings, reranking, CLIP, and ColPali. OpenAI-compatible API.
- **[FlashRAG](https://github.com/RUC-NLPIR/FlashRAG)** ![GitHub stars](https://img.shields.io/github/stars/RUC-NLPIR/FlashRAG?style=social) - Efficient toolkit for RAG research with 40+ retrieval and reranking models, 20+ benchmark datasets, and optimized evaluation pipelines (WWW 2025 Resource). MIT licensed.

#### Web Data Ingestion

- **[Crawl4AI](https://github.com/unclecode/crawl4ai)** ![GitHub stars](https://img.shields.io/github/stars/unclecode/crawl4ai?style=social) - LLM-friendly web crawler that turns websites into clean Markdown for RAG and agentic workflows.
- **[Lightpanda](https://github.com/lightpanda-io/browser)** ![GitHub stars](https://img.shields.io/github/stars/lightpanda-io/browser?style=social) - Machine-first headless browser in Zig; rendering-free and ultra-lightweight for AI agent browsing.
- **[Paperless-AI](https://github.com/clusterzx/paperless-ai)** ![GitHub stars](https://img.shields.io/github/stars/clusterzx/paperless-ai?style=social) - Automated document analyzer for Paperless-ngx with RAG-powered semantic search across your document archive.
- **[Firecrawl](https://github.com/firecrawl/firecrawl)** ![GitHub stars](https://img.shields.io/github/stars/firecrawl/firecrawl?style=social) - Web Data API for AI - search, scrape, and interact with the web at scale. Clean markdown/JSON output with proxy rotation and JS-blocking handled automatically.

---

### 🎨 6. Generative Media Tools

> Open-source models and applications for image, video, audio, and 3D generation and editing.

#### Image Generation & Editing

- **[ComfyUI](https://github.com/Comfy-Org/ComfyUI)** ![GitHub stars](https://img.shields.io/github/stars/Comfy-Org/ComfyUI?style=social) - Node-based visual workflow editor for Stable Diffusion, FLUX, etc.
- **[Stable Diffusion WebUI Forge - Neo](https://github.com/Haoming02/sd-webui-forge-classic)** ![GitHub stars](https://img.shields.io/github/stars/Haoming02/sd-webui-forge-classic?style=social) - Actively maintained Forge-based Stable Diffusion web UI with the familiar extension-driven workflow.
- **[Fooocus](https://github.com/lllyasviel/Fooocus)** ![GitHub stars](https://img.shields.io/github/stars/lllyasviel/Fooocus?style=social) - Midjourney-style UI with beautiful out-of-the-box results.
- **[Diffusers](https://github.com/huggingface/diffusers)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/diffusers?style=social) - PyTorch library for diffusion pipelines spanning image, video, and audio generation.
- **[InvokeAI](https://github.com/invoke-ai/InvokeAI)** ![GitHub stars](https://img.shields.io/github/stars/invoke-ai/InvokeAI?style=social) - Full-featured creative studio.
- **[PowerPaint (OpenMMLab)](https://github.com/open-mmlab/PowerPaint)** ![GitHub stars](https://img.shields.io/github/stars/open-mmlab/PowerPaint?style=social) - Versatile image inpainting model supporting text-guided inpainting, object removal, and outpainting (ECCV 2024).
- **[SD.Next](https://github.com/vladmandic/sdnext)** ![GitHub stars](https://img.shields.io/github/stars/vladmandic/sdnext?style=social) - All-in-one WebUI for AI generative image and video creation with multi-platform support, SDNQ quantization, and balanced CPU/GPU memory offload.

#### Video Generation

- **[Wan2.2 (Alibaba)](https://github.com/Wan-Video/Wan2.1)** ![GitHub stars](https://img.shields.io/github/stars/Wan-Video/Wan2.1?style=social) - Leading open Mixture-of-Experts text-to-video model.
- **[HunyuanVideo (Tencent)](https://github.com/Tencent-Hunyuan/HunyuanVideo)** ![GitHub stars](https://img.shields.io/github/stars/Tencent-Hunyuan/HunyuanVideo?style=social) - 13B-parameter systematic video generation framework. Leading quality among open models.
- **[SkyReels V2/V3 (Skywork)](https://github.com/SkyworkAI/SkyReels-V2)** ![GitHub stars](https://img.shields.io/github/stars/SkyworkAI/SkyReels-V2?style=social) - First open-source infinite-length film generative model using AutoRegressive Diffusion-Forcing.
- **[Mochi 1 (Genmo)](https://github.com/genmoai/mochi)** ![GitHub stars](https://img.shields.io/github/stars/genmoai/mochi?style=social) - 10B-parameter open video model.
- **[LTX-Video (Lightricks)](https://github.com/Lightricks/LTX-Video)** ![GitHub stars](https://img.shields.io/github/stars/Lightricks/LTX-Video?style=social) - Fast native 4K video generation.
- **[Stable Video Diffusion (Stability AI)](https://github.com/Stability-AI/generative-models)** ![GitHub stars](https://img.shields.io/github/stars/Stability-AI/generative-models?style=social) - Official image-to-video and text-to-video implementation within Stability AI's generative models repository.
- **[Latte (Vchitect)](https://github.com/Vchitect/Latte)** ![GitHub stars](https://img.shields.io/github/stars/Vchitect/Latte?style=social) - Latent Diffusion Transformer for video generation with state-of-the-art quality (TMLR 2025). Apache 2.0 licensed.
- **[Open-Sora-Plan (PKU-YuanGroup)](https://github.com/PKU-YuanGroup/Open-Sora-Plan)** ![GitHub stars](https://img.shields.io/github/stars/PKU-YuanGroup/Open-Sora-Plan?style=social) - Reproduction of Sora with full open-source pipeline for text-to-video generation. MIT licensed.
- **[Helios (PKU-YuanGroup)](https://github.com/PKU-YuanGroup/Helios)** ![GitHub stars](https://img.shields.io/github/stars/PKU-YuanGroup/Helios?style=social) - Efficient long-video generation framework with 24GB VRAM support for up to 10,000 frames (5+ minutes) and 1280×768 resolution. Apache 2.0 licensed.
- **[Open-Sora (HPC-AI Tech)](https://github.com/hpcaitech/Open-Sora)** ![GitHub stars](https://img.shields.io/github/stars/hpcaitech/Open-Sora?style=social) - Democratizing efficient video production with fully open-source 11B model achieving on-par performance with HunyuanVideo. End-to-end pipeline with training code and checkpoints. Apache 2.0 licensed.

#### Audio / Music / Voice Generation

- **[AudioCraft / MusicGen (Meta)](https://github.com/facebookresearch/audiocraft)** ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/audiocraft?style=social) - Controllable text-to-music and audio models.
- **[ACE-Step 1.5](https://github.com/ace-step/ACE-Step-1.5)** ![GitHub stars](https://img.shields.io/github/stars/ace-step/ACE-Step-1.5?style=social) - Local-first music generation model with broad hardware support across Mac, AMD, Intel, and CUDA devices.
- **[Fish Speech](https://github.com/fishaudio/fish-speech)** ![GitHub stars](https://img.shields.io/github/stars/fishaudio/fish-speech?style=social) - Zero-shot TTS and voice cloning.
- **[CosyVoice 2](https://github.com/FunAudioLLM/CosyVoice)** ![GitHub stars](https://img.shields.io/github/stars/FunAudioLLM/CosyVoice?style=social) - Natural multilingual TTS with emotional control.
- **[OuteTTS](https://github.com/edwko/OuteTTS)** ![GitHub stars](https://img.shields.io/github/stars/edwko/OuteTTS?style=social) - High-quality open TTS.
- **[Amphion](https://github.com/open-mmlab/Amphion)** ![GitHub stars](https://img.shields.io/github/stars/open-mmlab/Amphion?style=social) - Comprehensive toolkit for Audio, Music, and Speech Generation (9.7K stars).

#### 3D & Creative Tools

- **[Hunyuan3D-2 (Tencent)](https://github.com/Tencent-Hunyuan/Hunyuan3D-2)** ![GitHub stars](https://img.shields.io/github/stars/Tencent-Hunyuan/Hunyuan3D-2?style=social) - State-of-the-art open image-to-3D and text-to-3D.
- **[Trellis (Microsoft)](https://github.com/microsoft/TRELLIS)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/TRELLIS?style=social) - Structured 3D latents for high-quality generation.
- **[gsplat (3D Gaussian Splatting tools)](https://github.com/nerfstudio-project/gsplat)** ![GitHub stars](https://img.shields.io/github/stars/nerfstudio-project/gsplat?style=social) - High-performance 3D Gaussian Splatting library.
- **[LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio)** ![GitHub stars](https://img.shields.io/github/stars/MrNeRF/LichtFeld-Studio?style=social) - Native application for training, editing, and exporting 3D Gaussian Splatting scenes with MCMC optimization and timelapse generation. GPL-3.0 licensed.
- **[OpenSplat](https://github.com/pierotofy/OpenSplat)** ![GitHub stars](https://img.shields.io/github/stars/pierotofy/OpenSplat?style=social) - Production-grade, portable implementation of 3D Gaussian Splatting with CPU/GPU support for Windows, Mac, and Linux. Creates 3D scenes from camera poses and sparse points. AGPL-3.0 licensed.

---

<a id="section-7"></a>

### 🛠️ 7. Training & Fine-tuning Ecosystem

> Tools for model training, fine-tuning, synthetic data generation, and distributed training.

#### Full Training Frameworks

- **[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)** ![GitHub stars](https://img.shields.io/github/stars/hiyouga/LLaMA-Factory?style=social) - One-stop unified framework for SFT, DPO, ORPO, KTO with web UI.
- **[Axolotl](https://github.com/axolotl-ai-cloud/axolotl)** ![GitHub stars](https://img.shields.io/github/stars/axolotl-ai-cloud/axolotl?style=social) - YAML-driven full pipeline for SFT, DPO, GRPO.
- **[ms-swift](https://github.com/modelscope/ms-swift)** ![GitHub stars](https://img.shields.io/github/stars/modelscope/ms-swift?style=social) - Unified training framework for 600+ LLMs and 300+ MLLMs with CPT/SFT/DPO/GRPO (AAAI 2025).
- **[Unsloth](https://github.com/unslothai/unsloth)** ![GitHub stars](https://img.shields.io/github/stars/unslothai/unsloth?style=social) - 2× faster, 70% less memory fine-tuning.
- **[LitGPT](https://github.com/Lightning-AI/litgpt)** ![GitHub stars](https://img.shields.io/github/stars/Lightning-AI/litgpt?style=social) - Clean from-scratch implementations of 20+ LLMs.
- **[LLM Foundry](https://github.com/mosaicml/llm-foundry)** ![GitHub stars](https://img.shields.io/github/stars/mosaicml/llm-foundry?style=social) - Databricks' training framework for composable LLM training with StreamingDataset and Composer.
- **[torchtune](https://github.com/pytorch/torchtune)** ![GitHub stars](https://img.shields.io/github/stars/pytorch/torchtune?style=social) - PyTorch-native library for post-training, fine-tuning, and experimentation with LLMs.
- **[kohya_ss](https://github.com/bmaltais/kohya_ss)** ![GitHub stars](https://img.shields.io/github/stars/bmaltais/kohya_ss?style=social) - Gradio-based GUI and CLI for training Stable Diffusion models (LoRA, Dreambooth, fine-tuning, SDXL). Provides accessible interface to Kohya's powerful training scripts.
- **[TRL (Transformers Reinforcement Learning)](https://github.com/huggingface/trl)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/trl?style=social) - Official library for RLHF, SFT, DPO, ORPO.
- **[verl](https://github.com/volcengine/verl)** ![GitHub stars](https://img.shields.io/github/stars/volcengine/verl?style=social) - Volcano Engine Reinforcement Learning for LLMs with PPO, GRPO, REINFORCE++, DAPO (EuroSys 2025).
- **[NeMo-RL](https://github.com/NVIDIA-NeMo/RL)** ![GitHub stars](https://img.shields.io/github/stars/NVIDIA-NeMo/RL?style=social) - Scalable toolkit for efficient model reinforcement with DTensor and Megatron backends.
- **[OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)** ![GitHub stars](https://img.shields.io/github/stars/OpenRLHF/OpenRLHF?style=social) - Easy-to-use, scalable RLHF framework based on Ray. Supports PPO, GRPO, REINFORCE++, DAPO with vLLM integration and async training. Apache 2.0 licensed.
- **[LMFlow](https://github.com/OptimalScale/LMFlow)** ![GitHub stars](https://img.shields.io/github/stars/OptimalScale/LMFlow?style=social) - Extensible toolkit for finetuning and inference of large foundation models. Features RAFT alignment algorithm and comprehensive model support. Apache 2.0 licensed.
- **[H2O LLM Studio](https://github.com/h2oai/h2o-llmstudio)** ![GitHub stars](https://img.shields.io/github/stars/h2oai/h2o-llmstudio?style=social) - No-code GUI framework for fine-tuning LLMs. Streamlined interface for SFT, reward modeling, and model deployment. Apache 2.0 licensed.

#### LoRA / PEFT Tools

- **[PEFT (Parameter-Efficient Fine-Tuning)](https://github.com/huggingface/peft)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/peft?style=social) - Official library with LoRA, QLoRA, DoRA, etc.
- **[Liger Kernel](https://github.com/linkedin/Liger-Kernel)** ![GitHub stars](https://img.shields.io/github/stars/linkedin/Liger-Kernel?style=social) - Ultra-fast custom kernels for training speedup.
- **[MergeKit](https://github.com/arcee-ai/mergekit)** ![GitHub stars](https://img.shields.io/github/stars/arcee-ai/mergekit?style=social) - Advanced model merging tools.

#### Synthetic Data Generation

- **[distilabel](https://github.com/argilla-io/distilabel)** ![GitHub stars](https://img.shields.io/github/stars/argilla-io/distilabel?style=social) - End-to-end pipeline for synthetic instruction data.
- **[Data-Juicer](https://github.com/alibaba/data-juicer)** ![GitHub stars](https://img.shields.io/github/stars/alibaba/data-juicer?style=social) - High-performance data processing for LLM training.
- **[Argilla](https://github.com/argilla-io/argilla)** ![GitHub stars](https://img.shields.io/github/stars/argilla-io/argilla?style=social) - Open-source data labeling + synthetic data platform.
- **[SDV (Synthetic Data Vault)](https://github.com/sdv-dev/SDV)** ![GitHub stars](https://img.shields.io/github/stars/sdv-dev/SDV?style=social) - High-fidelity tabular and relational synthetic data.
- **[DataTrove (Hugging Face)](https://github.com/huggingface/datatrove)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/datatrove?style=social) - Platform-agnostic data processing pipelines for LLM training at scale. Handles filtering, deduplication, and tokenization on local machines or SLURM clusters.

#### Distributed Training

- **[DeepSpeed](https://github.com/deepspeedai/DeepSpeed)** ![GitHub stars](https://img.shields.io/github/stars/deepspeedai/DeepSpeed?style=social) - Extreme-scale training optimizations.
- **[Colossal-AI](https://github.com/hpcaitech/ColossalAI)** ![GitHub stars](https://img.shields.io/github/stars/hpcaitech/ColossalAI?style=social) - Unified system for 100B+ models.
- **[Megatron-LM](https://github.com/NVIDIA/Megatron-LM)** ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/Megatron-LM?style=social) - Distributed training framework and reference codebase for large transformer models at scale.
- **[Composer](https://github.com/mosaicml/composer)** ![GitHub stars](https://img.shields.io/github/stars/mosaicml/composer?style=social) - MosaicML's PyTorch library for scalable, efficient neural network training with algorithmic speedups.
- **[Ray Train](https://github.com/ray-project/ray)** ![GitHub stars](https://img.shields.io/github/stars/ray-project/ray?style=social) - Scalable distributed training.
- **[Nanotron (Hugging Face)](https://github.com/huggingface/nanotron)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/nanotron?style=social) - Minimalistic 3D-parallelism LLM pretraining with tensor, pipeline, and data parallelism. Designed for simplicity and speed.
- **[veScale (ByteDance)](https://github.com/volcengine/veScale)** ![GitHub stars](https://img.shields.io/github/stars/volcengine/veScale?style=social) - Hyperscale PyTorch distributed training with flexible FSDP implementation for LLMs and RL training at scale.
- **[GPT-NeoX (EleutherAI)](https://github.com/EleutherAI/gpt-neox)** ![GitHub stars](https://img.shields.io/github/stars/EleutherAI/gpt-neox?style=social) - Production-grade distributed training framework for large autoregressive transformers, powering models like GPT-J and GPT-NeoX-20B.

#### Model Quantization & Optimization

- **[LLM Compressor (vLLM)](https://github.com/vllm-project/llm-compressor)** ![GitHub stars](https://img.shields.io/github/stars/vllm-project/llm-compressor?style=social) - Transformers-compatible library for applying various compression algorithms to LLMs for optimized deployment with vLLM. Supports GPTQ, AWQ, SmoothQuant, AutoRound, and FP8/INT8 quantization with seamless Hugging Face integration.
- **[NVIDIA Model Optimizer](https://github.com/NVIDIA/Model-Optimizer)** ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/Model-Optimizer?style=social) - Unified library of SOTA model optimization techniques including quantization, pruning, distillation, and speculative decoding. Compresses deep learning models for deployment with TensorRT-LLM, TensorRT, and vLLM to optimize inference speed across NVIDIA hardware.

---

### 📊 8. MLOps / LLMOps & Production

> Tooling for tracking, deploying, monitoring, and operating AI systems in production.

#### Experiment Tracking & Versioning

- **[MLflow](https://github.com/mlflow/mlflow)** ![GitHub stars](https://img.shields.io/github/stars/mlflow/mlflow?style=social) - End-to-end open platform for the ML/LLM lifecycle.
- **[DVC (Data Version Control)](https://github.com/iterative/dvc)** ![GitHub stars](https://img.shields.io/github/stars/iterative/dvc?style=social) - Git-like versioning for data and models.
- **[ClearML](https://github.com/clearml/clearml)** ![GitHub stars](https://img.shields.io/github/stars/clearml/clearml?style=social) - Open-source platform for experiment tracking, orchestration, data management, and model serving.
- **[Weights & Biases Weave](https://github.com/wandb/weave)** ![GitHub stars](https://img.shields.io/github/stars/wandb/weave?style=social) - Open-source tracing and experiment tracking.
- **[Feast](https://github.com/feast-dev/feast)** ![GitHub stars](https://img.shields.io/github/stars/feast-dev/feast?style=social) - Open source feature store for ML. Manages offline/online feature storage with point-in-time correctness to prevent data leakage. Apache 2.0 licensed.

#### Deployment & Orchestration

- **[BentoML](https://github.com/bentoml/BentoML)** ![GitHub stars](https://img.shields.io/github/stars/bentoml/BentoML?style=social) - Unified framework to build, ship, and scale AI apps.
- **[Ray Serve](https://github.com/ray-project/ray)** ![GitHub stars](https://img.shields.io/github/stars/ray-project/ray?style=social) - Scalable model serving library.
- **[ZenML](https://github.com/zenml-io/zenml)** ![GitHub stars](https://img.shields.io/github/stars/zenml-io/zenml?style=social) - Pipeline and orchestration framework for taking ML and LLM systems from development to production.
- **[Kubeflow](https://github.com/kubeflow/kubeflow)** ![GitHub stars](https://img.shields.io/github/stars/kubeflow/kubeflow?style=social) - Kubernetes-native ML/LLM platform.
- **[KServe](https://github.com/kserve/kserve)** ![GitHub stars](https://img.shields.io/github/stars/kserve/kserve?style=social) - Kubernetes-based model serving.
- **[Seldon Core](https://github.com/SeldonIO/seldon-core)** ![GitHub stars](https://img.shields.io/github/stars/SeldonIO/seldon-core?style=social) - MLOps and LLMOps framework for deploying, managing and scaling AI systems in Kubernetes. Standardized deployment across model types with autoscaling, multi-model serving, and A/B experiments.
- **[Metaflow](https://github.com/Netflix/metaflow)** ![GitHub stars](https://img.shields.io/github/stars/Netflix/metaflow?style=social) - Netflix's ML platform for building and managing real-world AI systems. Powers thousands of projects at Netflix, Amazon, and DoorDash. Apache 2.0 licensed.
- **[Flyte](https://github.com/flyteorg/flyte)** ![GitHub stars](https://img.shields.io/github/stars/flyteorg/flyte?style=social) - Kubernetes-native workflow orchestration platform for AI/ML pipelines. Dynamic, resilient orchestration with strong type safety and reproducibility. Used by Lyft, Spotify, and Gojek. Apache 2.0 licensed.
- **[Prefect](https://github.com/prefecthq/prefect)** ![GitHub stars](https://img.shields.io/github/stars/prefecthq/prefect?style=social) - Workflow orchestration framework for building resilient data and ML pipelines. Python-native with modern observability and 200+ integrations. Apache 2.0 licensed.

#### Monitoring, Evaluation & Observability

- **[Langfuse](https://github.com/langfuse/langfuse)** ![GitHub stars](https://img.shields.io/github/stars/langfuse/langfuse?style=social) - #1 open-source LLM observability platform.
- **[Phoenix (Arize)](https://github.com/Arize-ai/phoenix)** ![GitHub stars](https://img.shields.io/github/stars/Arize-ai/phoenix?style=social) - AI observability & evaluation platform.
- **[Evidently](https://github.com/evidentlyai/evidently)** ![GitHub stars](https://img.shields.io/github/stars/evidentlyai/evidently?style=social) - ML & LLM monitoring framework.
- **[Opik (Comet)](https://github.com/comet-ml/opik)** ![GitHub stars](https://img.shields.io/github/stars/comet-ml/opik?style=social) - Production-ready LLM evaluation platform.
- **[LiteLLM](https://github.com/BerriAI/litellm)** ![GitHub stars](https://img.shields.io/github/stars/BerriAI/litellm?style=social) - AI Gateway to call 100+ LLM APIs in OpenAI format with unified cost tracking, guardrails, load balancing, and logging.
- **[OpenLIT](https://github.com/openlit/openlit)** ![GitHub stars](https://img.shields.io/github/stars/openlit/openlit?style=social) - OpenTelemetry-native LLM observability platform with GPU monitoring, evaluations, prompt management, and guardrails.
- **[OpenLLMetry (Traceloop)](https://github.com/traceloop/openllmetry)** ![GitHub stars](https://img.shields.io/github/stars/traceloop/openllmetry?style=social) - Open-source observability for GenAI/LLM applications based on OpenTelemetry with 25+ integration backends.
- **[Agenta](https://github.com/Agenta-AI/agenta)** ![GitHub stars](https://img.shields.io/github/stars/Agenta-AI/agenta?style=social) - Open-source LLMOps platform combining prompt playground, prompt management, LLM evaluation, and observability.
- **[Helicone](https://github.com/helicone/helicone)** ![GitHub stars](https://img.shields.io/github/stars/helicone/helicone?style=social) - Open-source LLM observability with request logging, caching, rate limiting, and cost analytics.
- **[Giskard](https://github.com/Giskard-AI/giskard-oss)** ![GitHub stars](https://img.shields.io/github/stars/Giskard-AI/giskard-oss?style=social) - Open-source evaluation and testing library for LLM agents. Red teaming, vulnerability scanning, RAG evaluation, and safety testing with modular architecture. Apache 2.0 licensed.
- **[Portkey Gateway](https://github.com/Portkey-AI/gateway)** ![GitHub stars](https://img.shields.io/github/stars/Portkey-AI/gateway?style=social) - Blazing fast AI Gateway to route 200+ LLMs with unified API. Integrated guardrails, load balancing, fallbacks, and cost tracking. MIT licensed.
- **[TensorZero](https://github.com/tensorzero/tensorzero)** ![GitHub stars](https://img.shields.io/github/stars/tensorzero/tensorzero?style=social) - Open-source LLMOps platform unifying LLM gateway, observability, evaluation, and experimentation. Production-grade with sub-1ms latency, used by Fortune 10 companies.

#### Guardrails & Safety Tools

- **[NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)** ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/NeMo-Guardrails?style=social) - Programmable guardrails toolkit for LLM-based conversational systems. Uses Colang to define dialog flows with input/output rails, jailbreak detection, fact-checking, and hallucination detection. Apache 2.0 licensed.
- **[Guardrails AI](https://github.com/guardrails-ai/guardrails)** ![GitHub stars](https://img.shields.io/github/stars/guardrails-ai/guardrails?style=social) - Python framework for adding input/output guardrails to LLM applications. Detects and mitigates risks like PII leakage, toxic language, competitor mentions, with 50+ validators in Guardrails Hub. Apache 2.0 licensed.
- **[LLM Guard](https://github.com/protectai/llm-guard)** ![GitHub stars](https://img.shields.io/github/stars/protectai/llm-guard?style=social) - Comprehensive security toolkit for LLM interactions with input/output scanners for prompt injection, PII anonymization, toxic content, secrets detection, and adversarial attack prevention. MIT licensed.
- **[LlamaGuard (Meta)](https://github.com/meta-llama/PurpleLlama)** ![GitHub stars](https://img.shields.io/github/stars/meta-llama/PurpleLlama?style=social) - Open safety classifier models.
- **[Garak](https://github.com/leondz/garak)** ![GitHub stars](https://img.shields.io/github/stars/leondz/garak?style=social) - LLM vulnerability scanner.
- **[Promptfoo](https://github.com/promptfoo/promptfoo)** ![GitHub stars](https://img.shields.io/github/stars/promptfoo/promptfoo?style=social) - LLM testing and red-teaming framework.

---

### 📈 9. Evaluation, Benchmarks & Datasets

> Benchmarks, evaluation frameworks, datasets, and supporting tools for model assessment.

#### Benchmark Suites

- **[LiveBench](https://github.com/LiveBench/LiveBench)** ![GitHub stars](https://img.shields.io/github/stars/LiveBench/LiveBench?style=social) - Contamination-free LLM benchmark with objective ground-truth scoring. ICLR 2025 spotlight paper featuring frequently-updated questions from recent sources. Tests math, coding, reasoning, language, instruction following, and data analysis.
- **[lm-evaluation-harness (EleutherAI)](https://github.com/EleutherAI/lm-evaluation-harness)** ![GitHub stars](https://img.shields.io/github/stars/EleutherAI/lm-evaluation-harness?style=social) - De-facto standard for generative model evaluation.
- **[HELM (Stanford)](https://github.com/stanford-crfm/helm)** ![GitHub stars](https://img.shields.io/github/stars/stanford-crfm/helm?style=social) - Holistic Evaluation of Language Models.
- **[SWE-bench](https://github.com/SWE-bench/SWE-bench)** ![GitHub stars](https://img.shields.io/github/stars/SWE-bench/SWE-bench?style=social) - Evaluates LLMs on real-world GitHub issues from 15+ Python repositories.
- **[GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA)** - Real-world multi-step agentic benchmark.
- **[OpenCompass](https://github.com/open-compass/opencompass)** ![GitHub stars](https://img.shields.io/github/stars/open-compass/opencompass?style=social) - Evaluation platform for benchmarking language and multimodal models across large benchmark suites.
- **[MLPerf Inference](https://github.com/mlcommons/inference)** ![GitHub stars](https://img.shields.io/github/stars/mlcommons/inference?style=social) - Industry-standard ML inference benchmarks with reference implementations for AI accelerators.
- **[SWE-rebench (Nebius)](https://huggingface.co/datasets/nebius/SWE-rebench)** - Continuously updated benchmark with 21,000+ real-world SWE tasks for evaluating agentic LLMs. Decontaminated, mined from GitHub.
- **[AgentBench (THUDM)](https://github.com/THUDM/AgentBench)** ![GitHub stars](https://img.shields.io/github/stars/THUDM/AgentBench?style=social) - Comprehensive benchmark to evaluate LLMs as agents across 8 diverse environments including household, web shopping, OS interaction, and database tasks. ICLR 2024. Apache 2.0 licensed.

#### Evaluation Frameworks

- **[DeepEval](https://github.com/confident-ai/deepeval)** ![GitHub stars](https://img.shields.io/github/stars/confident-ai/deepeval?style=social) - The "Pytest for LLMs".
- **[Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai)** ![GitHub stars](https://img.shields.io/github/stars/UKGovernmentBEIS/inspect_ai?style=social) - Framework for large language model evaluations from the UK AI Security Institute.
- **[RAGAs](https://github.com/explodinggradients/ragas)** ![GitHub stars](https://img.shields.io/github/stars/explodinggradients/ragas?style=social) - End-to-end RAG evaluation framework.
- **[Lighteval](https://github.com/huggingface/lighteval)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/lighteval?style=social) - Evaluation toolkit for LLMs across multiple backends with reusable tasks, metrics, and result tracking.
- **[Hugging Face Evaluate](https://github.com/huggingface/evaluate)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/evaluate?style=social) - Standardized evaluation metrics.
- **[OpenAI Evals](https://github.com/openai/evals)** ![GitHub stars](https://img.shields.io/github/stars/openai/evals?style=social) - Framework for evaluating LLMs and LLM systems with an open-source registry of 100+ community-contributed benchmarks. MIT licensed.

#### High-quality Open Datasets & Data Tools

- **[Hugging Face Datasets](https://github.com/huggingface/datasets)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/datasets?style=social) - Largest open repository of datasets.
- **[Cleanlab](https://github.com/cleanlab/cleanlab)** ![GitHub stars](https://img.shields.io/github/stars/cleanlab/cleanlab?style=social) - Data-centric AI package for automatically finding and fixing issues in datasets. Detects label errors, outliers, and ambiguous examples in ML datasets. Apache 2.0 licensed.
- **[FineWeb / FineWeb-2 (Hugging Face)](https://huggingface.co/datasets/HuggingFaceFW/fineweb)** - Curated 15T+ token web dataset for pre-training.
- **[OSWorld](https://github.com/xlang-ai/OSWorld)** ![GitHub stars](https://img.shields.io/github/stars/xlang-ai/OSWorld?style=social) - Multimodal agent benchmark dataset.

---

<a id="section-10"></a>

### 🛡️ 10. AI Safety, Alignment & Interpretability

> Tools for alignment, interpretability, safety evaluation, and adversarial testing.

#### Safety Evaluation Frameworks

- **[Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai)** ![GitHub stars](https://img.shields.io/github/stars/UKGovernmentBEIS/inspect_ai?style=social) - Framework for large language model evaluations from the UK AI Safety Institute. Systematic capability and safety assessments with built-in scaffolding for multi-turn dialog, tool use, and adversarial testing. MIT licensed.
- **[DeepEval](https://github.com/confident-ai/deepeval)** ![GitHub stars](https://img.shields.io/github/stars/confident-ai/deepeval?style=social) - LLM evaluation framework with built-in safety metrics including hallucination detection, bias detection, toxicity evaluation, and prompt alignment checking. Apache 2.0 licensed.

#### Alignment & RLHF Tools

- **[Safe-RLHF](https://github.com/PKU-Alignment/safe-rlhf)** ![GitHub stars](https://img.shields.io/github/stars/PKU-Alignment/safe-rlhf?style=social) - Safe reinforcement learning from human feedback.
- **[Alignment Handbook](https://github.com/huggingface/alignment-handbook)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/alignment-handbook?style=social) - Complete recipes for full-stack alignment.
- **[OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)** ![GitHub stars](https://img.shields.io/github/stars/OpenRLHF/OpenRLHF?style=social) - High-performance distributed RLHF framework.

#### Interpretability & Explainability

- **[interpret (Microsoft)](https://github.com/interpretml/interpret)** ![GitHub stars](https://img.shields.io/github/stars/interpretml/interpret?style=social) - Fit interpretable models and explain blackbox machine learning with state-of-the-art explainability techniques including Explainable Boosting Machines and SHAP-based explanations.
- **[TransformerLens](https://github.com/TransformerLensOrg/TransformerLens)** ![GitHub stars](https://img.shields.io/github/stars/TransformerLensOrg/TransformerLens?style=social) - Gold-standard for mechanistic interpretability.
- **[SAELens](https://github.com/jbloomAus/SAELens)** ![GitHub stars](https://img.shields.io/github/stars/jbloomAus/SAELens?style=social) - Sparse autoencoders for interpretable features.
- **[Captum](https://github.com/pytorch/captum)** ![GitHub stars](https://img.shields.io/github/stars/pytorch/captum?style=social) - PyTorch's official interpretability library.
- **[SHAP](https://github.com/shap/shap)** ![GitHub stars](https://img.shields.io/github/stars/shap/shap?style=social) - Game theoretic approach to explain the output of any machine learning model. Industry standard for model interpretability.
- **[XAI](https://github.com/EthicalML/xai)** ![GitHub stars](https://img.shields.io/github/stars/EthicalML/xai?style=social) - eXplainability toolbox for machine learning with bias evaluation and production monitoring tools.
- **[EasyEdit](https://github.com/zjunlp/EasyEdit)** ![GitHub stars](https://img.shields.io/github/stars/zjunlp/EasyEdit?style=social) - Easy-to-use knowledge editing framework for LLMs. Enables precise modification of model knowledge and behavior to correct hallucinations or outdated information. ACL 2024. MIT licensed.

#### Fairness & Bias Mitigation

- **[AI Fairness 360](https://github.com/Trusted-AI/AIF360)** ![GitHub stars](https://img.shields.io/github/stars/Trusted-AI/AIF360?style=social) - Comprehensive toolkit for detecting, understanding, and mitigating unwanted algorithmic bias in datasets and ML models.

#### Adversarial & Red-teaming Tools

- **[Garak](https://github.com/NVIDIA/garak)** ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/garak?style=social) - Automated LLM vulnerability scanner.
- **[Promptfoo](https://github.com/promptfoo/promptfoo)** ![GitHub stars](https://img.shields.io/github/stars/promptfoo/promptfoo?style=social) - Systematic prompt testing and red-teaming.
- **[LLM Guard](https://github.com/protectai/llm-guard)** ![GitHub stars](https://img.shields.io/github/stars/protectai/llm-guard?style=social) - Input/output scanner for LLMs.
- **[Adversarial Robustness Toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox)** ![GitHub stars](https://img.shields.io/github/stars/Trusted-AI/adversarial-robustness-toolbox?style=social) - Python library for machine learning security (evasion, poisoning, extraction, inference attacks).
- **[DeepTeam](https://github.com/confident-ai/deepteam)** ![GitHub stars](https://img.shields.io/github/stars/confident-ai/deepteam?style=social) - Framework to red team LLMs and LLM systems.

---

### 🧩 11. Specialized Domains

#### Scientific AI & Drug Discovery

- **[Boltz](https://github.com/jwohlwend/boltz)** ![GitHub stars](https://img.shields.io/github/stars/jwohlwend/boltz?style=social) - Open-source biomolecular interaction prediction models. Boltz-1 was the first fully open source model to approach AlphaFold3 accuracy; Boltz-2 adds binding affinity prediction for drug discovery. MIT licensed.
- **[OpenFold](https://github.com/aqlaboratory/openfold)** ![GitHub stars](https://img.shields.io/github/stars/aqlaboratory/openfold?style=social) - Trainable PyTorch reproduction of AlphaFold2. Complete open-source pipeline for protein structure prediction with competitive accuracy to the original. Apache 2.0 licensed.

#### Medical Imaging & Healthcare AI

- **[MONAI](https://github.com/Project-MONAI/MONAI)** ![GitHub stars](https://img.shields.io/github/stars/Project-MONAI/MONAI?style=social) - Medical Open Network for AI. End-to-end framework for healthcare imaging with state-of-the-art, production-ready training workflows. Apache 2.0 licensed.
- **[nnU-Net](https://github.com/MIC-DKFZ/nnUNet)** ![GitHub stars](https://img.shields.io/github/stars/MIC-DKFZ/nnUNet?style=social) - Self-configuring deep learning method for medical image segmentation. Automatically adapts to any dataset without manual parameter tuning. Widely adopted as the standard baseline for biomedical segmentation challenges. Apache 2.0 licensed.

#### Game AI & Simulations

- **[Unity ML-Agents](https://github.com/Unity-Technologies/ml-agents)** ![GitHub stars](https://img.shields.io/github/stars/Unity-Technologies/ml-agents?style=social) - Toolkit for training intelligent agents in games and simulations using deep reinforcement learning. Enables NPC behavior control, automated testing, and game design evaluation. Apache 2.0 licensed.
- **[OpenSpiel](https://github.com/google-deepmind/open_spiel)** ![GitHub stars](https://img.shields.io/github/stars/google-deepmind/open_spiel?style=social) - Collection of environments and algorithms for research in general reinforcement learning and search/planning in games from Google DeepMind. Apache 2.0 licensed.

#### Finance & Quantitative AI

- **[OpenBB](https://github.com/OpenBB-finance/OpenBB)** ![GitHub stars](https://img.shields.io/github/stars/OpenBB-finance/OpenBB?style=social) - Financial data platform for analysts, quants and AI agents. Open-source investment research infrastructure with extensive data integrations. AGPL-3.0 licensed.
- **[FinGPT](https://github.com/AI4Finance-Foundation/FinGPT)** ![GitHub stars](https://img.shields.io/github/stars/AI4Finance-Foundation/FinGPT?style=social) - Open-source financial large language models. Democratizing financial AI with data-centric training pipeline and multiple model releases for trading, analysis, and robo-advising. MIT licensed.
- **[FinRL](https://github.com/AI4Finance-Foundation/FinRL)** ![GitHub stars](https://img.shields.io/github/stars/AI4Finance-Foundation/FinRL?style=social) - Financial reinforcement learning framework for quantitative trading. Deep RL library for stock trading, portfolio allocation, and market execution with pre-built environments and benchmarks. MIT licensed.

#### Computer Vision

- **[OpenCV](https://github.com/opencv/opencv)** ![GitHub stars](https://img.shields.io/github/stars/opencv/opencv?style=social) - World's most widely used computer vision library.
- **[Ultralytics YOLO](https://github.com/ultralytics/ultralytics)** ![GitHub stars](https://img.shields.io/github/stars/ultralytics/ultralytics?style=social) - State-of-the-art real-time object detection.
- **[Detectron2](https://github.com/facebookresearch/detectron2)** ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/detectron2?style=social) - High-performance object detection library.
- **[CVAT](https://github.com/cvat-ai/cvat)** ![GitHub stars](https://img.shields.io/github/stars/cvat-ai/cvat?style=social) - Industry-leading data annotation platform for computer vision. Interactive video and image annotation tool used by tens of thousands of teams for machine learning at any scale.
- **[SAM 2](https://github.com/facebookresearch/sam2)** ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/sam2?style=social) - Promptable image and video segmentation model with released checkpoints and training code.
- **[Kornia](https://github.com/kornia/kornia)** ![GitHub stars](https://img.shields.io/github/stars/kornia/kornia?style=social) - Differentiable computer vision library.
- **[MediaPipe](https://github.com/google-ai-edge/mediapipe)** ![GitHub stars](https://img.shields.io/github/stars/google-ai-edge/mediapipe?style=social) - Cross-platform multimodal pipelines.

#### Reinforcement Learning & Robotics

- **[Stable-Baselines3](https://github.com/DLR-RM/stable-baselines3)** ![GitHub stars](https://img.shields.io/github/stars/DLR-RM/stable-baselines3?style=social) - Production-ready RL algorithms.
- **[Isaac Lab](https://github.com/isaac-sim/IsaacLab)** ![GitHub stars](https://img.shields.io/github/stars/isaac-sim/IsaacLab?style=social) - GPU-accelerated robot learning framework.
- **[MuJoCo](https://github.com/google-deepmind/mujoco)** ![GitHub stars](https://img.shields.io/github/stars/google-deepmind/mujoco?style=social) - General-purpose physics simulator for robotics, biomechanics, and ML research. High-fidelity contact dynamics with native Python and C++ bindings. Apache 2.0 licensed.
- **[Gymnasium (ex-OpenAI Gym)](https://github.com/Farama-Foundation/Gymnasium)** ![GitHub stars](https://img.shields.io/github/stars/Farama-Foundation/Gymnasium?style=social) - Standard RL environment API.

#### Time Series & Scientific AI

- **[Time Series Library (TSLib)](https://github.com/thuml/Time-Series-Library)** ![GitHub stars](https://img.shields.io/github/stars/thuml/Time-Series-Library?style=social) - Comprehensive benchmark for time-series models.
- **[Chronos (Amazon)](https://github.com/amazon-science/chronos-forecasting)** ![GitHub stars](https://img.shields.io/github/stars/amazon-science/chronos-forecasting?style=social) - Pretrained foundation models for time-series forecasting.
- **[Darts](https://github.com/unit8co/darts)** ![GitHub stars](https://img.shields.io/github/stars/unit8co/darts?style=social) - Easy-to-use time-series forecasting library.
- **[AutoTS](https://github.com/winedarksea/AutoTS)** ![GitHub stars](https://img.shields.io/github/stars/winedarksea/AutoTS?style=social) - Automated time series forecasting with broad model selection, ensembling, anomaly detection, and holiday effects. Designed for production deployment with minimal setup.

#### Edge / On-device AI

- **[TensorFlow Lite](https://github.com/tensorflow/tensorflow)** ![GitHub stars](https://img.shields.io/github/stars/tensorflow/tensorflow?style=social) - Lightweight on-device ML.
- **[ONNX Runtime](https://github.com/microsoft/onnxruntime)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/onnxruntime?style=social) - Cross-platform high-performance inference.
- **[ExecuTorch](https://github.com/pytorch/executorch)** ![GitHub stars](https://img.shields.io/github/stars/pytorch/executorch?style=social) - PyTorch runtime and toolchain for deploying AI models on mobile, embedded, and edge devices.
- **[OpenVINO](https://github.com/openvinotoolkit/openvino)** ![GitHub stars](https://img.shields.io/github/stars/openvinotoolkit/openvino?style=social) - Intel's toolkit for edge deployment.
- **[MicroTVM (Apache TVM)](https://github.com/apache/tvm)** ![GitHub stars](https://img.shields.io/github/stars/apache/tvm?style=social) - Compiler stack for microcontrollers.

#### Legal AI & Contract Analysis

- **[OpenContracts](https://github.com/Open-Source-Legal/OpenContracts)** ![GitHub stars](https://img.shields.io/github/stars/Open-Source-Legal/OpenContracts?style=social) - Self-hosted document annotation platform for legal AI. Semantic search, contract analysis, version control, and MCP integration for building legal knowledge bases. AGPL-3.0 licensed.

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
- **[NextChat](https://github.com/ChatGPTNextWeb/NextChat)** ![GitHub stars](https://img.shields.io/github/stars/ChatGPTNextWeb/NextChat?style=social) - Light and fast AI assistant supporting Web, iOS, macOS, Android, Linux, and Windows. One-click deploy with multi-model support. MIT licensed.
- **[big-AGI](https://github.com/enricoros/big-AGI)** ![GitHub stars](https://img.shields.io/github/stars/enricoros/big-AGI?style=social) - AI suite for power users with multi-model "Beam" chats, AI personas, voice, text-to-image, code execution, and PDF import. MIT licensed.
- **[Leon](https://github.com/leon-ai/leon)** ![GitHub stars](https://img.shields.io/github/stars/leon-ai/leon?style=social) - Your open-source personal assistant. Built around tools, context, memory, and agentic execution. Self-hosted, privacy-focused, and extensible. MIT licensed.
- **[Willow](https://github.com/HeyWillow/willow)** ![GitHub stars](https://img.shields.io/github/stars/HeyWillow/willow?style=social) - Open source, local, and self-hosted Amazon Echo/Google Home competitive voice assistant alternative with hardware support. Apache-2.0 licensed.
- **[CoPaw](https://github.com/agentscope-ai/CoPaw)** ![GitHub stars](https://img.shields.io/github/stars/agentscope-ai/CoPaw?style=social) - Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities. Apache-2.0 licensed.

#### Full Self-hosted AI Platforms

- **[AnythingLLM](https://github.com/Mintplex-Labs/anything-llm)** ![GitHub stars](https://img.shields.io/github/stars/Mintplex-Labs/anything-llm?style=social) - All-in-one RAG + agents platform.
- **[Dify](https://github.com/langgenius/dify)** ![GitHub stars](https://img.shields.io/github/stars/langgenius/dify?style=social) - Complete AI application platform with visual builder.
- **[Langflow](https://github.com/langflow-ai/langflow)** ![GitHub stars](https://img.shields.io/github/stars/langflow-ai/langflow?style=social) - Visual low-code platform for LangChain flows.
- **[Flowise](https://github.com/FlowiseAI/Flowise)** ![GitHub stars](https://img.shields.io/github/stars/FlowiseAI/Flowise?style=social) - Drag-and-drop LLM app builder.
- **[LocalAI](https://github.com/mudler/LocalAI)** ![GitHub stars](https://img.shields.io/github/stars/mudler/LocalAI?style=social) - Open-source AI engine running LLMs, vision, voice, image, and video models on any hardware. Self-hosted OpenAI-compatible API. MIT licensed.
- **[Onyx](https://github.com/onyx-dot-app/onyx)** ![GitHub stars](https://img.shields.io/github/stars/onyx-dot-app/onyx?style=social) - Full-featured AI platform with Chat, RAG, Agents, and Actions. 40+ document connectors and every LLM support. MIT licensed (Community Edition).

#### Desktop & Mobile AI Apps

- **[Jan](https://github.com/janhq/jan)** ![GitHub stars](https://img.shields.io/github/stars/janhq/jan?style=social) - Local-first AI app framework.
- **[Cherry Studio](https://github.com/CherryHQ/cherry-studio)** ![GitHub stars](https://img.shields.io/github/stars/CherryHQ/cherry-studio?style=social) - AI productivity studio with smart chat, autonomous agents, and 300+ assistants. Unified access to frontier LLMs. AGPL-3.0 licensed.
- **[DeepChat](https://github.com/ThinkInAIXYZ/deepchat)** ![GitHub stars](https://img.shields.io/github/stars/ThinkInAIXYZ/deepchat?style=social) - A smart assistant that connects powerful AI to your personal world. Built-in MCP and ACP support, multiple search engines, privacy-focused with local data storage. Apache-2.0 licensed.
- **[SillyTavern](https://github.com/SillyTavern/SillyTavern)** ![GitHub stars](https://img.shields.io/github/stars/SillyTavern/SillyTavern?style=social) - Highly customizable role-playing frontend.
- **[Chatbox](https://github.com/chatboxai/chatbox)** ![GitHub stars](https://img.shields.io/github/stars/chatboxai/chatbox?style=social) - Powerful desktop AI client for ChatGPT, Claude, and other LLMs. Cross-platform with modern UI. GPLv3 licensed (Community Edition).
- **[Maid](https://github.com/Mobile-Artificial-Intelligence/maid)** ![GitHub stars](https://img.shields.io/github/stars/Mobile-Artificial-Intelligence/maid?style=social) - Free and open-source Android app for interfacing with llama.cpp models locally and remote APIs (Anthropic, DeepSeek, Mistral, Ollama, OpenAI). MIT licensed.

#### Agent & Voice Infrastructure

- **[LiveKit Agents](https://github.com/livekit/agents)** ![GitHub stars](https://img.shields.io/github/stars/livekit/agents?style=social) - Framework for building realtime voice AI agents with WebRTC transport, STT-LLM-TTS pipelines, and production-grade orchestration. Used by Salesforce Agentforce and Tesla. Apache-2.0 licensed.
- **[Pipecat](https://github.com/pipecat-ai/pipecat)** ![GitHub stars](https://img.shields.io/github/stars/pipecat-ai/pipecat?style=social) - Open-source framework for voice and multimodal conversational AI. Build real-time voice agents with support for speech-to-text, LLMs, text-to-speech, and live video. BSD-2-Clause licensed.
- **[Agent Chat UI](https://github.com/langchain-ai/agent-chat-ui)** ![GitHub stars](https://img.shields.io/github/stars/langchain-ai/agent-chat-ui?style=social) - Web app for interacting with any LangGraph agent (Python & TypeScript) via a chat interface. Stream messages, handle interruptions, and view agent state. MIT licensed.

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

#### UI Components & Chat Libraries

- **[Assistant UI](https://github.com/assistant-ui/assistant-ui)** ![GitHub stars](https://img.shields.io/github/stars/assistant-ui/assistant-ui?style=social) - React/TypeScript library for building production-grade AI chat interfaces. Drop-in components for streaming messages, tool calls, and multi-modal inputs.
- **[Deep Chat](https://github.com/OvidijusParsiunas/deep-chat)** ![GitHub stars](https://img.shields.io/github/stars/OvidijusParsiunas/deep-chat?style=social) - Fully customizable AI chatbot component for your website. Supports OpenAI, direct API services, and custom endpoints. MIT licensed.

#### CLI Tools & API Clients

- **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** ![GitHub stars](https://img.shields.io/github/stars/google-gemini/gemini-cli?style=social) - Google's open-source AI agent for the terminal. Access Gemini models with built-in tool use, MCP support, and 1M token context. Apache 2.0 licensed.
- **[LLM (Simon Willison)](https://github.com/simonw/llm)** ![GitHub stars](https://img.shields.io/github/stars/simonw/llm?style=social) - CLI tool and Python library for interacting with dozens of LLMs via remote APIs or locally. Extensible plugin ecosystem, SQLite logging. Apache 2.0 licensed.
- **[AIChat](https://github.com/sigoden/aichat)** ![GitHub stars](https://img.shields.io/github/stars/sigoden/aichat?style=social) - All-in-one LLM CLI in Rust featuring Shell Assistant, Chat-REPL, RAG, AI Tools & Agents. Supports 20+ providers. MIT/Apache 2.0 licensed.
- **[aicommits](https://github.com/Nutlope/aicommits)** ![GitHub stars](https://img.shields.io/github/stars/Nutlope/aicommits?style=social) - CLI that writes your git commit messages for you with AI. Never write a commit message again. Supports multiple providers including OpenAI, Groq, xAI, Ollama, and LM Studio. MIT licensed.
- **[Codex CLI](https://github.com/openai/codex)** ![GitHub stars](https://img.shields.io/github/stars/openai/codex?style=social) - OpenAI's lightweight coding agent that runs in your terminal. Code generation, file editing, and command execution with approval. Apache 2.0 licensed.
- **[Repomix](https://github.com/yamadashy/repomix)** ![GitHub stars](https://img.shields.io/github/stars/yamadashy/repomix?style=social) - Powerful tool that packs your entire repository into a single AI-friendly file. Perfect for feeding codebases to LLMs with smart filtering and token counting. MIT licensed.

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
- **[ML For Beginners (Microsoft)](https://github.com/microsoft/ML-For-Beginners)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/ML-For-Beginners?style=social) - 12-week, 26-lesson, 52-quiz classic machine learning course for beginners. Comprehensive curriculum covering regression, classification, clustering, and NLP with practical projects.
- **[LLM Course (Maxime Labonne)](https://github.com/mlabonne/llm-course)** ![GitHub stars](https://img.shields.io/github/stars/mlabonne/llm-course?style=social) - End-to-end course for getting into Large Language Models with roadmaps and Colab notebooks. Covers pre-training, fine-tuning, RLHF, quantization, and prompt engineering.
- **[AI For Beginners (Microsoft)](https://github.com/microsoft/AI-For-Beginners)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/AI-For-Beginners?style=social) - 12-week, 24-lesson curriculum on Artificial Intelligence. Covers symbolic AI, neural networks, computer vision, NLP, and reinforcement learning with hands-on labs.
- **[Generative AI for Beginners (Microsoft)](https://github.com/microsoft/generative-ai-for-beginners)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/generative-ai-for-beginners?style=social) - 21 lessons covering generative AI fundamentals, prompt engineering, RAG applications, fine-tuning, and LLM app deployment with practical exercises.
- **[Fast.ai](https://github.com/fastai/fastai)** ![GitHub stars](https://img.shields.io/github/stars/fastai/fastai?style=social) - Legendary practical deep learning course.
- **[LangChain Academy](https://academy.langchain.com)** - Free courses on agents and RAG.

#### Starter Projects & Examples

- **[TensorFlow Tutorials](https://github.com/tensorflow/docs)** ![GitHub stars](https://img.shields.io/github/stars/tensorflow/docs?style=social) - Official guides for beginners to advanced users.
- **[Hugging Face Transformers Notebooks](https://github.com/huggingface/notebooks)** ![GitHub stars](https://img.shields.io/github/stars/huggingface/notebooks?style=social) - Run Transformers, Datasets, and more in Colab.

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
