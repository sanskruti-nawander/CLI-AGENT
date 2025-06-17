# Static Evaluation

This evaluation compares the output of the base model vs. the fine-tuned model across 5 required test prompts and 2 edge-case instructions. The BLEU score is used to measure similarity, and a plan quality score (0–2) is assigned based on accuracy and completeness.

| Prompt                                                       | BLEU  | Plan Score (0–2) |
|--------------------------------------------------------------|-------|------------------|
| Create a new Git branch and switch to it                     | 0.02  | 2                |
| Compress the folder reports into reports.tar.gz              | 0.02  | 2                |
| List all Python files in the current directory recursively   | 0.05  | 2                |
| Set up a virtual environment and install requests            | 0.10  | 2                |
| Fetch only the first ten lines of a file named output.log    | 0.14  | 2                |
| Delete all .log files recursively *(edge case)*              | 0.00  | 2                |
| Initialize a Git repo and add a remote origin *(edge case)*  | 0.08  | 2                |

---

**Average BLEU Score:** 0.06  
**Average Plan Score:** 2.0 / 2.0

### Evaluation Notes:
- The fine-tuned model consistently produced multi-step, command-specific plans.
- BLEU score remains low due to format differences but plan quality was strong and usable.
