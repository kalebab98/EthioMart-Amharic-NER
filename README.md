## ✅ Task 3: Fine-Tune NER Model (Amharic)

### Goal:
Train a transformer-based model (AfroXLMR) on annotated Amharic Telegram data to extract key business entities: **Product**, **Price**, and **Location**.

### Steps:
1. **Install Libraries**:
2. 2. **Preprocessing**:
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
