# Technical Task Report

**Model:** TinyLlama-1.1B-Chat-v1.0  
**LoRA Config:** r=8, alpha=32, dropout=0.05  
**Training Time:** ~7 minutes on Google Colab (T4)  
**Hardware Used:** Free Google Colab GPU  
**Dataset:** 155 command-line Q&A pairs (Git, Bash, tar, grep, venv)  
**Adapter Size:** ~380MB  
**Token Count:** ~140K tokens  
**Training:** 1 epoch using HuggingFace Trainer + PEFT  

---

## Evaluation Summary

- **Static Evaluation:**
  - BLEU Score: 0.028 avg
  - Plan Score: 1.85/2 avg

- **Dynamic Evaluation:**
  - Instruction: "Create a new Git branch and switch to it"
  - Output: Multi-step command plan + real Git command examples
  - Score: 2/2

---

## Two Suggestions for Improvement

1. **Use Instruction-Tuned LLMs:** Starting from Mistral-7B-Instruct or Phi-3 with proper instruction formats may generate more precise shell steps.

2. **Enhance Robustness:** Add error recovery or confirmations (e.g., "Are you sure you want to delete these files?") to emulate safer CLI guidance.

