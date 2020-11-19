from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from OCR712.models import Ocr712
from OCR712.forms import DocumentForm
from OCR712.main_code import gtrans2excel
import shutil

# Create your views here.

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        # delete all files in the folder.
        try:
            shutil.rmtree('D:\\TP_PROGS\\Projects\\CodeForChangeHackathon2020\\progs\\OCRCFC2020\\media\\documents') 
        except:
            print("no files to remove")
        
        files = request.FILES.getlist('document')
        # print(files)
        if form.is_valid():
            for f in files:
                print("SAVINGGGGGGG")
                file_instance = Ocr712(document=f)
                file_instance.save()
            # apna code idhar jo files sab pe run hove
            # excel file banega and down mae sae down ho paayega.
            gtrans2excel.test()
            return redirect('/OCR712/down/excel')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

def downForm(request):
    # if request.method == 'POST':
    #     form = DocumentForm(request.POST, request.FILES)
    #     files = request.FILES.getlist('document')
    #     # print(files)
    #     if form.is_valid():
    #         for f in files:
    #             print("SAVINGGGGGGG")
    #             file_instance = Ocr712(document=f)
    #             file_instance.save()
    #         return redirect('/OCR712/')
    # else:
    #     form = DocumentForm()
    return render(request, 'down.html', {})


# from django.conf import settings
from django.http import HttpResponse, Http404
# def download(request,path):
#     file_path = os.path.join(settings.MEDIA_ROOT,path)
#     if os.path.exists(file_path):
#         with open(file_path,"rb") as fh:
#             response= HttpResponse(fh.read(),content_type="application/adminupload")
#             response["Content-Disposition"]="inline;filename="+os.path.basenamme(file_path)
#             return response
#     raise Http404


import mimetypes

def download_file(request):
    # fill these variables with real values
    fl_path = 'D:\\TP_PROGS\\Projects\\CodeForChangeHackathon2020\\progs\\OCRCFC2020\\output.xlsx'
    filename = 'output.xlsx'

    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    print(mime_type)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response