from odoo import http
from odoo.http import request


class LoginAPI(http.Controller):

    @http.route('/test/login', type="json", auth="none")
    def login(self, db, email, password):
        request.session.authenticate(db, email, password)
        user_info = request.env['ir.http'].session_info()
        print(">>", user_info)
        vals = {
            "name": user_info['name'],
            "company": user_info['partner_display_name']
        }

        return {"status": 200, "message": "Login Success!", "respond": vals}

    @http.route('/test/info', type="json", auth="user", csrf=False)
    def get_user_info(self, **kw):
        partner_ids = request.env["res.partner"].search([])
        users = []
        for partner in partner_ids:
            name = partner['name']
            email = partner['email']
            id = partner['id']
            vals = {
                "id": id,
                "name": name,
                "email": email
            }
            users.append(vals)
        return {"message": "Partner Info", "partner counts": len(users), "respond": users}

    @http.route('/test/register', type="json", auth="public", csrf=False, cors="*")
    def user_register(self,email, name):
        new_user = request.env['res.partner'].sudo().create({"email": email , "name": name })
        print(new_user)
        respond = {
            "id": new_user.id,
            "name": new_user.name
        }
        return {"message" : "Register Success!", "respond": respond}



    @http.route('/test/update', type="json", auth="user", csrf=False, cors="*")
    def update_user(self, **kw):

        user_id = request.env.uid
        user = request.env['res.partner'].search([user_id])
        if user:
            user.write(kw)
        return {
            "message": "Update Success"
        }
