from odoo import api, fields, models

class Relative(models.Model):
    _name = "relative.class"
    _desciption = "relative"
    _order ="relationship,name"
    personnel_id = fields.Many2one('personnel_type.class', string='Nhân viên', required="True")
    name = fields.Char(string="Tên")
    relationship = fields.Selection([('father','Bố'),('mother','Mẹ'),('brother','Anh,em'),('sister','Chị em'),('other','Other')],string='Quan hệ', default='father')
    phone_number = fields.Char(string='Điện thoại')
    
    # _sql_constraints = [('check_phone_number','CHECK(len(phone_number)<10)','Số điện thoại có 10 số')]
    
    @api.model
    def filter(self, allre):
        allre = self.search([])
        print(allre.filtered(lambda c: c.relationship =='mother').read())
        print(allre.filtered_domain([('name','=','Nguyễn Thị Lý')]).personnel_id.name)
        
class Personnel_extend(models.Model):
    _inherit="personnel_type.class"
    
    numbers = fields.Integer(string="MTT")