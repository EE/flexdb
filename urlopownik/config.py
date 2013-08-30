app_name = "urlopownik"
prefix_url = "urlopownik"

static_files = {
    'js': {
        'urlopownik/js/': ['main.js', ]
    },
    'css': {
        'urlopownik/css/': ['main.css', ]
    },
    'html': {
        'urlopownik/html/': ['index.html', ]
    }
}

permissions = {
    "add": "Add requests and see status of it.",
    "accept": "Accept and see requests.",
}
