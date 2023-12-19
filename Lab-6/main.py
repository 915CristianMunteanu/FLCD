# This is a sample Python script.
from Grammar import Grammar
from parser import Parser

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Read grammar from a file
    grammar1 = Grammar("g1.txt")
    grammar2 = Grammar("g2.txt")
    grammar1.print_s()
    grammar1.print_terminals()
    grammar1.print_productions()
    grammar1.print_nonterminals()
    grammar1.print_productions_for_nonterminal("A")
    grammar1.check_cfg()

    parser1 = Parser(grammar1)
    parser2 = Parser(grammar2)

    parser1.add_productions_to_file("( int + int )")
    parser2.add_productions_to_file("< and or and >")

    parser1.parser_output.print_to_screen()
    parser1.parser_output.print_to_file("final.txt")