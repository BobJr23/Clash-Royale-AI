import os, random, shutil

src_img_dir = "my_dataset/images/train"
src_lbl_dir = "my_dataset/labels/train"

dst_img_dir = "my_dataset/images/val"
dst_lbl_dir = "my_dataset/labels/val"

os.makedirs(dst_img_dir, exist_ok=True)
os.makedirs(dst_lbl_dir, exist_ok=True)

all_imgs = [f for f in os.listdir(src_img_dir) if f.endswith(".jpg")]
val_size = int(0.1 * len(all_imgs))

val_imgs = random.sample(all_imgs, val_size)

for img in val_imgs:
    lbl = img.replace(".jpg", ".txt")
    shutil.move(os.path.join(src_img_dir, img), os.path.join(dst_img_dir, img))
    shutil.move(os.path.join(src_lbl_dir, lbl), os.path.join(dst_lbl_dir, lbl))
