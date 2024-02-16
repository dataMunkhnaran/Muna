import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np
from ultralytics import YOLO
from util import classify, set_background
set_background('C:/Users/517-1/Downloads/Test/images.png')

# set title
st.title('Tooth classification')

# set header
st.header('Please upload tooth image')

# upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# load classifier
model = YOLO('C:/Users/517-1/Downloads/Test/best.pt')

# load class names

class_names = ['A1', 'S', 'Q', 'E', 'C0', 'C1', 'C2', 'C3', 'C4', 'Ca', 'F', 'F1', 'H', 'P', 'Pq', 'R']

# Open the file and read lines
with open('C:/Users/517-1/Downloads/Test/labels.txt', 'r') as f:
    for line in f.readlines():
        # Strip whitespace and split the line by space
        parts = line.strip().split(' ')
        # Check if the line has at least two parts
        if len(parts) >= 2:
            # Add the second part (index 1) to the class names list
            class_names.append(parts[1])
        else:
            # If the line doesn't have the expected format, skip it
            print(f"Ignoring line: {line.strip()}")

# Close the file
f.close()


# display image
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)

    # classify image
    class_name, conf_score = classify(image, model, class_names)

    # write classification
    st.write("## {}".format(class_name))
    st.write("### score: {}%".format(int(conf_score * 1000) / 10))
