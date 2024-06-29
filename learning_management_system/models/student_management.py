from odoo import api, models, fields


class StudentManagement(models.Model):
    _name = 'student.management'
    _description = 'student management system'
    _rec_name = "student_name"

    student_name = fields.Char()
    enrollment_number = fields.Char(compute='_compute_enrollment_number')
    birthdate = fields.Date()
    address = fields.Text()
    speaking_language = fields.Selection([('hindi', 'Hindi'), ('english', 'English'), ('gujrati', 'Gujrati')])
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    student_image = fields.Binary()
    student_course_ids = fields.Many2one("course.name")
    student_course_details_ids = fields.Many2many(related="student_course_ids.all_subjects_ids", string="course_subjects",
                                                  readonly=True)  # compute="_compute_studetnt_subjects")
    mode_of_learning = fields.Selection([('online', 'Online'), ('offline', 'Offline')])
    offline_learning_id = fields.Many2many('learning.management.offline')
    course_plan_id = fields.Many2one("course.plan", string="Select course plan")
    course_plan_price = fields.Float(compute="_compute_course_plan", store=True)

    # student_course_details= fields.Many2many("subject.management", compute="_compute_studetnt_subjects")
    # @api.depends('student_course_ids')
    # def _compute_studetnt_subjects(self):
    #     for record in self:
    #         print(">>>>>>>>>>>>>>>>", record)
    #         print(">>>>>>>>>>>>>>>>", record.student_course_ids.ids)
    #         if record.student_course_ids:
    #             print(">>>>>>>>>>>>>>>>", record.student_course_ids)
    #             print(">>>>>>>>>>>>>>>>", record.student_course_ids.all_subjects)
    #             record.student_course_details = record.student_course_ids.all_subjects.ids

    @api.depends()
    def _compute_enrollment_number(self):
        for record in self:
            print("<<<<<<<<<<<<<<<<<<<<", record.id)
            if record.id:
                record.enrollment_number = 202400819010000 + record.id
            print("<<<<<<<<<<<<<<<<<<<<", record.enrollment_number)

    @api.depends('course_plan_id.add_discount', 'student_course_ids.course_base_price')
    def _compute_course_plan(self):
        for record in self:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n", record.student_course_ids.course_base_price)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n", record.course_plan_id.add_discount)
            if record.course_plan_id.name:
                total_discount = ((record.student_course_ids.course_base_price*record.course_plan_id.add_months)*record.course_plan_id.add_discount)
                record.course_plan_price = ((record.student_course_ids.course_base_price*record.course_plan_id.add_months) - total_discount)
