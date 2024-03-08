import wx
from PyPDF2 import PdfReader
from gtts import gTTS
import os

class PDFToAudioConverter(wx.Frame):
    def __init__(self, *args, **kw):
        super(PDFToAudioConverter, self).__init__(*args, **kw)
        
        self.pdf_file = None  # Başlangıçta None olarak tanımla
        self.audio_content = None  # Başlangıçta None olarak tanımla
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.pdf_label = wx.StaticText(panel, label="No File Chosen")
        vbox.Add(self.pdf_label, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        browse_btn = wx.Button(panel, label='Browse')
        browse_btn.Bind(wx.EVT_BUTTON, self.OnBrowse)
        vbox.Add(browse_btn, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        languages = ['English', 'Turkish']
        self.language_choice = wx.Choice(panel, choices=languages)
        self.language_choice.SetSelection(0)
        vbox.Add(self.language_choice, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        convert_btn = wx.Button(panel, label='Convert to Audio')
        convert_btn.Bind(wx.EVT_BUTTON, self.OnConvert)
        vbox.Add(convert_btn, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        self.audio_label = wx.StaticText(panel, label="No File Converted")
        vbox.Add(self.audio_label, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        download_btn = wx.Button(panel, label='Download')
        download_btn.Bind(wx.EVT_BUTTON, self.OnDownload)
        vbox.Add(download_btn, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        panel.SetSizer(vbox)
        self.SetTitle('PDF to Audiobook Converter')
        self.Centre()

    def OnBrowse(self, event):
        with wx.FileDialog(self, "Select a PDF file", wildcard="PDF files (*.pdf)|*.pdf",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # Kullanıcı iptal ederse çık

            pathname = fileDialog.GetPath()
            try:
                self.pdf_file = PdfReader(pathname)
                self.pdf_label.SetLabel(pathname)
            except Exception as e:
                wx.MessageBox(f'Failed to open PDF file: {e}', 'Error', wx.OK | wx.ICON_ERROR)
                self.pdf_file = None

    def OnConvert(self, event):
        if not self.pdf_file:
            wx.MessageBox('Please select a PDF file first.', 'Error', wx.OK | wx.ICON_ERROR)
            return
        
        pdf_to_text = ''
        try:
            for page in self.pdf_file.pages:
                pdf_to_text += page.extract_text()  # extract_text metodu kullanılarak metin çekilir
            
            lang_dict = {'English': 'en', 'Turkish': 'tr'}
            lang = lang_dict.get(self.language_choice.GetString(self.language_choice.GetSelection()))
            self.audio_content = gTTS(text=pdf_to_text, lang=lang)
            self.audio_label.SetLabel('Conversion complete. Ready to download.')
        except Exception as e:
            wx.MessageBox(f'Failed to convert PDF to audio: {e}', 'Error', wx.OK | wx.ICON_ERROR)
            self.audio_content = None

    def OnDownload(self, event):
        if not self.audio_content:
            wx.MessageBox('Please convert a PDF to audio first.', 'Error', wx.OK | wx.ICON_ERROR)
            return
        
        file_name = os.path.splitext(self.pdf_label.GetLabel())[0] + '.mp3'
        try:
            self.audio_content.save(file_name)
            wx.MessageBox(f'Audio saved as: {file_name}', 'Info', wx.OK | wx.ICON_INFORMATION)
        except Exception as e:
            wx.MessageBox(f'Failed to save audio file: {e}', 'Error', wx.OK | wx.ICON_ERROR)

def main():
    app = wx.App(False)
    ex = PDFToAudioConverter(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
