# Generated by Django 3.2.8 on 2022-02-18 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professional', '0029_alter_citation_sub_law_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citation',
            name='law_category',
            field=models.CharField(choices=[('antibail', 'anticipatory bail'), ('arbitration', 'arbitration'), ('bail', 'bail'), ('binding precedent', 'bindin precedent'), ('cocpr', 'code of civil procedure'), ('contempt', 'contempt'), ('contract', 'contract'), ('evidence', 'evidence'), ('execution of decree', 'executuon of decree'), ('fop', 'fixation of pay'), ('limitations', 'limitations'), ('mad', 'marriage and divorce'), ('negative equality', 'negative equality'), ('od/ss/rd', 'Obitor Dicta / Sub Silenso-Ratio/ Decidendi'), ('preliminary investigation', 'preliminary investigation'), ('pro dpc', 'Procedure Dpc'), ('review', 'review'), ('reference', 'reference'), ('sas', 'search and seizure'), ('s/pl', 'statutory/procedure law'), ('sba', 'substitution by amendment'), ('special relief', 'special relief'), ('tap', 'transfer and posting'), ('top', 'transfer of property'), ('u/p', 'upgradation/promotion'), ('zimma', 'zimma')], help_text='required', max_length=60, null=True),
        ),
    ]
