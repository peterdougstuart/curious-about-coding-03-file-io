from file_io.analyser import BaseAnalyserForm


class AnalyserForm(BaseAnalyserForm):
    def analyze(self, path):

        self.log_text(f"Starting analysis of: {path}")
        # ... do something ...
        self.log_text("Analysis complete!")


app = AnalyserForm()
app.mainloop()
