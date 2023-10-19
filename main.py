#pip install super_gradients
import os
import shutil
import random
from tqdm.notebook import tqdm
from super_gradients.training import dataloaders
from super_gradients.training.dataloaders.dataloaders import coco_detection_yolo_format_train, coco_detection_yolo_format_val
import torch
from super_gradients.training import models
from super_gradients.training.losses import PPYoloELoss
from super_gradients.training.metrics import DetectionMetrics_050
from super_gradients.training.models.detection_models.pp_yolo_e import PPYoloEPostPredictionCallback

dataset_params = {
    'data_dir':'/kaggle/input/face-detection-dataset',
    'train_images_dir':'/kaggle/input/face-detection-dataset/images/train',
    'train_labels_dir':'/kaggle/input/face-detection-dataset/labels/train',
    'val_images_dir':'/kaggle/input/face-detection-dataset/images/val',
    'val_labels_dir':'/kaggle/input/face-detection-dataset/labels/val',
    'test_images_dir':'/kaggle/input/face-detection-dataset/images/val',
    'test_labels_dir':'/kaggle/input/face-detection-dataset/labels/val',
    'classes': ['face']    
}
MODEL_ARCH = 'yolo_nas_l'
DEVICE = 'cuda' if torch.cuda.is_available() else "cpu"
BATCH_SIZE = 8
MAX_EPOCHS = 20
CHECKPOINT_DIR = f'/kaggle/working/'
EXPERIMENT_NAME = f'yolo_nas_face'