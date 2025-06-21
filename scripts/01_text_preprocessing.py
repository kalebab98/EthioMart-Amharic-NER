import pandas as pd
import re

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    # Remove emojis and special chars except Amharic Unicode (Ethiopic block)
    text = re.sub(r'[^\w\s\u1200-\u137F።፣፤፥፦፧፨]', '', text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def amharic_tokenizer(text):
    # Replace some punctuation with spaces (optional)
    text = text.replace('።', ' ').replace('፣', ' ')
    # Tokenize based on Amharic characters and numbers
    tokens = re.findall(r'[\u1200-\u137F]+|\d+', text)
    return tokens

# Load your scraped CSV
df = pd.read_csv('telegram_data.csv')

# Clean the messages
df['cleaned_message'] = df['Message'].apply(clean_text)

# Tokenize cleaned messages
df['tokens'] = df['cleaned_message'].apply(amharic_tokenizer)

# Join tokens back into a string (optional)
df['tokenized_message'] = df['tokens'].apply(lambda x: ' '.join(x))

# Optionally filter out rows with empty cleaned messages
df_cleaned = df[df['tokenized_message'] != '']

# Save to a new CSV
df_cleaned.to_csv('telegram_data_cleaned.csv', index=False)

print("Preprocessing complete. Cleaned data saved as telegram_data_cleaned.csv")
