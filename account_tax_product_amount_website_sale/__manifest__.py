{
    'name': 'Account Tax Product Amount Website Sale',
    'summary': 'Display ecotax fixed amounts on website shop (product page and cart)',
    'version': '19.0.1.0.0',
    'category': 'Website/eCommerce',
    'author': 'Moka',
    'license': 'LGPL-3',
    'depends': [
        'account_tax_product_amount',
        'website_sale',
    ],
    'data': [
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'account_tax_product_amount_website_sale/static/src/js/ecotax_variant_mixin.js',
        ],
    },

    'installable': True,
    'auto_install': False,
}
