from odoo import api, models, fields


class TeacherManagement(models.Model):
    _name = "teacher.management"
    _description = "teacher management system"
    _rec_name = "mode_of_teaching"

    teachername = fields.Char()
    teacher_subject_ids = fields.Many2many("subject.management")
    teacher_address = fields.Text()
    speaking_language = fields.Selection([('hindi', 'Hindi'), ('english', 'English'), ('gujrati', 'Gujrati')])
    photo = fields.Image()
    mode_of_teaching = fields.Selection([('online', 'Online'), ('offline', 'Offline')])
    student_id = fields.Many2one("student.management")

    @api.model_create_multi
    def create(self, vals_list):
        teacher = super().create(vals_list)
        print("\n\n\n\n\n\n\n\n>>>>>>>>>>>called")
        if teacher.mode_of_teaching == "online":
            learning_id = self.env['learning.management.online'].create({
                'teachername_online': teacher.teachername,
                'teacher_subject_online_ids': teacher.teacher_subject_ids.ids
            })

            if teacher.teacher_subject_ids == teacher.student_id.student_course_details_ids:
                learning_id = self.env['learning.management.online'].search(['teacher.student_id.student_course_details_ids'])
        else:
            learning_id = self.env['learning.management.offline'].create({
                'teachername_offline': teacher.teachername,
                'teacher_subject_offline_ids': teacher.teacher_subject_ids.ids,
            })
            print("\n\n\n\n\n\n\n\n>>>>>>>learning_id", learning_id)
        return teacher
