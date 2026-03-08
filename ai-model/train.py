import torch
from dataset_loader import load_dataset
from model import AgroModel

loader, classes = load_dataset("dataset")
model = AgroModel(len(classes))

opt = torch.optim.Adam(model.parameters(), lr=1e-4)
loss_fn = torch.nn.CrossEntropyLoss()

for epoch in range(5):
    total = 0
    for img, label in loader:
        pred = model(img)
        loss = loss_fn(pred, label)
        opt.zero_grad()
        loss.backward()
        opt.step()
        total += loss.item()
    print("epoch", epoch, total)

torch.save(model.state_dict(), "agro_model.pth")
