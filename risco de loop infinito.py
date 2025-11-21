while i < len(pedidos) and pedidos[i]["status"] == "pago":
    total += pedidos[i]["valor"]
    if not pedidos[i]["cancelado"]:
        validos += 1
    # (intencionalmente sem i += 1)