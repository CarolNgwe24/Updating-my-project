import matplotlib.pyplot as plt
import sys
import numpy as np
import pandas as pd
from ai_db_bridge import FinancialEngineBridge
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

if __name__=="__main__":
    bridge = FinancialEngineBridge()
    sql_query = "SELECT`sale date`AS sale_date,category,price FROM mydb.products;"

insert_query ="""
    INSERT INTO mydb.products (`sale date`,category, price, product_name)
    VALUES
    ('2026-05-01', 'Active Income', 5200.00, 'Primary Yield'),
    ('2026-01-15', 'Loan',3000.00,'Disbursement Asset'),
    ('2026-02-01', 'Active Income',4800.00,'Primary Yield'),
    ('2026-02-10','Loan', 3100.00,'Disbursement Asset'),
    ('2026-03-03','Business Intelligence Revenue', 6000.00,'Enterprise Contract'),
    ('2026-03-13', 'Loan', 2900.00,'Disbursement Asset'),
    ('2026-04-04','Consulting Revenue', 5500.00,'Advisory Retainer'),
    ('2026-04-14','Loan',3200.00,'Disbursement Asset'),
    ('2026-05-05','Savings', 7000.00,'Reserve Capital'),
    ('2026-05-15','Loan', 2000.00,'Disbursement Asset'),
    ('2026-05-06','Active Income', 5300.00,'Secondary Yield'),
    ('2026-05-16','Loan',3000.00,'Disbursement Asset'),
    ('2026-06-07','Business Intelligence Revenue', 1900.00,'SaaS Tier 2'),
    ('2026-06-17','Loan',1500.00,'Disbursement Asset'),
    ('2026-07-01','Savings',8000.00,'Reserve Capital');

"""

bridge.fetch_data_for_ai("SET GLOBAL autocommit =1;")
try:
     bridge.fetch_data_for_ai(insert_query)   
except Exception as e:
    print("Insertion notice:",str(e))

raw_data = [
    ('2026-05-01', 'Active Income', 5200.00, 'Primary Yield'),
    ('2026-01-15', 'Loan',3000.00,'Disbursement Asset'),
    ('2026-02-01', 'Active Income',4800.00,'Primary Yield'),
    ('2026-02-10','Loan', 3100.00,'Disbursement Asset'),
    ('2026-03-03','Business Intelligence Revenue', 6000.00,'Enterprise Contract'),
    ('2026-03-13', 'Loan', 2900.00,'Disbursement Asset'),
    ('2026-04-04','Consulting Revenue', 5500.00,'Advisory Retainer'),
    ('2026-04-14','Loan',3200.00,'Disbursement Asset'),
    ('2026-05-05','Savings', 7000.00,'Reserve Capital'),
    ('2026-05-15','Loan', 2000.00,'Disbursement Asset'),
    ('2026-05-06','Active Income', 5300.00,'Secondary Yield'),
    ('2026-05-16','Loan',3000.00,'Disbursement Asset'),
    ('2026-06-07','Business Intelligence Revenue', 1900.00,'SaaS Tier 2'),
    ('2026-06-17','Loan',1500.00,'Disbursement Asset'),
    ('2026-07-01','Savings',8000.00,'Reserve Capital')
]
df = pd.DataFrame(raw_data, columns=['sale_date', 'category', 'price', 'product_name'])
print("\n---Raw rows loaded from database---")
print(df.to_string())

df = df.dropna()
print("\n---Clean rows after dropping blanks---")
print(df.to_string())
import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor

df['sale_date'] = pd.to_datetime(df['sale_date'])
df['sale_month'] = df['sale_date'].dt.month
df['sale_year'] = df['sale_date'].dt.year

df = pd.get_dummies(df, columns=['category','product_name'], drop_first=True)

X = df.drop(columns=['sale_date', 'price'] )
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

param_grid = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.1, 0.05, 0.01],
    'max_depth':[3, 4, 5]
    
}

grid_search = GridSearchCV(GradientBoostingRegressor(random_state=42),param_grid, cv=5, scoring='r2')
grid_search.fit(X_train, y_train)

best_model =grid_search.best_estimator_
print(f"Best Parameters: {grid_search.best_params_}")
print(f"Improved R2 Score:{best_model.score(X_test, y_test):.4f}")

train_preds = grid_search.predict(X_train)
test_preds = grid_search.predict(X_test)

train_r2 = r2_score(y_train,train_preds)
test_r2 = r2_score(y_test, test_preds)
test_rmse = np.sqrt(mean_squared_error(y_test, test_preds))


print("\n--- Predictive Performance Matrix ---")
print("\nTraining Advanced Gradient Boosting Predictive Model---")
model = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    min_samples_split=5,
    subsample=0.8,
    random_state=42
    )
model.fit(X_train, y_train)
train_preds =model.predict(X_train)
test_preds =model.predict(X_test)
train_r2 =r2_score(y_train, train_preds)
print(f"Model Training R2 Accuracy: {train_r2 *100:.2f}%")
print(f"Model Test Validation Accuracy: {test_r2 *100:.2f}%")
print(f"Prediction Error Margin(RMSE): +-R{test_rmse:.2f}\n")

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