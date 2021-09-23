from odoo.http import Controller, request, route


class Main(Controller):
    @route("/test_saas_build/get_db_name", auth="public")
    def get_db_name(self, **kw):
        return request.env.cr.dbname
