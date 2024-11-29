from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas

def gerar_senhas_pdf(inicio=1, fim=100, nome_arquivo="senhas.pdf"):
    c = canvas.Canvas(nome_arquivo, pagesize=landscape(letter))
    
    
    x_inicial = 50
    y_inicial = 550 
    largura_bloco = 7 * 28.35
    altura_bloco = 3 * 28.35 
    espaco_entre_blocos = 0.5 * 28.35
    num_blocos_por_linha = 3 

    c.setFont("Helvetica", 10)
    
    x = x_inicial
    y = y_inicial
    
    contador = 0

    for numero in range(inicio, fim + 1):
        c.setStrokeColorRGB(0, 0, 0)
        c.setLineWidth(1)
        c.rect(x, y - altura_bloco, largura_bloco, altura_bloco, stroke=1, fill=0)
        
        c.setFont("Helvetica-Bold", 12)
        texto_titulo = "Título aqui"
        texto_titulo_largura = c.stringWidth(texto_titulo, "Helvetica-Bold", 12)
        c.drawString(x + (largura_bloco - texto_titulo_largura) / 2, y - 20, texto_titulo)
        
        texto_numero = f"Senha: {numero:03d}"
        texto_numero_largura = c.stringWidth(texto_numero, "Helvetica", 12)
        y_temp = y - (altura_bloco / 2) - 6
        
        c.setFont("Helvetica", 12)
        c.drawString(x + (largura_bloco - texto_numero_largura) / 2, y_temp, texto_numero)
        
        contador += 1

        if contador % num_blocos_por_linha == 0:
            x = x_inicial
            y -= altura_bloco + espaco_entre_blocos
        else:
            x += largura_bloco + espaco_entre_blocos
        
        if y < 100:
            c.showPage()
            c.setFont("Helvetica", 10)
            x = x_inicial
            y = y_inicial

    c.save()
    print(f"Senhas geradas e salvas em {nome_arquivo}")

gerar_senhas_pdf(1, 200, "PSA.pdf")
