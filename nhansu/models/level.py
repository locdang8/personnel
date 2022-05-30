# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError

class Level(models.Model):
    _name = 'level.class'
    _description = 'level education'

    name = fields.Char(string='Tên')
    detail = fields.Text(string='Mô tả')
    person_type_id = fields.One2many('personnel_type.class','level_id',string="Nhân viên",groups="nhansu.group_level_admin")
    count_p = fields.Integer(string="tong", compute="_set_person_count")
    # def _set_person_count(self):
    #     for re in self:
    #         cout_p = self.env['level.class'].search([('person_type_id','!=','')])
    #         re.count_p = cout_p
    #
    # def action_count_number(self):
    #     print('Test')
    
    def copy(self, default=None):
        if default is None:
            default={}
        if not default.get('name'):
            default['name']= _("%s (copy)",self.name)
        return super(Level, self).copy(default)        
    
    def name_get(self):
        val_list=[]
        for level in self:
            name="{} ({})".format(level.name,level.detail)
            val_list.append((level.id,name))
        return val_list
    
    # @api.model
    # def _name_search(self,name,args=None,operator='ilike',limit=100,name_get_uid=None):
    #     args=args or []
    #     domain=[]
    #     if name:
    #         domain=['|',('name',operator,name),('detail',operator,name)]
    #     rtn =self._search(domain+args,limit=limit)
    #     print("_name_search....",rtn)
    #     return rtn

    @api.model
    def _name_search(self,name,args=None,operator='ilike',limit=100,name_get_uid=None):
        args=args or []
        domain=[]
        if name:
            domain=['|',('name',operator,name),('detail',operator,name)]
        rtn =self._search(domain+args,limit=limit)
        print("_name_search....",rtn)
        return rtn
    
    def unlink(self):
        print('self...',self)
        for re in self:
            print('re...',re)
            if re.detail != None:
                raise UserError('K the xoa %s'%(re.name))
            rtn = super(Level,self).unlink()
        print(rtn)
        return rtn
    
    
    def timkiem(self):
        print('tim kiem theo _search', self._search([('name','ilike','12/12')],limit=3))
        print('tim kiem theo search', self.search([]))
        
    def _create_per(self,person):
        return self.env['personnel_type.class'].create({
                'name': person,
                'phone_numbe':'5677',
                'email':'liv'
            })
    def _test_per(self):
        per= self.create_per('Lê văn tuân')
        return self.create({
            'name':'Trung cap',
            'person_type_id':[
                (4,per.id)
                ]
            })
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        