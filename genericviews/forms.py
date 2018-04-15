from django import forms


class ProductForm(forms.Form):
    # variable for the name of the product
    name = forms.CharField(label="Name", max_length=100)
    rollNo = forms.CharField(label="Roll No", max_length=15)
    mobile = forms.CharField(label="Mobile", max_length=12)
    complaintType = forms.CharField(label="Complaint Type", max_length=10)
    hostelNo = forms.CharField(label="Hostel No", max_length=5)
    wing = forms.CharField(label="Wing", max_length=5)
    roomNo = forms.CharField(label="Room No", max_length=4)
    complaintTitle = forms.CharField(label="Complaint Title", max_length=100)
    # variable for the description of the product
    compalintDesc = forms.CharField(label="Complaint Description", max_length=350,widget=forms.Textarea)

