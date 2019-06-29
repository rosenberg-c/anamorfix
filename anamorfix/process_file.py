""" Command line utility to desqueeze anamorphic images from a given folder, and using stretch ratio. """

import os
import sys

try:
    from PIL import Image
except ImportError:
    print('Error: Pillow doesn\'t seem installed.\nInstall it with: pip3 install Pillow')
    sys.exit(1)


def desqueeze_img(file_path, dst_path, filename, stretch_ratio, dry=True, silent=False):
    if not silent:
        print('Desqueezing %s at %.3fx' % (filename, stretch_ratio))

    img = Image.open(file_path)
    width, height = img.size
    new_img = img.resize((width, int(height * (1.0 / stretch_ratio))))

    dst_file_path = os.path.join(dst_path, filename)

    if not dry:
        new_img.save(dst_file_path)
