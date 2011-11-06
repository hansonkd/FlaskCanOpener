from flask import Flask, render_template
from systemBlueprints import BlueprintList

## Configuration ##


app = Flask(__name__)
app.config.from_object(__name__)


for module in BlueprintList:
    print "Adding Blueprint... %s in %s" % (module.__name__.split('.')[-1], __name__)
    app.register_blueprint(module.blueprint_control, url_prefix = "/%s" % module.url_prefix)
    
    
import FlaskCanOpener.views

if __name__ == "__main__":
    app.run('0.0.0.0', debug = True)