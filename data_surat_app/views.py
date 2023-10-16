from datetime import date
from django.shortcuts import render,redirect,get_object_or_404
from . models import Dbsurat , KatagoriSurat
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    dbsurat = Dbsurat.objects.all()
    context =  { 
        'page_title' : 'Home',
        'dbsurat' : dbsurat
    }
    return render(request, "pages/index.html", context)

@csrf_protect
@login_required(login_url="/accounts/login/")
def dashboard(request):
    dbsurat = Dbsurat.objects.all()
    katagori = list(KatagoriSurat.objects.values_list("katagori", flat=True))

    context =  { 
        'page_title'    : 'Dashboard',
        'dbsurat'       : dbsurat,
        'katagori'   : katagori
    }
    return render(request, "pages/dashboard.html", context)


def dashboard_edit(request, id_dashboard_katagori_edit):
    edit_surat = get_object_or_404(Dbsurat, pk = id_dashboard_katagori_edit)

    if request.method == 'POST':
        get_surat = request.POST.get('surat')
        get_kategori = request.POST.get('kategori')
        get_tgl = request.POST.get('tanggal')
        get_no_surat = request.POST.get('no_surat')
        get_kepada = request.POST.get('kepada')
        get_perihal = request.POST.get('perihal')
        get_upload_file = edit_surat.upload_file.name

    
        edit_surat = Dbsurat(
            id = id_dashboard_katagori_edit,
            surat = get_surat,
            kategori = get_kategori,
            tgl = get_tgl,
            no_surat = get_no_surat,
            kepada = get_kepada,
            perihal = get_perihal,
            upload_file = get_upload_file
        )
        edit_surat.save()
        edit_surat.clean_fields()

        return redirect('dashboard')
    else:
        return render(request,'pages/dashboard.html')
    
def dashboard_delete(request, id_dashboard_katagori_delete):
    edit_surat = get_object_or_404(Dbsurat, pk = id_dashboard_katagori_delete)
    upload_file_files   = Dbsurat.objects.get(pk = id_dashboard_katagori_delete)

    if request.method == 'POST':
        get_surat = request.POST.get('surat')
        get_kategori = request.POST.get('kategori')
        get_tgl = request.POST.get('tanggal')
        get_no_surat = request.POST.get('no_surat')
        get_kepada = request.POST.get('kepada')
        get_perihal = request.POST.get('perihal')
        upload_file_files.upload_file.delete()

    
        edit_surat = Dbsurat(
            id = id_dashboard_katagori_delete,
            surat = get_surat,
            kategori = get_kategori,
            tgl = get_tgl,
            no_surat = get_no_surat,
            kepada = get_kepada,
            perihal = get_perihal,
            # upload_file = get_upload_file
        )
        edit_surat.delete()

        return redirect('dashboard')
    else:
        return render(request,'pages/dashboard.html')
    


@csrf_protect
@login_required(login_url="/accounts/login/")
def tambah_data(request):
    # hari_ini = date.today()
    klasifikasi = list(KatagoriSurat.objects.values_list("katagori", flat=True))
        
    get_surat = request.POST.get('surat')
    get_katagori = request.POST.get('katagori')
    get_tanggal = request.POST.get('tanggal')

    files_upload = request.FILES.get('file_name')
    files_name = str(files_upload).split(',')

    filename_list_count = len(files_name)

    try:  
        no_surat = files_name[0]
        kepada = files_name[1]
        prihal = files_name[2] 
        prihal_surat = prihal[:-4]

        upload_data = Dbsurat(
            surat       = get_surat,
            kategori    = get_katagori,
            tgl         = get_tanggal,
            no_surat    = no_surat,
            kepada      = kepada,
            perihal     = prihal_surat,
            upload_file = files_upload,
        )
        
    except Exception:
        pass
        
    else:
        if filename_list_count == 3:
            upload_data.save()
            return redirect('dashboard')
        else:
            # messages.warning(request,'bzdbdbzdb')
            print("ada yang salah, cek lagi ")
        
    context = {
        'page_title' : 'Tambah Data',
        'klasifikasi' : klasifikasi,
    }
   
    return render(request,'pages/tambah_data.html', context)

@csrf_protect        
@login_required(login_url="/accounts/login/")
def setting_katagori(request):
   
    katagori = KatagoriSurat.objects.all()

    context = {
        'page_title'    : 'Setting',
        'katagori'   : katagori,
        # 'klasifikasi' : klasifikasi,
        # 'kelompok' : kelompok,
    }    

    return render(request,'pages/setting_katagori.html', context)


def setting_katagori_add(request):
     
    if request.method == 'POST':
        nama_klasifikasi = request.POST.get('katagori_surat')
    
        tambah_katagori = KatagoriSurat(
            katagori = nama_klasifikasi
        )
        tambah_katagori.save()
        tambah_katagori.clean_fields()
        return redirect('setting_katagori')
    else:
         return render(request,'pages/setting_katagori.html')

def setting_katagori_edit(request, id_setting_katagori_edit):
    edit_surat = get_object_or_404(KatagoriSurat, pk = id_setting_katagori_edit)

    if request.method == 'POST':
        nama_klasifikasi = request.POST.get('katagori_surat')
    
        edit_surat = KatagoriSurat(
            id = id_setting_katagori_edit,
            katagori = nama_klasifikasi,
        )
        edit_surat.save()
        edit_surat.clean_fields()

        return redirect('setting_katagori')
    else:
        return render(request,'pages/setting_katagori.html')


def setting_katagori_delete(request, id_setting_katagori_delete):
    delete_surat = get_object_or_404(KatagoriSurat, pk = id_setting_katagori_delete)

    if request.method == 'POST':
        delete_surat.delete()
        return redirect('setting_katagori')
    
    return render(request,'pages/setting_katagori.html')