import pandas as pd
from transformers import GPT2Tokenizer

def tokenize_gpt2(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tokenizes lyrics for GPT-2 fine-tuning and adds columns for input IDs and attention masks.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the 'Lyrics' column to tokenize.

    Returns:
    - pd.DataFrame: The DataFrame with added columns 'input_ids' and 'attention_mask'.
    """
    # Drop rows with missing 'Lyrics'
    df = df.dropna(subset=["Lyrics"])
    
    # Ensure 'Lyrics' column exists
    if 'Lyrics' not in df.columns:
        raise ValueError("The DataFrame must contain a 'Lyrics' column.")
    
    # Load GPT-2 tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    
    # Set padding token to EOS token
    tokenizer.pad_token = tokenizer.eos_token
    
    # Batch tokenize lyrics
    tokenized = tokenizer.batch_encode_plus(
        df['Lyrics'].tolist(),
        max_length= 512,
        padding="max_length",
        truncation=True,
        return_tensors="pt"
    )
    
    # Add tokenized data to the DataFrame
    df['input_ids'] = tokenized['input_ids'].tolist()
    df['attention_mask'] = tokenized['attention_mask'].tolist()
    
    return df