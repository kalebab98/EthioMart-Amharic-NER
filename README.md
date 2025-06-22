# 🧩 Task 1: Data Ingestion & Preprocessing

> Collecting and preparing Amharic e-commerce messages from Telegram channels for NER tasks.

---

## 🚀 Objective

This task sets up the full pipeline to:

- 🔌 Connect to Ethiopian Telegram e-commerce channels.
- 📥 Scrape messages, metadata, and images.
- 🧹 Clean and tokenize Amharic text.
- 💾 Save structured data in CSV format for further analysis and annotation.

---

## 📁 Files Included

 Description                                  |
----------------------------------------------|
 Scraper using Telethon to collect Telegram data (text + images). |
 Preprocessing script (cleaning + tokenization). |
 Raw data collected from Telegram channels.   |
 Cleaned and tokenized Amharic text.   |

---

## 🔗 Telegram Channels Scraped

- `@Shageronlinestore`
- `@ZemenExpress`
- `@nevacomputer`
- `@Fashiontera`
- `@aradabrand2`
- `@Shewabrand`

---

## 🔧 Setup Instructions

```bash
pip install telethon pandas
