from odoo import api, fields, models,_

class Relative(models.Model):
    _name = "relative.class"
    _desciption = "relative"
    _order ="relationship,name"
    
    personnel_id = fields.Many2one('personnel_type.class', string='Nhân viên', store=True, required=True)
    name = fields.Char(string="Tên", required=True)
    relationship = fields.Selection([('father','Bố'),('mother','Mẹ'),('brother','Anh,em'),('sister','Chị em'),('other','Other')],string='Quan hệ', default='father',requried=True)
    phone_number = fields.Char(string='Điện thoại', required=True)
    # action_id = fields.One2many('personnel.wizard','relative_ids')
    
    
    _sql_constraints = [
        ('personnel_id_unique','UNIQUE(personnel_id)','Mỗi nhân viên chỉ có một thân nhân')
        ]
    @api.model
    def filter(self, allre):
        allre = self.search([])
        print(allre.filtered(lambda c: c.relationship =='mother').read())
        print(allre.filtered_domain([('name','=','Nguyễn Thị Lý')]).personnel_id.name)
    
    # @api.depends_context('name')
    # def _compute_get_phone(self):
    #     for re in self:
    #         print(re.env.context.get('name'))
    #         re.phone_number="12"
            
    # def copy(self, default=None):
    #     if default is None:
    #         default={}
    #     if not default.get('name'):
    #         default['name']= _("%s (copy)",self.name)
    #     return super(Relative, self).copy(default)        
    
    # @api.model_create_multi
    # def create(self,val_list):
    #     rtn = super(Relative, self).create(val_list)
    #     print(rtn)
    #     return rtn
    #


    def write(self, val):
        print('val....', val)
        rtn=super(Relative, self).write(val)
        print('rtn....', rtn)
    
    @api.model
    def default_get(self, field_list=[]):
        print(field_list)
        rtn = super(Relative,self).default_get(field_list)
        print(rtn)
        return rtn
    
    @api.model_create_multi
    def create(self,val):
        print('self.env....',self.env)
        print('self.env.user...',self.env.user)
        print('self.env.company...',self.env.company)
        print('self.env.companies....',self.env.companies)
        print('self.env.context....',self.env.context)
        
        return super(Relative,self).create(val)
    
    
    def view_perwizard(self):
        return {
            'type':'ir.actions.act_window',
            'res_model':'personnel.wizard',
            'view_mode':'form',
            'target':'new'        
            }
class Personnel_extend(models.Model):
    _inherit="personnel_type.class"
    _name="person2.class"

