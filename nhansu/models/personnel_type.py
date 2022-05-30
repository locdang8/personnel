from datetime import datetime, timedelta
from odoo import fields, api, models, _, registry
from odoo.exceptions import UserError, ValidationError


class Pofficial(models.Model):
    _name = "personnel_type.class"
    _inherit = "personnel.class"
    _description = "personnel_type"
    _rec_name = 'name'
    
    department_id = fields.Many2one('department.class', string='Phong ban', store=True)
    level_id = fields.Many2one('level.class', string='Trình độ học vấn', domain=[('detail', '=', 'chưa tốt nghiệp')])
    currency_id = fields.Many2one('res.currency', string="Loại tiền")
    
    pay = fields.Monetary(string="Lương gốc", currency_field="currency_id")
    bonus = fields.Monetary(string="Thưởng", currency_field="currency_id")
    pays = fields.Monetary(string="Lương nhân viên", currency_field="currency_id",
                           compute="_compute_pays", inverse="_inverse_pays", search="_search_pays")

    # process_ids = fields.One2many('process.class', 'person_type_id', string='Các khóa học') 
      
    img_ns = fields.Binary(string='Avatar', prefetch=True)
    status = fields.Boolean(string='Trạng thái', help="Check nếu là nhân viên chính thức")
    active = fields.Boolean(string="Hoạt động", default=True)
    
    name = fields.Char(string='Họ và tên', size=20)
    phone_number = fields.Char(string="Điện thoại")
    email = fields.Char(string="Email")

    year_birth = fields.Date(string="Năm sinh", default=fields.Date.subtract(fields.Date.today(),years=18))
    date_start = fields.Date(string="Ngay bắt đầu", default=fields.Date.add(fields.Date.today(), days=10))
    year_old = fields.Char(string='Tuổi', compute="_compute_year_old")
    
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Confirm'),
                              ('done', 'Done'),
                              ('cancel', 'Cancel')
                                ], default="draft")
    gender = fields.Selection(selection_add=[('new', 'New'), ('nam',)],
                              ondelete={'new': lambda ge: ge.write({'gender':'nu'})}, default='nam')
    
    detail = fields.Html(string="Chi tiết")
    
    lifeskills = fields.Float(string="Kỹ năng mềm", digits=0)
    english = fields.Float(string="Tiếng Anh", digits=0)

    count_person = fields.Integer(string="Số nhân viên", compute="_count_per")
    count_process = fields.Integer(compute="_compute_count_process", string="Số lượng khóa học")

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'tên đã tồn tại')
        ]
    
    # phương thức compute tính pays từ pay, status và pay
    @api.depends('status', 'pay', 'bonus')
    def _compute_pays(self):
        for re in self:
            if re.pay == False:
                re.pays = re.pay
            else:
                if re.status == True:
                    re.pays = (re.pay * 0.2) + re.pay + re.bonus
                else:
                    re.pays = re.pay
    
    # compute tính tuổi
    @api.depends('year_birth')
    def _compute_year_old(self):
        for r in self:
            if not r.year_birth:
                r.year_old = '0'
            date = fields.Date.today() - r.year_birth
            print('date...{} type{}'.format(date,type(date)))
            r.year_old= '3'
    

    # # compute tính số khóa học của mỗi nhân viên
    # def _compute_count_process(self):
    #     print('self...', self)
    #     count_process = len(self.mapped('process_ids'))
    #     self.count_process = count_process
    #     print(self.count_process)
    
    # inverse tính lại giá trị pay khi thay đổi pays
    def _inverse_pays(self):
        for re in self:
            if re.pays and re.pay and re.bonus:
                re.pay = (re.pays - re.bonus) / (1.2)
    
    def _search_pays(self, operator, value):
        print('value.....', value)
        pay = (value - bonus) / (1.2)
        return [('pay', '=', pay)]
    
    # Kiểm tra số điện thoại                
    @api.constrains('phone_number')
    def _check_trangthai(self):
        if self.phone_number != False:
            if len(self.phone_number) != 4 and self.phone_number[0] != 0:
                raise ValidationError(_('số điện thoại không hợp lệ'))
        else:
            raise ValidationError(_('so dien thoai chua duoc nhap'))
        
    @api.model
    def create(self, val):
        print('env....', self.env)
        print('user.....', self.env.user.name)
        print('company....', self.env.company)
        print('companies...', self.env.companies)
        print('context....', self.env.context)
        print('sudo.....', self.sudo())
        
        val['level_id'] = self.env['level.class'].browse(1).id
        # val['process_id']=[(0,0,{'date_start': fields.Date.today()})
        #                     ]
        # val['process_ids'] = [(6, 0, self.env['process.class'].browse([1, 2, 3, 4]).mapped('id'))]
        rtn = super(Pofficial, self).create(val)
        return rtn
    
    def write(self, val):
        # val['process_ids'] = [(1, self.process_ids.id, {'date_start':fields.Date.today() - timedelta(days=10)})]
        # val['process_id']=[(2,self.process_id.id,0)] #xoa luon ban ghi co id la id
        return super(Pofficial, self).write(val)
    
    def unlink(self):
        for re in self:
            if re.pays > 10000:
                raise UserError(_('Dont delete person has pays {}'.format(re.pays)))
        rtn = super(Pofficial, self).unlink()
        return rtn
    
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = _('copy %s', self.name)
        return super(Pofficial, self).copy(default)
    
    def name_get(self):
        val_list = []
        for per in self:
            name = "{}{}".format(per.name, per.email)
            val_list.append((per.id, name))
        return val_list
        
    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', '|', ('name', operator, name), ('phone_number', operator, name), ('email', operator, name)]
        return self._search(domain + args, limit=limit)
                   
