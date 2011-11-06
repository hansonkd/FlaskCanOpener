from flask import Blueprint, render_template, abort, redirect, url_for, jsonify

from CannedZen import GlobalSettings
GlobalSettings.reconfigure( installPath = "/home/kyle/czinstall/bin/")

from CannedZen import Admin
from FlaskCanOpener.Utils import generateBlueprintCtx

url_prefix = "control"
blueprint_control = Blueprint('generic_controller', __name__, **generateBlueprintCtx(__file__))

commandLog = {}

@blueprint_control.route('/')
def listPackages():
        ctx = {'packages': Admin.getStates()}
        return render_template('listAvailable.html', **ctx)

@blueprint_control.route('/app/', defaults={'app': ''})
@blueprint_control.route('/app/<app>')
def getControlsForApp(app):
    if not app:
        return redirect(url_for('generic_controller.listPackages'))
    ctx = {'commands': Admin.getCommands()[app], 'app': app}
    return render_template('appCommands.html', **ctx)


@blueprint_control.route('/command/', defaults={'app': '', 'command': ''})
@blueprint_control.route('/command/<app>/<command>')
def doCommand(app, command):
    if not app:
        return redirect(url_for('generic_controller.listPackages'))
    elif not command:
        return redirect(url_for('generic_controller.getControlsForApp', app = app))
    engine = Admin.getEngine(app)
    commandFunc = getattr(engine, command)
    commandLog["%s.%s" % (app, command)] = commandFunc()
    ctx = {'commands': Admin.getCommands()[app], 'app': app, 'command': command}
    return render_template('executeCommand.html', **ctx)

@blueprint_control.route('/commandState/', defaults={'app': '', 'command': ''})
@blueprint_control.route('/commandState/<app>/<command>')
def getCommandState(app, command):
    if not app:
        return redirect(url_for('generic_controller.listPackages'))
    elif not command:
        return redirect(url_for('generic_controller.getControlsForApp', app = app))
    runningProcess = commandLog["%s.%s" % (app, command)]
    output = runningProcess.stdout.readline()
    if not output and runningProcess.poll() is None:
        output = "EndOfCommand"
    return jsonify({'commandOutput': output})