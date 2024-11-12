{
    'name': 'Google OAuth2 Authentication',
    'version': '1.0',
    'category': 'Authentication',
    'summary': 'Google SSO Authentication',
    'description': """
        This module provides Google OAuth2 authentication capabilities.
    """,
    'author': 'Your Name',
    'website': 'your-website.com',
    'license': 'LGPL-3',
    'depends': ['auth_oauth', 'base'],
    'data': [
        'data/auth_oauth_data.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}