from odoo import models, fields


class SubjectManagement(models.Model):
    _name = "subject.management"
    _description = "Subject management course"

    name = fields.Char(required=True)
    price = fields.Float(required=True)
