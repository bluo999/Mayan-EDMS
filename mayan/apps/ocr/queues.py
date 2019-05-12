from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from mayan.apps.task_manager.classes import CeleryQueue

queue_ocr = CeleryQueue(name='ocr', label=_('OCR'))
queue_ocr.add_task_type(
    dotted_path='mayan.apps.ocr.tasks.task_do_ocr',
    label=_('Document version OCR')
)
