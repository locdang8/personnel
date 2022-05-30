# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Department(models.Model):
    _name = 'department.class'
    _description = 'department'
    _rec_name = "fullname"
    fullname = fields.Char(string='Tên')
    phone_number = fields.Char(string='Điện thoại')
    address = fields.Text(string='Địa chỉ')
    person_id = fields.One2many('personnel_type.class','department_id',string="Danh sach nhan vien",
                                 groups="nhansu.group_department_admin")
    department_count = fields.Integer(string="Tong", compute="_get_count",readonly=True)
    person_count = fields.Integer(string="Tong", compute="_get_person")
    
    def create_record(self):
        self.env['department.class'].name_create([{'name':'Loc'},{'name':'sd'}])
    
    def _get_count(self):
        depart = self.search_count([])
        self.department_count=depart
    
    def _get_person(self):
        self.person_count=len(self.mapped('person_id'))
            
    def action_count_number(self):
        print('Test')
        
    def action_cout_person(self):
        print('Test')