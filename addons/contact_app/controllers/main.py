from odoo.http import request, route, Controller


class ContactApp(Controller):
    @route("/contact_app/standalone_app", auth="public",website=True)
    def standalone_app(self):
        return request.render(
            'contact_app.standalone_app',
            {
                'session_info': request.env['ir.http'].get_frontend_session_info(),
            }
        )
