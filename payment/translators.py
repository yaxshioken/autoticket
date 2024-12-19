from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class MyModel(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_("Title"), max_length=200)
    )

    def __unicode__(self):
        return self.title
if __name__ == '__main__':
    MyModel.objects.translated(title='cheese omelet')
    MyModel.objects.active_translations(title='cheese omelet')
    print()