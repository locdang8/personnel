# -*- coding: utf-8 -*-
from datetime import datetime, date
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Personnel(models.Model):
    _name = 'personnel.class'
    _description = 'personnel'
    
    department_id = fields.Many2one('department.class', string='Phong ban')
    currency_id = fields.Many2one('res.currency', string="Loại tiền")
    process_id= fields.One2many('process.class','person_type_id', string='Các khóa học')
    
    img_ns =fields.Binary(string='Avatar')
    status = fields.Boolean(string='Trạng thái', help="Check nếu là nhân viên chính thức")
    name = fields.Char(string='Họ và tên', size=20)
    year_birth = fields.Date(string="Năm sinh")
    phone_number = fields.Char(string="Điện thoại")
    email = fields.Char(string="Email")
    date_start = fields.Date(string="Ngay bắt đầu", default=fields.Date.today())
    
    state = fields.Selection([('draft','Draft'),('confirm','Confirm'),('done','Done'),('cancel','Cancel')], default="draft")
    pay = fields.Monetary(string="Lương gốc")
    bonus =fields.Monetary(string="Thưởng")
    gender = fields.Selection([('nam','Nam'),('nu','Nu')])
    
    _sql_constraints = [('phone_unique','unique(phone_number)','số điện thoại đã tồn tại')]
    
    @api.constrains('phone_number')
    def _check_trangthai(self):
        if self.phone_number!=False:
            if len(self.phone_number)!=10 and self.phone_number[0]!=0:
                raise ValidationError('số điện thoại không hợp lệ')
        else:
            raise ValidationError('so dien thoai chua duoc nhap')
        
    

    def write(self,val):
        val ={
                'year_birth': date.today()
                }
        for re in self:
            re=re.browse([1,2])
        return super().write(val)
    

    