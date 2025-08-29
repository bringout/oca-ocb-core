# Patch: Fix Bosnian Translation File Errors

## Module: base_setup

### Description
This patch fixes critical syntax and structural errors in the Bosnian (bs) translation file that were causing Odoo view parsing errors. The issues involved msgid/msgstr mismatches where the translation content didn't match the structure of the source English text.

### Files Modified
- `base_setup/i18n/bs.po`

### Issues Fixed

#### 1. Company/Companies Entry Mismatch
**Location**: Lines 346-347
**Problem**: The msgid contained HTML spans with `attrs` attributes for Company/Companies, but the msgstr contained completely different HTML content about building icons.

**Before**:
```po
msgid "<span class=\"o_form_label\" attrs=\"{'invisible':[('company_count', '&gt;', '1')]}\">\n                                            Company\n                                        </span>\n                                        <span class=\"o_form_label\" attrs=\"{'invisible':[('company_count', '&lt;=', '1')]}\">\n                                            Companies\n                                        </span>\n                                        <br/>"
msgstr "<i class=\"fa fa-lg fa-building-o\"/>\n                                            <span class=\"Tekst-muted\">\n                                                the creation of documents between your companies\n                                            </span>"
```

**After**:
```po
msgid "<span class=\"o_form_label\" attrs=\"{'invisible':[('company_count', '&gt;', '1')]}\">\n                                            Company\n                                        </span>\n                                        <span class=\"o_form_label\" attrs=\"{'invisible':[('company_count', '&lt;=', '1')]}\">\n                                            Companies\n                                        </span>\n                                        <br/>"
msgstr "<span class=\"o_form_label\" attrs=\"{'invisible':[('company_count', '&gt;', '1')]}\">\n                                            Kompanija\n                                        </span>\n                                        <span class=\"o_form_label\" attrs=\"{'invisible':[('company_count', '&lt;=', '1')]}\">\n                                            Kompanije\n                                        </span>\n                                        <br/>"
```

#### 2. "About" Entry Mismatch
**Location**: Lines 358-359
**Problem**: Simple text msgid "About" had HTML content in msgstr instead of simple translation.

**Before**:
```po
msgid "About"
msgstr "<span class=\"o_form_label\">Format</span>\n                                        <span class=\"fa fa-lg fa-building-o\" title=\"Vrednosti postavljene ovde su specifične za kompaniju.\" aria-label=\"Vrednosti postavljene ovde su specifične za kompaniju.\" groups=\"base.group_multi_company\" role=\"img\"/>"
```

**After**:
```po
msgid "About"
msgstr "O programu"
```

#### 3. "Save" Instruction Mismatch
**Location**: Lines 28-29
**Problem**: HTML instruction with `<strong>` tags had completely different HTML content in msgstr.

**Before**:
```po
msgid "<strong>Save</strong> this page and come back here to set up the feature."
msgstr "<span class=\"o_form_label\">Šablon dokumenta</span>\n                                        <span class=\"fa fa-lg fa-building-o\" title=\"Vrednosti postavljene ovde su specifične za kompaniju.\" aria-label=\"Vrednosti postavljene ovde su specifične za kompaniju.\" groups=\"base.group_multi_company\" role=\"img\"/>"
```

**After**:
```po
msgid "<strong>Save</strong> this page and come back here to set up the feature."
msgstr "<strong>Sačuvajte</strong> ovu stranicu i vratite se ovdje da postavite funkciju."
```

#### 4. Extra Blank Line Removal
**Location**: Line 405
**Problem**: Extra blank line causing malformed PO file syntax.
**Fix**: Removed the extra blank line to maintain proper PO file structure.

### Technical Details

**Root Cause**: The translation file contained entries where the msgstr (translation) content was copied from different entries, creating structural mismatches that caused Odoo's view parser to fail when processing `attrs` attributes.

**Error Symptoms**:
- `SyntaxError: unexpected character after line continuation character`
- `\"{'invisible':` parsing errors in Odoo logs
- View cache corruption issues

**Validation**: 
- PO file now passes `msgfmt --check` validation
- All msgid/msgstr pairs maintain structural consistency
- HTML attributes and tags are properly preserved in translations

### Impact
- Resolves Odoo view parsing errors caused by malformed translation entries
- Ensures proper display of dynamic UI elements with visibility conditions
- Maintains consistency between English source and Bosnian translations
- Prevents view cache corruption issues

### Reason
Critical bug fix to ensure proper functioning of Odoo views with Bosnian language locale. The mismatched translations were causing system-wide view rendering failures.

### Future Translation Updates

**Important Workflow Note**: 
For future updates to Bosnian translations (bs.po files), the proper workflow is:

1. **Update the master translation file**: `packages/TRANSLATION_BS.xlsx`
2. **Use translation scripts**: Run `scripts/translation_bs*` scripts to propagate changes
3. **Avoid direct .po file editing**: Direct editing of individual .po files should be avoided as it bypasses the centralized translation management system

This ensures consistency across all modules and prevents translation drift between the master Excel file and individual .po files.

**Translation Quality**: If any of the translations in this patch need improvement, they should be corrected in the next translation cycle using the proper workflow above.


### Ernad

packages/odoo-bringout-oca-ocb-base_setup/base_setup/i18n


Ovo ručno postaviti:

```
msgid ""
"<span class=\"o_form_label\" attrs=\"{'invisible':[('active_user_count', '&gt;', '1')]}\">\n"
"                                            Active User\n"
"                                        </span>\n"
"                                        <span class=\"o_form_label\" attrs=\"{'invisible':[('active_user_count', '&lt;=', '1')]}\">\n"
"                                            Active Users\n"
"                                        </span>"
msgstr ""
"<span class=\"o_form_label\" attrs=\"{'invisible':[('active_user_count', '&gt;', '1')]}\">\n"
"                                            Activni korisnik\n"
"                                        </span>\n"
"                                        <span class=\"o_form_label\" attrs=\"{'invisible':[('active_user_count', '&lt;=', '1')]}\">\n"
"                                            Activni korisnici\n"
"                                        </span>"

#. module: base_setup
#: model_terms:ir.ui.view,arch_db:base_setup.res_config_settings_view_form
msgid ""
"<span class=\"o_form_label\" attrs=\"{'invisible':[('company_count', '&gt;', '1')]}\">\n"
"                                            Company\n"
"                                        </span>\n"
"                                        <span class=\"o_form_label\" attrs=\"{'invisible':[('company_count', '&lt;=', '1')]}\">\n"
"                                            Companies\n"
"                                        </span>\n"
"                                        <br/>"
msgstr ""
"<span class=\"o_form_label\" attrs=\"{'invisible':[('company_count', '&gt;', '1')]}\">\n"
"                                            Preduzeće\n"
"                                        </span>\n"
"                                        <span class=\"o_form_label\" attrs=\"{'invisible':[('company_count', '&lt;=', '1')]}\">\n"
"                                            Preduzeća\n"
"                                        </span>\n"
"                                        <br/>"


#. module: base_setup
#: model_terms:ir.ui.view,arch_db:base_setup.res_config_settings_view_form
msgid ""
"<span class=\"o_form_label\" attrs=\"{'invisible':[('language_count', '&gt;', '1')]}\">\n"
"                                                language\n"
"                                            </span>\n"
"                                            <span class=\"o_form_label\" attrs=\"{'invisible':[('language_count', '&lt;=', '1')]}\">\n"
"                                                languages\n"
"                                            </span>"
msgstr ""
"<span class=\"o_form_label\" attrs=\"{'invisible':[('language_count', '&gt;', '1')]}\">\n"
"                                                jezik\n"
"                                            </span>\n"
"                                            <span class=\"o_form_label\" attrs=\"{'invisible':[('language_count', '&lt;=', '1')]}\">\n"
"                                                jezici\n"
"                                            </span>"
```



---
**Patch Created:** 2025-08-27  
**Applied By:** Claude Code Assistant  
**Severity:** Critical - System functionality impact  
**Note**: Emergency patch - future translation updates should follow proper workflow via TRANSLATION_BS.xlsx
