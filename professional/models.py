from django.db import models
from django.db.models.fields import BooleanField
from django.utils import timezone
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)

from django_currentuser.db.models import CurrentUserField

from account.models import CustomUser

# Create your models here.

#######  CHOICES FOR LAWS ################

type_of_law = (
    ('civil', 'civil'),
    ('service', 'service'),
    ('criminal', 'criminal'),
    ('taxation', 'taxation'),
    ('corporate', 'corporate'),

)

sub_type_of_law = (

    ('arbitration','arbitration'),
    ('armed force tribunal', 'armed force tribunal'),
    ('banking', 'banking'),
    ('central civil service', 'central civil service'),
    ('comercial court','comercial court'),
    ('company', 'company'),
    ('crpc', 'crpc'),
    ('cyber_crime', 'cyber_crime'),
    ('fema', 'fema'),
    ('gst', 'gst'),
    ('ipc', 'ipc'),
    ('it', 'it'),
    ('land acquisation','land acquisation'),
    ('nclt', 'nclt'),
    ('ndps', 'ndps'),
    ('ni_act', 'ni_act'),
    ('others', 'others'),
    ('para military', 'para military'),
    ('pc act','pc act'),
    ('pmla', 'pmla'),
    ('pocso', 'pocso'),
    ('sebi', 'sebi'),
    ('service-tax', 'service-tax'),
    ('specific performance','specific performance'),
    ('vat', 'vat'),


)

category= (
    ('antibail', 'anticipatory bail'),
    ('arbitration', 'arbitration'),
    ('bail', 'bail'),
    ('binding precedent', 'bindin precedent'),
    ('contempt', 'contempt'),
    ('execution of decree', 'executuon of decree'),
    ('fop', 'fixation of pay'),
    ('limitations', 'limitations'),
    ('negative equality', 'negative equality'),
    ('od/ss/rd', 'Obitor Dicta / Sub Silenso-Ratio/ Decidendi'),
    ('preliminary investigation', 'preliminary investigation'),
    ('pro dpc', 'Procedure Dpc'),
    ('review', 'review'),
    ('reference', 'reference'),
    ('sas', 'search and seizure'),
    ('s/pl', 'statutory/procedure law'),
    ('sba', 'substitution by amendment'),
    ('special relief', 'special relief'),
    ('tap', 'transfer and posting'),
    ('u/p', 'upgradation/promotion'),
    ('zimma', 'zimma'),
)

INSTITUTION = (
    ('Commission', 'Commission'),
    ('The Supreme Court of India', 'The Supreme Court of India'),
    ('The Allahabad High Court', 'Allahabad High Court'),
    ('The Andhra Pradesh High Court', 'Andhra Pradesh High Court'),
    ('The Bombay High Court', 'Bombay High Court'),
    ('The Calcutta High Court', 'Calcutta High Court'),
    ('The Chhattisgarh High Court', 'Chhattisgarh High Court'),
    ('The Delhi High Court', 'Delhi High Court'),
    ('The Gujarat High Court', 'Gujarat High Court'),
    ('The Guwahati High Court', 'Guwahati High Court'),
    ('The Himachal Pradesh High Court', 'Himachal Pradesh High Court'),
    ('The Jammu and Kashmir High Court', 'Jammu and Kashmir High Court'),
    ('The Jharkhand High Court	', 'Jharkhand High Court'),
    ('The Karnataka High Court', 'Karnataka High Court'),
    ('The Kerala High Court', 'Kerala High Court'),
    ('The Madhya Pradesh High Court', 'Madhya Pradesh High Court'),
    ('The Madras High Court', 'Madras High Court'),
    ('The Manipur High Court', 'Manipur High Court'),
    ('The Meghalaya High Court', 'Meghalaya High Court'),
    ('The Odisha High Court', 'Odisha High Court'),
    ('The Patna High Court', 'Patna High Court'),
    ('The Rajasthan High Court', 'Rajasthan High Court'),
    ('The Telangana High Court', 'Telangana High Court'),
    ('The Tripura High Court', 'Tripura High Court'),
    ('The Uttarakhand High Court', 'Uttarakhand High Court'),
    
    ('Administrative Tribunal', 'Administrative Tribunal'),
    ('Appellate Tribunal for Electricity', 'Appellate Tribunal for Electricity'),
    ('Appellate Tribunal under Smugglers and Foreign Exchange Manipulators Act', 'Appellate Tribunal under Smugglers and Foreign Exchange Manipulators Act'),
    ('Armed Forces Tribunal', 'Armed Forces Tribunal'),
    ('Customs, Excise and Service Tax Appellate Tribunal', 'Customs, Excise and Service Tax Appellate Tribunal'),
    ('Debt Recovery Tribunal', 'Debt Recovery Tribunal'),
    ('Income Tax Appellate Tribunal', 'Income Tax Appellate Tribunal'),
    ('Industrial Tribunal', 'Industrial Tribunal'),
    ('National Companies Law Appellate Tribunal', 'National Companies Law Appellate Tribunal'),
    ('National Consumer Disputes Redressal Commission', 'National Consumer Disputes Redressal Commission'),
    ('National Green Tribunal', 'National Green Tribunal'),
    ('Railway Claims Tribunal', 'Railway Claims Tribunal'),
    ('Securities Appellate Tribunal', 'Securities Appellate Tribunal'),
    ('The Telecom Disputes Settlement and Appellate Tribunal', 'The Telecom Disputes Settlement and Appellate Tribunal'),
)

# tribunal_list = (

#     ('Industrial Tribunal', 'Industrial Tribunal'),
#     ('Income Tax Appellate Tribunal', 'Income Tax Appellate Tribunal'),
#     ('Customs, Excise and Service Tax Appellate Tribunal', 'Customs, Excise and Service Tax Appellate Tribunal'),
#     ('Appellate Tribunal under Smugglers and Foreign Exchange Manipulators Act', 'Appellate Tribunal under Smugglers and Foreign Exchange Manipulators Act'),
#     ('Administrative Tribunal', 'Administrative Tribunal'),
#     ('Railway Claims Tribunal', 'Railway Claims Tribunal'),
#     ('Securities Appellate Tribunal', 'Securities Appellate Tribunal'),
#     ('Debt Recovery Tribunal', 'Debt Recovery Tribunal'),
#     ('The Telecom Disputes Settlement and Appellate Tribunal', 'The Telecom Disputes Settlement and Appellate Tribunal'),
#     (' National Companies Law Appellate Tribunal', ' National Companies Law Appellate Tribunal'),
#     ('Industrial Tribunal', 'Industrial Tribunal'),
#     ('National Consumer Disputes Redressal Commission', 'National Consumer Disputes Redressal Commission'),
#     ('Appellate Tribunal for Electricity', 'Appellate Tribunal for Electricity'),
#     ('Armed Forces Tribunal', 'Armed Forces Tribunal'),
#     ('National Green Tribunal', 'National Green Tribunal'),


# )

citation_type = (

    ('SCC', 'SCC'),
    ('AIR', 'AIR'),
    ('AIOL', 'AIOL'),
    ('MLJ', 'MLJ'),
    ('Scale', 'Scale'),
    ('Supreme', 'Supreme'),
    ('A11CJ', 'A11CJ'),
    ('SCC(L&S)', 'SCC(L&S)'),
    ('FLR', 'FLR'),
    ('MhLJ', 'MhLJ')
)



######### END FOR CHOICES FOR LAWS ##############

class Citation(models.Model):
   
    institution_name =models.CharField(max_length=255, choices=INSTITUTION ,null=True, blank= True)

    # tribunals = models.CharField(max_length=255, choices= tribunal_list,blank=True ,null=True)

    apelLate_type = models.CharField(max_length=255,null=True,help_text="required")

    judge_name = models.TextField(null=True, help_text="required")

    case_no = models.TextField(null=True, help_text="required")
    
    party_name = models.TextField(null=True, help_text="required")

    advocate_petitioner =  models.TextField(null=True, help_text="required", blank=True)
    
    advocate_respondent =  models.TextField(null=True, help_text="required", blank=True)

    judgements= RichTextField(null=True,help_text="required")

    date_of_order= models.DateField(null=True,help_text="required")

    headnote = models.TextField(null=True, help_text="required")
    
    references = RichTextField(help_text="references of previous cases",blank= True,null=True)

    equivalent_citations = models.CharField(max_length=255, blank= True, null= True)


    title= models.TextField(help_text="case number and year (required)" ,null=True)


    sub_title= RichTextField(help_text="main point for decision (required)",null=True)


    
    law_type= models.CharField(max_length=40, choices= type_of_law ,null=True, help_text="required")


    sub_law_type= MultiSelectField(choices= sub_type_of_law ,null=True, help_text="required")


    law_category= models.CharField(max_length=60, choices=category ,null=True, help_text="required")

    reportable = BooleanField(default= False)

    non_reportable = BooleanField(default= False)

    over_ruled = BooleanField(default= False)

    diary_no = models.CharField(max_length=255,blank=True, null=True)

    page_no = models.CharField(max_length=255,blank=True, null=True)

    uploaded_on = models.DateTimeField(blank=True, null=True, auto_now=timezone.now(), editable=False)

    uploaded_by = models.CharField(max_length=255, blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):

        current_user = get_current_authenticated_user()
        
        user =CustomUser.objects.get(email = current_user)

        self.uploaded_by = user.email

        super(Citation, self).save(*args, **kwargs)
   

   
   