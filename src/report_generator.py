from datetime import datetime

def generate_report(compliance_results):
    report = []
    report.append("MedSafe Compliance Report")
    report.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("-" * 50)

    if not compliance_results:
        report.append("No compliance issues found. All checks passed!")
    else:
        report.append(f"Total issues found: {len(compliance_results)}")
        report.append("")

        for result in compliance_results:
            report.append(f"File: {result['file']}")
            report.append(f"Line: {result['line']}")
            report.append(f"Issue: {result['issue']}")
            report.append(f"Severity: {result['severity'].upper()}")
            report.append("-" * 30)

    report.append("\nRecommendations:")
    if compliance_results:
        report.append("1. Review and address all high severity issues immediately.")
        report.append("2. Plan to resolve medium severity issues in the near future.")
        report.append("3. Consider best practices for low severity issues.")
    else:
        report.append("1. Continue maintaining good coding practices and security awareness.")
        report.append("2. Regularly update dependencies and review code for potential vulnerabilities.")

    return "\n".join(report)

if __name__ == "__main__":
    # Test the report generator
    sample_results = [
        {'file': 'test.py', 'line': 10, 'issue': 'Use of eval', 'severity': 'high'},
        {'file': 'utils.py', 'line': 25, 'issue': 'Missing logging import', 'severity': 'medium'}
    ]
    print(generate_report(sample_results))