from odoo import api, models, fields, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError


class OfflineLearningManagement(models.Model):
    _name = "learning.management.offline"
    _rec_name = "teachername_offline"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    teacher_subject_offline_ids = fields.Many2many("subject.management")
    allocated_students_ids = fields.Many2many("student.management", "learning_management_offline_students_rel")
    teachername_offline = fields.Char()
    start_time = fields.Float()
    end_time = fields.Float()
    duration = fields.Float(compute="_compute_time_difference")
    state = fields.Selection([('new', 'New'), ('canceled', 'Canceled'), ('scheduled', 'Scheduled'), ], default='new')
    count_allocated_students = fields.Integer(compute="compute_offer_count")

    def action_open_student_details(self):
        student_ids = self.env['student.management'].search([('student_course_details_ids', 'in', self.teacher_subject_offline_ids.ids)])
        print("\n\n\n\n\n students: ", student_ids)
        return {
            'name': _('Students'),
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'res_model': 'student.management',
            'domain': [('id', 'in', student_ids.ids)],
        }

    # @api.constrains('start_time', 'end_time')
    # def validate_time(self):
    #     print("\n\n\n\n\n\n\n\n\nthis is my dadnfhzdjhajhn\n\n\n\n\n")
    #     for record in self:
    #         if record.end_time < record.start_time:
    #             raise UserError(("you cannot add end time smaller than start time"))

    @api.depends('start_time', 'end_time')
    def _compute_time_difference(self):
        for record in self:
            if record.start_time and record.end_time:
                time1 = record.start_time
                time2 = record.end_time
                record.duration = time2 - time1
            else:
                record.duration = 0

    def schedulebutton(self):
        self.state = 'scheduled'

    def cancelbutton(self):
        self.state = 'canceled'

    @api.depends('allocated_students_ids.student_name')
    def compute_offer_count(self):
        for record in self:
            # print(">>>>>>>>>>>>>>>>>>>>", record.id)
            offer_count = self.env['student.management'].search_count([('student_course_details_ids', 'in', self.teacher_subject_offline_ids.ids)])
            record.count_allocated_students = offer_count

    @api.model_create_multi
    def create(self, vals_list):
        schedules = super().create(vals_list)
        print("\n\n\n\n\n\n\n\n", schedules)
        if schedules.teachername_offline:
            learning_id = self.env['schedules.management'].create({
                'teacher_name': schedules.teachername_offline,
            })
        return schedules

    # def write(self, vals):
    #     new_schedules = super().write(vals)
    #     if 'start_time' in vals:
    #         learning_id = self.env['schedules.management'].write({
    #             'datetime_start': new_schedules.start_time,
    #             'datetime_end': new_schedules.end_time,
    #         })
    #     return new_schedules

    # def update_record(self):
    #     record = self.env['schedules.management'].browse()
    #     record.write({
    #         'datetime_start': new_schedules.start_time,
    #         'datetime_end': new_schedules.end_time,
    #     })
