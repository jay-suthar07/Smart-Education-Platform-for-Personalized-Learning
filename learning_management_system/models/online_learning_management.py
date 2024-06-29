from odoo import api, models, fields, _


class OnlineLeaningManagement(models.Model):
    _name = 'learning.management.online'
    _description = 'learning management system'
    _rec_name = "teachername_online"
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    # online_teachers_id = fields.Many2one("teacher.management")
    allocated_student_id = fields.Many2one("student.management")
    teacher_subject_online_ids = fields.Many2many("subject.management")
    teachername_online = fields.Char()
    teacher_subject_online_ids = fields.Many2many("subject.management")

    start_time = fields.Float()
    end_time = fields.Float()
    duration = fields.Float(compute="_compute_time_difference")
    state = fields.Selection([('new', 'New'), ('canceled', 'Canceled'), ('scheduled', 'Scheduled'), ], default='new')
    count_allocated_students = fields.Integer(compute="compute_offer_count")

    def action_open_student_details(self):
        student_ids = self.env['student.management'].search([('student_course_details_ids', 'in', self.teacher_subject_online_ids.ids)])
        print("\n\n\n\n\n students: ", student_ids)
        return {
            'name': _('Students'),
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'res_model': 'student.management',
            'domain': [('id', 'in', student_ids.ids)],
        }

    @api.constrains('start_time', 'end_time')
    def validate_time(self):
        print("\n\n\n\n\n\n\n\n\nthis is my dadnfhzdjhajhn\n\n\n\n\n")
        for record in self:
            if record.end_time < record.start_time:
                raise UserError(("you cannot add end time smaller than start time"))

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

    @api.depends('allocated_student_id.student_name')
    def compute_offer_count(self):
        for record in self:
            # print(">>>>>>>>>>>>>>>>>>>>", record.id)
            offer_count = self.env['student.management'].search_count([('student_course_details_ids', 'in', self.teacher_subject_online_ids.ids)])
            record.count_allocated_students = offer_count
