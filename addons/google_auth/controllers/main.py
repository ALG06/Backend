from odoo import http
from odoo.http import request
import json

class GoogleAuthController(http.Controller):
    @http.route('/api/auth/google', type='json', auth='none', methods=['POST'], csrf=False)
    def google_auth(self, **post):
        google_id = post.get('google_id')
        email = post.get('email')
        name = post.get('name')
        
        if not (google_id and email):
            return {'error': 'Missing required fields'}
            
        # Find or create user
        user = request.env['res.users'].sudo().search([
            ('oauth_uid', '=', google_id),
            ('oauth_provider_id', '=', request.env.ref('google_auth.provider_google').id)
        ], limit=1)
        
        if not user:
            # Create new user
            values = {
                'name': name,
                'login': email,
                'email': email,
                'oauth_uid': google_id,
                'oauth_provider_id': request.env.ref('google_auth.provider_google').id,
            }
            try:
                user = request.env['res.users'].sudo().create(values)
            except Exception as e:
                return {'error': str(e)}
        
        # Generate token
        token = request.env['auth.token'].sudo().generate_token(user.id)
        
        return {
            'token': token,
            'user_id': user.id,
            'name': user.name,
            'email': user.login,
        }