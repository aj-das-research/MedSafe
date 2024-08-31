import os
import zipfile
from git import Repo
from .code_parser import parse_code
from .compliance_checker import check_compliance
from .report_generator import generate_report

REPO_URL = "https://github.com/aj-das-research/MedSafe.git"

class MedSafeAnalyzer:
    def __init__(self):
        self.codebase = None

    def load_from_zip(self, zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            self.codebase = zip_ref.extractall('temp_codebase')
        print(f"Codebase loaded from zip file: {zip_path}")

    def load_from_git(self, repo_url=REPO_URL):
        Repo.clone_from(repo_url, 'temp_codebase')
        self.codebase = 'temp_codebase'
        print(f"Codebase loaded from git repository: {repo_url}")

    def analyze(self):
        if not self.codebase:
            raise ValueError("No codebase loaded. Please load a codebase first.")

        parsed_code = parse_code(self.codebase)
        compliance_results = check_compliance(parsed_code)
        report = generate_report(compliance_results)

        return report

    def cleanup(self):
        if os.path.exists('temp_codebase'):
            for root, dirs, files in os.walk('temp_codebase', topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir('temp_codebase')
        print("Temporary codebase cleaned up.")

def main():
    analyzer = MedSafeAnalyzer()
    
    # Example usage
    analyzer.load_from_git()
    report = analyzer.analyze()
    print(report)
    analyzer.cleanup()

if __name__ == "__main__":
    main()