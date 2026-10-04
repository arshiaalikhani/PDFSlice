# PDFSlice

A lightweight desktop application for extracting selected page ranges from PDF files using **Python**, **Tkinter**, and **pypdf**.

PDFSlice provides a simple graphical interface for opening a PDF, selecting a start and end page, and exporting the selected range as a new PDF file.

## Features

- Simple graphical user interface
- Open PDF files using a file picker
- Automatically detect the total number of pages
- Select a custom start and end page
- Validate page numbers before processing
- Extract a continuous range of pages
- Save the result automatically as `output.pdf`
- Clear error and success messages
- No command-line interaction required

## Screenshot

The application provides a compact desktop interface where you can:

1. Select a PDF file.
2. Confirm the selected file.
3. Enter the first page to extract.
4. Enter the last page to extract.
5. Export the selected pages.

## Requirements

- Python 3.x
- pypdf
- Tkinter

Tkinter is included with most standard Python installations.

Install `pypdf` with:

```bash
pip install pypdf
```

## Usage

Clone the repository:

```bash
git clone https://github.com/yourusername/PDFSlice.git
cd PDFSlice
```

Install the required dependency:

```bash
pip install pypdf
```

Run the application:

```bash
python pdfslice.py
```

## How It Works

After launching PDFSlice:

1. Click **Select** to choose a PDF file.
2. Click **Confirm File**.
3. The application reads the PDF and displays its total page count.
4. Enter the desired start and end pages.
5. Click **Save output.pdf**.
6. The extracted PDF will be created in the same directory as the original file.

For example, selecting:

```text
Start page: 10
End page:   25
```

will create a new PDF containing pages **10 through 25**, inclusive.

## Validation

PDFSlice checks for several common problems before creating the output file:

- No file path provided
- File does not exist
- Invalid or unreadable PDF
- Non-numeric page numbers
- Page numbers outside the PDF's range
- Start page greater than end page

This prevents invalid page ranges from being passed to the PDF writer.

## Built With

- **Python** — application logic
- **Tkinter** — graphical user interface
- **pypdf** — PDF reading and writing

## Current Limitations

The current version:

- extracts one continuous page range at a time;
- always saves the result as `output.pdf`;
- saves the output in the directory of the source PDF;
- does not currently merge multiple PDF files;
- does not provide drag-and-drop support;
- does not display PDF page previews.

## Possible Future Improvements

Potential additions include:

- Custom output filenames
- User-selectable output directories
- Extraction of multiple separate page ranges
- PDF merging
- Drag-and-drop file support
- Page previews
- Recent-file history
- Dark mode
- Standalone executable builds for Windows
- Cross-platform packaging

## Project Structure

```text
PDFSlice/
├── pdfslice.py
├── README.md
└── requirements.txt
```

Example `requirements.txt`:

```text
pypdf
```

## License

This project can be distributed under the MIT License.

## Contributing

Contributions, bug reports, and feature suggestions are welcome.

If you find an issue or have an idea for improving PDFSlice, feel free to open an issue or submit a pull request.
