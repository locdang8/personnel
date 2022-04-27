from odoo import models, fields
class ModelWirazd(models.TransientModel):
    _name = "wirazd_new.class"
    
    name=fields.Char(string="Tên")
    date = fields.Date(string="Date")
    