product_prices = {
    'rtx 4090': '₱109,995',
    'rtx 4080': '₱84,200',
    'rtx 4070': '₱33,100',
    'rtx 4060': '₱18,500',
    'rtx 3090': '₱88,000',
    'rtx 3080': '₱41,000',
    'rtx 3070': '₱29,500',
    'rtx 3060': '₱19,950',
    'rtx 3050': '₱15,000',
    'gtx 1050 ti': '₱12,995',
}

print(product_prices)

print(product_prices.get('rtx 4060'))

product_prices['rtx 3050'] = '₱15,495'

product_prices.pop('rtx 3060')

print('gtx 1050 ti:', product_prices['gtx 1050 ti'])