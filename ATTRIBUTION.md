# Asset attribution

Every non-code asset in this repository (fonts, icons, images, example documents) is listed here with its author, source and licence. `cargo xtask assets` (part of `cargo xtask ci`) fails if an asset file is missing from this table.

**Policy:** Protected upstream trademarks and logo artwork have been excluded from this fork.
The TabDocs application logo originates from the fork maintainer's supplied artwork. Existing
open-licensed fonts, dictionaries and other third-party assets keep their upstream licenses.
See `NOTICE`, `LICENSE-MIT` and `LICENSE-APACHE` for the original authorship requirements.

Generated-in-code art is original and has no file to list: the UI icon set (`crates/ui-egui/src/icons.rs`), the sample documents and templates (`crates/engine/src/sample.rs`), the table and style previews, and theme colours (`crates/engine/src/cmd/design.rs`).

| Asset | Author | Source | Licence | Notes |
|---|---|---|---|---|
| `assets/app-icon/tabdocs-source.png` | TabDocs fork creator (user-provided) | Supplied logo | User-supplied branding | Replacement identity asset; confirm reuse rights before redistribution |
| `assets/app-icon/tabdocs-1024.png` | TabDocs fork creator | Generated from tabdocs-source.png | Same as source | Branded app icon |
| `assets/app-icon/tabdocs-macos-512.png` | TabDocs fork creator | Generated from tabdocs-source.png | Same as source | macOS app icon |
| `assets/app-icon/tabdocs.ico` | TabDocs fork creator | Generated from tabdocs-source.png | Same as source | Windows executable/installer icon |
| `assets/app-icon/tabdocs.icns` | TabDocs fork creator | Generated from tabdocs-source.png | Same as source | macOS application icon |
| `assets/app-icon/tabdocs.svg` | TabDocs fork creator | Embedded supplied PNG | Same as source | Source for other sizes |
| `assets/app-icon/hicolor/16x16/apps/org.tabdocs.TabDocs.png` | TabDocs fork creator | Generated from tabdocs-source.png | Same as source | Linux icon |
| `assets/app-icon/hicolor/24x24/apps/org.tabdocs.TabDocs.png` | TabDocs fork creator | Generated from tabdocs-source.png | Same as source | Linux icon |
| `assets/app-icon/hicolor/32x32/apps/org.tabdocs.TabDocs.png` | TabDocs fork creator | Generated from tabdocs-source.png | Same as source | Linux icon |
| `assets/app-icon/hicolor/48x48/apps/org.tabdocs.TabDocs.png` | TabDocs fork creator | Generated from tabdocs-source.png | Same as source | Linux icon |
| `assets/app-icon/hicolor/64x64/apps/org.tabdocs.TabDocs.png` | TabDocs fork creator | Generated from tabdocs-source.png | Same as source | Linux icon |
| `assets/app-icon/hicolor/128x128/apps/org.tabdocs.TabDocs.png` | TabDocs fork creator | Generated from tabdocs-source.png | Same as source | Linux icon |
| `assets/app-icon/hicolor/256x256/apps/org.tabdocs.TabDocs.png` | TabDocs fork creator | Generated from tabdocs-source.png | Same as source | Linux icon |
| `assets/app-icon/hicolor/512x512/apps/org.tabdocs.TabDocs.png` | TabDocs fork creator | Generated from tabdocs-source.png | Same as source | Linux icon |
| `assets/app-icon/hicolor/scalable/apps/org.tabdocs.TabDocs.svg` | TabDocs fork creator | Embedded supplied PNG | Same as source | Linux scalable wrapper |
| `packaging/macos/dmg/background.svg` | TabDocs fork maintainer | New minimalist background | Same as TabDocs source | macOS DMG artwork |
| `packaging/macos/dmg/background.tiff` | TabDocs fork maintainer | Generated from supplied icon | Same as TabDocs source | macOS DMG background |

| `assets/hyphenation/en-us.pat` | DesignCraft contributors (generated) | trained from the Moby list by DesignCraft's patgen | Public Domain (CC0-1.0) | Our own Liang hyphenation patterns (no TeX patterns) |
| `assets/hyphenation/en-us.dic` | Grady Ward (Moby Hyphenator II word list); converted by DesignCraft contributors | https://www.gutenberg.org/ebooks/3204 (file `mhyph.txt`, SHA-256 `eeb30474c86b8af3469035ec1a0913e35905325ca885290db9dfed9881e230ac`), via DesignCraft | Public Domain | ~165k words with break points; drives spelling and hyphenation |
| `assets/fonts/Inter-Medium.ttf` | Rasmus Andersson / The Inter Project Authors | https://github.com/rsms/inter | OFL-1.1 (`assets/fonts/OFL-Inter.txt`) | Open-source typeface (Latin UI/document font, carried over from DesignCraft) |
| `assets/fonts/Inter-Regular.ttf` | Rasmus Andersson / The Inter Project Authors | https://github.com/rsms/inter | OFL-1.1 (`assets/fonts/OFL-Inter.txt`) | Open-source typeface (Latin UI/document font, carried over from DesignCraft) |
| `assets/fonts/Inter-SemiBold.ttf` | Rasmus Andersson / The Inter Project Authors | https://github.com/rsms/inter | OFL-1.1 (`assets/fonts/OFL-Inter.txt`) | Open-source typeface (Latin UI/document font, carried over from DesignCraft) |
| `assets/fonts/JetBrainsMono-Regular.ttf` | The JetBrains Mono Project Authors | https://github.com/JetBrains/JetBrainsMono | OFL-1.1 (`assets/fonts/OFL-JetBrainsMono.txt`) | Open-source typeface (Latin UI/document font, carried over from DesignCraft) |
| `assets/fonts/OFL-Inter.txt` | (licence text) | upstream project | — |  |
| `assets/fonts/OFL-JetBrainsMono.txt` | (licence text) | upstream project | — |  |
| `assets/fonts/OFL-SourceSans3.txt` | (licence text) | upstream project | — |  |
| `assets/fonts/OFL-SourceSerif4.txt` | (licence text) | upstream project | — |  |
| `assets/fonts/SourceSans3-Bold.ttf` | Paul D. Hunt / Frank Grießhammer, Adobe (released as open source) | https://github.com/adobe-fonts/source-sans · https://github.com/adobe-fonts/source-serif | OFL-1.1 (`assets/fonts/OFL-SourceSans3.txt`, `OFL-SourceSerif4.txt`) | Open-source typeface (Latin UI/document font, carried over from DesignCraft) |
| `assets/fonts/SourceSans3-It.ttf` | Paul D. Hunt / Frank Grießhammer, Adobe (released as open source) | https://github.com/adobe-fonts/source-sans · https://github.com/adobe-fonts/source-serif | OFL-1.1 (`assets/fonts/OFL-SourceSans3.txt`, `OFL-SourceSerif4.txt`) | Open-source typeface (Latin UI/document font, carried over from DesignCraft) |
| `assets/fonts/SourceSans3-Regular.ttf` | Paul D. Hunt / Frank Grießhammer, Adobe (released as open source) | https://github.com/adobe-fonts/source-sans · https://github.com/adobe-fonts/source-serif | OFL-1.1 (`assets/fonts/OFL-SourceSans3.txt`, `OFL-SourceSerif4.txt`) | Open-source typeface (Latin UI/document font, carried over from DesignCraft) |
| `assets/fonts/SourceSans3-Semibold.ttf` | Paul D. Hunt / Frank Grießhammer, Adobe (released as open source) | https://github.com/adobe-fonts/source-sans · https://github.com/adobe-fonts/source-serif | OFL-1.1 (`assets/fonts/OFL-SourceSans3.txt`, `OFL-SourceSerif4.txt`) | Open-source typeface (Latin UI/document font, carried over from DesignCraft) |
| `assets/fonts/SourceSerif4-Bold.ttf` | Paul D. Hunt / Frank Grießhammer, Adobe (released as open source) | https://github.com/adobe-fonts/source-sans · https://github.com/adobe-fonts/source-serif | OFL-1.1 (`assets/fonts/OFL-SourceSans3.txt`, `OFL-SourceSerif4.txt`) | Open-source typeface (Latin UI/document font, carried over from DesignCraft) |
| `assets/fonts/SourceSerif4-BoldIt.ttf` | Paul D. Hunt / Frank Grießhammer, Adobe (released as open source) | https://github.com/adobe-fonts/source-sans · https://github.com/adobe-fonts/source-serif | OFL-1.1 (`assets/fonts/OFL-SourceSans3.txt`, `OFL-SourceSerif4.txt`) | Open-source typeface (Latin UI/document font, carried over from DesignCraft) |
| `assets/fonts/SourceSerif4-It.ttf` | Paul D. Hunt / Frank Grießhammer, Adobe (released as open source) | https://github.com/adobe-fonts/source-sans · https://github.com/adobe-fonts/source-serif | OFL-1.1 (`assets/fonts/OFL-SourceSans3.txt`, `OFL-SourceSerif4.txt`) | Open-source typeface (Latin UI/document font, carried over from DesignCraft) |
| `assets/fonts/SourceSerif4-Regular.ttf` | Paul D. Hunt / Frank Grießhammer, Adobe (released as open source) | https://github.com/adobe-fonts/source-sans · https://github.com/adobe-fonts/source-serif | OFL-1.1 (`assets/fonts/OFL-SourceSans3.txt`, `OFL-SourceSerif4.txt`) | Open-source typeface (Latin UI/document font, carried over from DesignCraft) |
| `assets/fonts/SourceSerif4-Semibold.ttf` | Paul D. Hunt / Frank Grießhammer, Adobe (released as open source) | https://github.com/adobe-fonts/source-sans · https://github.com/adobe-fonts/source-serif | OFL-1.1 (`assets/fonts/OFL-SourceSans3.txt`, `OFL-SourceSerif4.txt`) | Open-source typeface (Latin UI/document font, carried over from DesignCraft) |
| craft-fonts (optional build input, not files in this repo): BIZ UDPGothic, BIZ UDMincho, Shippori Mincho | see https://github.com/storytold/craft-fonts/blob/main/ATTRIBUTION.md | embedded only when built with `CRAFT_FONTS_DIR` (all official releases) | OFL-1.1 | Japanese UI and document fallback |
| `crates/ui-egui/src/i18n/uk.tsv` | @dmatviichuk with Codex | Original translation from the English interface labels in this repository; no other product localisation copied | MIT OR Apache-2.0 | Ukrainian interface catalog; spelling checked with external VESUM and ULIF dictionaries, neither bundled |
| `crates/ui-egui/src/i18n/pt-br.tsv` | @edurbs with ZCode | Original translation from the English interface labels in this repository; no other product localisation copied | MIT OR Apache-2.0 | Brazilian Portuguese interface catalog; spelling checked with the external pt_BR Hunspell dictionary, not bundled |
