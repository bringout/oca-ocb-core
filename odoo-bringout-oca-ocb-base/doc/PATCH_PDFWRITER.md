# PyPDF2 Compatibility Patch

## Overview

This patch addresses the PyPDF2 deprecation error that occurs when using PyPDF2 version 3.0.0 or higher with Odoo. The original error was:

```
PyPDF2.errors.DeprecationError: PdfFileWriter is deprecated and was removed in PyPDF2 3.0.0. Use PdfWriter instead.
```

## Problem

In PyPDF2 3.0.0, several classes and methods were deprecated and removed:
- `PdfFileWriter` → `PdfWriter`
- `PdfFileReader` → `PdfReader` 
- `addPage()` → `add_page()`
- `addMetadata()` → `add_metadata()`
- `getNumPages()` → `len(pages)`
- `getPage(n)` → `pages[n]`
- `appendPagesFromReader()` → `append_pages_from_reader()`
- `_addObject()` → `_add_object()`

## Solution

This patch provides backward compatibility by creating wrapper classes that:
1. Inherit from the new PyPDF2 classes (`PdfWriter`, `PdfReader`)
2. Provide the old method signatures as compatibility methods
3. Gracefully handle both old and new PyPDF2 versions

## Files Modified

### 1. `odoo/tools/pdf.py`
- Added compatibility wrapper classes `PdfFileWriter` and `PdfFileReader`
- Updated import logic to handle both PyPDF2 2.x and 3.x
- Added method aliases for deprecated methods
- Updated `BrandedFileWriter` class to use new API with fallback

### 2. `odoo/addons/base/models/ir_actions_report.py`
- Added compatibility import logic
- Created local compatibility classes with required method aliases
- Added support for `numPages` property and related methods

## Implementation Details

### Compatibility Import Pattern
```python
try:
    from PyPDF2 import PdfReader, PdfWriter
    
    # Create compatibility classes
    class PdfFileWriter(PdfWriter):
        def addPage(self, page):
            return self.add_page(page)
        
        def addMetadata(self, metadata):
            return self.add_metadata(metadata)
        
        def _addObject(self, obj):
            return self._add_object(obj)
    
    class PdfFileReader(PdfReader):
        def getNumPages(self):
            return len(self.pages)
        
        def getPage(self, page_num):
            return self.pages[page_num]

except ImportError:
    # Fallback to old API for older PyPDF2 versions
    from PyPDF2 import PdfFileWriter, PdfFileReader
```

### Method Compatibility Mapping
| Old Method (PyPDF2 < 3.0) | New Method (PyPDF2 ≥ 3.0) | Compatibility Method |
|---------------------------|---------------------------|---------------------|
| `PdfFileWriter.addPage()` | `PdfWriter.add_page()` | ✅ Wrapped |
| `PdfFileWriter.addMetadata()` | `PdfWriter.add_metadata()` | ✅ Wrapped |
| `PdfFileWriter._addObject()` | `PdfWriter._add_object()` | ✅ Wrapped |
| `PdfFileReader.getNumPages()` | `len(PdfReader.pages)` | ✅ Wrapped |
| `PdfFileReader.getPage()` | `PdfReader.pages[]` | ✅ Wrapped |
| `PdfFileWriter.appendPagesFromReader()` | `PdfWriter.append_pages_from_reader()` | ✅ Wrapped |

## Testing

The patch has been tested with:
- PyPDF2 3.0.0+ (new API)
- PyPDF2 2.x (old API via fallback)
- `OdooPdfFileWriter` instantiation
- PDF generation workflows
- Report generation (original error case)

## Branch Information

- **Branch**: `pdfwrite`
- **Based on**: Current main/master branch
- **Type**: Compatibility patch
- **Impact**: Backward compatible - no breaking changes

## Author

- **Developer**: Ernad Husremović (hernad@bring.out.ba)
- **Company**: bring.out.doo Sarajevo
- **Date**: 2025-09-02

## Related Issues

This patch resolves the PyPDF2 deprecation error encountered in:
- Report generation (`/report/pdf/` endpoints)
- PDF merge operations
- PDF attachment handling
- Account EDI PDF operations

## Future Considerations

While this patch provides immediate compatibility, consider:
1. Eventually migrating to the new PyPDF2 API directly
2. Monitoring PyPDF2 changelog for future deprecations
3. Testing with future PyPDF2 versions

## Installation

This patch is automatically applied when using the `pdfwrite` branch. No additional installation steps required.