########
import sys
import os
sys.path.append("/home/kyle/CZ")
#######

from FlaskCanOpener import app
from cannedBlueprints import BlueprintList


for module in BlueprintList:
    print "Adding Blueprint... %s in %s" % (module.__name__.split('.')[-1], __name__)
    app.register_blueprint(module.blueprint_control, url_prefix = '/%s' % (module.url_prefix))
    
app.run('0.0.0.0', debug=True)
