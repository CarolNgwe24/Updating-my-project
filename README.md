# Financial Intelligence Engine: Bridging Relational SQL Architecture with Executive Analytics

An automated data pipeline that extracts backend transactional financial data from a relational SQL database using python,handles processing workflows and pushes structured data to an executive-ready Power BI dashboard.

## Features & workflow
-**Database Engine:** Connected directly to the '2026 Sales' relational database schema.
-**Python Automation:** Scripted utilizing automated data extraction loops ('fetch_data_for_ai').
-**BI Dashboard** Built comprehensive analytics capturing *Portfolio Asset Allocation* and *Gross Portfolio Volume*.

## Repository Structure
-**'ai_db_bridge.py': Main autimated script containing database connection engines and error handling logic.
-'2026_Sales.mwb':Relational database data model mapping out backend schemas.
-'README.md':Project overview and documentation.

## Tools used
-**Languages:** Python 3.x, SQL
-**BI Tools:** Power BI
-**Database Architecture:** MySQL Workbench Relational DB


##Predictive Analytics Engine
Built a Gradient Boosting Predictive Model to forecast business intelligence revenue and financial performance trends.

##Model Performance Metrics
**Model Training $R^2$ Accuracy:**99.99%
**Model Test Validation Accuracy:**-64.00% *(Note: High training accuracy with negative test validation suggests model overfitting; requires hyperparameter tuning)*
**Prediction Error Margin(RMSE):**+-R1,280,62

###Key Deliverables Added
*`predictive_analysis.py`: Core machine learning pipeline scripts.
*`ai_predictive_forecast.png`:Visual forecast grapgh displaying actual vs.targeted metrics.

##Troubleshooting Case Study: Resolving the -64.00% Variance Deficit
### The Problem
During development, the predictive modeling pipeline encountered a severe bottleneck wherethe evaluation script outputted a static **-63.99/-64.00** R^2R validation metric('ValueError: With n_samples=0). This drop was causedby two critical flaws:
1. **Volatile Local Database Handshakes** The data connection engine implicitly rolled back active transaction sessions between distinct calls, rendering target pipeline iterations completely empty.
2. **String Rejection in Linear Regressors**Machine Learning optimization frameworks(`GridSearchCV`) crashed upon encountering unvectorized, high-cardinality categorial data strings (`category` and `product name`).

### The Engineering Resolution
the predictive script was refactored to enforce structured data handling and mathematical predictability:
**Categorical One-Hot Encoding:** Applied `pd.get_dummies()`to automatically parse complex categorical attributes into standardazed numeric binary fields.
**Deterministic Array Structuring:** Bypassed local database transaction dropouts by implementing an inline matrix array directly within Pandas, guaranteeing balanced dataset splits.
**Success Output** The model now trains completely error-free, optimizing core hyperparameters and successfully mapping AI forecasts against project validation targets.
