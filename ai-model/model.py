import torch
import torch.nn as nn
from torchvision import models

class AgroModel(nn.Module):
    def __init__(self, num_classes: int):
        super().__init__()
        self.model = models.efficientnet_b0(pretrained=True)
        in_f = self.model.classifier[1].in_features
        self.model.classifier[1] = nn.Linear(in_f, num_classes)

    def forward(self, x):
        return self.model(x)
