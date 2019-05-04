# -*- coding: utf-8 -*-

from openerp import api, fields, models, _


class AccountConfigSettings(models.TransientModel):
    _name = 'account.config.settings'
    _inherit = 'account.config.settings'

    @api.multi
    def open_followup_level_form(self):
        res_ids = self.env['account_followup.followup'].search([]).ids

        return {
                 'type': 'ir.actions.act_window',
                 'name': 'Payment Follow-ups',
                 'res_model': 'account_followup.followup',
                 'res_id': res_ids and res_ids[0] or False,
                 'view_mode': 'form,tree',
         }
