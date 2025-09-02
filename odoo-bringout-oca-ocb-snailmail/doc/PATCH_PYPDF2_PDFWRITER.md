# PyPDF2 Compatibility Patch - Snailmail

## Overview

This patch addresses the PyPDF2 deprecation error in the snailmail module when using PyPDF2 version 3.0.0 or higher. The original error was:

```
PyPDF2.errors.DeprecationError: PdfFileWriter is deprecated and was removed in PyPDF2 3.0.0. Use PdfWriter instead.
```

## Problem

In PyPDF2 3.0.0, several classes and methods were deprecated and removed:
- `PdfFileWriter` → `PdfWriter`
- `PdfFileReader` → `PdfReader` 
- `addPage()` → `add_page()`
- `appendPagesFromReader()` → `append_pages_from_reader()`
- `getPage(n)` → `pages[n]`

## Affected Functionality

The snailmail module uses PyPDF2 for:
- Appending cover pages to invoices (`_append_cover_page` method)
- Adding blank buffer pages 
- Merging PDF pages
- PDF page manipulation for postal services

## Solution

This patch provides backward compatibility by creating wrapper classes that:
1. Inherit from the new PyPDF2 classes (`PdfWriter`, `PdfReader`)
2. Provide the old method signatures as compatibility methods
3. Gracefully handle both old and new PyPDF2 versions

## Files Modified

### `snailmail/models/snailmail_letter.py`
- Added compatibility import logic
- Created local compatibility classes with required method aliases:
  - `PdfFileWriter.addPage()` → `PdfWriter.add_page()`
  - `PdfFileWriter.appendPagesFromReader()` → `PdfWriter.append_pages_from_reader()`
  - `PdfFileReader.getPage()` → `PdfReader.pages[]`

## Implementation Details

### Compatibility Import Pattern
```python
try:
    from PyPDF2 import PdfWriter, PdfReader
    
    # Create compatibility classes for PyPDF2 3.0+
    class PdfFileWriter(PdfWriter):
        def addPage(self, page):
            return self.add_page(page)
        
        def appendPagesFromReader(self, reader, after_page_append=None):
            return self.append_pages_from_reader(reader, after_page_append)
    
    class PdfFileReader(PdfReader):
        def getPage(self, page_num):
            return self.pages[page_num]

except ImportError:
    # Fallback to old API for older PyPDF2 versions
    from PyPDF2 import PdfFileWriter, PdfFileReader
```

## Testing

The patch has been tested with:
- PyPDF2 3.0.0+ (new API)
- PyPDF2 2.x (old API via fallback)
- Cover page attachment functionality
- PDF merge operations in snailmail workflows

## Branch Information

- **Branch**: `pdfwrite`
- **Based on**: Current master branch
- **Type**: Compatibility patch
- **Impact**: Backward compatible - no breaking changes

## Author

- **Developer**: Ernad Husremović (hernad@bring.out.ba)
- **Company**: bring.out.doo Sarajevo
- **Date**: 2025-09-02

## Related Issues

This patch resolves the PyPDF2 deprecation error encountered in:
- Snailmail cover page generation
- Invoice PDF processing
- Postal service document handling

## Installation

This patch is automatically applied when using the `pdfwrite` branch. No additional installation steps required.

## Future Considerations

While this patch provides immediate compatibility, consider:
1. Eventually migrating to the new PyPDF2 API directly
2. Testing with future PyPDF2 versions
3. Coordinating with main oca-ocb-base PyPDF2 compatibility efforts