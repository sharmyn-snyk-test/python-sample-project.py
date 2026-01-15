import os

def insecure_file_open(filename):
    # Potential security issue: Path Traversal
    with open(filename, 'r') as f:
        return f.read()

if __name__ == "__main__":
    print("App running...")
