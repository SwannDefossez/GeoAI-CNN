import os
import shutil

def delete_subfolders_for_countries(folder_path, countries_to_delete):
  
    folder_path = os.path.abspath(folder_path)
    
    
    deleted_count = 0
    
    
    with os.scandir(folder_path) as entries:
        for entry in entries:
            if entry.is_dir() and entry.name in countries_to_delete:
            
                shutil.rmtree(entry.path)
                print(f"Supprimé: {entry.name}")
                deleted_count += 1
                
    print(f"Total de dossiers supprimés dans {folder_path}: {deleted_count}")


countries_to_delete = ['AO', 'AZ', 'BA', 'BH', 'BJ', 'BN', 'BY', 'BZ', 'CD', 'CI', 'CM', 'CN', 'CU', 'CY', 'DZ', 
                       'EG', 'ET', 'FO', 'GE', 'GN', 'GP', 'HK', 'HN', 'HT', 'IN', 'IQ', 'IR', 'KW', 'KZ', 'LA', 
                       'LB', 'LC', 'LR', 'MG', 'ML', 'MM', 'MQ', 'MU', 'MZ', 'NI', 'NP', 'OM', 'PG', 'PK', 'QA', 
                       'RE', 'RW', 'SL', 'SV', 'TG', 'TJ', 'TL', 'TM', 'TN', 'TT', 'UZ', 'VN', 'XK', 'ZM']

folders = ['sorted_by_country_train', 'sorted_by_country_test']

for folder in folders:
    delete_subfolders_for_countries(folder, countries_to_delete)
