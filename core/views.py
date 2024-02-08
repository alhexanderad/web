from django.shortcuts import render
import os

def index(request):  
  return render(request, 'index.html',{})

def viewPDF(request):
  pdf_file_path = "/home/inti/github/web/0002-IC.pdf" 
  if os.path.exists(pdf_file_path):
    context={'pdf_file': pdf_file_path}
    return render(request, 'pdf.html',context)
  else:
    return render(request, 'error.html',{'message':'El archivo PDF no existe.'})