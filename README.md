# 📂 Python File Explorer (Tkinter)

A functional, multi-pane Windows File Explorer clone built using Python's `tkinter` and `ttk` modules. This application provides a graphical interface to navigate the local file system, view directory summaries, and inspect file metadata.

## ✨ Key Features
* **Hierarchical Navigation:** A dynamic tree-view (Left Pane) that expands directories on demand to explore the `C:\` drive.
* **Real-time Summaries:** A top-level summary pane that calculates the number of subdirectories, total files, and immediate file size for the selected folder.
* **Detailed File View:** A right-hand pane listing file names, paths, sizes, and last-modified timestamps.
* **Interactive Popups:** Integrated event binding that triggers a summary popup with detailed metadata when a specific file is selected.
* **UI/UX Elements:** Includes custom scrollbars (vertical and horizontal) and specialized text tagging for a responsive user experience.

## 🛠️ Technical Implementation
* **OS Interfacing:** Leverages the `os` and `datetime` modules to pull live system data and format timestamps.
* **Event-Driven Logic:** Uses `<<TreeviewSelect>>` bindings to trigger data refreshes across multiple panes simultaneously.
* **Recursive Prevention:** Implements a tracking system (`selectedItemsLeft`) to prevent redundant data loading and ensure UI performance.

## 🚀 How to Run
1. Ensure you have Python installed.
2. Run the script:
   ```bash
   python explorer.py
