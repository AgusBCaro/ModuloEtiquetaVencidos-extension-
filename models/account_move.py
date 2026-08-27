# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, timedelta


class AccountMove(models.Model):
    _inherit = 'account.move'

    is_overdue_90 = fields.Boolean(
        string="Vencido > 90 días",
        compute="_compute_is_overdue_90",
        search="_search_is_overdue_90",
        help="Indica si la factura publicada en estado 'No pagadas' supera los 90 días desde su vencimiento."
    )

    overdue_badge_status = fields.Selection(
        selection=[
            ('vencida', 'Vencida'),
            ('normal', 'No pagada'),
        ],
        string="Etiqueta Vencimiento",
        compute="_compute_is_overdue_90",
        search="_search_overdue_badge_status",
        help="Etiqueta visual que muestra 'Vencida' cuando la factura impaga supera los 90 días de mora."
    )

    @api.depends('payment_state', 'invoice_date_due', 'invoice_date', 'state')
    def _compute_is_overdue_90(self):
        today = date.today()
        for move in self:
            # Evaluar facturas publicadas (posted) impagas o parcialmente pagadas
            if move.state == 'posted' and move.payment_state in ('not_paid', 'partial'):
                # Usar fecha de vencimiento o respaldar con fecha de factura
                due_date = move.invoice_date_due or move.invoice_date
                if due_date:
                    days_overdue = (today - due_date).days
                    if days_overdue > 90:
                        move.is_overdue_90 = True
                        move.overdue_badge_status = 'vencida'
                        continue
            move.is_overdue_90 = False
            move.overdue_badge_status = 'normal'

    def _search_is_overdue_90(self, operator, value):
        today = date.today()
        limit_date = today - timedelta(days=90)

        # Manejar operadores booleanos (= True, != True, = False, etc.)
        is_true = (operator in ('=', '==') and value is True) or (operator in ('!=', '<>') and value is False)

        domain = [
            ('state', '=', 'posted'),
            ('payment_state', 'in', ('not_paid', 'partial')),
            '|',
            '&', ('invoice_date_due', '!=', False), ('invoice_date_due', '<', limit_date),
            '&', ('invoice_date_due', '=', False), ('invoice_date', '<', limit_date),
        ]

        if not is_true:
            return ['!',] + domain
        return domain

    def _search_overdue_badge_status(self, operator, value):
        if value == 'vencida':
            return self._search_is_overdue_90('=', True)
        else:
            return self._search_is_overdue_90('=', False)
