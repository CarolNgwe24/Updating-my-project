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
