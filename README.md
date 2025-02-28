# Password Manager
#### Video Demo: <https://youtu.be/79OeAgF59tM>
#### Description:

A secure command-line password management solution built with Python. This application helps users generate strong random passwords, securely store credentials for various websites/services, and manage their digital authentication details through an encrypted master password system.

## Features Overview

### Core Functionality
- **Master Password Protection**: First-time users create a master password that encrypts access to the password vault
- **Password Generation**: Creates strong 12-character passwords using mixed case letters, numbers, and symbols
- **Credential Storage**: Securely saves website/service names with associated passwords in encrypted CSV format
- **Password Management**: Full CRUD (Create, Read, Update, Delete) functionality for stored credentials
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux systems

### Security Implementation
- Master password verification with 3-attempt lockout
- Local credential storage without cloud dependencies
- Generated passwords contain 72 possible characters
- No plaintext password display after initial entry

## Technical Architecture

### File Structure
- `project.py`: Main application logic and functions
- `test_project.py`: Unit tests using pytest framework
- `requirements.txt`: Dependency specifications
- `passwords.csv`: Encrypted credential storage (auto-generated)
- `master_password.txt`: Hashed master password (auto-generated)

### Key Functions
- **`main()`**: Orchestrates program flow and user interface
- **`check_master_password()`**: Handles authentication logic and attempt tracking
- **`generate_password()`**: Implements cryptographically-secure random generation
- **`load_passwords()`**: Manages CSV read operations and data parsing
- **`save_passwords()`**: Handles CSV write operations with proper file locking

## Development Decisions

### Storage Format Choice
The CSV format was selected over JSON/SQLite for:
- Human readability during debugging
- Easy integration with spreadsheet applications
- Simple implementation for file-based operations
- Lower memory footprint for small datasets

### Security Considerations
While not enterprise-grade, the system implements:
- Master password confirmation during setup
- Input sanitization for service names
- Immediate password hashing after entry
- Clean credential deletion implementation

### Testing Methodology
The test suite verifies:
- Password generation meets length requirements
- All generated characters are from approved set
- CSV loading handles both populated and empty files
- Password saving maintains data integrity
- Edge cases like duplicate service entries

## Installation & Usage

### Requirements
- Python 3.10+
- pytest (for testing only)

```bash
pip install -r requirements.txt
