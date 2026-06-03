import matplotlib.pyplot as plt
import sys
import numpy as np
import pandas as pd
from ai_db_bridge import FinancialEngineBridge
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

if __name__=="__main__":
    bridge = FinancialEngineBridge()
    sql_query = "SELECT`sale date`AS sale_date,category,price FROM mydb.products;"

insert_query ="""
    INSERT INTO mydb.products (sale date,category, price, product_name)
    VALUES
    ('2026-05-01', 'Active Income', 5000.00, 'Primary Yield'),
    ('2026-05-02','Loan', 3000.00,'Disbursement Asset'),
    ('2026-05-03','Business Intelligence Revenue', 1850.00,'Enterprise Contract'),
    ('2026-05-04','Consulting Revenue', 1200.00,'Advisory Retainer'),
    ('2026-05-05','Savings', 70.00,'Reserve Capital'),
    ('2026-05-06','Active Income', 4800.00,'Secondary Yield'),
    ('2026-05-07','Business Intelligence Revenue', 1900.00,'SaaS Tier 2');
"""
try:
     bridge.fetch_data_for_ai(insert_query)
     bridge.fetch_data_for_ai("COMMIT;")
except Exception as e:
    print("Insertion notice",str(e))

try:
     raw_data = bridge.fetch_data_for_ai(sql_query)
     df =pd.DataFrame(raw_data, columns=['sale_date','category','price'])
except Exception as e:
     print(f"Error fetching data: {e}")
     sys.exit(1)

print("\n---Raw rows loaded from database---")
print(df.to_string())

df = df.dropna()
print("\n---Clean rows after dropping blanks---")
print(df.to_string())

df = pd.get_dummies(df, columns=["category"],drop_first=True)

X = df.drop(columns=["sale_date", "price"])
y = df["price"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)


print("\nTraining Advanced Gradient Boosting Predictive Model...")
model = LinearRegression()
model.fit(X_train, y_train)

cat_col=[col for col in df.columns if 'category' in col.lower()][0]
df = pd.get_dummies(df, columns=[cat_col],drop_first=True)

X = df.drop(columns=["sale_date","price"])
y = df["price"]


train_preds = model.predict(X_train)
test_preds = model.predict(X_test)

train_r2 = r2_score(y_train,train_preds)
test_r2 = r2_score(y_test, test_preds)
test_rmse = np.sqrt(mean_squared_error(y_test, test_preds))


print("\n--- Predictive Performance Matrix ---")
print(f"Model Training R2 Accuracy: {train_r2 *100:.2f}%")
print(f"Model Test Validation Accuracy: {test_r2 *100:.2f}%")
print(f"Prediction Error Margin(RMSE): +-${test_rmse:.2f}\n")

import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
df['sale_date'] =pd.to_datetime(df['sale_date'])
plt.bar(df['sale_date'].dt.strftime('%m-%d'), df['price'], color='#1f77b4', alpha=0.6, label='Actual Dashboard Value')

test_dates = df.loc[X_test.index,'sale_date'].dt.strftime('%m-%d')
plt.scatter(test_dates, test_preds, color='#d62728', s=100, zorder=5, label='AI Forecasted Target')

plt.title('Financial Intelligence Engine: AI Predictive Forecast Mapping',fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Execution Timeline (2026)',fontsize=11, labelpad=10)
plt.ylabel('Asset Price Matrix (ZAR)', fontsize=11, labelpad=10)
plt.grid(axis='y',linestyle='--', alpha=0.5)
plt.legend(frameon=True, facecolor='#f8f9fa', edgecolor='none')
plt.tight_layout()

plt.savefig('ai_predictive_forecast.png', dpi=300)
print("Success! Visual forecast graph saved as'ai_predictive_forecast.png'")
plt.show()

sys.exit(0)
if __name__== "__main__":
    bridge = FinancialEngineBridge()

    sql_query = "SELECT`sale_date`, category, price FROM mydb.products;"

    raw_data = bridge.fetch_data_for_ai(sql_query)
    df = pd.DataFrame(raw_data, columns=["sale_date","category","price"])
    run_advanced_predictive_analysis (df)