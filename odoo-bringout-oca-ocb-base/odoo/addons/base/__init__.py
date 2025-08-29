# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models
from . import populate
from . import report
from . import wizard


def post_init(cr, registry):
    """Post-init housekeeping.

    - Rewrites ICP's to force groups (existing behavior)
    - Removes enterprise/proprietary "to_buy" module promos from Apps list
    """
    from odoo import api, SUPERUSER_ID

    env = api.Environment(cr, SUPERUSER_ID, {})

    # Keep existing behavior
    env['ir.config_parameter'].init(force=True)

    # Remove enterprise/proprietary promotional stubs so they don't show in Apps
    try:
        Module = env['ir.module.module']
        promos = Module.search([
            ('to_buy', '=', True),
            ('license', 'in', ['OEEL-1', 'OEEL', 'OPL-1', 'Proprietary']),
        ])
        if promos:
            promos.unlink()
    except Exception:
        # Best-effort cleanup; never break base post-init
        pass
