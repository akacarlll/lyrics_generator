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
            # Supprime l'extension .csv si elle est présente
            if file_name.endswith(".xlsx"):
                file_name = file_name[:-5]  # Retire les 4 derniers caractères (".xlsx")
            # Remplace les espaces par des underscores
            # file_name = file_name.replace(" ", "_")
            # file_name = file_name.replace("'", "")
            # Ajoute le nom de fichier transformé à la liste
            file_names.append(file_name)
    
    return file_names
