# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Department(models.Model):
    _name = 'department.class'
    _description = 'department'
    name = fields.Char(string='Tên')
    phone_number = fields.Char(string='Điện thoại')
    address = fields.Text(string='Địa chỉ')
    person_id = fields.Many2many('personnel_type.class','person_type_db','personnel_type_id',string="Danh sach nhan vien")
    department_count = fields.Integer(string="Tong", compute="_get_count")
    def create_record(self):
        self.env['department.class'].create({'name':'Loc','phone_number':'123'})
        
    def _get_count(self):
        for re in self:
            depart = self.env['department.class'].search_count([])
            re.department_count=depart
    
    def action_count_number(self):
        print('Test')