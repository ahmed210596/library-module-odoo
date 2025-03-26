{
    'name': 'Library Security',
    'version': '1.0',
    'depends': ['library_module'],  
    'author': 'Your Name',
    'category': 'Library',
    'description': 'Adds Librarian group and permissions for library books',
    'data': [
        'security/library_groups.xml',
        'security/ir.model.access.csv',
        'views/library_book_form_inherit.xml',
       
    ],
    'installable': True,
}
