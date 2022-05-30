# -*- coding: utf-8 -*-
from datetime import datetime, date
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Personnel(models.Model):
    _name = 'personnel.class'
    _description = 'personnel'
    
    gender = fields.Selection([('nam','Nam'),('nu','Nu')])
    
    def set_draft(self):
        self.state = "draft"

    def set_confirm(self):
        self.state = "confirm"               

    def set_done(self):
        self.state = "done"

    def set_cancel(self):
        self.state = "cancel"

    def _count_per(self):
        for re in self:
            count_person = self.env['personnel_type.class'].search_count([])
            re.count_person = count_person

    def action_person_count(self):
        print('ok')

    # def action_process_count(self):
    #     return { 
    #         'type':'ir.actions.act_window',
    #         'res_model':'process.class',
    #         'view_mode':'tree',
    #         }
    def custom_btn(self):
        rtn = self.env['personnel_type.class'].with_env().create({'name':'logger','phone_number':'7654','active':True})
        print('rtn....',rtn)
        return rtn
    