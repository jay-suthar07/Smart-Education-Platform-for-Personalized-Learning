from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class CoursePlan(models.Model):
    _name = 'course.plan'
    # _rec_name = 'course_plan'

    name = fields.Char()
    add_discount = fields.Float(default="1")
    add_months = fields.Integer(default="1")
    # calculated_price = fields.Float(compute="_compute_course_plan")

    # @api.depends('add_discount', 'student_management_id.student_course_ids.course_base_price')
    # def _compute_course_plan(self):
    #     for record in self:
    #         if record.name:
    #             record.calculated_price = record.student_management_id.student_course_ids.course_base_price // record.add_discount

    @api.constrains('add_discount')
    def valid_selling(self):
        for record in self:
            if record.add_discount <= 0:
                raise UserError(("the discount must be grater than 0"))
