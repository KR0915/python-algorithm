import sys

def main(lines):
    # 1行目の入力は商品数
    num_products = int(lines[0])
    
    # 2行目の入力は注文数
    num_orders = int(lines[1])
    
    # 商品在庫の初期化
    stock = {}
    
    # 商品の在庫情報を取得
    for i in range(2, 2 + num_products):
        product_id, quantity, price = lines[i].split()
        stock[int(product_id)] = int(quantity)
    
    results = []
    
    # 注文情報を処理
    for i in range(2 + num_products, 2 + num_products + num_orders):
        parts = lines[i].split()
        command = parts[0]
        product_id = int(parts[1])
        quantity = int(parts[2])
        
        if command == 'order':
            if product_id in stock and stock[product_id] >= quantity:
                stock[product_id] -= quantity
                results.append(f"received order {product_id} {quantity}")
            else:
                results.append(f"sold out {product_id}")
    
    # 結果を出力
    for result in results:
        print(result)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
