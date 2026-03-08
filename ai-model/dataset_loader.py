from torchvision import datasets, transforms
from torch.utils.data import DataLoader

def load_dataset(path):
    tfm = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor()
    ])
    ds = datasets.ImageFolder(path, transform=tfm)
    dl = DataLoader(ds, batch_size=32, shuffle=True)
    return dl, ds.classes
