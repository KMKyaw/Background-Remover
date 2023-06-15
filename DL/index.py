import torch
import torchvision.transforms as T
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2.data import MetadataCatalog
from PIL import Image

cfg = get_cfg()
cfg.MODEL.DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
# Path to the model's config file
cfg.merge_from_file("./detectron2/configs/Base-RCNN-C4.yaml")
# Set the threshold for segment prediction
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
# Path to the model's weights file
cfg.MODEL.WEIGHTS = "path/to/model_weights.pth"
predictor = DefaultPredictor(cfg)
