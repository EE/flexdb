import importlib


class ConfigException(Exception):
    def __init__(self, app_name):
        self.app_name = app_name

    def __unicode__(self):
        return self.app_name


class ImportException(ConfigException):
    def __unicode__(self):
        return "{} config could not be loaded.".format(self.app_name)


class ContentException(ConfigException):
    def __init__(self, app_name, reason):
        self.reason = reason
        super(ContentException, self).__init__(app_name)

    def __unicode__(self):
        return "{}: {}".format(self.app_name, self.reason)


class PermissionExeption(ConfigException):
    def __init__(self, app_name, perm):
        self.perm = perm
        super(PermissionExeption, self).__init__(app_name)

    def __unicode__(self):
        return "{} does not exist in {}".format(self.perm, self.app_name)


class Config(object):
    def __init__(self, app, mod):
        try:
            self.app_name = mod.app_name
            self.prefix_url = mod.prefix_url
            self.static_files = mod.static_files
            self.permissions = mod.permissions
        except AttributeError as e:
            raise ContentException(app, "{}".format(e))

    def has_permission(self, perm):
        return perm in self.permissions

    def js(self):
        js_list = []
        for prefix, suffixes in self.static_files['js'].iteritems():
            js_list += [prefix + suffix for suffix in suffixes]
        return js_list

    def css(self):
        css_list = []
        for prefix, suffixes in self.static_files['css'].iteritems():
            css_list += [prefix + suffix for suffix in suffixes]
        return css_list

    def templates(self):
        template_list = []
        for prefix, suffixes in self.static_files['html'].iteritems():
            template_list += [prefix + suffix for suffix in suffixes]
        return template_list


# trzeba gdzies wylistowac pola ktore musza byc w configu app
def get_config(app):
    try:
        mod = importlib.import_module(app + '.config')
    except ImportError:
        raise ImportException(app)

    return Config(app, mod)
