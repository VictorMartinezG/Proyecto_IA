# chatbot_atencion.py
import random

def obtener_respuesta(mensaje):
    mensaje = mensaje.lower()

    temas = {
        "saludo": ["hola", "buenas", "qué tal", "hey", "holi"],
        "horarios": ["horario", "hora", "abren", "cierran", "abierto"],
        "precio": ["precio", "cuánto cuesta", "vale", "costo"],
        "envío": ["envío", "entrega", "reparto", "llegar", "envían"],
        "pagos": ["pago", "formas de pago", "tarjeta", "efectivo", "transferencia"],
        "ubicación": ["dónde están", "ubicación", "dirección", "cómo llegar"],
        "reclamo": ["reclamo", "queja", "problema", "error", "mal servicio"],
        "pedido": ["pedido", "orden", "número de pedido", "mi pedido"],
        "cancelación": ["cancelar", "cancelación", "anular"],
        "cambio": ["cambiar", "devolución", "reembolso", "garantía"],
        "producto": ["producto", "disponible", "existencia", "tienen", "hay"],
        "promo": ["promoción", "descuento", "oferta", "promo"],
        "contacto": ["contacto", "teléfono", "whatsapp", "instagram", "redes"],
        "agradecimiento": ["gracias", "muy amable", "perfecto"],
        "despedida": ["adiós", "hasta luego", "nos vemos", "bye"]
    }

    respuestas = {
        "saludo": [
            "¡Hola! 👋 ¿En qué puedo ayudarte hoy?",
            "¡Bienvenido! 😊 ¿Cómo puedo servirte?",
            "¡Hola! Soy tu asistente virtual. ¿Qué necesitas?"
        ],
        "horarios": [
            "📅 Atendemos de lunes a sábado de 9:00 a.m. a 7:00 p.m.",
            "🕘 Nuestro horario es de 9:00 a 19:00 hrs, de lunes a sábado.",
            "⏰ Puedes visitarnos de lunes a sábado de 9 a.m. a 7 p.m."
        ],
        "precio": [
            "💰 Depende del producto. ¿Cuál te interesa?",
            "📦 Dime qué producto te interesa y te doy el precio exacto.",
            "🛒 Con gusto. ¿Qué artículo te interesa consultar?"
        ],
        "envío": [
            "🚚 Hacemos envíos a todo el país en 2 a 5 días hábiles.",
            "📦 Trabajamos con paqueterías confiables. Tu pedido está seguro.",
            "🛫 Envíos rápidos y seguros. ¿A qué ciudad sería?"
        ],
        "pagos": [
            "💳 Aceptamos efectivo, tarjetas, transferencias y pagos en línea.",
            "🤑 Puedes pagar como más te convenga: tarjeta, efectivo o SPEI.",
            "✔️ Sí, aceptamos pagos electrónicos, efectivo o depósitos bancarios."
        ],
        "ubicación": [
            "📍 Estamos en Av. Principal #123, Ciudad Ejemplo.",
            "🏬 Nuestra tienda está cerca del centro, junto a la farmacia.",
            "📌 Puedes encontrarnos en Google Maps como 'Tienda Ejemplo'."
        ],
        "reclamo": [
            "😓 Lamentamos mucho el inconveniente. ¿Podrías decirnos qué pasó?",
            "💬 Por favor, cuéntanos el problema y lo solucionamos.",
            "🛠️ Vamos a ayudarte. Describe el error que tuviste."
        ],
        "pedido": [
            "📄 ¿Tienes tu número de pedido? Lo necesito para ayudarte.",
            "🧾 Con tu número de orden puedo rastrear el estado del envío.",
            "🔍 Envíame el número de pedido para checarlo en el sistema."
        ],
        "cancelación": [
            "❌ ¿Deseas cancelar un pedido? Dime tu número de orden.",
            "🛑 Podemos ayudarte a cancelar. Solo necesitamos el número del pedido.",
            "📋 Envíanos los datos del pedido que quieres cancelar."
        ],
        "cambio": [
            "🔁 Aceptamos devoluciones dentro de los primeros 7 días.",
            "🔄 ¿Tu producto tiene falla? Lo cambiamos sin problema.",
            "📦 Para reembolsos o garantías, mándanos los detalles del producto."
        ],
        "producto": [
            "🧐 ¿Qué producto estás buscando? Te digo si lo tenemos.",
            "📦 Tenemos una gran variedad. Dime el nombre del artículo.",
            "📋 ¿Puedes especificar qué producto necesitas consultar?"
        ],
        "promo": [
            "🎉 Tenemos 10% de descuento en compras mayores a $500.",
            "🔥 Este mes hay promos en línea y en tienda física.",
            "🎁 Revisa nuestras historias en Instagram para ver todas las ofertas."
        ],
        "contacto": [
            "📲 Escríbenos por WhatsApp: 55-1234-5678 o en IG: @tiendaejemplo",
            "📧 También puedes enviarnos un correo a: contacto@tienda.com",
            "💬 Estamos en Instagram y Facebook como @tiendaejemplo"
        ],
        "agradecimiento": [
            "🙌 ¡Gracias por contactarnos! Estamos para servirte.",
            "😊 Con gusto, cualquier otra duda aquí estaré.",
            "👏 ¡Un placer ayudarte!"
        ],
        "despedida": [
            "👋 ¡Hasta luego! Que tengas un excelente día.",
            "💬 Si necesitas algo más, no dudes en escribir.",
            "🙏 ¡Gracias por escribirnos! Nos vemos pronto."
        ]
    }

    for tema, palabras in temas.items():
        for palabra in palabras:
            if palabra in mensaje:
                return random.choice(respuestas[tema])

    # Si no entendió el mensaje
    return random.choice([
        "🤔 No entendí muy bien. ¿Podrías explicarlo de otra forma?",
        "🧐 ¿Podrías reformular tu pregunta?",
        "😅 Aún estoy aprendiendo. Intenta preguntarlo de otra manera."
    ])
