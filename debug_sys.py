__version__ = "2.4.1"
__authors__ = ["CUISSET Mattéo"]
#=============================== IMPORTS ZONE ===============================
from datetime import datetime
import os

#=============================== INIT ZONE ===============================
num_log = 0

#=============================== MAIN ZONE ===============================
def log(msg_type : str | list[str], msg_content : str, content_size_limit : int = 150, file : str = 'gaza')-> None:
    """
    Enregistre un message dans un fichier journal spécifié.
    
    Cette fonction ajoute une nouvelle entrée dans le fichier journal spécifié, 
    avec un numéro d'entrée, la date et l'heure actuelles, le type de message et 
    le contenu du message. Si le contenu du message dépasse la limite de taille 
    spécifiée, seuls les premiers caractères jusqu'à la limite sont enregistrés.
    
    Args:
        msg_type (str | list[str]): Le ou les types du message à enregistrer.
        msg_content (str): Le contenu du message à enregistrer.
        content_size_limit (int, optional): La limite de taille du contenu du message. 
                                            Par défaut, elle est fixée à 150 caractères.
        file (str, optional): Le nom du fichier journal dans lequel enregistrer le message. 
                              Par défaut, il est fixé à 'gaza.log'.
    
    Retourne:
        None
    """
    global num_log
    num_log += 1
    try:
        if isinstance(msg_type, list): msg_type = ' | '.join(msg_type)
        with open(f'{file}.log', 'a', encoding="UTF8") as file:
            file.write(f'({num_log}) : {datetime.now()} : {msg_type} : {msg_content[:content_size_limit]}\n')
    except Exception as e:
        with open(f'{file}.log', 'a', encoding="UTF8") as file:
            file.write(f'({num_log}) : {datetime.now()} : LOG_ERROR : {e}\n')

def clear_logs(file: str = 'gaza.log', archive: bool = True, saving_folder: str = None) -> bool:
    """
    Efface le contenu d'un fichier log et l'archive éventuellement dans un dossier spécifié.

    Paramètres :
    - file (str, facultatif) : Chemin d'accès complet du fichier log à effacer et à archiver.
        Par défaut, 'gaza.log'.
    - archive (bool, facultatif) : Si True, le fichier log sera archivé avant d'être effacé.
        Par défaut, True.
    - saving_folder (str, facultatif) : Chemin d'accès du dossier dans lequel l'archive du fichier log
        sera sauvegardée. Si aucun dossier n'est spécifié ou si le dossier n'existe pas, l'archive sera
        sauvegardée dans le même dossier que le fichier log d'origine.
        Par défaut, None.

    Retourne :
    - bool : True si le fichier log a été effacé et éventuellement archivé avec succès, False sinon.

    """
    if not file.endswith('.log'):
        file += '.log'

    try:
        if os.path.isfile(file):
            with open(file, 'r+') as log_file:
                logs = log_file.read()
                if archive:
                    archive_filename = f"{logs[6:16]}_{logs[17:25].replace(':', '')]}.log"
                    archive_path = os.path.join(saving_folder if saving_folder is not None and os.path.isdir(saving_folder) else os.path.dirname(file), archive_filename)
                    with open(archive_path, 'w') as archived_logs:
                        archived_logs.write(logs)
                log_file.seek(0)
                log_file.write('')
                log_file.truncate()
            return True
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return False