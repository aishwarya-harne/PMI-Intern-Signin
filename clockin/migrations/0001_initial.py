# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-23 13:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruitment_source', models.CharField(default='N/A', max_length=100, verbose_name='Recruitment Source')),
                ('responsible_recruiter', models.CharField(default='N/A', max_length=100, verbose_name='Responsible Recruiter')),
                ('status', models.CharField(default='N/A', max_length=50, verbose_name='Status')),
                ('resource_last_name', models.CharField(default='N/A', max_length=100, verbose_name='Resource Last Name')),
                ('resource_first_name', models.CharField(default='N/A', max_length=100, verbose_name='Resource First Name')),
                ('date_of_hire', models.DateField(default=datetime.date.today, verbose_name='Date of Hire')),
                ('HUBzone', models.BooleanField(default=True, verbose_name='HUBzone')),
                ('resource_type', models.CharField(default='N/A', max_length=100, verbose_name='Resource Type')),
                ('payroll_company', models.CharField(default='N/A', max_length=100, verbose_name='Payroll Company')),
                ('probationary_end', models.DateField(default=datetime.date.today, verbose_name='Probationary End')),
                ('supervisor_name', models.CharField(default='N/A', max_length=100, verbose_name='Supervisor Name')),
                ('resource_email', models.CharField(default='N/A', max_length=100, verbose_name='Resource Email')),
                ('home_address', models.CharField(default='N/A', max_length=100, verbose_name='Home Address')),
                ('resource_telephone', models.CharField(default='000-000-0000', max_length=100, verbose_name='Resource Personal Telephone')),
                ('employment_status', models.CharField(choices=[('C', 'Current'), ('F', 'Former'), ('L', 'Leave')], default='N/A', max_length=50, verbose_name='Employment Status')),
                ('PMI_career_title', models.CharField(default='N/A', max_length=100, verbose_name='PMI Career Title    ')),
                ('department', models.CharField(default='N/A', max_length=100, verbose_name='Department/Project Assigned')),
                ('project_title', models.CharField(default='N/A', max_length=100, verbose_name='Project/Functional Title')),
                ('contract_labor', models.CharField(default='N/A', max_length=100, verbose_name='Contract Labor Category')),
                ('GSA_labor', models.CharField(default='N/A', max_length=100, verbose_name='GSA Labor Category')),
                ('billable', models.CharField(choices=[('B', 'Billable'), ('N', 'Non-Billable')], default='N/A', max_length=50, verbose_name='Billable/Non-Billable')),
                ('GSA_vehicle', models.CharField(default='N/A', max_length=100, verbose_name='GSA Vehicle')),
                ('work_location', models.CharField(default='N/A', max_length=100, verbose_name='Work Location')),
                ('hourly_pay', models.IntegerField(default=0, max_length=50, verbose_name='Hourly Pay Rate')),
                ('GSA_rate', models.CharField(default='N/A', max_length=100, verbose_name='GSA Rate')),
                ('discount', models.IntegerField(default=0, max_length=50, verbose_name='Discount (%)')),
                ('client_bill', models.CharField(default='N/A', max_length=100, verbose_name='Client Bill Rate')),
                ('comments', models.CharField(default='N/A', max_length=400, verbose_name='Comments (Task Codes, Invoicing POC, COI)')),
                ('offer_sent', models.BooleanField(default=True, verbose_name='Offer/Contract Sent')),
                ('clock_sequence', models.IntegerField(default=0, max_length=50, verbose_name='Clock Sequence')),
                ('offer_contract', models.CharField(default='N/A', max_length=100, verbose_name='Offer Contract/NDA FE')),
                ('campin', models.BooleanField(default=True, verbose_name='CAMPIN Sent to Candidate')),
                ('clearance_packet', models.BooleanField(default=True, verbose_name='Clearance Packet Complete')),
                ('clearance_packet_sent', models.BooleanField(default=True, verbose_name='Completed Clearance Packet Sent to JA')),
                ('clearance_packet_submitted', models.BooleanField(default=True, verbose_name='Clearance Packet Submitted to Census')),
                ('cleared_date', models.DateField(default=datetime.date.today, verbose_name='Cleared Date')),
                ('commission_logged', models.BooleanField(default=True, verbose_name='Commission Logged?')),
                ('commission_due', models.DateField(default=datetime.date.today, verbose_name='Commission Due Date')),
                ('PMI_email', models.CharField(default='N/A', max_length=100, verbose_name='PMI Email')),
                ('google_groups', models.CharField(default='N/A', max_length=100, verbose_name='Google Groups')),
                ('toolkit', models.CharField(default='N/A', max_length=100, verbose_name='Toolkit')),
                ('paycom_login', models.CharField(default='N/A', max_length=100, verbose_name='Paycom Login')),
                ('efaact', models.CharField(default='N/A', max_length=100, verbose_name='eFAACT')),
                ('computer', models.CharField(default='N/A', max_length=100, verbose_name='Computer')),
                ('software_r', models.CharField(default='N/A', max_length=400, verbose_name='Software Requests')),
                ('gb_security_r', models.CharField(default='N/A', max_length=400, verbose_name='GB Security Access Request')),
                ('business_cards', models.CharField(default='N/A', max_length=100, verbose_name='Business Cards (if needed provide info to include)')),
                ('orientation_date', models.DateField(default=datetime.date.today, verbose_name='Orientation Date')),
                ('_401k_eligible', models.BooleanField(default=True, verbose_name='401K Eligible')),
                ('completed', models.BooleanField(default=True, verbose_name='Completed')),
                ('termination_date', models.DateField(default=datetime.date.today, verbose_name='Termination Date')),
                ('rehire', models.BooleanField(default=True, verbose_name='Rehire (T/F)')),
            ],
        ),
    ]
