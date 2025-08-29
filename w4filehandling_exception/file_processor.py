def file_processor():
    """
    File Handling and Exception Handling Assignment
    - Reads a file and writes modified version to new file
    - Handles errors for non-existent or unreadable files
    - Allows user to choose modification type
    """
    
    print("FILE MODIFIER APPLICATION")
    print("=" * 40)
    
    # Get input filename with error handling
    while True:
        try:
            input_filename = input("Enter the filename to read: ").strip()
            
            # Try to open and read the file
            with open(input_filename, 'r', encoding='utf-8') as file:
                original_content = file.read()
            
            print(f"Successfully read '{input_filename}'")
            print(f"Original content length: {len(original_content)} characters")
            break
            
        except FileNotFoundError:
            print(f"Error: File '{input_filename}' not found. Please try again.")
        except PermissionError:
            print(f"Error: Permission denied to read '{input_filename}'. Try a different file.")
        except UnicodeDecodeError:
            print(f"Error: Cannot decode '{input_filename}'. It might be a binary file.")
        except Exception as e:
            print(f"Unexpected error: {e}. Please try again.")
    
    # Ask user what modification they want
    print("\nSELECT MODIFICATION TYPE:")
    print("1. Uppercase with line numbers")
    print("2. Add custom prefix to each line")
    print("3. Reverse line order")
    print("4. Remove empty lines")
    print("5. Custom text transformation")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            if choice in ['1', '2', '3', '4', '5']:
                break
            else:
                print("Please enter a number between 1 and 5")
        except:
            print("Invalid input. Please try again.")
    
    # Get additional input based on choice
    if choice == '2':
        prefix = input("Enter the prefix to add to each line: ")
    elif choice == '5':
        custom_text = input("Enter text to append to the content: ")
    
    # Process the content with selected modification
    print("\nTRANSFORMING FILE CONTENT...")
    modified_content = transform_content(original_content, choice, 
                                       prefix if choice == '2' else None,
                                       custom_text if choice == '5' else None)
    
    # Show preview of changes
    print("\nMODIFICATION SUMMARY:")
    print(f"Original size: {len(original_content)} characters")
    print(f"Modified size: {len(modified_content)} characters")
    
    # Show sample of changes
    print("\nSAMPLE OF MODIFICATIONS:")
    original_sample = original_content[:100] + "..." if len(original_content) > 100 else original_content
    modified_sample = modified_content[:100] + "..." if len(modified_content) > 100 else modified_content
    print(f"Original: {original_sample}")
    print(f"Modified: {modified_sample}")
    
    # Get output filename
    output_filename = input("\nEnter output filename (or press Enter for 'modified_file.txt'): ").strip()
    if not output_filename:
        output_filename = "modified_file.txt"
    
    # Write modified content to new file
    try:
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        print(f"Successfully wrote modified content to '{output_filename}'")
        print(f"New file created with {len(modified_content)} characters")
        
    except Exception as e:
        print(f"Error writing to file: {e}")

def transform_content(content, choice, prefix=None, custom_text=None):
    """
    Transform the file content based on user choice
    """
    if not content.strip():
        return "EMPTY FILE - NO CONTENT TO TRANSFORM"
    
    lines = content.split('\n')
    transformed_lines = []
    
    # Apply selected transformation
    if choice == '1':  # Uppercase with line numbers
        for i, line in enumerate(lines, 1):
            if line.strip():
                transformed_line = f"LINE {i}: {line.strip().upper()}"
                transformed_lines.append(transformed_line)
            else:
                transformed_lines.append("(EMPTY LINE)")
                
    elif choice == '2':  # Add custom prefix
        for i, line in enumerate(lines, 1):
            if line.strip():
                transformed_line = f"{prefix} {line.strip()}"
                transformed_lines.append(transformed_line)
            else:
                transformed_lines.append(f"{prefix} (EMPTY LINE)")
                
    elif choice == '3':  # Reverse line order
        transformed_lines = [line.strip() for line in lines if line.strip()]
        transformed_lines.reverse()
        
    elif choice == '4':  # Remove empty lines
        transformed_lines = [line.strip() for line in lines if line.strip()]
        
    elif choice == '5':  # Custom text append
        transformed_lines = [line.strip() for line in lines if line.strip()]
        transformed_content = '\n'.join(transformed_lines)
        return f"{transformed_content}\n\n--- ADDED CONTENT ---\n{custom_text}"
    
    # Add header and footer for most transformations
    if choice != '5':  # Don't add header/footer for custom text mode
        header = "TRANSFORMED FILE CONTENT\n"
        header += "=" * 40 + "\n"
        header += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        header += f"Transformation type: {get_transformation_name(choice)}\n"
        header += "=" * 40 + "\n\n"
        
        footer = "\n" + "=" * 40 + "\n"
        footer += "END OF TRANSFORMED CONTENT"
        
        return header + '\n'.join(transformed_lines) + footer
    
    return '\n'.join(transformed_lines)

def get_transformation_name(choice):
    """Get descriptive name for the transformation"""
    transformations = {
        '1': 'Uppercase with line numbers',
        '2': 'Custom prefix added',
        '3': 'Line order reversed',
        '4': 'Empty lines removed',
        '5': 'Custom text appended'
    }
    return transformations.get(choice, 'Unknown transformation')

def main():
    """Main function to run the application"""
    try:
        file_processor()
        
        print("\n" + "=" * 40)
        print("ASSIGNMENT OUTCOMES ACHIEVED:")
        print("- File reading and writing")
        print("- User-driven content transformation")
        print("- Error handling implemented")
        print("- Multiple modification options")
        
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"Unexpected program error: {e}")

# Import needed for timestamp
from datetime import datetime

# Run the program
if __name__ == "__main__":
    main()