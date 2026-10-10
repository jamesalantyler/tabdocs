# TabDocs — Multi-document tabs + workspace restoration (custom source build)

This is a community modification of the TabDocs source code. The application remains
TabDocs; upstream branding, formats and editor engine have not been replaced.

## Features

- **Open multiple files** in independent tabs above the ribbon. Undo/redo, view/canvas state and
  document Save/Save As remain isolated.
- **Drag tab labels** to reorder within the pinned or unpinned group. Tabs can also be moved by
  right-clicking and choosing Move tab left/right. The tab bar scrolls horizontally when crowded.
- **Pin / Unpin** from the right-click menu. Pinned tabs appear first and have a pushpin icon;
  pin order is remembered across restarts.
- **Context menu:** Pin/Unpin, Move Left, Move Right, Copy Full Path, Close, Close Other Unpinned Tabs,
  Close All Tabs, Reopen Closed Tab. Close Others leaves pinned tabs alone.
- **Reopen closed tab** with `Ctrl+Shift+T` (Windows/Linux) or via the right-click tab menu.
  Reopen reloads the saved file from disk (not any edits you explicitly discarded); the recent
  history holds up to 20 file-backed tabs during the current run.
- **Session restoration:** On normal window close or File > Exit, TabDocs records the open tabs,
  their on-disk paths, pinning, order, and selected tab in its existing `ui.json` preferences. A
  normal launch reopens them. Missing/unreadable files are skipped without blocking the startup.
- **Save Changes prompts** run for every dirty document at exit without deleting tabs from the
  workspace before preferences can be written. Cancel aborts exit. Save As during exit updates the
  restored filename. Choosing Don't Save discards edits; reopening loads the last saved file.
- **Explicit Close All or closing the last tab** clears session restoration: on the next normal
  launch TabDocs opens an empty document.

## Shortcuts

- `Ctrl+Tab` / `Ctrl+Shift+Tab` — next / previous tab.
- `Ctrl+Shift+T` — reopen most recently closed file-backed tab.
- `Ctrl+N` / `Ctrl+O` / `Ctrl+S` / `Ctrl+W` — existing New / Open / Save / Close behavior.

## Build on Windows

Requires Rust 1.90+ and Microsoft C++ Build Tools (Desktop development with C++ workload).
Open PowerShell in the folder containing `Cargo.toml`, then run:

```powershell
cargo build --release --locked -p tabdocs
.\target\release\tabdocs.exe
```

Use no `--sample` or explicit document command-line arguments to test workspace restoration.
The executable is in `target\release\tabdocs.exe`.

Run unit tests:

```powershell
cargo test --locked -p tabdocs-ui-egui
```

To preserve your existing working version, build this source in a **new folder** rather than
copying its files into your currently running TabDocs build. If you have Git and your existing
working source is the previous Multi-Document Tabs edition, you can apply the optional incremental
patch with `git apply` from the project root.

## Scope & limitations

- Preferences store **file paths**, not document data. Untitled tabs reopen blank; unsaved content
  is **not** restored, and closing without saving discards edits. Save important drafts first.
- Restoration is saved on **clean application exit**, not continuously in the background, so
  a crash or forced termination might not preserve the latest workspace arrangement.
- A launch with `--sample` or explicit filenames overrides automatic session restoration.
- In-memory undo history, selections, scroll offsets, and AutoSave authority are not reconstructed
  across program restarts; reopened documents are freshly loaded from disk.
- Tab history (Ctrl+Shift+T) is held in memory and resets on restart.
- The original source for this modification is not compiled in the ChatGPT working environment,
  which does not have a Rust compiler. Compilation and runtime verification must happen on the
  Windows machine. The project remains subject to TabDocs's upstream licenses/attributions.
