# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Level(models.Model):
    _name = 'level.class'
    _description = 'level education'

    name = fields.Char(string='Tên')
    detail = fields.Html(string='Mô tả')
    person_type_id = fields.One2many('personnel_type.class','level_id',string="Nhân viên")
    count_p = fields.Integer(string="tong", compute="_set_person_count")
    # def _set_person_count(self):
    #     for re in self:
    #         cout_p = self.env['level.class'].search([('person_type_id','!=','')])
    #         re.count_p = cout_p
    #
    # def action_count_number(self):
    #     print('Test')