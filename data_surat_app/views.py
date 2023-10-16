from django.shortcuts import render,redirect
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
def tambah_data(request):
    id_username = request.user.pk
    username = request.user

    # now = datetime.now()
    # year = now.strftime("%Y")

    # hari_ini = date.today()

    # surat_id = NamaSurat.objects.filter(id_user = id_username).values_list("nama_surat" , flat=True)
    # klasifikasi = KlasifikasiSurat.objects.filter(id_user = id_username).values_list("nama_klasifikasi" , flat=True)
    # kelompok = KelompokSurat.objects.filter(id_user = id_username).values_list("nama_kelompok", flat=True)
   
    get_surat = request.POST.get('surat')
    get_klasifikasi = request.POST.get('klasifikasi')
    get_tanggal = request.POST.get('tanggal')

    files_upload = request.FILES.get('file_name')
    files_name = str(files_upload).split(',')

    filename_list_count = len(files_name)

    # print(username)
   
    try:  

        print(get_surat)
        no_surat = files_name[0]
        kepada = files_name[1]
        prihal = files_name[2] 
        prihal_surat = prihal[:-4]


        # upload_data = DatabaseSurat(
        #     id_user     = id_username,
        #     username    = username,
        #     surat       = get_surat,
        #     klasifikasi = get_klasifikasi,
        #     kelompok    = get_kelompok,
        #     tgl         = get_tanggal,
        #     no_surat    = no_surat,
        #     kepada      = kepada,
        #     perihal     = prihal_surat,
        #     upload_file = files_upload,
        #     today       = hari_ini,
        #     tahun       = year,
        # )
        
    except Exception:
        pass
        
    else:
        if filename_list_count == 3:
            # upload_data.save()
            return redirect('home')
        else:
            # messages.warning(request,'bzdbdbzdb')
            print("ada yang salah, cek lagi ")
        
    context = {
        'page_title' : 'Tambah Data',
        # 'klasifikasi' : klasifikasi,
        # 'kelompok' : kelompok,
        
    }
   
    return render(request,'pages/tambah_data.html', context)

@csrf_protect        
@login_required(login_url="/accounts/login/")
def setting(request):
   
    klasifikasi = KatagoriSurat.objects.all()

    context = {
        'page_title'    : 'Setting',
        'klasifikasi'   : klasifikasi,
        # 'klasifikasi' : klasifikasi,
        # 'kelompok' : kelompok,
    }    

    return render(request,'pages/settings.html', context)


def setting_tambah_data(request):
     
    if request.method == 'POST':
        nama_klasifikasi = request.POST.get('klasifikasi_surat')
    
        tambah_katagori = KatagoriSurat(
            katagori = nama_klasifikasi
        )
        tambah_katagori.save()
        tambah_katagori.clean_fields()
        return redirect('setting')
    else:
         return render(request,'pages/settings.html')

