from src.data_loader import load_pair_files
from src.dataset_split import split_dataset
from src.model_setup import get_model_and_tokenizers
from src.tokenization import tokenize_function
from datasets import Dataset, DatasetDict

def main():
    # Load dataset
    df = load_pair_files("data/src_train.txt", "data/tgt_train.txt")

    # Split dataset
    train_data, val_data, test_data = split_dataset(df)

    # Hugging Face DatasetDict
    dataset = DatasetDict({
        "train": Dataset.from_pandas(train_data),
        "validation": Dataset.from_pandas(val_data),
        "test": Dataset.from_pandas(test_data)
    })

    # Model + Tokenizers
    model, tokenizer, decoder_tokenizer = get_model_and_tokenizers()

    # Tokenize
    tokenized_datasets = dataset.map(
        lambda x: tokenize_function(x, tokenizer, decoder_tokenizer),
        batched=True
    )

    print("✅ Pipeline ready! Tokenized dataset size:", len(tokenized_datasets["train"]))

if __name__ == "__main__":
    main()
