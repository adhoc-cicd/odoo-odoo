# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Advanced Check Management',
    'version': "1.0.0",
    'category': 'Accounting/Localizations',
    'summary': 'Checks Management',
    'description': """
Own Checks Management
---------------------

Extends 'Check Printing Base' module to manage own checks with more features:

* allow using own checks that are not printed but filled manually by the user
* allow to use deferred or electronic checks
  * printing is disabled
  * check number is set manually by the user
* add an optional "Check Cash-In Date" for post-dated checks (deferred payments)
* add a menu to track own checks

Third Party Checks Management
-----------------------------

Add new "Third party check Management" feature.

There are 2 main Payment Methods additions:

* New Third Party Checks:

   * allow the user create a check on the fly from a payment
   * create a third party check from a customer payment

* Existing Third party check:

   * allow the user to reuse a Third party check already created
   * pay a vendor bill using an existing Third party check
   * move an existing checks between journals (i.e. move to Rejected)
   * Send/Receive again a check already used in a Vendor Bill/Customer INV
   * allow the user to do mass check transfers

""",
    'author': 'ADHOC SA',
    'license': 'LGPL-3',
    'images': [
    ],
    'depends': [
        'account_check_printing',
        'base_vat',
    ],
    'data': [
        'data/account_payment_method_data.xml',
        'security/ir.model.access.csv',
        'views/account_payment_view.xml',
        'views/account_journal_view.xml',
        'wizards/account_payment_register_views.xml',
        'wizards/l10n_latam_payment_mass_transfer_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
