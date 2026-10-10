# TabDocs rebranding notes

The source was rebranded from an upstream open-source project. The original protected logo directory
and screenshots were removed; app icons are generated from `assets/app-icon/tabdocs-source.png`.
The internal Rust packages and binary targets are now named `tabdocs`, `tabdocs-cli` and `tabdocs-web`.
Old application preferences do **not** migrate automatically to the new TabDocs settings directory.

## Windows build

1. Extract the archive to a new folder (do not overwrite the working tab-enabled build).
2. Open PowerShell in the extracted `TabDocs` folder.
3. Run `cargo build --release --locked -p tabdocs`.
4. Launch `.\target\release\tabdocs.exe`.
5. Run `cargo test --locked -p tabdocs-ui-egui`.

This build has **not** been compiled in the packaging environment.

## License

Keep `LICENSE-MIT`, `LICENSE-APACHE`, `NOTICE` and relevant lines in `ATTRIBUTION.md` intact.
Original attribution is a legal notice, not an endorsement. Do not strip it out when publishing.

## Distribution cautions

* Update your fork's package publisher, signing certificates and repository URLs as appropriate.
* The supplied TabDocs PNG is the only app branding source; `python packaging/generate-icons.py`
  regenerates Windows/macOS/Linux icons (requires Pillow).
* The macOS disk-image layout needs validation on macOS before publishing a DMG.
