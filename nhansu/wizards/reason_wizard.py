from odoo import api, fields,models,_
class ReasonWizard(models.TransientModel):
    _name = 'reason.wizard'
    _description = 'reason wizard'
    
    reason = fields.Char(string="Lý do xin nghỉ")