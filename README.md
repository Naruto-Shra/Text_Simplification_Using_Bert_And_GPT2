# Text_Simplification_Using_Bert_And_GPT2
This project implements a **Text Simplification Model** using a **BERT Encoder** and **GPT-2 Decoder** with Hugging Face’s `transformers` library.  
It takes a complex sentence as input and generates a simplified version of it.

🔹 **Why BERT + GPT-2?**

This project uses a sequence-to-sequence (Seq2Seq) approach with:
BERT (Encoder): Learns deep contextual representations of the input (complex sentence).
GPT-2 (Decoder): Generates fluent and simplified output in natural language.
Together, this encoder-decoder architecture combines the understanding power of BERT with the generation capability of GPT-2.

🔹**Workflow**

Dataset Preparation
Parallel corpus of complex → simplified sentences.
Example:
Complex: "The physician prescribed the medication to alleviate the patient’s symptoms."
Simplified: "The doctor gave medicine to help the patient feel better."
Preprocessing & Tokenization
Convert sentences into token IDs for model training.
Align input (complex) and output (simplified) sequences.Model Training
The model minimizes cross-entropy loss between predicted and target simplified sentences.
Uses teacher forcing during training to stabilize learning.
Evaluation & Inference
On new text, the model encodes the complex sentence with BERT and generates simplified text using GPT-2.
