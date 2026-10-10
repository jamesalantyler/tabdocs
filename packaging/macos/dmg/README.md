# TabDocs macOS DMG assets

This fork ships a fresh `background.svg` and `background.tiff` using the TabDocs icon.
The original upstream `.DS_Store` file has been removed to prevent inherited branding.
macOS DMG packaging can run without a prebuilt `.DS_Store`; Finder will use its default layout.
To generate a branded Finder layout, install the dependencies listed in `generate.py` and run
`python3 packaging/macos/dmg/generate.py` on a supported system before packaging.
