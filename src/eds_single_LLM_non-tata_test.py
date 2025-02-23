import os
import dotenv
from smolagents import CodeAgent, LiteLLMModel
from telemetry_setup import logging_setup

dotenv.load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
logging_setup()

prompt_context = """
1. Character Definition:
Act as a senior bioinformatics researcher with 10 years experience in DNA sequence analysis and machine learning. Your expertise focuses on promoter prediction and sequence classification using deep learning approaches, with emphasis on memory-efficient processing of large genomic datasets.

2. Request Architecture:
Primary Objective: Design and implement a DNA sequence classifier that can identify specific genomic elements.
Step 1: Validate and sample data using safe memory practices
Step 2: Design appropriate neural architecture
Step 3: Implement evaluation framework
Success Metrics: Model must achieve reasonable accuracy while maintaining memory efficiency

3. Example Injection:
Good Pattern:
- Implementing batch processing for large files
- Using proper sequence encoding (one-hot or k-mer)
- Including data validation steps

Anti-Pattern:
- Loading entire dataset into memory
- Using string manipulation for DNA sequences
- Skipping data validation steps

4. Adjustment Constraints:
Technical Boundaries:
- Max sample size: 10 sequences
- File paths: /workspace/datasets/human_non_tata_promoters/human_nontata_promoters_train.csv and /workspace/datasets/human_non_tata_promoters/human_nontata_promoters_test.csv
- Memory limit: Keep under 2GB RAM usage
- Do not view /workspace/datasets/human_non_tata_promoters/dataset_description.md
- Required directory:
  - /workspace/results (create if not exists)

5. Type Specification:
Return format must be:
{
    "data_validation": {
        "files_exist": bool,
        "sample_size": int,
        "sequence_length": int,
        "class_distribution": dict
    },
    "model_architecture": {
        "layers": list,
        "parameters": dict
    },
    "evaluation_metrics": {
        "accuracy": float,
        "sensitivity": float,  // True Positive Rate
        "specificity": float,  // True Negative Rate
        "f1_score": float,
        "output_path": str    // Path to saved metrics CSV
    }
}

6. Evaluation Protocol:
Before finalizing, verify:
1. File existence and permissions
2. Sequence validity (ACGT alphabet)
3. Memory usage monitoring
4. Basic model architecture soundness
5. Metrics calculation:
   - Accuracy = (TP + TN) / (TP + TN + FP + FN)
   - Sensitivity = TP / (TP + FN)
   - Specificity = TN / (TN + FP)
   - F1 Score = 2 * (Precision * Recall) / (Precision + Recall)
6. Save metrics to: /workspace/results/non_tata_metrics.csv
"""

model = LiteLLMModel(model_id="gpt-4o-mini-2024-07-18", api_key=api_key, temperature=0.4)
agent = CodeAgent(
    tools=[],
    model=model,
    add_base_tools=False,
    additional_authorized_imports=["*"],
    max_steps=5,
)

task = "Design and implement initial validation steps for DNA sequence classification."

agent.run(prompt_context + "\n\nTask: " + task)