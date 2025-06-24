## 🧠 Task 5: Model Interpretability

### Tools Used:
- **SHAP (SHapley Additive exPlanations)**
- **LIME (Local Interpretable Model-Agnostic Explanations)**

### Insights:
- High SHAP values on key tokens like prices (`3000 ብር`) and locations (`አዲስ አበባ`)
- LIME validated predictions for B-PRICE and B-LOC tags
- Function words and punctuation had little impact — as expected

### Challenges Identified:
- Confusion with rare or ambiguous terms
- Overprediction of the "O" (non-entity) class by smaller models
