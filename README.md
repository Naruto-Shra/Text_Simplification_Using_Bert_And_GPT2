# Text_Simplification_Using_Bert_And_GPT2
This project implements a **Text Simplification Model** using a **BERT Encoder** and **GPT-2 Decoder** with Hugging Face’s `transformers` library.  
It takes a complex sentence as input and generates a simplified version of it.

text-simplification/
│
├── data/ # Dataset files
│ ├── src_train.txt # Complex sentences
│ ├── tgt_train.txt # Simplified sentences
│
├── src/ # Core source code
│ ├── init.py
│ ├── data_loader.py # Dataset loading
│ ├── dataset_split.py # Train/Val/Test split
│ ├── tokenization.py # Tokenization logic
│ ├── model_setup.py # Model and tokenizer setup
│ ├── train.py # (Optional) training loop
│ ├── evaluate.py # (Optional) evaluation
│
├── notebooks/
│ ├── model.ipynb # Original Jupyter notebook
│
├── main.py # Orchestrates full pipeline
├── requirements.txt # Dependencies
└── README.md # Project documentation
