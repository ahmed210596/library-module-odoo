{
    'name': 'Library Module',
    'version': '1.0',
    'depends': [ 'web','mail'],
    'data': [
        'security/ir.model.access.csv',
        
        'views/library_book_views.xml',
        'report/library_report.xml',
        'views/assets.xml',
        'views/email_template.xml',
        'views/library_menu.xml',
        
        'views/Scheduled_notification.xml',
        'views/email_template_return.xml',
        'views/library_book_reviews_view.xml'
    ],
    'qweb': [
    'views/library_dashboard_template.xml',
],
    
    'application': True,
}
