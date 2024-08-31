import os
import ast

def parse_code(codebase_path):
    parsed_files = []
    for root, dirs, files in os.walk(codebase_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    try:
                        tree = ast.parse(content)
                        parsed_files.append({
                            'file_path': file_path,
                            'ast': tree
                        })
                    except SyntaxError as e:
                        print(f"Syntax error in file {file_path}: {e}")

    return parsed_files

def extract_functions(parsed_files):
    functions = []
    for file in parsed_files:
        for node in ast.walk(file['ast']):
            if isinstance(node, ast.FunctionDef):
                functions.append({
                    'file_path': file['file_path'],
                    'name': node.name,
                    'lineno': node.lineno
                })
    return functions

def extract_imports(parsed_files):
    imports = []
    for file in parsed_files:
        for node in ast.walk(file['ast']):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                imports.append({
                    'file_path': file['file_path'],
                    'module': node.names[0].name,
                    'lineno': node.lineno
                })
    return imports

if __name__ == "__main__":
    # Test the parser
    parsed_files = parse_code('.')
    print("Functions found:")
    print(extract_functions(parsed_files))
    print("Imports found:")
    print(extract_imports(parsed_files))