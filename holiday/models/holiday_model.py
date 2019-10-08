from odoo import api,fields,models

class Holiday(models.TransientModel):
    _name = "holiday.model"
    _description = "Send Well Wishes Emails to Customers"
    inherit_id = "web.external_layout"

    holiday_name = fields.Selection([("jamhuri","Jamhuri Day"),
                                     ("madaraka","Madaraka Day"),
                                     ("labor","Labor Day"),
                                     ("mashujaa","Mashujaa Day"),
                                     ("christmas","Christmas Day"),
                                     ("new_year","New Years Day"),
                                     ("easter","Easter")])
    customer_ids = fields.Many2many("res.partner",string="Customers")

    @property
    def datas(self):
        return dict(self._fields['holiday_name'].selection).get(self.holiday_name)

    @api.multi
    def reopen_form(self):
        self.ensure_one()
        return {'type': 'ir.actions.act_window', 'res_model': self.name, 'res_id': self.id, 'view_type': 'form',
                'view_mode': 'form', 'target': 'new'}

    @api.multi
    def print_report(self):
        self.ensure_one()
        context = {"docs":self.holiday_name}
        return {'type': 'ir.actions.report', 'report_name': 'holiday.report_holiday_template',
                'report_type': "qweb-html",'datas':self.datas}

    @api.multi
    def get_holiday_card(self):
        self.ensure_one()

        return {'type': 'ir.actions.act_window', 'res_model': self.name, 'res_id': self.id, 'view_type': 'form',
                'view_mode': 'form', 'target': 'new'}