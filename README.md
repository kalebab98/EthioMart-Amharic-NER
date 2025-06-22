
---

## 🏷️ `task-2` Branch — `README.md`

```markdown
# 🏷️ Task 2: Amharic NER Annotation (CoNLL Format)

> Manually labeling key business entities from Telegram-based e-commerce text in Amharic.

---

## 🎯 Goal

Create a high-quality **CoNLL-formatted dataset** for fine-tuning NER models by identifying:

- 🛍️ Products
- 💵 Prices
- 📍 Locations

---

## 📁 Files Included

| File                     | Description                             |
|--------------------------|-----------------------------------------|
| `amharic_ner_data.conll` | Labeled Amharic messages in CoNLL format |
| `label_examples.txt`     | Sample annotated messages for reference |

---

## 🧠 Entity Types

| Tag        | Meaning                                 |
|------------|-----------------------------------------|
| `B-Product` | Beginning of a product name             |
| `I-Product` | Inside a product name                   |
| `B-PRICE`   | Beginning of a price                    |
| `I-PRICE`   | Inside a price                          |
| `B-LOC`     | Beginning of a location                 |
| `I-LOC`     | Inside a location                       |
| `O`         | Not part of any named entity            |

---

## ✍️ Sample Annotation (CoNLL)

```text
የሕፃናት   B-Product
መጠጫ     I-Product
ዋጋ፦     B-PRICE
3000     I-PRICE

አዲስ     B-LOC
አበባ     I-LOC
