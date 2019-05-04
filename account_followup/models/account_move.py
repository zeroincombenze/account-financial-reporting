# -*- coding: utf-8 -*-

from openerp import api, fields, models, _


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    followup_line_id = fields.Many2one(
        'account_followup.followup.line', 
        'Follow-up Level', 
         ondelete='restrict'
    )
    followup_date = fields.Date(
        'Latest Follow-up'
    )
    result = fields.Float(
        compute='_get_result', 
        string="Balance"
    ) 

    @api.multi
    @api.depends('debit', 'credit')
    def _get_result(self):
        for aml in self:
            aml.result = aml.debit - aml.credit
