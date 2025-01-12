import os


def get_file_names(folder_path):
    # Liste pour stocker les noms de fichiers sans extension .csv
    file_names = []
    
    # Parcours de tous les éléments dans le dossier
    for file_name in os.listdir(folder_path):
        # Vérifie si l'élément est un fichier
        if os.path.isfile(os.path.join(folder_path, file_name)):
            # Ignorer les fichiers commençant par ".git"
            if file_name.startswith(".git"):
                continue
            if file_name.endswith(".xlsx"):
                file_name = file_name[:-5]  # Retire les 4 derniers caractères (".xlsx")
            if file_name.startswith("_"):
                file_name = file_name[1:]
            file_names.append(file_name)
    
    return file_names
