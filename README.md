## 🔍 Task 4: Model Comparison & Selection

### Models Compared:
- **AfroXLMR (XLM-R-based)** ✅
- **Multilingual BERT (mBERT)** ❌
- **DistilBERT Multilingual** ❌

### Observations:
| Model        | F1 Score | Precision | Recall | Notes                                  |
|--------------|----------|-----------|--------|----------------------------------------|
| AfroXLMR     | 1.0      | 1.0       | 1.0    | Best performance on all entity types   |
| mBERT        | Low      | Low       | Low    | Struggled with class imbalance         |
| DistilBERT   | Low      | Low       | Low    | Failed to detect many entities         |

### Decision:
**AfroXLMR** was selected for production due to its superior contextual understanding of Amharic and high classification performance.
