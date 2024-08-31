import ast

# Define some example rules (to be expanded)
PROHIBITED_MODULES = ['pickle', 'subprocess']
REQUIRED_IMPORTS = ['logging']

def check_compliance(parsed_code):
    compliance_results = []

    for file in parsed_code:
        file_path = file['file_path']
        tree = file['ast']

        # Check for prohibited modules
        imports = [node for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom))]
        for import_node in imports:
            if isinstance(import_node, ast.Import):
                module = import_node.names[0].name
            else:  # ImportFrom
                module = import_node.module

            if module in PROHIBITED_MODULES:
                compliance_results.append({
                    'file': file_path,
                    'line': import_node.lineno,
                    'issue': f"Use of prohibited module: {module}",
                    'severity': 'high'
                })

        # Check for required imports
        imported_modules = set(node.names[0].name if isinstance(node, ast.Import) else node.module for node in imports)
        for required_module in REQUIRED_IMPORTS:
            if required_module not in imported_modules:
                compliance_results.append({
                    'file': file_path,
                    'line': 1,
                    'issue': f"Missing required import: {required_module}",
                    'severity': 'medium'
                })

        # Check for potential security issues (example: use of eval)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'eval':
                compliance_results.append({
                    'file': file_path,
                    'line': node.lineno,
                    'issue': "Use of 'eval' function (potential security risk)",
                    'severity': 'high'
                })

    return compliance_results

if __name__ == "__main__":
    # Test the compliance checker
    from code_parser import parse_code
    parsed_code = parse_code('.')
    results = check_compliance(parsed_code)
    for result in results:
        print(f"{result['file']}:{result['line']} - {result['issue']} (Severity: {result['severity']})")