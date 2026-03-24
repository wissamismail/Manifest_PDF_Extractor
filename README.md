# 📄 Manifest PDF Extractor

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> A Python tool for extracting structured shipping manifest data from PDF documents using PDFMiner, with optional machine learning capabilities via LSTM models.

---

## 🚀 Overview

**Manifest_PDF_Extractor** is a specialized tool designed to parse shipping manifest PDFs and extract key logistics information into a structured CSV format. It uses coordinate-based text extraction to accurately capture fields such as Bill of Lading (BOL), shipper/consignee details, port information, container specifications, and arrival dates.

The project also includes a Jupyter notebook (`MyLSTM.ipynb`) demonstrating how extracted manifest data can be used to train LSTM models for classification or anomaly detection tasks.

---

## ✨ Features

- 🔍 **Coordinate-Based PDF Parsing**: Uses `pdfminer` to extract text from specific bounding box locations in manifest PDFs
- 📦 **Comprehensive Field Extraction**:
  - Bill of Lading (BOL) number
  - Shipping line & carrier information
  - Shipper & consignee details with location parsing
  - Port of loading & discharge (city/country)
  - Container size, TEUs, and weight metrics
  - Commodity codes and descriptions
  - Arrival dates and manifest metadata
- 🌍 **Geolocation Support**: Automatically extracts and validates city/country names using `GeoText` and `geopy`
- 📊 **CSV Export**: Outputs structured data ready for analysis or database import
- 🤖 **ML Integration**: Includes an LSTM model notebook for predictive analytics on manifest data
- 🔁 **Multi-Page Support**: Handles multi-page manifest documents with BOL continuity tracking

---

## 📁 Project Structure

```
Manifest_PDF_Extractor/
├── MainAnalysis.py      # Main PDF parsing engine and orchestration
├── Manifest.py          # Data model class for manifest entries
├── utils.py             # Helper functions: CSV export, location extraction
├── MyLSTM.ipynb         # Jupyter notebook: LSTM model for classification
├── Tammo.pdf            # Sample manifest PDF for testing
├── old/                 # Legacy/backup files
└── .idea/               # IDE configuration (PyCharm)
```

---

## 🛠️ Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Install Dependencies

```bash
pip install pdfminer.six geotext geopy pandas numpy matplotlib scikit-learn tensorflow keras
```

> 💡 **Note**: The LSTM notebook requires TensorFlow/Keras. Install with:
> ```bash
> pip install tensorflow  # Includes keras
> ```

---

## 📖 Usage

### Basic PDF Extraction

```python
from MainAnalysis import parse_pdf
from utils import my_functions

# Parse a manifest PDF (adjust page limit as needed)
parse_pdf('path/to/your_manifest.pdf', pages=150)

# Export extracted data to CSV
# (CSV is automatically generated as 'myManifest.csv' after parsing)
```

### Run Directly

```bash
python MainAnalysis.py
```

> This will process `Tammo.pdf` (included sample) and generate `myManifest.csv`.

### Using the LSTM Model (Optional)

1. Open `MyLSTM.ipynb` in Jupyter Notebook or Google Colab
2. Ensure your extracted CSV data is preprocessed and loaded
3. Run cells sequentially to:
   - Load and preprocess data
   - Train the LSTM model
   - Evaluate performance metrics
   - Save/load the trained model

---

## 🧩 Configuration

### Customizing Field Coordinates

The `ItemBBOX` class in `utils.py` defines bounding box coordinates for each field. Adjust these values if your manifest PDFs use a different layout:

```python
class ItemBBOX:
    BOL = [77, 466, 2]  # [x0, y1, line_index]
    Shipping_Line = [78, 530, 0]
    # ... add/modify other fields as needed
```

> 🔎 **Tip**: Use a PDF coordinate inspector tool to identify exact text positions in your documents.

### Adding New Fields

1. Add the field to the `Manifest` class in `Manifest.py`
2. Define its coordinates in `ItemBBOX` in `utils.py`
3. Add extraction logic in `get_text_from_elements()` in `MainAnalysis.py`
4. Include the field in `header_list` and `get_list()` for CSV export

---

## 📤 Output Format

The tool generates `myManifest.csv` with the following columns:

| Column | Description |
|--------|-------------|
| Shipping Line | Carrier/transport company |
| Shipper | Exporter name |
| Shipper Location - City,Province | Origin city |
| Shipper Location - Country | Origin country |
| Commodity Code | HS/customs code |
| Cont. Size | Container dimensions (e.g., 20, 40) |
| TEU's | Twenty-foot Equivalent Units |
| Package Class | Packaging type |
| Weight (ORG) in Tonne | Gross weight |
| Commodity | Goods description |
| BOL # | Bill of Lading number |
| Consignee | Importer/recipient |
| Actual Port of Loading | Departure port |
| Place of delivery-City,Province | Destination city |
| Place of delivery- Country | Destination country |
| Actual Port of Discharge-City,Province | Arrival port city |
| Actual Port of Discharge- Country | Arrival port country |
| Date of Arrival | Expected arrival date |
| Month/Year | Parsed date components |
| Manifest Type | Export/Import designation |

---

## 🧪 Testing

```bash
# Run with sample file
python MainAnalysis.py

# Verify output
cat myManifest.csv
```

---

## ⚠️ Limitations & Notes

- **Layout-Specific**: Designed for manifests with consistent formatting. Coordinate values may need adjustment for different PDF templates.
- **Geocoding Rate Limits**: `geopy.Nominatim` has usage policies—add delays or use alternative services for bulk processing.
- **PDF Compatibility**: Works best with text-based PDFs. Scanned/image-based PDFs require OCR preprocessing.
- **Error Handling**: Includes try/except blocks, but complex/malformed PDFs may require manual review.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m 'Add some feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Open a Pull Request

Please ensure code follows PEP 8 and includes docstrings for new functions.

---

## 📄 License

This project is licensed under the MIT License—see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [PDFMiner](https://github.com/pdfminer/pdfminer.six) for robust PDF text extraction
- [GeoText](https://github.com/dieghernan/geotext) & [GeoPy](https://github.com/geopy/geopy) for location parsing
- TensorFlow/Keras team for the LSTM implementation framework

---

> 💬 **Have questions or suggestions?** Open an [issue](https://github.com/wissamismail/Manifest_PDF_Extractor/issues) or contact the maintainer.

*Last updated: March 2026*
