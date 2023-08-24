import logging
import os
from datetime import datetime

LOGFILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}" #Date and time of loggin

logs_path = os.path.join(os.getcwd(), "logs", LOGFILE)
os.makedirs(logs_path,exist_ok=True)

LOGSPATH = os.path.join(logs_path, LOGFILE)

logging.basicConfig(
    filename=LOGSPATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)

if __name__ == "__main__":
    logging.warning("Logging has started")
