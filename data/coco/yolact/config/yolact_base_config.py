# Import necessary classes and constants
from data.config import Config
from data import COCO_LABEL_MAP  # Import or define your label map

from yolact.data import dataset_base

# Define your class names for your dataset
# Define your class names for your dataset
YOUR_DATASET_CLASSES = ["Ali", "Obaid", "John", "Sun", "Arraya", "Zain", "Sara", "Zubair", "qewer", "Power"]

# Create a new dataset configuration for your dataset
your_dataset = dataset_base.copy({
    'name': 'Your Dataset Name',

    # Training images and annotations
    'train_images': '/coco/train2017/',
    'train_info': '/coco/train_dataset.json',  # Update with your annotation file

    # Validation images and annotations.
    'valid_images': '/coco/valid2017/',
    'valid_info': '/coco/valid_dataset.json',  # Update with your annotation file

    # Whether or not to load GT. 55555555555If this is False, eval.py quantitative evaluation won't work.
    'has_gt': True,

    # Update with your class names
    'class_names': YOUR_DATASET_CLASSES,

    # If your label IDs are not sequential, provide a label map (category_id -> index in class_names + 1)
    # Otherwise, you can omit this line or set it to None
    'label_map': None
})


# Replace the dataset configuration in the config dictionary
cfg = {
    'dataset_base': dataset_base,
    'dataset': your_dataset,  # Replace 'your_dataset' with the name you want to use
    # ...
    # Other configuration options
    # ...
}
