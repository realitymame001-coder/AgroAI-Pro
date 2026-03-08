import kaggle

kaggle.api.dataset_download_files(
    "emmarex/plantdisease",
    path="dataset",
    unzip=True
)
