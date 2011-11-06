#FlaskCanOpener

**FlaskCanOpener is a web interface for installing and managing application
installed by CannedZen. The goal of the project is to have an easy way to remotely
monitor, deploy, and interact with a server solely through the web interface.**

## How get started

Install with CannedZen, then launch the server with `czmanage.py FlaskCanOpener run`.
If you want to immediatly launch the browser after running, execute `czmanage.py FlaskCanOpener hotStart`

## Interacting with CannedZen

FlaskCanOpener will automatically hook in and expose the available commands for
applications installed with CannedZen. It can install and uninstall individual
components as well as full deployments.