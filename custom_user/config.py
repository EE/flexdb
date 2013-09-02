app_name = "custom_user"
prefix_url = "custom_user"
static_files = {
    'js': {
        'custom_user/js/': ['main.js', ]
    },
    'css': {
        'custom_user/css/': ['main.css', ]
    },
    'html': {
        '': []
    }
}
permissions = {
    "edit": "Editing other users data.",
    "permissions": "Changing permissions of users.",
}
