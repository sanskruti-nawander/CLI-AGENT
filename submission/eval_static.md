# Static Evaluation

Each instruction was tested on both the base model and the fine-tuned model. BLEU score was computed based on overlap, and plan quality was rated from 0 to 2.

| Prompt | BLEU | Plan Quality (0–2) |
|--------|------|--------------------|
| Create a new Git branch and switch to it | 0.02 | 2 |
| Search for a word 'error' in all .log files | 0.02 | 2 |
| Activate a Python virtual environment | 0.02 | 2 |
| Compress a folder using tar and gzip | 0.05 | 2 |
| List all hidden files in a directory | 0.04 | 1 |
| Delete all .log files recursively (edge case) | 0.00 | 2 |
| Initialize a Git repo and add a remote (edge case) | 0.04 | 2 |

**Average BLEU Score:** 0.028  
**Average Plan Score:** 1.85
