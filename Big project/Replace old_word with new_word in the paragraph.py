def replace_word(paragraph, old_word, new_word):
    # Replace old_word with new_word in the paragraph
    updated_paragraph = paragraph.replace(old_word, new_word)
    return updated_paragraph

def main():
    # Input the paragraph from the user
    paragraph = input("Enter the paragraph: ")
    
    # Input the word to be replaced
    old_word = input("Enter the word to be replaced: ")
    
    # Input the new word to replace with
    new_word = input("Enter the new word: ")
    
    # Replace the word in the paragraph
    updated_paragraph = replace_word(paragraph, old_word, new_word)
    
    # Output the updated paragraph
    print("\nUpdated Paragraph:")
    print(updated_paragraph)

if __name__ == "__main__":
    main()
