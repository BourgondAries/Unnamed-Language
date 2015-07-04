#include "CrossTerminalToString.hpp"


namespace tul
{
	namespace parser
	{
		namespace dependency
		{
			std::string CrossTerminalToString::convertToString(protocols::CrossTerminal cross_terminal)
			{
				switch (cross_terminal)
				{
					case protocols::CrossTerminal::ENTER: return "ENTER";
					case protocols::CrossTerminal::EXIT: return "EXIT";
					case protocols::CrossTerminal::NONE: return "NONE";
					case protocols::CrossTerminal::FIELD_DECLARATION_LIST: return "FIELD_DECLARATION_LIST";
					case protocols::CrossTerminal::DECLARATION: return "DECLARATION";
					case protocols::CrossTerminal::ACCESS_SPECIFIER: return "ACCESS_SPECIFIER";
					case protocols::CrossTerminal::OPTIONAL_EQUALS: return "OPTIONAL_EQUALS";
					case protocols::CrossTerminal::COMMA_SEPARATED_LIST: return "COMMA_SEPARATED_LIST";
					case protocols::CrossTerminal::OPTIONAL_CALL: return "OPTIONAL_CALL";
					case protocols::CrossTerminal::METHOD_DECLARATION_LIST: return "METHOD_DECLARATION_LIST";
					case protocols::CrossTerminal::COMMA_SEPARATED_TYPE_AND_NAME_LIST: return "COMMA_SEPARATED_TYPE_AND_NAME_LIST";
					case protocols::CrossTerminal::STATEMENT_LIST: return "STATEMENT_LIST";
					case protocols::CrossTerminal::COMMA_SEPARATED_LIST_ITEM: return "COMMA_SEPARATED_LIST_ITEM";
					case protocols::CrossTerminal::STATEMENT: return "STATEMENT";
					case protocols::CrossTerminal::TYPE: return "TYPE";
					case protocols::CrossTerminal::GROUPER_LEFT_BRACE: return "GROUPER_LEFT_BRACE";
					case protocols::CrossTerminal::GROUPER_RIGHT_BRACE: return "GROUPER_RIGHT_BRACE";
					case protocols::CrossTerminal::GROUPER_LEFT_BRACKET: return "GROUPER_LEFT_BRACKET";
					case protocols::CrossTerminal::GROUPER_RIGHT_BRACKET: return "GROUPER_RIGHT_BRACKET";
					case protocols::CrossTerminal::GROUPER_LEFT_PARENTHESIS: return "GROUPER_LEFT_PARENTHESIS";
					case protocols::CrossTerminal::GROUPER_RIGHT_PARENTHESIS: return "GROUPER_RIGHT_PARENTHESIS";
					case protocols::CrossTerminal::IDENTIFIER_CLASS: return "IDENTIFIER_CLASS";
					case protocols::CrossTerminal::IDENTIFIER_ENUMERATION: return "IDENTIFIER_ENUMERATION";
					case protocols::CrossTerminal::IDENTIFIER_PACKAGE: return "IDENTIFIER_PACKAGE";
					case protocols::CrossTerminal::IDENTIFIER_SUBROUTINE: return "IDENTIFIER_SUBROUTINE";
					case protocols::CrossTerminal::IDENTIFIER_VARIABLE: return "IDENTIFIER_VARIABLE";
					case protocols::CrossTerminal::INTEGER_LITERAL: return "INTEGER_LITERAL";
					case protocols::CrossTerminal::KEYWORD_ASSEMBLY: return "KEYWORD_ASSEMBLY";
					case protocols::CrossTerminal::KEYWORD_DO: return "KEYWORD_DO";
					case protocols::CrossTerminal::KEYWORD_FOR: return "KEYWORD_FOR";
					case protocols::CrossTerminal::KEYWORD_GOTO: return "KEYWORD_GOTO";
					case protocols::CrossTerminal::KEYWORD_IF: return "KEYWORD_IF";
					case protocols::CrossTerminal::KEYWORD_LABEL: return "KEYWORD_LABEL";
					case protocols::CrossTerminal::KEYWORD_PRIVATE: return "KEYWORD_PRIVATE";
					case protocols::CrossTerminal::KEYWORD_PUBLIC: return "KEYWORD_PUBLIC";
					case protocols::CrossTerminal::KEYWORD_RESTRICTED: return "KEYWORD_RESTRICTED";
					case protocols::CrossTerminal::KEYWORD_WHILE: return "KEYWORD_WHILE";
					case protocols::CrossTerminal::PRIMITIVE_SIGNED: return "PRIMITIVE_SIGNED";
					case protocols::CrossTerminal::PRIMITIVE_UNSIGNED: return "PRIMITIVE_UNSIGNED";
					case protocols::CrossTerminal::STRING: return "STRING";
					case protocols::CrossTerminal::SYMBOL_PLUS: return "SYMBOL_PLUS";
					case protocols::CrossTerminal::SYMBOL_PLUS__PLUS: return "SYMBOL_PLUS__PLUS";
					case protocols::CrossTerminal::SYMBOL_MINUS: return "SYMBOL_MINUS";
					case protocols::CrossTerminal::SYMBOL_MINUS__MINUS: return "SYMBOL_MINUS__MINUS";
					case protocols::CrossTerminal::SYMBOL_STAR: return "SYMBOL_STAR";
					case protocols::CrossTerminal::SYMBOL_STAR__STAR: return "SYMBOL_STAR__STAR";
					case protocols::CrossTerminal::SYMBOL_FORWARD_SLASH: return "SYMBOL_FORWARD_SLASH";
					case protocols::CrossTerminal::SYMBOL_BACKWARD_SLASH: return "SYMBOL_BACKWARD_SLASH";
					case protocols::CrossTerminal::SYMBOL_AMPERSAND__AMPERSAND: return "SYMBOL_AMPERSAND__AMPERSAND";
					case protocols::CrossTerminal::SYMBOL_BAR__BAR: return "SYMBOL_BAR__BAR";
					case protocols::CrossTerminal::SYMBOL_AMPERSAND: return "SYMBOL_AMPERSAND";
					case protocols::CrossTerminal::SYMBOL_BAR: return "SYMBOL_BAR";
					case protocols::CrossTerminal::SYMBOL_CARET: return "SYMBOL_CARET";
					case protocols::CrossTerminal::SYMBOL_EXCLAMATION_MARK: return "SYMBOL_EXCLAMATION_MARK";
					case protocols::CrossTerminal::SYMBOL_DOT__DOT: return "SYMBOL_DOT__DOT";
					case protocols::CrossTerminal::SYMBOL_DOT: return "SYMBOL_DOT";
					case protocols::CrossTerminal::SYMBOL_COMMA: return "SYMBOL_COMMA";
					case protocols::CrossTerminal::SYMBOL_COLON__COLON: return "SYMBOL_COLON__COLON";
					case protocols::CrossTerminal::SYMBOL_COLON: return "SYMBOL_COLON";
					case protocols::CrossTerminal::SYMBOL_SEMICOLON: return "SYMBOL_SEMICOLON";
					case protocols::CrossTerminal::SYMBOL_LESS_THAN__LESS_THAN: return "SYMBOL_LESS_THAN__LESS_THAN";
					case protocols::CrossTerminal::SYMBOL_LESS_THAN: return "SYMBOL_LESS_THAN";
					case protocols::CrossTerminal::SYMBOL_GREATER_THAN__GREATER_THAN: return "SYMBOL_GREATER_THAN__GREATER_THAN";
					case protocols::CrossTerminal::SYMBOL_GREATER_THAN: return "SYMBOL_GREATER_THAN";
					case protocols::CrossTerminal::UNIDENTIFIED: return "UNIDENTIFIED";
					default: return "";
				}
			}
		}
	}
}