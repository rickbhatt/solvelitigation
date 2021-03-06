# Generated by Django 3.2.8 on 2022-02-14 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professional', '0026_auto_20220213_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citation',
            name='court_name',
        ),
        migrations.RemoveField(
            model_name='citation',
            name='tribunals',
        ),
        migrations.AddField(
            model_name='citation',
            name='institution_name',
            field=models.CharField(blank=True, choices=[('Commission', 'Commission'), ('The Supreme Court of India', 'The Supreme Court of India'), ('The Allahabad High Court', 'Allahabad High Court'), ('The Andhra Pradesh High Court', 'Andhra Pradesh High Court'), ('The Bombay High Court', 'Bombay High Court'), ('The Calcutta High Court', 'Calcutta High Court'), ('The Chhattisgarh High Court', 'Chhattisgarh High Court'), ('The Delhi High Court', 'Delhi High Court'), ('The Gujarat High Court', 'Gujarat High Court'), ('The Guwahati High Court', 'Guwahati High Court'), ('The Himachal Pradesh High Court', 'Himachal Pradesh High Court'), ('The Jammu and Kashmir High Court', 'Jammu and Kashmir High Court'), ('The Jharkhand High Court\t', 'Jharkhand High Court'), ('The Karnataka High Court', 'Karnataka High Court'), ('The Kerala High Court', 'Kerala High Court'), ('The Madhya Pradesh High Court', 'Madhya Pradesh High Court'), ('The Madras High Court', 'Madras High Court'), ('The Manipur High Court', 'Manipur High Court'), ('The Meghalaya High Court', 'Meghalaya High Court'), ('The Odisha High Court', 'Odisha High Court'), ('The Patna High Court', 'Patna High Court'), ('The Rajasthan High Court', 'Rajasthan High Court'), ('The Telangana High Court', 'Telangana High Court'), ('The Tripura High Court', 'Tripura High Court'), ('The Uttarakhand High Court', 'Uttarakhand High Court'), ('Industrial Tribunal', 'Industrial Tribunal'), ('Income Tax Appellate Tribunal', 'Income Tax Appellate Tribunal'), ('Customs, Excise and Service Tax Appellate Tribunal', 'Customs, Excise and Service Tax Appellate Tribunal'), ('Appellate Tribunal under Smugglers and Foreign Exchange Manipulators Act', 'Appellate Tribunal under Smugglers and Foreign Exchange Manipulators Act'), ('Administrative Tribunal', 'Administrative Tribunal'), ('Railway Claims Tribunal', 'Railway Claims Tribunal'), ('Securities Appellate Tribunal', 'Securities Appellate Tribunal'), ('Debt Recovery Tribunal', 'Debt Recovery Tribunal'), ('The Telecom Disputes Settlement and Appellate Tribunal', 'The Telecom Disputes Settlement and Appellate Tribunal'), (' National Companies Law Appellate Tribunal', ' National Companies Law Appellate Tribunal'), ('Industrial Tribunal', 'Industrial Tribunal'), ('National Consumer Disputes Redressal Commission', 'National Consumer Disputes Redressal Commission'), ('Appellate Tribunal for Electricity', 'Appellate Tribunal for Electricity'), ('Armed Forces Tribunal', 'Armed Forces Tribunal'), ('National Green Tribunal', 'National Green Tribunal')], max_length=255, null=True),
        ),
    ]
