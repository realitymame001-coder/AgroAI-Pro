def accuracy(preds, labels):
    correct = (preds.argmax(1) == labels).sum().item()
    return correct / len(labels)
