from odoo import models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _get_additionnal_combination_info(self, product_or_template, quantity, uom, date, website):
        combination_info = super()._get_additionnal_combination_info(
            product_or_template, quantity, uom, date, website
        )

        currency = website.currency_id

        tax_amount_ids = self.env['account.tax.product.amount']

        if product_or_template._name == 'product.product':
            tax_amount_ids = product_or_template.tax_amount_ids
        else:
            variant = product_or_template.product_variant_ids[:1]
            if variant:
                tax_amount_ids = variant.tax_amount_ids

        ecotax_amounts = []
        for ta in tax_amount_ids.filtered(
            lambda t: t.type_tax_use == 'sale' and t.amount > 0
        ):
            amount = ta.company_id.currency_id._convert(
                from_amount=ta.amount,
                to_currency=currency,
                company=ta.company_id,
                date=date,
            )
            ecotax_amounts.append({'name': ta.tax_id.name, 'amount': amount})

        combination_info['ecotax_amounts'] = ecotax_amounts
        return combination_info
