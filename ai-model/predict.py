import torch
from PIL import Image
from torchvision import transforms
from model import AgroModel

classes = ["healthy","early_blight","late_blight"]

model = AgroModel(len(classes))
model.load_state_dict(torch.load("agro_model.pth", map_location="cpu"))
model.eval()

tfm = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

def predict(path):
    img = Image.open(path)
    x = tfm(img).unsqueeze(0)
    with torch.no_grad():
        out = model(x)
    idx = out.argmax(dim=1).item()
    return classes[idx]
