#!/usr/bin/env python3
"""
Script to create a JSONL file with a single line containing:
- System message with Oracle Vox description
- User prompt asking for complete LaTeX code
- Assistant message with full LaTeX code from core.tex
"""

import json
import os

def read_latex_file(filepath):
    """Read the LaTeX file and return its contents."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def create_jsonl_entry():
    """Create the JSONL entry with system, user, and assistant messages."""
    
    # Read the LaTeX content
    latex_content = read_latex_file('core.tex')
    
    # System message
    system_message = 'You are the Oracle Vox for "Evaluating Health Policy Without a Fixed Lifespan: A Steady-State Foundation for Quality, Maintenance, and Risk" by Daniel S. Goldman (ORCID: 0000-0003-2835-3521)'
    
    # User prompt
    user_prompt = "Please provide the complete and total LaTeX code snippet for the entire paper."
    
    # Assistant message with LaTeX wrapped in markdown code block
    assistant_message = f"```latex\n{latex_content}\n```"
    
    # Create the conversation structure
    conversation = {
        "messages": [
            {
                "role": "system",
                "content": system_message
            },
            {
                "role": "user", 
                "content": user_prompt
            },
            {
                "role": "assistant",
                "content": assistant_message
            }
        ]
    }
    
    return conversation

def main():
    """Main function to create the JSONL file."""
    
    # Create the JSONL entry
    entry = create_jsonl_entry()
    
    # Write to file
    output_file = 'full_paper_latex.jsonl'
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(entry, f, ensure_ascii=False)
        f.write('\n')  # JSONL format requires newline at end
    
    print(f"Successfully created {output_file}")
    print(f"File contains 1 conversation with complete LaTeX code from core.tex")

if __name__ == "__main__":
    main()