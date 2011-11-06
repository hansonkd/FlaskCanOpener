import os, imp


def generate_moduleList(init_file):
    dir = os.path.dirname(init_file)
    file_list = os.listdir(dir)
    ret = []
    for module in file_list:
        modulePath = os.path.join(dir, module)
        if module.startswith('__init__.py') or module.endswith('pyc'):
            continue
        f, filename, description = imp.find_module(module, 
                                           [dir])
        ret.append(imp.load_module(module[:-3], f, filename, description))
    return ret

def generateBlueprintCtx(file):
    dir = os.path.dirname(file)
    staticDir = os.path.join(dir, 'static')
    templateDir = os.path.join(dir, 'templates')
    return {'static_folder': staticDir, 'template_folder': templateDir}
    
    