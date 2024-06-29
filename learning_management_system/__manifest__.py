# -*- coding: utf-8 -*-
{
    'name': 'Learning Management',
    'description': '',
    'version': '17.0.1.1',
    'summary': 'Learning Management system ',
    'author': 'Jay suthar',
    'maintainer': 'Jay suthar',
    'depends':[
        'mail',
    ],
    'data': [
        "security/ir.model.access.csv",
        "views/learning_management_online.xml",
        "views/student_management.xml",
        "views/learning_management_offline.xml",
        "views/teacher_management.xml",
        "views/Course_management.xml",
        "views/subject_management.xml",
        "views/menu_item.xml",
        "views/course_plan.xml",
        "views/schedules.xml"
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
