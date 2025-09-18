import pandas as pd

def load_pair_files(complex_path, simplified_path):
    with open(complex_path, "r", encoding="utf-8") as f_complex, \
         open(simplified_path, "r", encoding="utf-8") as f_simplified:
        complex_sentences = f_complex.readlines()
        simplified_sentences = f_simplified.readlines()

    return pd.DataFrame({
        "complex_sentence": [line.strip() for line in complex_sentences],
        "simplified_sentence": [line.strip() for line in simplified_sentences]
    })
