import sys

from anamorfix.anamorfix import desqueeze_images_in_folder

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: anamorfix.py "C:\\Path\\To\\Images" <stretch-ratio>')
        sys.exit(1)
    desqueeze_images_in_folder(img_path=sys.argv[1], stretch_ratio=float(sys.argv[2]))
