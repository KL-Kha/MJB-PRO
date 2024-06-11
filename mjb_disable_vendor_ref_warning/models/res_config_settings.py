# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api, _

import logging as logger
_logger = logger.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    disable_vendor_ref_warning = fields.Boolean(config_parameter='mjb_disable_vendor_ref_warning.disable_vendor_ref_warning')