import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure output folders exist
os.makedirs("figures", exist_ok=True)
os.makedirs("tables", exist_ok=True)

def generate_outputs():

    # Load feature store data
    df = pd.read_csv("feature_store_dataset_cleaned.csv")

    # ============================
    # RQ1
    # Does user activity drive purchasing?
    # ============================

    plt.figure()
    plt.scatter(df["sessions_30d"], df["purchases_30d"])
    plt.xlabel("Sessions in last 30 days")
    plt.ylabel("Purchases in last 30 days")
    plt.title("RQ1: User Activity vs Purchases")
    plt.tight_layout()
    plt.savefig("figures/RQ1_Fig1.pdf")
    plt.close()

    rq1_table = df.groupby("is_premium")[["total_spent_30d", "purchases_30d"]].mean()
    rq1_table.to_excel("tables/RQ1_Table1.xlsx")

    # ============================
    # RQ2
    # Does order value explain spending?
    # ============================

    plt.figure()
    plt.scatter(df["avg_order_value_30d"], df["total_spent_30d"])
    plt.xlabel("Average Order Value (30d)")
    plt.ylabel("Total Spent (30d)")
    plt.title("RQ2: Order Value vs Total Spending")
    plt.tight_layout()
    plt.savefig("figures/RQ2_Fig1.pdf")
    plt.close()

    rq2_table = df.groupby("has_saved_card")[["total_spent_30d"]].mean()
    rq2_table.to_excel("tables/RQ2_Table1.xlsx")

    # ============================
    # RQ3
    # Do support issues reduce future purchases?
    # ============================

    plt.figure()
    plt.scatter(df["support_tickets_30d"], df["will_purchase_7d"])
    plt.xlabel("Support Tickets (30d)")
    plt.ylabel("Will Purchase in Next 7 Days")
    plt.title("RQ3: Support Issues vs Purchase Probability")
    plt.tight_layout()
    plt.savefig("figures/RQ3_Fig1.pdf")
    plt.close()

    rq3_table = df.groupby("support_tickets_30d")[["will_purchase_7d"]].mean()
    rq3_table.to_excel("tables/RQ3_Table1.xlsx")

    print("All figures and tables generated successfully.")

if __name__ == "__main__":
    generate_outputs()
