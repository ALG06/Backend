from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    google_oauth_client_id = fields.Char(
        string='Google OAuth Client ID',
        config_parameter='google_auth.client_id')
    google_oauth_client_secret = fields.Char(
        string='Google OAuth Client Secret',
        config_parameter='google_auth.client_secret')
