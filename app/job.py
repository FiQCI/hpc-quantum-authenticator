import os
import time
from app.logger import create_logger


logger = create_logger()
def prune_expired_tokens():
    directory = "tokens"

    file_age_limit = 2 * 60 * 60  # 2 hours in seconds
    #file_age_limit = 60 # for testing purposes
    current_time = time.time()

    if os.path.exists(directory):
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                file_creation_time = os.stat(file_path).st_mtime        
                file_age = current_time - file_creation_time
        
                if file_age > file_age_limit:
                    os.remove(file_path)
                    logger.info("Deleted expired file {file}")
    else:
        pass





