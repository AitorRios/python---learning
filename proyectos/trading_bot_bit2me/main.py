import requests
import time 

#ultimas 50 operaciones
trader_50_vistos = set()
def last_trade():
    buy = 0
    sell = 0
    volumen_buy = 0
    volumen_sell = 0
    ultimo_precio = 0
    ultimo_tiempo = 0
    #peticion a la api
    respuesta = requests.get("https://gateway.bit2me.com/v1/trading/trade/last",
                            params={
                                "symbol": "BTC/EUR",
                                "limit": "50"
                            },
                            timeout=10
    )
    #transformar los datos a datos manipulables
    datos = respuesta.json()
    #guardamo la hora de llamada
    tamestamp = time.time()

    ultimo_precio += datos[0][1]
    ultimo_tiempo += datos[0][3]
    eliminar = datos[49]
    identificar_eliminados = (eliminar[1], eliminar[2], eliminar[3])

    for presion in datos:
        # filtrar operaciones repetidas
        identificadores = (presion[1], presion[2], presion[3])
        if identificadores in trader_50_vistos:
            continue
        else:
            trader_50_vistos.add(identificadores)
            #eliminamos la operacion mas antigua y menatenemos 50 operaciones en set
            if len(trader_50_vistos) > 50:
                if identificar_eliminados in trader_50_vistos:
                    trader_50_vistos.remove(identificar_eliminados)
        # contabilizar valumen y cantidad de compras y ventas
        if presion[0] == "buy":
            buy += 1
            volumen_buy +=presion[2]
                
        else: 
            sell +=1
            volumen_sell +=presion[2]
        
    return {"buy":buy,
            "sell":sell,
            "volumen_buy":volumen_buy,
            "volumen_sell":volumen_sell, 
            "ultimo_precio":ultimo_precio, 
            "ultimo_tiempo":ultimo_tiempo,
            "tamestamp":tamestamp
    }
#libro de ordenes por ejecutar
def order_book():
    #peticion a la api
    respuesta = requests.get("https://gateway.bit2me.com/v2/trading/order-book",
                            params={
                                "symbol": "BTC/EUR"
                },
                timeout=10
    )
    #transformamos a datos manipulables
    datos = respuesta.json()
    #guardamos el tiempo de la llamada
    tamestamp = time.time()
    #separacion de los datos
    bids = datos["bids"]
    asks = datos["asks"]
    #diferencia entre el maximo y el minimo precio
    mejor_bid = bids[0][0]
    mejor_ask = asks[0][0]
    return {"bids":bids,
            "asks":asks,
            "mejor_bid":mejor_bid,
            "mejor_ask":mejor_ask,
            "timestamp":tamestamp
    }
#datos de las velas
def vela():
    try:
        #calculos de hora
        tiempo_actual = time.localtime()
        andtime = time.mktime(tiempo_actual) * 1000
        startime = andtime - 3600000
        #llamada a la api
        respuesta = requests.get("https://gateway.bit2me.com/v1/trading/candle",
                                params={
                                    "symbol": "BTC/EUR",
                                    "interval": "5",
                                    "startTime": str(startime),
                                    "endTime": str(andtime),
                                    "limit": "12"
                                },
                                timeout=10
        )
        respuesta.raise_for_status()
        datos = respuesta.json()
        #control errores de devolucion de datos, validacion JSON
        if not isinstance(datos, list):
            return None
        if not datos:
            return None
        if len(datos) != 12:
            return None
        #ideas mejorar codigo, en vez de variables un diccionario
        timestamp = []
        apertura = []
        high = []
        low = []
        close = []
        volume = []
        #bucle para craar las listas
        for valor in datos:
            #control si devuelme cantidades diferentes de datos
            if len(valor) == 6:
                timestamp.append(valor[0]) 
                apertura.append(valor[1])
                high.append(valor[2])
                low.append(valor[3])
                close.append(valor[4])
                volume.append(valor[5])
            else:
                return None
            
        return {"timestamp":timestamp,
            "open":apertura,
            "high":high,
            "low":low,
            "close": close,
            "volumen": volume
        }
    #control de errores
    except requests.exceptions.JSONDecodeError:
        print("La respuesta no contiene JSON válido")
        return None
    except requests.exceptions.RequestException:
        print("Error en la petición de la API")
        return None

def spread(best_ask, best_bid):
    spreads = best_ask - best_bid
    spreads_relativo = (best_ask - best_bid)/((best_ask + best_bid) / 2) * 100
    return {"spread":spreads,
            "spread_medio":spreads_relativo
    }
#desequilibro del volumen del libro entre compradores y vendedores
def desequilibrio_orden_book(asks, bids):
    volumen_compras = 0
    volumen_ventas = 0
    for compra in bids:
        volumen_compras += compra[1]

    for ventas in asks:
        volumen_ventas += ventas[1] 

    desequilibrio = (volumen_compras - volumen_ventas)/(volumen_compras + volumen_ventas)
    
    return desequilibrio
#volumen en un rango del rango 0.5 
rango_superiores = []
rango_inferior = []
def volumen_en_rango(best_ask, best_bid, asks, bids, media_libro):
    meda_libro = (best_bid + best_ask) / 2
    rango = meda_libro * 0.005
    limite_superior = meda_libro + rango
    limite_inferior = meda_libro - rango
    volumen_ventas = 0
    volumen_compras = 0
    #bucle filtrado de rango en asks
    for precio, volumen in asks:
        if  meda_libro <= precio <= limite_superior:
            rango_superiores.append([precio, volumen])
    #bucle filtrado de rango en bids
    for precio, volumen in bids:
        if meda_libro >= precio >= limite_inferior:
            rango_inferior.append([precio, volumen])
    #sumamos los volumenes del rango
    for precio, volumen in rango_superiores:
        volumen_ventas += volumen
    for precio, volumen in rango_inferior:
        volumen_compras += volumen

    return {"volumen_ventas": volumen_ventas,
            "volumen_compras": volumen_compras
    }
#profundidad del volumen en el libro
def Profundidad_book(rango_super, rango_infer, media_libro):
    profundidad_superior = {}
    profundidad_inferior = {}
    #tramo superior rangos
    for precio, volumen in rango_super:
        diferencia = precio - media_libro
        tramo = int(diferencia / 10)
        if tramo in profundidad_superior:
            profundidad_superior[tramo] += volumen
        else:
            profundidad_superior[tramo] = volumen

    for precio, volumen in rango_infer:
        diferencia = media_libro - precio
        tramo = int(diferencia / 10)
        if tramo in profundidad_inferior:
            profundidad_inferior[tramo] += volumen
        else:
            profundidad_inferior[tramo] = volumen
    # falta hacer lo mismo pero con el de superior
    return { "profundidad_inferior":profundidad_inferior, "profundidad_superior": profundidad_superior}

def analisis_order_book(datos):
    timestamp = datos["timestamp"]
    media_libro = (datos["mejor_bid"] + datos["mejor_ask"]) / 2
    resultado_spread = spread(datos["mejor_ask"], datos["mejor_bid"])
    resultado_desequilibrio = desequilibrio_orden_book(datos["asks"], datos["bids"])
    resultado_volumen_rango = volumen_en_rango(datos["mejor_ask"], datos["mejor_bid"], datos["asks"], datos["bids"], media_libro)
    resultado_profundidad_book = Profundidad_book(datos["asks"], datos["bids"], media_libro)
    return {"volumen_rango": resultado_volumen_rango, 
            "spread": resultado_spread,
            "desequilibrio": resultado_desequilibrio,
            "profundidad": resultado_profundidad_book,
            "timestamp": timestamp
    }

def analisis_last_trader():
    return


#bucle principal control de peticiones
def principal():
    tiempo_local = time.time()
    ultima_peticion_5 = 0
    datos_vela = None
    
    while datos_vela is None:
        datos_vela = vela()
        if datos_vela is None:
            time.sleep(5)

    ultima_peticion_5 = tiempo_local
    ultima_10segundos = tiempo_local
    
    #bucle de peticion de las apis
    while True:
        tiempo_local = time.time()
        diferencia = tiempo_local - ultima_peticion_5
        diferencia_2 = tiempo_local - ultima_10segundos   
        #condicional de los 5m
        if diferencia >= 296:
            nuevas_vela = vela()
            while nuevas_vela is None:
                nuevas_vela = vela()
                if nuevas_vela is None:
                    time.sleep(5)
            datos_vela = nuevas_vela
            nuevo_tiempo = time.time()
            ultima_peticion_5 = nuevo_tiempo
            
        #condicional de los 5s
        if diferencia_2 >= 5:
            datos_order_book = order_book()
            analisis = analisis_order_book(datos_order_book)
            time.sleep(0.5)
            print(analisis)
            
            ultima_10segundos = tiempo_local
        time.sleep(5)

principal()