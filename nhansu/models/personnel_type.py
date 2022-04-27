from odoo import fields, api, models
class Pofficial(models.Model):
    _name = "personnel_type.class"
    _inherit = "personnel.class"
    _description = "personnel_type"
    _rec_name = 'name'
    pays = fields.Monetary(string="Lương nhân viên", compute="_set_pay_official")
    gender = fields.Selection(selection_add=[('other','Other'),('nam',)])
    level_id = fields.Many2one('level.class',string='Trình độ học vấn')
    count_person = fields.Integer(string="Số nhân viên", compute="_count_per")
    count_process = fields.Integer(compute="_compute_count_process")
    detail = fields.Html(string="Chi tiết")
    def create_re(self):
        vals= self.env['personnel_type.class'].create({
            'name':'NGuye','phone_number':'0123456779'
            })
    @api.depends('status','pay','bonus')
    def _set_pay_official(self):
        for re in self:
            if re.pay ==False:
                re.pays = re.pay
            else:
                if re.status == True:
                    re.pays = (re.pay*0.2) + re.pay + re.bonus
                else:
                    re.pays= re.pay
    def set_draft(self):
        self.state="draft"
    def set_confirm(self):
        self.state="confirm"               
    def set_done(self):
        self.state="done"
    def set_cancel(self):
        self.state="cancel"
    def _count_per(self):
        for re in self:
            count_person = self.env['personnel_type.class'].search_count([])
            re.count_person = count_person
    def action_person_count(self):
        print('ok')
    def action_process_count(self):
        return { 
            'type':'ir.actions.act_window',
            'res_model':'process.class',
            'view_mode':'tree',
            }
    def _compute_count_process(self):
        for re in self:
            count_process = self.env['personnel_type.class'].search_count([('process_id','=','re.id')])
            re.count_process = count_process
            print(re.count_process)