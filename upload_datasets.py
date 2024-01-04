from datasets import load_dataset

cats_vs_dogs    = load_dataset("imagefolder", data_dir="./cats-vs-dogs-imagefolder-dataset", drop_labels = False)

cats_vs_dogs    .push_to_hub("ajinkyakolhe112/cats_vs_dogs_classification")