# CLI-AGENT

## 🚀 How to Run

### ✅ Requirements

Install the dependencies:

```bash
pip install transformers peft torch
```

> Note: Use Python 3.8+ with GPU support (if available).

---

### ▶️ Run the Agent

```bash
python agent.py "Create a new Git branch and switch to it"
```

- It will load the LoRA adapter from `submission/training/adapter_model/`
- Generate a step-by-step shell plan
- Simulate the first command using `echo`
- Log all steps to `logs/trace.jsonl`

---

## 🧠 Model Details

- Base Model: TinyLlama/TinyLlama-1.1B-Chat-v1.0  
- LoRA Config: r=8, alpha=32, dropout=0.05  
- Epochs: 1  
- Fine-tuning Tool: HuggingFace Transformers + PEFT

---

## 📦 Output

- You will see the generated shell plan in your terminal
- Steps will be saved to `logs/trace.jsonl` in JSONL format

---

## 📽️ Demo

Demo is recorded in this [MP4 video on YouTube](https://youtu.be/ztonhOArkJY?feature=shared) 
