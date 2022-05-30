from datetime import datetime, date, timedelta
from odoo import api, fields, models
class Subject(models.Model):
    _name ="subject.class"
    _description="subject class"
    _inherits={'process.class':'process_id'}
    _rec_name = "subject_name"
    # process_id = fields.Many2one('process.class', string="Process id")
    subject_name = fields.Char(string="Tên môn")
    detail = fields.Html(default="> <b><a>dff</a>xin chao</b> &-> &amp;",sanitize=False, string="ko có sanitize")
    detail2 = fields.Html(default="> <b><a>dff</a>xin chao </b> &-> &amp;", sanitize=True, string="có")
    test1= fields.Binary(string="test1", attachment=True)
    test2= fields.Binary(string="test2", attachment=False)
    test3 = fields.Binary(string="test3", prefetch=True)
