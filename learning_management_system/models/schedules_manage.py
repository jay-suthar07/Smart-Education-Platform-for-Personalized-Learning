from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Schedules(models.Model):
    _name = "schedules.management"
    _rec_name = "teacher_name"

    # schedule_session = fields.Selection([('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'),

    #                                      ('thruesday', 'Thruesday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')])
    teacher_name = fields.Char(required=True)
    offline_learning_id = fields.Many2one("learning.management.offline")
    datetime_start = fields.Float(related="offline_learning_id.start_time")
    datetime_end = fields.Float(related="offline_learning_id.end_time")
