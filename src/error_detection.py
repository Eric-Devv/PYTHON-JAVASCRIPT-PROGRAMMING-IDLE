from pyflakes.api import check
from pyflakes.reporter import Reporter
import io

def detect_errors(code):
    reporter_output = io.StringIO()
    reporter = Reporter(reporter_output, io.StringIO())
    check(code, filename='temp/temp.py', reporter=reporter)
    errors = reporter_output.getvalue().strip().splitlines()
    return errors
