# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Argentinean Website',
    'version': '1.0',
    'category': 'Localization',
    'sequence': 14,
    'author': 'Odoo, ADHOC SA',
    'description': """Be able to see Identification Type and AFIP Responsibility in ecommerce checkout form.""",
    'depends': [
        'website_sale',
        'l10n_ar',
    ],
    'data': [
        'data/ir_model_fields.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/website_demo.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
}
