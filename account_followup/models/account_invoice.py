# -*- coding: utf-8 -*-

from openerp import api, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def write(self, vals):
        if vals.get('state', False) =='paid':
            for inv in self:
                if inv.move_id and inv.type == "out_invoice":
                    receivable_line = inv.move_id.line_ids.filtered(lambda l: l.account_id.internal_type == 'receivable')
                    if receivable_line:
                        receivable_line.blocked = True
        return super(AccountInvoice, self).write(vals)
