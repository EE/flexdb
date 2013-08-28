import importlib


# trzeba gdzies wylistowac pola ktore musza byc w configu app
def get_settings(app):  # get_config ?
    try:
        mod = importlib.import_module(app + '.config')
    except ImportError:
        return None
    config = {
        'app_name': mod.app_name,
        'prefix_url': mod.prefix_url,
        'template_path': mod.template_path,
        'static_files': mod.static_files,
        'permissions ': mod.permissions,
    }
    return config
