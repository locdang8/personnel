# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from odoo import models, fields, api


class Process(models.Model):
    _name = 'process.class'
    _description = 'process education'
    
    person_type_id = fields.Many2one('personnel_type.class', string='nhân sự')
    model = fields.Char('Resource Model', readonly=True)
    process_id=fields.Many2oneReference(model_field="model", string="Process")
    name = fields.Char(string="Tên", related="person_type_id.name")
    ids = fields.One2many(string="one2many", related='person_type_id.process_ids')
    date_start = fields.Date(string='từ ngày', index=True)
    duration = fields.Float(string='Thời gian', digits=(2,1),group_operator="avg")
    date_stop = fields.Date(string='Đến ngày', compute="_set_date_stop", inverse="_set_duration")
    training_type = fields.Selection([('online','Online'),('offline','Offline')],string='Loại hình đào tạo')
    date_add = fields.Datetime(string="Them ngay thang", default=datetime.today())
    img_1920 = fields.Image('Logo')
    def test_date(self):
        rtn=fields.Date.to_date(self.date_add)
        print('date_add...',rtn)
        print('date_start....',fields.Datetime.to_datetime(self.date_start))
        print('duration....',self.date_stop-self.date_start)
        print('date_start add', self.date_start+ timedelta(days=11))
        print('date add 10 day', fields.Date.add(self.date_start, months=2))
        print('date theo mui gio', fields.Date.context_today(self))
        print('date end off', fields.Date.end_of(self.date_start, 'day'))
        print('date start on', fields.Date.start_of(self.date_start, 'week'))
        print('date subtract', fields.Date.subtract(self.date_start, days=1))
        print('date to string', fields.Date.to_string(self.date_start))
        print('string to date', fields.Date.to_date('2022-02-12'))
    # @api.depends('date_start','duration')
    # def _set_date_stop(self):
    #     for re in self:
    #         if re.date_start == False and re.duration == False:
    #             re.date_stop = re.date_start
    #         else:
    #             duration= timedelta(days=re.duration, seconds=-1 )
    #             re.date_stop = re.date_start + duration
                
    # def _set_duration(self):
    #     for re in self:
    #         if not(re.date_start and re.date_stop):
    #             continue
    #         re.duration = (re.date_stop - re.date_start).days +1
    #

    @api.model_create_multi
    def create(self, val_list):
        val_list[0]['training_type']='online'
        print('val_list', val_list)
        return super().create(val_list)
    @api.model
    def name_create(self,name):
        return super().name_create({'name':name}).name_get()[0]
    # @api.model
    # def _name_search(self, name, args=None, operator='ilike', limit=100):
    #     args = args or []
    #     domain = []
    #     if name:
    #         domain = [('name',operator,name)]
    #
    #     return self._search(name, domain+args, limit=limit)