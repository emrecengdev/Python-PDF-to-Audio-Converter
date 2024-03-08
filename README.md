Based on the script you've provided, here's a detailed README.md in English and Markdown format. This README includes a brief introduction, installation instructions, usage guide, and acknowledges the libraries used in your project.

```markdown
# PDF to Audio Converter

This project is a desktop application developed in Python that allows users to convert PDF documents into audio files. Using a simple graphical user interface (GUI) built with wxPython, users can select a PDF file, choose the language for the audio output, and then convert the text into spoken words using Google's Text-to-Speech (gTTS) service. The result is an MP3 file that can be downloaded and listened to offline. This tool is especially useful for visually impaired users or anyone who prefers to listen to text rather than read it.

## Installation

Before running this application, ensure you have Python installed on your system. This project was developed using Python 3.8, but it should be compatible with other Python 3 versions.

1. Clone the repository or download the project files.
2. Navigate to the project directory in your terminal or command prompt.
3. Install the required packages by running:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes the following libraries:
- PyPDF2
- gTTS
- Pillow
- wxPython

## Usage

To start the application, navigate to the project directory and run:

```bash
python pdfToAudio.py
```

### Step-by-Step Guide:

1. **Launch the Application:** Execute the script to open the GUI.
2. **Select a PDF File:** Click the 'Browse' button to select the PDF document you want to convert.
3. **Choose a Language:** Select the language from the dropdown that you want the audio file to be in. Currently, English and Turkish are supported.
4. **Convert to Audio:** Press the 'Convert to Audio' button to begin the conversion process. The application will extract text from the PDF and convert it to audio using the selected language.
5. **Download:** Once the conversion is complete, a 'Download' button will appear. Click it to save the MP3 file to your computer.

## Libraries Used

- **[PyPDF2](https://pypi.org/project/PyPDF2/):** For reading PDF files and extracting text.
- **[gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/):** For converting text into speech.
- **[Pillow](https://pypi.org/project/Pillow/):** (Not directly used in the script but included in requirements, possibly for future enhancements or GUI elements.)
- **[wxPython](https://www.wxpython.org/):** For creating the graphical user interface.

## Contributing

Contributions to improve the application are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

Please ensure you have a `LICENSE` file in your repository if you mention it in the README. If you plan to use a different license, update the README accordingly.