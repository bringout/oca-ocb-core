from PyPDF2 import errors, filters, generic, PdfReader, PdfWriter as _Writer
from PyPDF2.generic import create_string_object

__all__ = [
    "PdfReader",
    "PdfWriter",
    "create_string_object",
    "errors",
    "filters",
    "generic",
]


class PdfWriter(_Writer):
    def getFields(self, *args, **kwargs):
        return self.get_fields(*args, **kwargs)

    def _addObject(self, *args, **kwargs):
        return self._add_object(*args, **kwargs)

    def cloneReaderDocumentRoot(self, reader):
        # PyPDF2 3.0 renamed camelCase to snake_case and removed the old names
        return self.clone_reader_document_root(reader)
