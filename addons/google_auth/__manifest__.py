{
    'name': 'Google OAuth2 Authentication',
    'version': '1.0',
    'category': 'Authentication',
    'summary': 'Google SSO Authentication',
    'depends': ['auth_oauth', 'base'],
    'data': [
        'data/auth_oauth_data.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': True,
}
