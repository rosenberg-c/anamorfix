""" Command line utility to desqueeze anamorphic images from a given folder, and using stretch ratio. """

import os

from anamorfix.process_file import desqueeze_img


def desqueeze_images_in_folder(img_path: str, stretch_ratio: float):
    """ Create a `dst` folder in specified path, and place dequeezed images in it. """

    dst_path = os.path.join(img_path, "dst")
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)

    for filename in os.listdir(img_path):
        file_path = os.path.join(img_path, filename)

        if filename.startswith("."):  # Skip dot files, for example macOS creates .DS_Store files within directories.
            continue

        if not os.path.isfile(file_path):
            continue

        desqueeze_img(file_path=file_path, dst_path=dst_path, filename=filename, stretch_ratio=stretch_ratio, dry=False)
