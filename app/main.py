""" import subprocess
import threading
import time
from dotenv import load_dotenv
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger=get_logger(__name__)

load_dotenv()

def run_backend():
    try:
        logger.info("starting backend service..")
        subprocess.run(["uvicorn" , "app.backend.api:app" , "--host" , "127.0.0.1" , "--port" , "9999"], check=True)
    except CustomException as e:
        logger.error("Problem with backend service")
        raise CustomException("Failed to start backend" , e)
    
def run_frontend():
    try:
        logger.info("Starting Frontend service")
        subprocess.run(["streamlit" , "run" , "app/frontend/ui.py"],check=True)
    except CustomException as e:
        logger.error("Problem with frontend service")
        raise CustomException("Failed to start frontend" , e)
    
if __name__=="__main__":
    try:
        threading.Thread(target=run_backend).start()
        time.sleep(2)
        run_frontend()
    
    except CustomException as e:
        logger.exception(f"CustomException occured : {str(e)}")


     """

""" 
import subprocess

import threading

import time

from dotenv import load_dotenv

from app.common.logger import get_logger

from app.common.custom_exception import CustomException



logger = get_logger(__name__)

load_dotenv()



def run_backend():

    try:

        logger.info("Starting backend service..")

        process = subprocess.Popen(

            [

                "uvicorn",

                "app.backend.api:app",

                "--host", "127.0.0.1",

                "--port", "9999",

                "--reload",              # reload helps debugging

                "--log-level", "debug"   # show detailed logs

            ],

            stdout=subprocess.PIPE,

            stderr=subprocess.PIPE,

            text=True

        )



        # Stream backend logs to console

        for line in process.stderr:

            print("BACKEND:", line, end="")



    except Exception as e:

        logger.error("Problem with backend service")

        raise CustomException("Failed to start backend", e)



def run_frontend():

    try:

        logger.info("Starting frontend service..")

        subprocess.run(

            ["streamlit", "run", "app/frontend/ui.py"],

            check=True

        )

    except Exception as e:

        logger.error("Problem with frontend service")

        raise CustomException("Failed to start frontend", e)



if __name__ == "__main__":

    try:

        threading.Thread(target=run_backend, daemon=True).start()

        time.sleep(2)

        run_frontend()

    except CustomException as e:

        logger.exception(f"CustomException occurred: {str(e)}")

 """


import subprocess
import threading
import time
from dotenv import load_dotenv
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
import sys

logger = get_logger(__name__)
load_dotenv()

backend_process = None

def run_backend():
    global backend_process
    try:
        logger.info("Starting backend service..")
        process = subprocess.Popen(
            [
                "uvicorn",
                "app.backend.api:app",
                "--host", "127.0.0.1",
                "--port", "9999",
                "--reload",              # reload helps debugging
                "--log-level", "debug"   # show detailed logs
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        backend_process = process

        # Stream backend logs to console
        for line in process.stderr:
            print("BACKEND:", line, end="")

    except Exception as e:
        logger.error("Problem with backend service")
        raise CustomException("Failed to start backend", e)

def run_frontend():
    try:
        logger.info("Starting frontend service..")
        subprocess.run(
            ["streamlit", "run", "app/frontend/ui.py"],
            check=True
        )
    except KeyboardInterrupt:
        print("Stopped by user.")
        if backend_process and backend_process.poll() is None:
            backend_process.terminate()
            backend_process.wait(timeout=5)  # Wait briefly for clean shutdown
        sys.exit(0)
    except Exception as e:
        logger.error("Problem with frontend service")
        if backend_process and backend_process.poll() is None:
            backend_process.terminate()
        raise CustomException("Failed to start frontend", e)

if __name__ == "__main__":
    try:
        threading.Thread(target=run_backend, daemon=True).start()
        time.sleep(2)
        run_frontend()
    except CustomException as e:
        logger.exception(f"CustomException occurred: {str(e)}")