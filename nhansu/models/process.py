# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import models, fields, api


class Process(models.Model):
    _name = 'process.class'
    _description = 'process education'
    
    person_type_id = fields.Many2one('personnel_type.class', string='nhân sự')
    name = fields.Char(string="Tên", related="person_type_id.name")
    date_start = fields.Date(string='từ ngày', index=True)
    duration = fields.Float(string='Thời gian', digits=(2,1))
    date_stop = fields.Date(string='Đến ngày', compute="_set_date_stop", inverse="_set_duration")
    training_type = fields.Selection([('online','Online'),('offline','Offline')],string='Loại hình đào tạo')
    
    @api.depends('date_start','duration')
    def _set_date_stop(self):
        for re in self:
            if re.date_start == False and re.duration == False:
                re.date_stop = re.date_start
            else:
                duration= timedelta(days=re.duration, seconds=-1 )
                re.date_stop = re.date_start + duration
    def _set_duration(self):
        for re in self:
            if not(re.date_start and re.date_stop):
                continue
            re.duration = (re.date_stop - re.date_start).days +1