# -*- coding: utf-8 -*-
{
    'name': "MATRIX - OBJECT ORIENTED",

    'summary': """
        For Openhealth system. Matrix Object Oriented.
    """,

    'description': """

        9 Sep 2019

        For Openhealth. New Appointment Module (Object Oriented).
        Matrix model to solve the 2d bidimensional multi cell problem
        generated by Appointments. 
    """,

    'author': "DataMetrics",
    
    'website': "http://jrevilla.com/",
    
    'category': 'Object Oriented',
    
    'version': '1.0',

    # any module necessary for this one to work correctly
    #'depends': ['base'],
    #'depends': ['base', 'oehealth'],
    #'depends': ['base', 'oehealth', 'openhealth'],
    'depends': ['base', 'openhealth', 'price_list'],


    # always loaded
    'data': [

        #'views/oeh_patient.xml',
        #'views/patient_personal.xml',          # Dep




        'security/ir.model.access.csv',
        'security/matrix_security.xml',             # Groups



        #'views/views.xml',
        #'views/templates.xml',
        #'views/matrix_graph.xml',
        #'views/x2m_demo.xml',


        #'data/doctors.xml',     # Dep !



        'views/server_actions.xml',
        'views/lima_app_actions.xml',
        'views/tacna_app_actions.xml',


        #'views/menus_dep.xml',     # Dep 
        'views/menus.xml',



        #'wizard/wizard.xml',
        #'views/project.xml',
        #'views/user.xml',
        #'views/task.xml',
        #'views/matrix.xml',


        'views/patient.xml',




        'views/app_search.xml',

        'views/app_calendar.xml',


        #'views/appointment_actions.xml',
        'views/appointment.xml',



        'views/slot.xml',
        'views/slot_actions.xml',

        'views/container.xml',

        'views/doctor.xml',
        #'views/agenda.xml',



    ],



    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],


    # Static - Style Css 
    'css': ['static/src/css/jx.css'],
    
}


