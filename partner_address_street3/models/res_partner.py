# Copyright 2014-2020 Camptocamp SA
# @author: Nicolas Bessi
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    """Add third field in address"""

    _inherit = "res.partner"

    street3 = fields.Char("Street 3")

    @api.model
    def _address_fields(self):
        res = super()._address_fields()
        res.append("street3")
        return res

    def _display_address(self, without_company=False):
        """Remove empty lines which can happen when street3 field is empty."""
        res = super()._display_address(without_company=without_company)
        while "\n\n" in res:
            res = res.replace("\n\n", "\n")
        return res
