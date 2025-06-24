# 📦 **EthioMart Amharic NER System**

**EthioMart** aims to become the central hub for Telegram-based e-commerce in Ethiopia by aggregating business data such as **product names**, **prices**, and **locations** from multiple independent vendor channels.  
This project builds an **Amharic Named Entity Recognition (NER)** system to extract and structure such data for downstream analytics and business decision-making.

---

## 🔍 **Project Overview**

With the growing use of **Telegram for commerce in Ethiopia**, vendors are scattered across isolated channels. This project solves the **fragmentation problem** by:

- 🔄 **Scraping** real-time messages and media from Telegram vendor channels  
- 🧹 **Preprocessing** Amharic text using custom tokenization and normalization  
- 🏷️ **Labeling** key entities in Amharic: `Product`, `Price`, `Location`  
- 🤖 **Fine-tuning transformer-based models**: `XLM-RoBERTa`, `mBERT`, `AfroXLMR`  
- 📊 **Generating vendor analytics** to support micro-lending decisions  

---

## 📁 **Project Structure**

```bash
ethiomart-amharic-ner/
│
├── data/
│   ├── raw/                      # Raw scraped data
│   └── processed/                # Cleaned and labeled datasets
│       ├── amharic_ner_data.conll
│       
├── notebooks/
│   └── 01_data_ingestion.ipynb   # Telegram scraping logic
│    └── Task-3NERmodel.ipynb
│   └── task-4a.ipynb
│   └──Task-5a.ipynb
│   └──Task-6a.ipynb
│
├── scripts/
│   └── 01_text_preprocessing.py  # Cleaning, normalization, tokenization
│
├── README.md
├── requirements.txt
└── .gitignore
```

# 📦 Amharic E-Commerce Data Extractor: Tasks 3–6

This repository contains the implementation of Tasks 3 through 6 of the **B5W4 Challenge – Amharic E-Commerce Data Extractor**, which focuses on fine-tuning transformer models for Amharic Named Entity Recognition (NER), comparing models, interpreting predictions, and building a FinTech-ready vendor analytics engine.

---

## ✅ Task 3: Fine-Tune NER Model (Amharic)

### Goal:
Train a transformer-based model (AfroXLMR) on annotated Amharic Telegram data to extract key business entities: **Product**, **Price**, and **Location**.

### Steps:
1. **Install Libraries**:
2. **Preprocessing**:
- Read CoNLL-formatted data (`amharic_ner_data.conll`)
- Encode labels and tokenize Amharic text using `AutoTokenizer`

3. **Model**:
- Pretrained: `Davlan/afro-xlmr-base`
- Fine-tuned using Hugging Face's `Trainer`

4. **Metrics**:
- Evaluation via `seqeval` (F1, precision, recall)

5. **Save Artifacts**:
- Trained model and tokenizer saved to `amharic_ner_final_model/`
- Compressed as `amharic_ner_model.zip` for deployment

---

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

---

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

---

## 📊 Task 6: Vendor Scorecard Engine

### Objective:
Score vendors based on engagement and business consistency using NER outputs + Telegram post metadata.

### Metrics:
- **Avg. Views per Post**
- **Posts per Week**
- **Avg. Product Price (ETB)**
- **Top Product by Views**

