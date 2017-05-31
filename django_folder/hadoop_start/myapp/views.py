from django.shortcuts import render,redirect
from myapp import forms
from myapp.forms import UserForm,UserProfileInfoForm,SaasForm,IaasForm
from os import system
import urllib
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

myip = '192.168.43.188'


def index(request):
    return render(request,'myapp/index.html')

def IaasService(request):
    form = forms.IaasForm()
    if request.method == 'POST':
        form = forms.IaasForm(request.POST)
        if form.is_valid():
            client_type = form.cleaned_data['client_type']
            vm_name = form.cleaned_data['vm_name']
            instance_type = form.cleaned_data['instance_type']
            instance_variant = form.cleaned_data['instance_variant']
            ram = form.cleaned_data['RAM']
            vcpu = form.cleaned_data['vCPUs']
            size = form.cleaned_data['HDD']
            network_install_type = form.cleaned_data['network_install_type']
            bridge_connectivity = form.cleaned_data['bridge']
            provision = form.cleaned_data['provision']
            access_type = form.cleaned_data['access_type']
            def myFun(img_type):
                if network_install_type == 'select1':
                    print('You Selected installation via IMG')
                    if provision == 'select1':
                        print('Thick Provisioning')
                        if access_type == 'select1':
                            print('TigerVNC')
                            system("virt-install --name {} --memory {} --vcpus {} --os-type linux --cdrom  /images_files/{} --disk=/iaas/{}.img,size={} --network  bridge=mybr --graphics vnc,password=redhat,listen=0.0.0.0,port=5911  --noautoconsole".format(vm_name,ram,vcpu,img_type,vm_name,size))
                            #print(instance_variant)
                            #print(instance_type)
                        else:
                            print('NOVNC')
                            system("virt-install --name {} --memory {} --vcpus {} --os-type  linux --cdrom /images_files/{} --disk=/iaas/{}.img,size={} --network  bridge=mybr --graphics vnc,password=redhat,listen=0.0.0.0,port=5913  --noautoconsole".format(vm_name,ram,vcpu,img_type,vm_name,size))
                    else:
                        print('Thin Provisioning')
                        system("qemu-img create -f qcow2  /iaas/{}.qcow2  {}".format(vm_name,size))
                        if access_type == 'select1':
                            print('TigerVNC')
                            system("virt-install --name {} --memory {} --vcpus {} --os-type linux --cdrom /images_files/{} --disk=/iaas/{}.qcow2  --network  bridge=mybr --graphics vnc,password=redhat,listen=0.0.0.0,port=5910  --noautoconsole".format(vm_name,ram,vcpu,img_type,vm_name))
                        else:
                            print('NOVNC')
                            system("virt-install --name {} --memory {} --vcpus {} --os-type linux --cdrom /images_files/{} --disk=/iaas/{}.qcow2  --network  bridge=mybr --graphics vnc,password=redhat,listen=0.0.0.0,port=5914  --noautoconsole".format(vm_name,ram,vcpu,img_type,vm_name))
                elif network_install_type == 'select2':
                    print('You Selected installation FTP')
                    if provision == 'select1':
                        print('Thick Provisioning')
                        if access_type == 'select1':
                            print('TigerVNC')
                            system("virt-install --name {} --memory {} --vcpus {} --os-type linux  --location ftp://{}/pub/{}  --disk=/iaas/{}.img,size={} --network  bridge=mybr --graphics vnc,password=redhat,listen=0.0.0.0,port=5915  --noautoconsole".format(vm_name,ram,vcpu,myip,instance_variant,img_type,vm_name,size))

                        else:
                            print('NOVNC')
                            system("virt-install --name {} --memory {} --vcpus {} --os-type linux  --location ftp://{}/pub/{}  --disk=/iaas/{}.img,size={} --network  bridge=mybr --graphics vnc,password=redhat,listen=0.0.0.0,port=5916  --noautoconsole".format(vm_name,ram,vcpu,myip,instance_variant,img_type,vm_name,size))

                    else:
                        print('Thin Provisioning')
                        system("qemu-img create -f qcow2  /iaas/{}.qcow2  {}".format(vm_name,size))
                        if access_type == 'select1':
                            print('TigerVNC')
                            system("virt-install --name {} --memory {} --vcpus {} --os-type  linux --location ftp://{}/pub/{}  --disk=/iaas/{}.qcow2  --network  bridge=mybr --graphics vnc,password=redhat,listen=0.0.0.0,port=5917  --noautoconsole".format(vm_name,ram,vcpu,myip,instance_variant,img_type,vm_name))

                        else:
                            print('NOVNC')
                            system("virt-install --name {} --memory {} --vcpus {} --os-type linux  --location ftp://{}/pub/{}  --disk=/iaas/{}.qcow2  --network  bridge=mybr --graphics vnc,password=redhat,listen=0.0.0.0,port=5918  --noautoconsole".format(vm_name,ram,vcpu,myip,instance_variant,img_type,vm_name))

                else:
                    print('You Selected installation HTTP')
                    if provision == 'select1':
                        print('Thick Provisioning')
                        if access_type == 'select1':
                            print('TigerVNC')
                            system("virt-install --name {} --memory {} --vcpus {} --os-type  linux  --location http://{}/{}  --disk=/iaas/{}.img,size={} --network  bridge=mybr --graphics vnc,password=redhat,listen=0.0.0.0,port=5919  --noautoconsole".format(vm_name,ram,vcpu,myip,instance_variant,img_type,vm_name,size))

                        else:
                            print('NOVNC')
                            system("virt-install --name {} --memory {} --vcpus {} --os-type  linux   --location http://{}/{}  --disk=/iaas/{}.img,size={} --network  bridge=mybr --graphics vnc,password=redhat,listen=0.0.0.0,port=5920  --noautoconsole".format(vm_name,ram,vcpu,myip,instance_variant,img_type,vm_name,size))

                    else:
                        print('Thin Provisioning')
                        system("qemu-img create -f qcow2  /iaas/{}.qcow2  {}".format(vm_name,size))
                        if access_type == 'select1':
                            print('TigerVNC')
                            system("virt-install --name {} --memory {} --vcpus {} --os-type  --location http://{}/{}  --disk=/iaas/{}.qcow2  --network  bridge=mybr --graphics vnc,password=redhat,listen=0.0.0.0,port=5921  --noautoconsole".format(vm_name,ram,vcpu,myip,instance_variant,img_type,vm_name))

                        else:
                            print('NOVNC')
                            system("virt-install --name {} --memory {} --vcpus {} --os-type   --location http://{}/{}  --dis/iaas/{}.qcow2  --network  bridge=mybr --graphics vnc,password=redhat,listen=0.0.0.0,port=5922  --noautoconsole".format(vm_name,ram,vcpu,myip,instance_variant,img_type,vm_name))

            if client_type == 'select1':
                print("You are window client")
            else:
                print('you are linux client')
                if instance_type == 'select1':
                    print('instance type is Linux')
                    if instance_variant == 'select1':
                        print('You required Ubuntu')
                        img_type = 'ubuntu-14.04-desktop-amd64.iso'
                        myFun(img_type)
                    elif instance_variant == 'select2':
                        print('You required kali linux')
                        img_type = 'kali-linux-2016.2-amd64.iso'
                        myFun(img_type)
                    elif instance_variant == 'select3':
                        print('You required LinuxMint')
                        img_type = 'linuxmint-11-gnome-dvd-64bit.iso'
                        myFun(img_type)
                    elif instance_variant == 'select4':
                        print('You required RHEL6')
                        img_type = 'rhel-server-6.4-x86_64-dvd.iso'
                        myFun(img_type)
                    else:
                        print('You required RHEL7')
                        img_type = 'rhel-server-7.2-x86_64-dvd.iso'
                        myFun(img_type)
                else:
                    print('instance type is Windows')


    return render(request,'myapp/iaas.html',{'form' : form})

def SaasService(request):
    form = forms.SaasForm()
    if request.method == 'POST':
        form = forms.SaasForm(request.POST)
        if form.is_valid():
            #Do something code here
            cip = request.META.get('REMOTE_ADDR')
            cname = form.cleaned_data['name']
            sft_name = form.cleaned_data['software_name']
            list_of_software = {'select1' : 'firefox','select2' : 'atom','select3' : 'gnome-terminal','select4' : 'xterm','select5' : 'google-chrome','select6' : 'virt-manager','select7' : 'virt-viewer'}
            def mySoftware():
                system('useradd -s  /usr/bin/{}  {}'.format(list_of_software[sft_name],cname))
                system("echo '{}' |  passwd  {}  --stdin".format(cname,cname))
                #system("setfacl -m  u:{}:rx  /usr/bin/{}".format(cname,list_of_software[sft_name]))   (Removing acc. based restriction)
                fh = open('/root/Desktop/{}.sh'.format(cname),'a+')
                fh.write("#! /bin/bash\n\nsshpass -p '{}' ssh -o StrictHostKeyChecking=no -X -l {} {} {}".format(cname,cname,myip,list_of_software[sft_name]))
                fh.close()
                system('chmod +x /root/Desktop/{}.sh'.format(cname))
                status = system("sshpass -p 'redhat' scp -o StrictHostKeyChecking=no /root/Desktop/{}.sh  root@{}:/root/Desktop/".format(cname,cip))
                system("echo 'y' | rm /root/Desktop/{}.sh".format(cname))
                if status == 0:
                    return HttpResponse("<h1>Congratulation!!!</h1><h1>A file named {}.sh has been sent to you.</h1><h1>Run command using 'bash {}.sh' on your terminal to get requested software</h1>".format(cname,cname))
                else:
                    return HttpResponse("<h1>Failure!</h1>")
            if sft_name == 'select1':
                #print('you select firefox')
                mySoftware()
            elif sft_name == 'select2':
                #print('you select atom text editor')
                mySoftware()
            elif sft_name == 'select3':
                #print('you select terminal')
                mySoftware()
            elif sft_name == 'select4':
                #print('you select terminal')
                mySoftware()
            elif sft_name == 'select5':
                system('useradd  {}'.format(cname))
                system("echo '{}' |  passwd  {}  --stdin".format(cname,cname))
                fh = open('/root/Desktop/{}.sh'.format(cname),'a+')
                fh.write("#! /bin/bash\n\nsshpass -p '{}' ssh -o StrictHostKeyChecking=no -X -l {} {} {}".format(cname,cname,myip,list_of_software[sft_name]))
                fh.close()
                system('chmod +x /root/Desktop/{}.sh'.format(cname))
                status = system("sshpass -p 'redhat' scp -o StrictHostKeyChecking=no /root/Desktop/{}.sh  root@{}:/root/Desktop/".format(cname,cip))
                system("echo 'y' | rm /root/Desktop/{}.sh".format(cname))
                if status == 0:
                    return HttpResponse("<h1>Congratulation!!!</h1><h1>A file named {}.sh has been sent to you.</h1><h1>Run command using 'bash {}.sh' on your terminal to get requested software</h1>".format(cname,cname))
                else:
                    return HttpResponse("<h1>Failure!</h1>")
            elif sft_name == 'select6':
                mySoftware()
            elif sft_name == 'select6':
                mySoftware()
    return render(request,'myapp/saas.html',{'form' : form})

def form_name_view(request):
    form = forms.StorageFormName()

    if request.method == 'POST':
        form = forms.StorageFormName(request.POST)
        if form.is_valid():
            #Do something code here
            cip = request.META.get('REMOTE_ADDR')
            cname = form.cleaned_data['name']
            st_name = form.cleaned_data['storage_dir']
            sz = form.cleaned_data['size']
            st_type = form.cleaned_data['storage_type']
            st_security = form.cleaned_data['storage_security']
            def myData():
                system("echo 'y' |  lvcreate --name {} --size {}M myvg".format(cname,sz))
                system("mkdir /client_folder/{}".format(st_name))
                system("mkfs.ext4 /dev/myvg/{}".format(cname))
                system("mount /dev/myvg/{}  /client_folder/{}".format(cname,st_name))
            if st_type == 'choice1' and st_security == 'select2':
                myData()
                fh = open('/etc/exports','a+')
                fh.write("\n/client_folder/{}   *(rw,no_root_squash)".format(st_name))
                fh.close()
                system("exportfs -r")
                fh = open('/root/Desktop/{}.sh'.format(cname),'a+')
                fh.write("#! /bin/bash\n\nmkdir /media/{}\n\nmount {}:/client_folder/{}  /media/{}".format(cname,myip,st_name,cname))
                fh.close()
                system('chmod +x /root/Desktop/{}.sh'.format(cname))
                status = system("sshpass -p 'redhat' scp -o StrictHostKeyChecking=no /root/Desktop/{}.sh  root@{}:/root/Desktop/".format(cname,cip))
                system("echo 'y' | rm /root/Desktop/{}.sh".format(cname))
                if status == 0:
                    return HttpResponse("<h1>Congratulation!!!</h1><h1>A file has been sent to you.</h1><h1>Please Double click on {}.sh file to get requested storage</h1>".format(cname))
                else:
                    return HttpResponse("<h1>Failure!</h1>")
            elif st_type == 'choice1' and st_security == 'select1':
                #return redirect('secure')
                myData()
                system("useradd {}".format(cname))
                system("echo '{}' | passwd {} --stdin".format(cname,cname))
                system('chown {} /client_folder/{}'.format(cname,st_name))
                system('chmod 700 /client_folder/{}'.format(st_name))
                fh = open('/root/Desktop/{}.sh'.format(cname),'a+')
                fh.write("#! /bin/bash\n\nmkdir /media/{} \n\nyum install fuse-sshfs\n\nsshfs -o StrictHostKeyChecking=no {}@{}:/client_folder/{}  /media/{}".format(st_name,cname,myip,st_name,st_name))
                fh.close()
                status = system("sshpass -p 'redhat' scp -o StrictHostKeyChecking=no /root/Desktop/{}.sh  root@{}:/root/Desktop/".format(cname,cip))
                system("echo 'y' | rm /root/Desktop/{}.sh".format(cname))
                if status == 0:
                    return HttpResponse("<h1>A file named {}.sh has been sent to you.</h1><h1>Please run this file using 'bash {}.sh' command in your terminal to get required storage</h1><h1>Your password is {}".format(cname,cname,cname))
                else:
                    return HttpResponse("<h1>Failure!</h1>")
            elif st_type == 'choice1' and st_security == 'select3':
                return HttpResponse("<http><body><h1>Welcome to Object Storage as a service with High Availability</h1></body></http>")
            elif st_type == 'choice2':
                system("echo 'y' |  lvcreate --name {} --size {}M  blkvg".format(cname,sz))
                fh = open('/etc/tgt/conf.d/{}.conf'.format(st_name),'a+')
                fh.write('<target  {}>\n  backing-store   /dev/blkvg/{}\n</target>'.format(cname,cname))
                fh.close()
                system('systemctl restart tgtd')
                system('setenforce 0')
                system('iptables -F')
                fh = open('/root/Desktop/{}.sh'.format(cname),'w+')
                fh.write('#! /bin/bash\n\nyum install iscsi-initiator-utils\n\niscsiadm --mode discoverydb --type  sendtargets --portal  {}  --discover\n\niscsiadm --mode node --targetname {} --portal {}:3260 --login'.format(myip,cname,myip))
                fh.close()
                status = system("sshpass -p 'redhat' scp -o StrictHostKeyChecking=no /root/Desktop/{}.sh  root@{}:/root/Desktop/".format(cname,cip))
                system("echo 'y' | rm /root/Desktop/{}.sh".format(cname))
                if status == 0:
                    return HttpResponse("<h1>A file named {}.sh has been sent to you.</h1><h1>Please run this file using 'bash {}.sh' command in your terminal to get required storage</h1>".format(cname,cname))
                else:
                    return HttpResponse("<h1>Failure!</h1>")
                #return HttpResponse("<http><body><h1>Welcome to Block Storage as a service</h1></body></http>")
    return render(request,'myapp/staas.html',{'form' : form})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)  # grabbing the user form data in user_form variable
        profile_form = UserProfileInfoForm(data=request.POST)  # Grabbing the profile form in profile_form
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()    # saving the user form to the databse
            user.set_password(user.password)  # Hashing the password
            user.save()   # save the hash password to the database
            profile = profile_form.save(commit=False) # We are not saving the profile form to the databse yet. This is bcoz with the conflicting with user form
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm() # if the request is not a POST request then we just create an instance of class UserForm() instead of invalidating and saving it to further
        profile_form = UserProfileInfoForm()  #Similer instance of class UserProfileInfoForm
    return render(request,'myapp/registration.html',{'user_form':user_form,'profile_form':profile_form,
                'registered':registered}) # passing context dictnory variable referenced in registration.html file
