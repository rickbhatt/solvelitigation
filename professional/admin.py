from django.contrib import admin

from .models import Citation

@admin.register(Citation)
class CitationAdmin(admin.ModelAdmin):
    list_display = ('title','law_type','sub_law_type','law_category','court_name','tribunals','commission','date_of_order','uploaded_on', 'uploaded_by')
    ordering= ('-uploaded_on',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('court_name','tribunals','commission','apelLate_type','judge_name','case_no','party_name',' advocate_petitioner','advocate_respondent','judgements','date_of_order',' headnote','references','equivalent_citations','title','sub_title','law_type','sub_law_type', 'law_category',  'reportable', 'non_reportable', 'over_ruled', 'diary_no', 'page_no',)}
         ),
    )
