from django.forms import ModelForm

from squirrel_tracker.models import Squirrel


class SquirrelForm(ModelForm):
    def as_div(self):
        return self._html_output(
            normal_row="""<div class="form-group row %(html_class_attr)s">
	<div class="col-4">%(label)s</div>
	<div class="col-8">%(field)s</div>
	<div class="col-4" style="color: #718093;">%(help_text)s</div>
	<div class="col-4" style="color: #e84118;">%(errors)s</div>
</div>""",
            error_row='<div class="error">%s</div>',
            row_ender='</div>',
            help_text_html=' <div class="help-block">%s</div>',
            errors_on_separate_row=False,
        )

    class Meta:
        model = Squirrel
        fields = '__all__'