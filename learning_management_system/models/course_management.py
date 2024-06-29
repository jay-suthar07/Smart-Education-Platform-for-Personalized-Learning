from odoo import models, fields, api


class CourseManagement(models.Model):
    _name = 'course.name'
    _description = 'course management system'
    _rec_name = 'course_name'

    course_name = fields.Char(required=True)
    course_description = fields.Text()
    contact_number = fields.Integer()
    course_medium_language = fields.Selection([('english', 'English'), ('hindi', 'Hindi'), ('gujrati', 'Gujrati')], required=True)
    schedules = fields.Datetime()
    check_course_availability = fields.Datetime()
    all_subjects_ids = fields.Many2many("subject.management", required=True)
    course_base_price = fields.Float(compute="_Compute_course_price", store=True)

    @api.depends('all_subjects_ids.price')
    def _Compute_course_price(self):
        for record in self:
            # course_price = 0.0
            # for subject in record.all_subjects_ids:  #another method
            #     course_price += subject.price
            # record.course_price = course_price
            record.course_base_price = sum(record.all_subjects_ids.browse(record.all_subjects_ids.ids).mapped('price'))
