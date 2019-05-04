# -*- coding: utf-8 -*-

from openerp import api, fields, models, _
from lxml import etree
from odoo.tools.misc import formatLang
# from odoo.exceptions import UserError
from odoo.addons.account_followup.report import account_followup_print


class Followup(models.Model):
    _name = 'account_followup.followup'
    _description = 'Account Follow-up'
    _rec_name = 'name'


    followup_line = fields.One2many(
        'account_followup.followup.line', 
        'followup_id', 
        'Follow-up', 
        copy=True
    )
    company_id = fields.Many2one(
        'res.company', 
        'Company', 
        required=True,
        default=lambda self: self.env['res.company']._company_default_get('account_followup.followup')
    )
    name = fields.Char(
        related='company_id.name', 
        string= "Name", 
        readonly=True
    )
    _sql_constraints = [('company_uniq',
                         'unique(company_id)',
                         'Only one follow-up per company is allowed')]


class FollowupLine(models.Model):

    @api.model
    def _get_desc(self):
        return '''Dear %(partner_name)s,

Exception made if there was a mistake of ours, it seems that the following amount stays unpaid. Please, take appropriate measures in order to carry out this payment in the next 8 days.

Would your payment have been carried out after this mail was sent, please ignore this message. Do not hesitate to contact our accounting department.

Best Regards,'''

    @api.model
    def _get_default_template(self):
        try:
            return self.env.ref('account_followup.email_template_account_followup_default')#probuse
        except ValueError:
            return False

    _name = 'account_followup.followup.line'
    _description = 'Follow-up Criteria'

    name = fields.Char(
        string= 'Follow-Up Action', 
        required=True
    )
    sequence = fields.Integer(
        string='Sequence', 
        help="Gives the sequence order when displaying a list of follow-up lines."
    )
    delay = fields.Integer(
        string='Due Days', 
        help="The number of days after the due date of the \
        invoice to wait before sending the reminder. \
        Could be negative if you want to send a polite alert beforehand.", 
        required=True
    )
    followup_id = fields.Many2one(
        'account_followup.followup', 
        string='Follow Ups', 
        required=True, 
    )
    description = fields.Text(
        string='Printed Message', 
        translate=True,
        default=_get_desc,
    )
    send_email = fields.Boolean(
        string='Send an Email', 
        help="When processing, it will send an email",
        default=True,
    )
    send_letter = fields.Boolean(
        string='Send a Letter', 
        help="When processing, it will print a letter",
        default=True,
    )
    manual_action = fields.Boolean(
        string='Manual Action', 
        help="When processing, it will set the \
        manual action to be taken for that customer. ",
        default=False,
    )
    manual_action_note = fields.Text(
        string='Action To Do', 
        placeholder="e.g. Give a phone call, check with others , ..."
    )
    manual_action_responsible_id = fields.Many2one(
        'res.users', 
        string='Assign a Responsible', 
    )
    email_template_id = fields.Many2one(
        'mail.template', 
        string='Email Template', 
        ondelete='set null',
        default=_get_default_template
    )
    _order = 'delay'
    _sql_constraints = [('days_uniq',
                         'unique(followup_id, delay)',
                         'Days of the follow-up levels must be different')]

    @api.one
    @api.constrains('description')
    def _check_description(self):
        lang = self.env.user.lang
        for line in self.with_context(lang=lang).browse():
            if line.description:
                try:
                    line.description % {'partner_name': '',
                                        'date':'',
                                        'user_signature': '',
                                        'company_name': ''}
                except:
                    return False

        return True
