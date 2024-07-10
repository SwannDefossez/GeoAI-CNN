import csv
import os
import shutil


csv_path = 'train.csv'  

images_folder = 'extracted_images_train' 

sorted_folder = 'sorted_by_country_train'
os.makedirs(sorted_folder, exist_ok=True)


id_to_country = {}


with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        id_to_country[row['id']] = row['country']


for image_file in os.listdir(images_folder):
  
    image_id = os.path.splitext(image_file)[0]
    if image_id in id_to_country:
        country_label = id_to_country[image_id]  
        source_path = os.path.join(images_folder, image_file)
        country_folder = os.path.join(sorted_folder, country_label)
        os.makedirs(country_folder, exist_ok=True)
        destination_path = os.path.join(country_folder, image_file)
        shutil.move(source_path, destination_path)
    else:
        print(f"ID non trouvé pour l'image: {image_file}")

print("Images classées par label de pays.")
