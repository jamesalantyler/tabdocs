# TabDocs

**TabDocs** is a free, open-source word processor with multi-document tabs, built in Rust.

Its familiar ribbon interface supports word processing, DOCX import/export, page layout,
formatting, comments, review tools and more. The multi-document functionality is an
independently maintained enhancement to an existing MIT/Apache-2.0 project.

![TabDocs icon](assets/app-icon/tabdocs-source.png)

## Tab features

- Open several documents in one application window with independent editing sessions.
- Switch with Ctrl+Tab and Ctrl+Shift+Tab; create or close individual tabs.
- Independent undo/redo, selection, zoom and scroll state.
- Save prompts for unsaved changes and duplicate-open protection.
- Remember open saved documents, selected tab, tab order and pinned tabs across restarts.
- Pin tabs, reorder tabs, scroll overflowing tabs and manage them by right-click.
- Reopen recently closed tabs with Ctrl+Shift+T.

**Limit:** Session restoration reopens saved files; it is not crash recovery for unsaved edits.

## Building on Windows

Install [Rust](https://rustup.rs/) (MSVC toolchain) and the Visual Studio C++ build tools and Windows SDK.
Then open PowerShell in this repository and run:

```powershell
cargo build --release --locked -p tabdocs
.\target\release\tabdocs.exe
```

Run automated tests:

```powershell
cargo test --locked -p tabdocs-ui-egui
```

CLI build: `cargo build --release --locked -p tabdocs-cli`.

## Licenses, provenance and trademarks

TabDocs is an independently modified distribution of open-source software.
This fork is not affiliated with, authorized by or endorsed by the original project.
The original copyright notices, MIT and Apache 2.0 license files, and third-party
attributions are retained in `NOTICE`, `LICENSE-MIT`, `LICENSE-APACHE` and `ATTRIBUTION.md`.
The original project's restricted logos and promotional imagery have been excluded.
The TabDocs logo is supplied for this fork; its use is governed by its creator.

## Notes

- This source package has been **statically checked, not compiled** in the packaging environment.
  Build and test locally before publishing binaries.
- The fork uses its own preference directory; existing preferences from other distributions
  are not migrated automatically.
- Installer signing and official release automation require your own credentials and publisher information.
