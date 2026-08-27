# -*- coding: utf-8 -*-
{
    'name': 'Facturación - Alerta Vencido 90 Días',
    'version': '1.0.0',
    'category': 'Accounting/Accounting',
    'summary': 'Etiqueta automáticamente como Vencida las facturas no pagadas con más de 90 días de antigüedad',
    'description': """
Módulo de extensión para Odoo Facturación / Contabilidad.
=========================================================
- Detecta facturas publicadas con estado de pago 'No pagadas' (o parciales) que hayan superado 90 días desde su vencimiento.
- Muestra la etiqueta / badge 'Vencida' resaltada en rojo en la lista de facturas.
- Destaca visualmente la fila de la factura en rojo.
- Añade el filtro de búsqueda rápida 'Vencidas (> 90 días)' en la barra de búsqueda de Facturación.
    """,
    'author': 'Antigravity AI',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'account',
    ],
    'data': [
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
