# from simple_image_download import simple_image_download as simp

# response = simp.simple_image_download

# keywords = ["building workers"]

# for kw in keywords:
#     response().download(kw,200)

from bing_image_downloader.downloader import download

query_string = "ảnh cccd"
output_dir = r"F:\AI\datasets\cccd_datasets\cccd_dataset_v_3"

download(
    query_string,
    limit=100,
    output_dir=output_dir,
    adult_filter_off=True,
    force_replace=False,
    timeout=60,
    verbose=True,
)
