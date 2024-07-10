import os
import zipfile


zip_folder = "dataset/osv5m/images/train/"


extracted_folder = 'extracted_images_train'
os.makedirs(extracted_folder, exist_ok=True)

for zip_filename in os.listdir(zip_folder):
    if zip_filename.endswith('.zip'):
        zip_path = os.path.join(zip_folder, zip_filename)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
      
            for zip_info in zip_ref.infolist():
                if zip_info.filename[-1] == '/':
                    continue 
                zip_info.filename = os.path.basename(zip_info.filename) 
                zip_ref.extract(zip_info, extracted_folder)
       
        os.remove(zip_path)

print("Extraction et nettoyage terminés.")
