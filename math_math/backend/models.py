from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from DjangoUeditor.models import UEditorField


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content_ueditor = UEditorField('content', width="1000", height="600", imagePath="upload/ueditor/images/",\
                           filePath="upload/ueditor/files/", default='')
    content_ckeditor = RichTextUploadingField()