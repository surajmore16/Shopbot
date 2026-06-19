from ragas import evaluate
from ragas.metrics import faithfulness, context_precision
from datasets import Dataset
from dotenv import load_dotenv

from evaluation.test_cases import TEST_CASES
from src.retriever import retrieve
from src.prompt import answer

load_dotenv()


def build_evaluation_dataset() -> Dataset:
    rows = []

    for case in TEST_CASES:
        evidence = retrieve(case["query"])

        contexts = [e["text"] for e in evidence] if evidence else [""]

        generated = answer(case["query"])

        rows.append(
            {
                "question": case["query"],
                "answer": generated,
                "contexts": contexts,
                "ground_truth": case["expected_answer"],
            }
        )

    return Dataset.from_list(rows)


dataset = build_evaluation_dataset()

result = evaluate(
    dataset,
    metrics=[
        faithfulness,
        context_precision,
)

print("\n--- ShopBot Evaluation — Book 1 Baseline ---")
print(f"Faithfulness: {result['faithfulness']:.2f}")
print(f"Context Precision: {result['context_precision']:.2f}")
print("--------------------------------------------")