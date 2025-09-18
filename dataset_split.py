from sklearn.model_selection import train_test_split

def split_dataset(df, test_size=0.2, val_size=0.5, random_state=42):
    train_data, temp_data = train_test_split(df, test_size=test_size, random_state=random_state)
    val_data, test_data = train_test_split(temp_data, test_size=val_size, random_state=random_state)
    return train_data, val_data, test_data
