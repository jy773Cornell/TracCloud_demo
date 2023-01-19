from django.db import models
from utils.ModelManager import MyModelManager


# User
class User(models.Model):
    UID = models.CharField(verbose_name="UID", primary_key=True, max_length=48)

    Username = models.CharField(verbose_name="User Name", unique=True, max_length=64)
    Password = models.CharField(verbose_name="Password", max_length=32)
    Type = models.ForeignKey(verbose_name="User Type", to="UserType", to_field="UTID", related_name="usertype",
                             null=True,
                             blank=True, on_delete=models.SET_NULL)

    Name = models.CharField(verbose_name="Actual Name", max_length=64)
    BusinessName = models.CharField(verbose_name="Business Name", max_length=256)
    RegistrationNo = models.CharField(verbose_name="Registration No.", null=True, blank=True, max_length=128)
    RegExpireDate = models.DateField(verbose_name="Registration Expire Date", null=True, blank=True)
    Address = models.CharField(verbose_name="Address", null=True, blank=True, max_length=256)
    City = models.CharField(verbose_name="City", null=True, blank=True, max_length=64)
    County = models.CharField(verbose_name="County", null=True, blank=True, max_length=64)
    State = models.CharField(verbose_name="State", null=True, blank=True, max_length=64)
    Zipcode = models.CharField(verbose_name="Zip Code", null=True, blank=True, max_length=16)
    Country = models.CharField(verbose_name="Country", null=True, blank=True, max_length=64)
    Phone = models.CharField(verbose_name="Phone Number", null=True, blank=True, max_length=16)
    Cell = models.CharField(verbose_name="Cell Number", null=True, blank=True, max_length=16)
    Email = models.EmailField(verbose_name="Email", null=True, blank=True)

    AddedBy = models.ForeignKey(verbose_name="Added By", to="User", to_field="UID", related_name="useraddedby",
                                null=True,
                                blank=True, on_delete=models.SET_NULL)
    SelfActivated = models.BooleanField(verbose_name="Self Activated Status")
    Valid = models.BooleanField(verbose_name="Valid Status", default=False)

    objects = MyModelManager()
    objects.prefix("UID")

    def __str__(self):
        return "{} ({})".format(self.Username, self.Type)


# User Type
class UserType(models.Model):
    UTID = models.CharField(verbose_name="UTID", primary_key=True, max_length=48)
    TypeName = models.CharField(verbose_name="Type Name", unique=True, max_length=128)
    InfoDataTable = models.CharField(verbose_name="Info Data Table", null=True, blank=True, max_length=256)
    Valid = models.BooleanField(verbose_name="Valid Status", default=True)

    objects = MyModelManager()
    objects.prefix("UTID")

    def __str__(self):
        return self.TypeName


# User Relation
class UserRelation(models.Model):
    URID = models.CharField(verbose_name="URID", primary_key=True, max_length=48)
    Requester = models.ForeignKey(verbose_name="Requester", to="User", to_field="UID", related_name="requester",
                                  null=True, blank=True, on_delete=models.SET_NULL)
    Provider = models.ForeignKey(verbose_name="Provider", to="User", to_field="UID", related_name="provider", null=True,
                                 blank=True, on_delete=models.SET_NULL)
    RelationType = models.ForeignKey(verbose_name="Relation Type", to="UserRelationType", to_field="URTID",
                                     related_name="relationtype", null=True, blank=True, on_delete=models.SET_NULL)
    AddedBy = models.ForeignKey(verbose_name="Added By", to="User", to_field="UID", related_name="relationaddedby",
                                null=True,
                                blank=True, on_delete=models.SET_NULL)
    Valid = models.BooleanField(verbose_name="Valid Status", default=False)

    objects = MyModelManager()
    objects.prefix("URID")

    def __str__(self):
        return "Relation: {}, Requester: {}, Provider: {}".format(self.RelationType, self.Requester, self.Provider)


# User Relation Type
class UserRelationType(models.Model):
    URTID = models.CharField(verbose_name="URTID", primary_key=True, max_length=48)
    TypeName = models.CharField(verbose_name="Type Name", unique=True, max_length=128)
    Note = models.TextField(verbose_name="Note", null=True, blank=True)
    Valid = models.BooleanField(verbose_name="Valid Status", default=True)

    objects = MyModelManager()
    objects.prefix("URTID")

    def __str__(self):
        return self.TypeName
