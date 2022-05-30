from odoo import models, fields
class PersonnelWizard(models.TransientModel):
    _name = "personnel.wizard"
    _desciption = "Personnel wizard"
    
    
    relative_ids = fields.Many2one('relative.class',string="Relative")
    personnel_ids= fields.Many2many('personnel_type.class', string="Personnel")
    
    def subscribe(self):
        self.relative_ids.personnel_ids |=self.personnel_ids
        return{}