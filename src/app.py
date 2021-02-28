import sys
import subprocess
import flask_petclinic
from flask_petclinic.application_service import app, run_app

# ---------------------------------------------------------------------------------
#  MAIN
# ---------------------------------------------------------------------------------

if __name__ == '__main__':
    run_app(app)
