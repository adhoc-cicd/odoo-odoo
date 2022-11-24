# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.addons.l10n_latam_check.tests.common import L10nLatamCheckTest
from odoo.tests.common import tagged


@tagged('post_install_l10n', 'post_install', '-at_install')
class TestOwnChecks(L10nLatamCheckTest):

    def test_01_pay_with_multiple_checks(self):
        """ Create one chec first check should choose deferred check by default. On current check force a different
        number than next one """
        vals_list = [{
            'ref': 'Deferred check',
            'partner_id': self.partner_a.id,
            'amount': '00000001',
            'check_number': '50',
            'payment_type': 'outbound',
            'journal_id': self.bank_journal.id,
            'payment_method_line_id': self.bank_journal._get_available_payment_method_lines('outbound').filtered(lambda x: x.code == 'check_printing').id,
        }]
        payment = self.env['account.payment'].create(vals_list)
        payment.action_post()
        self.assertRecordValues(payment, [{
            'state': 'posted',
            'is_move_sent': True,
        }], 'Checks where not created properly')
