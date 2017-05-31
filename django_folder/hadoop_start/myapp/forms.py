from django import forms
from django.contrib.auth.models import User
from myapp.models import UserProfileInfo

class StorageFormName(forms.Form):
        name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
        storage_dir = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
        #storage_type = forms.CharField()
        CHOICES=[('choice1','Object Storage'),
         ('choice2','Block Storage')]
        storage_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
        storage_security_choices = (('select1', 'Secure'),('select2', 'Not Secure'),('select3', 'High Available(HA)'),)
        storage_security = forms.CharField(widget=forms.Select(choices = storage_security_choices,attrs={'class' : 'form-control'}))
        size = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control'}))

class IaasForm(forms.Form):
    vm_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}),label='VM Name')
    CHOICES=[('select1','Windows'),('select2','Linux')]
    client_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Are you a ?')
    instance_choices1 = (('select1', 'Linux'),('select2', 'Windows'),)
    instance_type = forms.CharField(widget=forms.Select(choices = instance_choices1,attrs={'class' : 'form-control'}),label='Instance Type')
    instance_choices2 = (('select1', 'Ubuntu'),('select2', 'Kali'),('select3', 'linuxmint'),('select4', 'RHEL6'),('select5', 'RHEL7'),)
    instance_variant = forms.CharField(required=False, widget=forms.Select(choices = instance_choices2,attrs={'class' : 'form-control'}),label='Instance Variant')
    RAM = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control'}),label='RAM')
    vCPUs = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control'}),label='Virtual CPUs')
    HDD = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control'}),label='Hard Disk')
    network_inst_choices = (('select1', 'Via img file'),('select2', 'Via FTP'),('select3', 'Via HTTP'))
    network_install_type = forms.CharField(widget=forms.Select(choices = network_inst_choices,attrs={'class' : 'form-control'}),label='Network Installation Type')
    CHOICES=[('select1','Yes'),
     ('select2','No')]
    bridge = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Do you want Bridge Connectivity ?')
    provision_choices = (('select1','Enable Thick Provisioning'),('select2','Enable Thin Provisioning'))
    provision = forms.CharField(widget=forms.Select(choices = provision_choices,attrs={'class' : 'form-control'}),label='Which Provisioning do you want ?')
    access_choices = (('select1', 'Through TigerVNC'),('select2', 'Through NoVNC'),)
    access_type = forms.CharField(widget=forms.Select(choices = access_choices,attrs={'class' : 'form-control'}),label='Access Type')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password','email')

class SaasForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    software_choices = (('select1', 'firefox'),('select2', 'atom editor'),('select3', 'terminal'),('select4' , 'xterminal'),('select5' , 'Google Chrome'),('select6', 'virt-manager'),('select7', 'virt-viewer'))
    software_name = forms.CharField(widget=forms.Select(choices = software_choices,attrs={'class' : 'form-control'}))
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
