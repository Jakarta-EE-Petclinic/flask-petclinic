from database import app, run_run_with_debug, port

import flask_petclinic.application_views


def run_web():
    app.logger.info(" ")
    app.logger.info("#############################################################")
    app.logger.info("#                  ^Petclinic - WEB                         #")
    app.logger.info("#############################################################")
    app.logger.info(" ")
    app.run(debug=run_run_with_debug, port=port)

