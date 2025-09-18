def tokenize_function(examples, tokenizer, decoder_tokenizer, max_length=128):
    inputs = tokenizer(examples["complex_sentence"], truncation=True, padding="max_length", max_length=max_length)
    outputs = decoder_tokenizer(examples["simplified_sentence"], truncation=True, padding="max_length", max_length=max_length)
    inputs["labels"] = outputs["input_ids"]
    return inputs
