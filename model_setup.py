from transformers import EncoderDecoderModel, AutoTokenizer

def get_model_and_tokenizers():
    model = EncoderDecoderModel.from_encoder_decoder_pretrained(
        "bert-base-uncased", "gpt2"
    )

    encoder_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    decoder_tokenizer = AutoTokenizer.from_pretrained("gpt2")
    
    decoder_tokenizer.pad_token = decoder_tokenizer.eos_token
    model.config.decoder_start_token_id = decoder_tokenizer.bos_token_id
    model.config.pad_token_id = decoder_tokenizer.pad_token_id
    
    return model, encoder_tokenizer, decoder_tokenizer
