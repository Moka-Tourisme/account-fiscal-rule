from odoo.addons.website_sale.controllers.variant import WebsiteSaleVariantController
from odoo.http import request, route


class WebsiteSaleVariantControllerEcotax(WebsiteSaleVariantController):

    @route(
        '/website_sale/get_combination_info',
        type='jsonrpc',
        auth='public',
        methods=['POST'],
        website=True,
        readonly=True,
    )
    def get_combination_info_website(
        self, product_template_id, product_id, combination, add_qty, uom_id=None, **kwargs
    ):
        result = super().get_combination_info_website(
            product_template_id, product_id, combination, add_qty, uom_id=uom_id, **kwargs
        )

        # ecotax_amounts may have been stripped by super (it's not in the pop list,
        # but the product_template model adds it). Re-fetch from a fresh call if needed.
        # In practice ecotax_amounts is kept because it's not in the popped keys list.
        ecotax_amounts = result.pop('ecotax_amounts', [])
        result['ecotax_html'] = request.env['ir.ui.view']._render_template(
            'account_tax_product_amount_website_sale.ecotax_amounts',
            values={
                'ecotax_amounts': ecotax_amounts,
                'currency': request.website.currency_id,
            },
        )
        return result
