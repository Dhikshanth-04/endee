import pandas as pd
from endee_client import store_insight

def load_data():
    try:
        return pd.read_csv("data/company.csv")
    except:
        return pd.DataFrame({
            "name": ["Alice", "Bob", "Charlie"],
            "performance_score": [9, 6, 4]
        })


def get_best_employee():
    df = load_data()
    best = df.loc[df['performance_score'].idxmax()]

    insight = f"Best performer is {best['name']} with score {best['performance_score']}"
    status = store_insight(insight)

    return {
        "best_employee": best['name'],
        "score": int(best['performance_score']),
        "endee_status": status
    }


def get_underperformers():
    df = load_data()
    low = df[df['performance_score'] < 5]

    insight = f"Underperformers: {low['name'].tolist()}"
    status = store_insight(insight)

    return {
        "underperformers": low['name'].tolist(),
        "endee_status": status
    }


def get_strategy():
    df = load_data()
    avg = df['performance_score'].mean()

    if avg > 7:
        decision = "Expand business"
    elif avg > 5:
        decision = "Optimize performance"
    else:
        decision = "Restructure company"

    explanation = generate_explanation(avg, decision)

    insight = f"Strategy: {decision}, Avg Score: {avg}"
    status = store_insight(insight)

    return {
        "company_avg": round(avg, 2),
        "strategy": decision,
        "explanation": explanation,
        "endee_status": status
    }
def generate_explanation(avg, decision):
    if decision == "Expand business":
        return (
            "The company is performing at a high level overall. "
            "Most employees are exceeding expectations, indicating strong operational efficiency. "
            "This is an ideal time to scale operations, enter new markets, or increase investments."
        )

    elif decision == "Optimize performance":
        return (
            "The company shows moderate performance with room for improvement. "
            "Some employees are underperforming, which affects overall efficiency. "
            "Focusing on training, process improvements, and performance monitoring is recommended."
        )

    else:
        return (
            "The overall performance is below expectations. "
            "Multiple employees are underperforming, which may indicate structural or management issues. "
            "A restructuring strategy, including role reassignment or leadership changes, should be considered."
        )