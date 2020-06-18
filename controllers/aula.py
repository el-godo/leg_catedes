import os
import webbrowser as wb
def abrir_pdf():
	
	os.system('explorer')#abre el explorador de carpetas de windows
	os.startfile("D:\libros\\ajedrez") #ruta de la carpeta
	wb.open_new(r'D:\libros\\ajedrez\\AJEDREZ ORACULAR')
	return dict()