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
│
├── scripts/
│   └── 01_text_preprocessing.py  # Cleaning, normalization, tokenization
│
├── README.md
├── requirements.txt
└── .gitignore
